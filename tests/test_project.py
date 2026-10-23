import json
import shutil
import tempfile
import unittest
from pathlib import Path
from scripts.validate import ROOT, validate
from scripts.setup_worktrees import plan

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    def tearDown(self):
        self.temp.cleanup()
    def edit(self, path, change):
        p = self.root / path
        data = json.loads(p.read_text())
        change(data)
        p.write_text(json.dumps(data))
    def test_valid(self):
        self.assertEqual(validate(self.root)["workstreams"], 10)
    def test_duplicate_task(self):
        self.edit("collaboration/TASKS.json", lambda d: d["tasks"].append(d["tasks"][0].copy()))
        with self.assertRaises(AssertionError): validate(self.root)
    def test_unknown_source(self):
        self.edit("collaboration/TASKS.json", lambda d: d["tasks"][0]["input_sources"].append("missing"))
        with self.assertRaises(AssertionError): validate(self.root)
    def test_unowned_claim(self):
        self.edit("collaboration/TASKS.json", lambda d: d["tasks"][0].update(status="claimed"))
        with self.assertRaises(AssertionError): validate(self.root)
    def test_unsafe_artifact(self):
        self.edit("workstreams/REGISTRY.json", lambda d: d["workstreams"][0].update(expected_artifact="../escape"))
        with self.assertRaises(AssertionError): validate(self.root)
    def test_plan_does_not_create(self):
        command = plan(self.root, "knowledge-evidence", "codex", "brief-001")
        self.assertIn("work/knowledge-evidence/codex/brief-001", command)
        self.assertFalse(Path(command[-2]).exists())
    def test_reject_bad_names(self):
        with self.assertRaises(ValueError): plan(self.root, "../bad", "codex", "task")

if __name__ == "__main__": unittest.main()
