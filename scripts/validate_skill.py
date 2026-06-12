#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "skills/productivity/browser-computer-automation/SKILL.md"
content = skill.read_text(encoding="utf-8")

assert content.startswith("---"), "SKILL.md must start with frontmatter"
end = content.find("\n---\n", 3)
assert end != -1, "SKILL.md frontmatter must close with ---"

frontmatter = content[3:end]
fields = {}
for line in frontmatter.splitlines():
    if ":" in line and not line.startswith(" "):
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"')

assert fields.get("name") == "browser-computer-automation", "wrong skill name"
assert fields.get("description"), "missing description"
assert len(fields["description"]) <= 1024, "description too long"
assert content[end + 5 :].strip(), "empty skill body"
assert len(content) <= 100_000, "skill file too large"

print("OK:", fields["name"], "chars:", len(content), "description:", len(fields["description"]))

