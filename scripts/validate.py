"""Structural checks only; not evidence verification or security certification."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATES = {"proposed", "claimed", "in_progress", "review", "accepted", "blocked", "rejected"}

def validate(root=ROOT):
    registry = json.loads((root / "workstreams/REGISTRY.json").read_text())
    tasks = json.loads((root / "collaboration/TASKS.json").read_text())["tasks"]
    sources = json.loads((root / "evidence/SOURCES.json").read_text())["sources"]
    ids = [s["id"] for s in registry["workstreams"]]
    assert len(ids) == len(set(ids)), "Duplicate stream ID"
    source_ids = [s["id"] for s in sources]
    assert len(source_ids) == len(set(source_ids)), "Duplicate source ID"
    task_ids = [t["id"] for t in tasks]
    assert len(task_ids) == len(set(task_ids)), "Duplicate task ID"
    assert registry["shared_contract"]["status"] in STATES
    for stream in registry["workstreams"]:
        for key in ("problem", "expected_artifact", "acceptance", "non_goals"):
            assert stream.get(key), f"Missing {key}"
        path = Path(stream["expected_artifact"])
        assert not path.is_absolute() and ".." not in path.parts, "Unsafe artifact path"
    for task in tasks:
        assert task["stream_id"] in ids, "Unknown stream"
        assert task["status"] in STATES, "Unknown task state"
        assert set(task["input_sources"]) <= set(source_ids), "Unknown source"
        if task["status"] in {"claimed", "in_progress", "review", "accepted"}:
            assert task["owner"], "Owned state requires owner"
        if task["status"] == "accepted":
            assert task["review"], "Acceptance requires review record"
    for name in ("README.md", "AGENTS.md", "COLLABORATION.md", "GEMINI.md", "portfolio/THESIS.md"):
        assert (root / name).is_file(), f"Missing {name}"
    return {"workstreams": len(ids), "tasks": len(tasks), "sources": len(sources)}

if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
