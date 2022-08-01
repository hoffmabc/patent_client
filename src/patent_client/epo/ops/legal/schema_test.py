from pathlib import Path
import json
import datetime
import lxml.etree as ET
from patent_client.util.test import compare_dicts
from .schema import LegalSchema
from patent_client.util import Model

test_dir = Path(__file__).parent / "test"
expected_dir = Path(__file__).parent / "test" / "expected"

def test_example():
    tree = ET.parse(test_dir / "example.xml")
    result = LegalSchema().load(tree)
    expected = json.loads((expected_dir / "example.json").read_text())
    compare_dicts(json.loads(result.to_json()), expected)
