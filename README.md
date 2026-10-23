# Defence AI Workbench

A multi-workstream portfolio and collaboration hub for an independent application to Estonia's Defence Forces AI Accelerator. Drones are one specialization, not the umbrella identity.

## Thesis
Turn information and human expertise into useful, measurable AI capabilities: capture -> structure -> coordinate -> produce -> verify -> human decision -> controlled learning.

Proposed contribution: AI Systems / Product Engineer, connecting workflow automation, knowledge systems, forecasting, simulation, sensor data and evaluation. This is proposed positioning, not an official title or a claim of established expertise in every area.

## Start here
1. Read portfolio/THESIS.md and evidence/SOURCES.json.
2. Read COLLABORATION.md and AGENTS.md.
3. Select a workstream from workstreams/REGISTRY.json.
4. Agree one task with the user using collaboration/TASKS.json; do not assume proposed ownership is accepted.
5. Work on a task branch/worktree; submit a reviewed artifact or PR, not a direct main edit.

## Current status
Implemented: repository metadata/contracts, task backlog, collaboration instructions, local worktree planner and structural validator with tests. These tools do not implement the application capabilities. All domain workstreams are proposed or research-stage. No automatic agent integration, paid runs, deployment, branch protection or live GitHub Issues have been configured.

## Local commands
Requires Python 3.10+ and Git for worktrees. No third-party Python dependencies.

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/setup_worktrees.py --stream knowledge-evidence --agent codex --task brief-001
# Review the printed command before adding --apply.
```

Git worktrees are local directories, not GitHub-hosted execution environments or security sandboxes. No local worktrees have been created on the user's computer by this scaffold.

## Shared context
GitHub is the durable project hub; separate chats are not a shared memory bus. ChatGPT/Gemini need their own authorized repository access or an uploaded snapshot. Browser research sessions can return a handoff without direct write access; coding integrations can propose branches and PRs if separately configured.

agentic-universe remains the canonical general-purpose graph. This is a defence-focused projection; proposed generic improvements go upstream only after review. Do not copy the entire graph or silently change its canonical files.

## Boundaries
Synthetic, public or explicitly authorized nonsensitive data only. No classified material belongs on this GitHub repository, private or otherwise. No weapon integration, autonomous targeting, interception or combat navigation implementation. No military deployment, clearance, partnership, funding award or performance claim is established by this project. No license is granted by this initial draft; choose one before public release.
