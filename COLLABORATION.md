# Shared collaboration protocol

## Where collaboration happens
GitHub repository: IsleOf/defence-ai-workbench. Documents and reviewed artifacts are durable context; task IDs coordinate work; branches/PRs carry proposed changes. GitHub Issues may later become the task board, but none are created by this scaffold. Until then collaboration/TASKS.json is the backlog.

The user is product owner and final approver, not a mandatory message relay if repository tools are available. No assistant is a permanent chief of staff. Select task ownership by availability and evidence; one accountable owner per task, with independent review where practical. Model agreement is not independent factual verification.

## Access modes
- ChatGPT browser: authorize GitHub access if available. OpenAI's GitHub app is documented as read-only; use Codex separately for code edits/pushes. Do not assume the two integrations share configuration.
- Gemini browser: import the authorized repository/code where available; repository context is not a promise of write access or continuous synchronization. Record the snapshot/commit and refresh before another task.
- Codex or Gemini CLI: with separately configured credentials, operate in a task-specific local clone/worktree and propose a branch/PR. Gemini CLI also has a GitHub Action integration, but no action is installed here.
- Perplexity: use its connected GitHub tools when available; external writes remain approval-gated.
- No repository access: upload the current ZIP or relevant files to the assistant and request a structured handoff or patch. Do not pretend it has inspected live main.

No assistant can read another provider's private chat automatically. Contribute a user-reviewed export or concise source packet; remove secrets and sensitive material first. Do not publish private chat links or bulk personal history by default.

## First-pass assignments, proposals only
ChatGPT: challenge the overall thesis, develop task C01, and identify unsupported career/capability claims.
Gemini: develop task G01, verify sources and surface missing connections with exact references.
Perplexity: maintain source provenance and task P01; reconcile only after independent first passes.
Coding agent: task E01, implement and test a bounded shared contract once scope is agreed.
Reviewers should first form an independent assessment before reading each other's conclusions, then compare disagreements. Roles can change; these are not capabilities guaranteed by a vendor.

## Task lifecycle
proposed -> claimed -> in_progress -> review -> accepted; alternatively blocked or rejected.
Task claim is a reviewed repository update or an acknowledged Issue assignment, not a race-safe distributed lock. If concurrent claims conflict, stop and ask the user to assign ownership.

1. Read README, AGENTS, the relevant source records and stream charter.
2. Record the actual base commit or label the context as a snapshot/unknown.
3. Agree one task, allowed files, artifact, success checks and reviewer.
4. Use branch work/<stream>/<agent>/<task>. Never share the same writable checkout concurrently.
5. Return a bounded artifact, evidence, test results, limitations and unresolved questions.
6. Review contradictions explicitly; do not replace uncertainty with a consensus paragraph.
7. User approves consequential conclusions, merges, publication, access changes and paid runs.
8. Accepted generic insights may be proposed upstream to agentic-universe; never silently promote them.

## Worktrees and credentials
Run the setup script locally in a clone; it prints a plan by default. Use --apply only after reviewing. Each task gets a separate branch and working directory. Worktrees share repository metadata and are not security boundaries. Keep agent credentials/configuration outside the shared project; separate auth paths alone do not replace real OS/container permission controls.

No automatic merges, paid model calls, bot workflows or branch protection are enabled. Branch protection and permissions must be configured explicitly if desired; AGENTS instructions do not enforce them.

## Universal handoff
Task ID; stream; actor; base commit/snapshot; files inspected; sources; artifact path or patch; factual claims and supporting evidence; tests actually run; limitations; disagreements; proposed next step; human decision required. Never claim a file was committed or a test ran unless it actually happened.

## Copy to ChatGPT
We are collaborating on private GitHub repository IsleOf/defence-ai-workbench for an Estonian Defence Forces AI Accelerator application. Read README.md, AGENTS.md, COLLABORATION.md, portfolio/THESIS.md, evidence/SOURCES.json and workstreams/REGISTRY.json. First establish your actual repository access and base commit; if unavailable ask for those files, not broader account access. Propose task C01: independently challenge the overall capability architecture, suggest real cross-workstream connections, and flag unsupported claims. Do not narrow the portfolio to drones, invent experience, modify main or publish. Return the universal handoff. If using read-only ChatGPT, provide a patch/handoff; use Codex separately only if configured and approved.

## Copy to Gemini
We are collaborating on private GitHub repository IsleOf/defence-ai-workbench. Import/read the current authorized repository or request the source packet. Read the same onboarding files and state snapshot/commit freshness. Propose task G01: independently audit the evidence map, find missing connections across automation, knowledge, forecasting, simulation, sensors, compute and resilience, and distinguish prior user ideas from new suggestions. Verify consequential claims against original sources; do not reuse old assistant citations as proof. Return the universal handoff. Do not assume browser import can push changes; use an approved coding integration or return a patch.

## Reference documentation
https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
https://workspaceupdates.googleblog.com/2025/06/upload-code-folders-and-github-repositories-to-gemini.html
https://github.com/google-github-actions/run-gemini-cli
https://git-scm.com/docs/git-worktree
Access and features depend on the actual account and workspace configuration. This scaffold does not connect other services on the user's behalf.
