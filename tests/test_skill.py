import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _frontmatter():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = FRONTMATTER.match(text)
    assert m, "SKILL.md must start with YAML frontmatter `--- ... ---`"
    return m.group(1)


def _field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
    assert m, f"frontmatter missing '{key}'"
    return m.group(1).strip()


def test_required_files_present():
    for f in ["SKILL.md", "TEMPLATES.md", "PLATFORMS.md", "README.md", "LICENSE"]:
        assert (ROOT / f).is_file(), f"missing required file: {f}"


def test_frontmatter_has_name_and_description():
    fm = _frontmatter()
    _field(fm, "name")
    _field(fm, "description")


def test_name_is_lowercase_hyphens_and_short():
    name = _field(_frontmatter(), "name")
    assert re.fullmatch(r"[a-z0-9-]+", name), f"name must be lowercase-hyphens: {name!r}"
    assert not name.startswith("-") and not name.endswith("-"), "name must not start/end with hyphen"
    assert len(name) <= 64, f"name must be <= 64 chars, got {len(name)}"


def test_description_within_limit():
    desc = _field(_frontmatter(), "description")
    assert 0 < len(desc) <= 1024, f"description must be 1-1024 chars, got {len(desc)}"


def test_description_mentions_when_to_use():
    desc = _field(_frontmatter(), "description")
    assert "Use when" in desc or "use when" in desc, "description should say when to trigger"


def test_skill_md_under_500_lines():
    lines = (ROOT / "SKILL.md").read_text(encoding="utf-8").splitlines()
    assert len(lines) <= 500, f"SKILL.md is {len(lines)} lines, must be <= 500"


def test_referenced_files_exist():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    refs = re.findall(r"\]\(([A-Z_]+\.md)\)", text)
    for ref in refs:
        assert (ROOT / ref).is_file(), f"SKILL.md references missing file: {ref}"
