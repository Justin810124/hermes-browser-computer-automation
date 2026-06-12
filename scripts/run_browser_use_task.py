#!/usr/bin/env python3
"""Run a Browser Use task with this project's safety prompt.

This script is intentionally small. It gives Hermes a concrete runner for
ordinary web tasks while keeping sensitive gates human-controlled.
"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SAFETY_BOUNDARY = """
Safety boundary:
- Do not bypass CAPTCHA, PerimeterX, reCAPTCHA, Cloudflare Turnstile, 2FA, device verification, identity, tax, payment, purchase, subscription, publish, or legal attestation gates.
- If one appears, stop and report exactly what requires human action.
- Do not inspect passwords, cookies, local storage, browser profile files, payment data, tax IDs, identity documents, or private tokens.
- Save drafts when asked, but do not publish or make irreversible external changes unless the user explicitly confirmed that exact action.
"""


def build_task(user_task: str) -> str:
    return f"{user_task.strip()}\n\n{SAFETY_BOUNDARY.strip()}\n"


def choose_llm():
    provider = os.getenv("HERMES_BROWSER_USE_LLM", "browser-use").strip().lower()
    model = os.getenv("HERMES_BROWSER_USE_MODEL", "").strip()

    if provider in {"browser-use", "browseruse", "cloud"}:
        from browser_use import ChatBrowserUse

        return ChatBrowserUse()

    if provider == "openai":
        from browser_use import ChatOpenAI

        kwargs = {}
        if model:
            kwargs["model"] = model
        return ChatOpenAI(**kwargs)

    raise SystemExit(
        f"Unsupported HERMES_BROWSER_USE_LLM={provider!r}. "
        "Use 'browser-use' or 'openai'."
    )


async def run(args: argparse.Namespace) -> None:
    try:
        from dotenv import load_dotenv
        from browser_use import Agent
    except Exception as exc:  # pragma: no cover - friendly runtime error
        raise SystemExit(
            "Browser Use is not installed. Run: bash scripts/install_browser_use.sh"
        ) from exc

    load_dotenv(ROOT / ".env")
    task = build_task(args.task)

    if args.dry_run:
        print("DRY RUN: Browser Use task prompt")
        print("=" * 40)
        print(task)
        print("real_chrome:", args.real_chrome)
        return

    llm = choose_llm()

    if args.real_chrome:
        from browser_use import Browser

        browser = Browser.from_system_chrome(profile_directory=args.profile)
        agent = Agent(task=task, llm=llm, browser=browser)
    else:
        agent = Agent(task=task, llm=llm)

    await agent.run()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True, help="Natural-language browser task")
    parser.add_argument(
        "--real-chrome",
        action="store_true",
        help="Use Browser.from_system_chrome() to preserve existing Chrome login state",
    )
    parser.add_argument(
        "--profile",
        default=None,
        help="Chrome profile directory, for example 'Default' or 'Profile 5'",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the final task prompt without running Browser Use",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    asyncio.run(run(args))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
