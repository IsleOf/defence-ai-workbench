"""Print a task worktree plan; --apply explicitly creates local Git state."""
import argparse
import json
import re
import shlex
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def plan(repo, stream, agent, task):
    for value in (stream, agent, task):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
            raise ValueError("Use lowercase letters, numbers and single hyphens")
    branch = f"work/{stream}/{agent}/{task}"
    target = repo.parent / (repo.name + "-worktrees") / f"{stream}-{agent}-{task}"
    return ["git", "-C", str(repo), "worktree", "add", "-b", branch, str(target), "HEAD"]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stream", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--task", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    ids = {s["id"] for s in json.loads((ROOT / "workstreams/REGISTRY.json").read_text())["workstreams"]}
    if args.stream not in ids:
        parser.error("Unknown workstream")
    command = plan(ROOT, args.stream, args.agent, args.task)
    print(shlex.join(command))
    if args.apply:
        top = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"], text=True).strip()
        if Path(top).resolve() != ROOT.resolve():
            raise SystemExit("Run from the intended repository, not a nested checkout")
        dirty = subprocess.check_output(["git", "-C", str(ROOT), "status", "--porcelain"], text=True)
        if dirty.strip():
            raise SystemExit("Commit or resolve local changes first; worktree starts at committed HEAD")
        subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
