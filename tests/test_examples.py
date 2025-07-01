import json
import re
from pathlib import Path

import pytest

from scripts.parse_markdown_examples_to_json import parse_markdown_examples_to_json

PROBLEMS_DIR = Path(__file__).parent.parent / "obsidian" / "problems"


def extract_example_blocks(md_text: str):
    match = re.search(r"## Примеры\s+(.*?)(?:\n## |\Z)", md_text, re.DOTALL)
    if not match:
        return None, None
    block = match.group(1)
    json_match = re.search(r"```json\s*(\{.*?})\s*```", block, re.DOTALL)
    if not json_match:
        return block, None
    try:
        return block, json.loads(json_match.group(1))
    except json.JSONDecodeError:
        return block, None


def get_test_cases():
    cases = []
    for md_path in PROBLEMS_DIR.glob("*.md"):
        print(f"Checking {md_path}")
        with open(md_path, encoding="utf-8") as f:
            content = f.read()
        block, expected_json = extract_example_blocks(content)
        print(f"Found block: {bool(block)}, json: {bool(expected_json)}")
        if block and expected_json:
            cases.append((md_path.name, block, expected_json))
    print(f"Total test cases: {len(cases)}")
    return cases


@pytest.mark.parametrize("filename,example_block,expected_json", get_test_cases())
def test_parse_examples(filename, example_block, expected_json):
    parsed = parse_markdown_examples_to_json(example_block)
    actual = parsed

    def normalize(obj):
        pretty = json.dumps(obj, indent=2, ensure_ascii=False)
        pretty = re.sub(
            r'\[\s+([^\[\]]+?)\s+]',
            lambda m: '[' + m.group(1).replace('\n', '').replace(' ', '') + ']',
            pretty
        )
        return pretty

    assert normalize(actual) == normalize(expected_json), f"Ошибка в файле {filename}"
