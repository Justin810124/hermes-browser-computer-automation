#!/usr/bin/env python3
"""Decision harness for Hermes browser/computer automation.

Hermes should call this before touching a browser. The harness makes the
control-surface decision explicit and returns concrete next commands.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STOP_GATES = [
    "CAPTCHA",
    "PerimeterX",
    "Cloudflare Turnstile",
    "2FA",
    "identity verification",
    "tax forms",
    "payment",
    "publish",
    "legal attestation",
]

STOP_WORDS = {
    "captcha",
    "perimeterx",
    "turnstile",
    "2fa",
    "two-factor",
    "verification code",
    "identity",
    "tax",
    "w-9",
    "w-8",
    "payment",
    "purchase",
    "subscribe",
    "publish",
    "final submit",
    "legal attestation",
}

REAL_CHROME_WORDS = {
    "real chrome",
    "current chrome",
    "already open",
    "logged in",
    "logged-in",
    "login state",
    "existing session",
    "my chrome",
    "fiverr",
    "upwork",
    "seller portal",
    "dashboard",
}

NATIVE_UI_WORDS = {
    "file picker",
    "upload",
    "finder",
    "desktop",
    "macos",
    "native",
    "drag",
    "drop",
    "screenshot",
}

API_WORDS = {
    "github issue",
    "github repo",
    "gmail",
    "google calendar",
    "google drive",
    "slack",
    "notion",
}

ORDINARY_WEB_WORDS = {
    "open",
    "visit",
    "search",
    "summarize",
    "extract",
    "browse",
    "click",
    "fill",
    "form",
}


@dataclass
class Environment:
    hermes: bool
    browser_use_python: bool
    browser_use_api_key: bool
    computer_use_enabled: bool
    cua_driver: bool


@dataclass
class Decision:
    control_surface: str
    reason: str
    stop_gates: list[str]
    next_command: str | None
    handoff_prompt: str | None
    warnings: list[str]
    environment: Environment


def contains_any(text: str, words: set[str]) -> bool:
    return any(word in text for word in words)


def shell_quote(value: str) -> str:
    return "'" + value.replace("'", "'\"'\"'") + "'"


def command_output(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT, timeout=10)
    except Exception:
        return ""


def read_env_file() -> dict[str, str]:
    env = dict(os.environ)
    env_path = ROOT / ".env"
    if env_path.exists():
        for raw in env_path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            env.setdefault(key.strip(), value.strip())
    return env


def inspect_environment() -> Environment:
    hermes = shutil.which("hermes") is not None
    browser_use_python = (ROOT / ".venv-browser-use/bin/python").exists()
    env = read_env_file()
    browser_use_api_key = bool(env.get("BROWSER_USE_API_KEY") or env.get("OPENAI_API_KEY"))
    tools = command_output(["hermes", "tools", "list"]) if hermes else ""
    computer_use_enabled = bool(re.search(r"enabled\s+computer_use|computer_use", tools))
    cua_driver = Path("/Applications/CuaDriver.app/Contents/MacOS/cua-driver").exists()
    return Environment(
        hermes=hermes,
        browser_use_python=browser_use_python,
        browser_use_api_key=browser_use_api_key,
        computer_use_enabled=computer_use_enabled,
        cua_driver=cua_driver,
    )


def decide(task: str, mode: str) -> Decision:
    text = task.lower()
    env = inspect_environment()
    warnings: list[str] = []

    if contains_any(text, STOP_WORDS):
        surface = "stop"
        reason = "The task mentions a human-verification, legal, payment, tax, or publish gate."
        next_command = None
        handoff = "Ask the user to complete or explicitly confirm this gate in the real UI before continuing."
    elif mode != "auto":
        surface = mode
        reason = f"User/operator forced mode={mode}."
        next_command, handoff = command_for_surface(surface, task, env)
    elif contains_any(text, API_WORDS):
        surface = "api/connector"
        reason = "The task appears to have a purpose-built connector or API path."
        next_command = None
        handoff = "Use the connector/API first. Fall back to browser/computer use only if authentication or coverage blocks the API path."
    elif contains_any(text, NATIVE_UI_WORDS) or (
        contains_any(text, REAL_CHROME_WORDS) and ("current" in text or "already open" in text)
    ):
        surface = "computer_use/CuaDriver"
        reason = "The task needs the current visible Chrome session, native macOS UI, uploads, or desktop handoff."
        next_command, handoff = command_for_surface(surface, task, env)
    elif contains_any(text, REAL_CHROME_WORDS):
        surface = "browser-use-real-chrome"
        reason = "The task needs authenticated Chrome state but does not clearly require native UI."
        next_command, handoff = command_for_surface(surface, task, env)
    elif contains_any(text, ORDINARY_WEB_WORDS):
        surface = "browser-use"
        reason = "The task is an ordinary web workflow suitable for Browser Use."
        next_command, handoff = command_for_surface(surface, task, env)
    else:
        surface = "hermes-browser"
        reason = "No stronger signal was found; use simple browser tools first and switch if blocked."
        next_command, handoff = command_for_surface(surface, task, env)

    if surface.startswith("browser-use") and not env.browser_use_python:
        warnings.append("Browser Use is not installed. Run: bash scripts/install_browser_use.sh")
    if surface.startswith("browser-use") and not env.browser_use_api_key:
        warnings.append("Browser Use needs .env with BROWSER_USE_API_KEY or OPENAI_API_KEY.")
    if surface == "computer_use/CuaDriver" and not env.computer_use_enabled:
        warnings.append("Hermes computer_use toolset may not be enabled.")
    if surface == "computer_use/CuaDriver" and not env.cua_driver:
        warnings.append("CuaDriver is not installed at /Applications/CuaDriver.app.")

    return Decision(
        control_surface=surface,
        reason=reason,
        stop_gates=STOP_GATES,
        next_command=next_command,
        handoff_prompt=handoff,
        warnings=warnings,
        environment=env,
    )


def command_for_surface(surface: str, task: str, env: Environment) -> tuple[str | None, str | None]:
    quoted_task = shell_quote(task)
    if surface == "browser-use":
        return (
            f".venv-browser-use/bin/python scripts/run_browser_use_task.py --task {quoted_task}",
            None,
        )
    if surface == "browser-use-real-chrome":
        return (
            ".venv-browser-use/bin/python scripts/run_browser_use_task.py "
            f"--real-chrome --profile Default --task {quoted_task}",
            "Close duplicate Chrome windows if Browser Use cannot attach to the profile.",
        )
    if surface == "computer_use/CuaDriver":
        return (
            None,
            "Use computer_use/CuaDriver on Google Chrome. Capture first, act one step at a time, re-capture after every navigation/save/upload/modal.",
        )
    if surface == "hermes-browser":
        return (
            None,
            "Use Hermes browser tools. If authentication, native UI, or anti-bot appears, switch surfaces before continuing.",
        )
    return None, None


def print_text(decision: Decision) -> None:
    print(f"Control surface: {decision.control_surface}")
    print(f"Reason: {decision.reason}")
    print("Stop gates: " + ", ".join(decision.stop_gates))
    if decision.next_command:
        print("\nNext command:")
        print(decision.next_command)
    if decision.handoff_prompt:
        print("\nHandoff:")
        print(decision.handoff_prompt)
    if decision.warnings:
        print("\nWarnings:")
        for warning in decision.warnings:
            print(f"- {warning}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument(
        "--mode",
        default="auto",
        choices=[
            "auto",
            "api/connector",
            "browser-use",
            "browser-use-real-chrome",
            "hermes-browser",
            "computer_use/CuaDriver",
            "stop",
        ],
    )
    parser.add_argument("--json", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    decision = decide(args.task, args.mode)
    if args.json:
        print(json.dumps(asdict(decision), indent=2))
    else:
        print_text(decision)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
