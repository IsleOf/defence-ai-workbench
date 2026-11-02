# G01 Evidence Audit — ChatGPT execution

- **Audit date:** 2026-11-02
- **Repository:** `IsleOf/defence-ai-workbench`
- **Base:** `760a5344707db6297462bd8578f17dee49d8d737` (`origin/main` at clone time)
- **Local branch:** `work/knowledge-evidence/chatgpt/g01`
- **Task:** G01 — verify source coverage; distinguish historical ideas from new connections.
**Authorship/access note:** The product owner selected G01. This is ChatGPT's local audit, **not a Gemini-produced report**. The supplied Gemini conversations were not accessible in the earlier read-only check. C01 had been read during the earlier project-context check, so this is **not a blind independent review**; I did not consult its branch while drafting G01. In the cloned `main` snapshot, G01 remains proposed/unowned; the user's selection is recorded in chat, not published to the task registry. No push, PR, merge, or change to the canonical Agentic Universe checkout was made.

## Executive finding

The workbench has a coherent proposed theme: provenance-linked workflows that capture and structure information, produce a checkable result, measure it, and preserve human review. The repository already labels many claims as proposed, research-stage, or unknown. Its largest evidence weakness is not the absence of ideas; it is that several S04 research notes cite transient web-search IDs instead of durable source links, and some specific claims are over-attributed or stripped of their experimental limits.

The current public Estonian Defence Forces Force Transformation Command page describes AI use spanning day-to-day staff/support work, data and situational awareness, decision support, testing, and traceable use. This is **thematic alignment only**; it does not verify the user-provided vacancy, its requirements, a relationship with the Defence Forces, or the candidate's ability to deliver any capability. [Official page](https://mil.ee/en/landforces/force-transformation-command/)

## Source coverage and limits

| Source | Audit result | Permitted use in the portfolio |
|---|---|---|
| **S01 — job advertisement** | `evidence/SOURCES.json` says the ad was pasted on 2026-10-23, but the ad text or a stable employer URL is not in this repository snapshot. `THESIS.md` records a 2026-10-31 deadline; that date is past as of this audit, and was not independently verified against the employer. | Do not quote requirements, role title, or vacancy status as verified until the original ad or official listing is restored and checked. The current Force Transformation Command page is not a substitute for a job posting. |
| **S02 — architecture/foundations** | The named path exists at the inspected local Agentic Universe `HEAD` (`4e50223c4aa04b1d90593d64f30178f43d513475`), but its content was not read in this G01 pass. The source register describes its support as design patterns. | Treat the register's description as provenance metadata only; do not infer implementation or reliability from path existence. |
| **S03 — archived conversations** | Both paths named in the source register exist at that local `HEAD`, but their content was not read in this G01 pass. The source register describes them as conceptual evaluation/handoff patterns. | Use only as leads for attributed historical concepts; do not treat path existence as implementation or employment evidence, or turn assistant suggestions into user achievements. |
| **S04 — four research notes** | All four notes were read from their recorded historical commits (see references). They demonstrate prior research activity. Their inline web-search IDs are not durable citations, so most claims cannot be audited from the note alone. Selected primary-source claims were rechecked below. | Research interests and hypotheses only. Do not present the notes as user-built systems, operational results, or current product status. |
| **S05 — private Drive artifacts** | A metadata-only lookup confirmed `estonian_fpv_swarm.md` exists (reported size 12,374 bytes; modified 2025-12-28). Its contents were **not read or copied**, in keeping with the project boundary against reproducing weaponization material. An initial recursive filename lookup timed out after 300 seconds. A targeted exact-name/path check did not locate the energy-comparison item; after a scoped listing showed the parent folder was mixed, I stopped further enumeration. | The source register's “historical breadth” label is appropriate. Neither artifact supports performance, funding, readiness, or implementation claims in this audit. Energy-source coverage remains unknown. |
| **S06 — retrieved memory** | The register itself calls this incomplete and non-verbatim. | Leads for finding original material, not proof of exact wording, ownership, or outcomes. |

## S04 claim checks

These checks validate selected historical claims, not the full technical literature or current state of the art. The papers below were submitted in August/September 2026; they are used to audit those older notes, not as automatically current evidence.

1. **SwarmWorld / stigmergic reuse — substantially supported, but simulation-bounded.** The primary paper reports approximately 95% of first adoption beginning with physical observation. Its evidence comes from agent societies in a deterministic simulated world, with four matched seeds in key studies. The structural-knockout assay measures graph connectivity; the authors explicitly distinguish it from physical recovery after agents disappear from a running world. Preserve the number only with those limits. [Paper](https://arxiv.org/html/2608.26081v1)
2. **AgentPanel — statistic is accurate, inference must stay narrow.** The paper reports a 20-person human study; 65% favored AgentPanel for breadth of research directions, while preferences were more mixed for feasibility (45% favored it, 25% favored their usual tools, 30% saw no difference). This supports an exploratory-workflow hypothesis, not general superiority or defence-task performance. [Paper](https://arxiv.org/html/2608.03283v1)
3. **History Matters — proposal, not field proof.** The paper proposes history-dependent delegation policies and a monetary collaboration mechanism in heterogeneous multi-agent reinforcement learning. Its abstract does not establish that these mechanisms are suitable for the workbench or improve real-world outcomes. [Paper](https://arxiv.org/html/2608.03833v1)
4. **SkillBloat — numerical range checks out in its evaluated configurations.** The current arXiv version reports average-best token amplification from 5.4184× to 10.1455× across four tested agent/backend configurations. This is a controlled resource-abuse study, not a measurement of this portfolio's systems or a universal rate. The note should keep the benchmark/configuration attached to the number. [Paper](https://arxiv.org/html/2608.21929v2)
5. **SKILL.state — 93.8% is a derived conversion, not the paper's wording.** The paper reports 1,062,387 versus 65,408 cumulative tokens at horizon T=100 (16.2× fewer). The corresponding reduction is 93.83%; the report's 93.8% is numerically consistent, but should be marked derived and kept attached to that benchmark. The paper reports results on controlled warehouse/repository tasks, not a production reliability guarantee. [Paper](https://arxiv.org/html/2608.26263v3)
6. **Compaction safety rates in the attack-surface note — unresolved.** The stated 0%→30% and up-to-59% violation rates are attached only to transient search IDs, with no stable paper title, URL, version, or table in the note. Do not repeat them until a primary source and exact experiment are added.
7. **“OpenMAIC (MIT)” and 80%/100-step role adoption — attribution gap.** The current official OpenMAIC repository describes an interactive classroom project under THU-MAIC and lists an MIT license. The repository does not substantiate the note's 80%-within-100-steps role-emergence result. “MIT” may refer to the license rather than the institution; the intended source and statistic remain unverified. [Official repository](https://github.com/THU-MAIC/OpenMAIC)
8. **Anthropic's 60-subagent example — counts are supported; role labels were embellished.** Anthropic describes two agents developing key mathematical ideas, 13 contributing ideas, 30 attempting but unable to develop new ideas, 13 validators, and two writers. The note's labels “planners,” “context-feeders,” “idea-generators,” and “synthesizers” are interpretations, not the source's stated categories. It is one mathematics task, not a general staffing ratio. [Anthropic report](https://www.anthropic.com/research/riemann-zeta)

The prediction-market note is a documented interest in timestamped evidence, calibration, replay, and evaluation. Trading platforms, profit claims, and current repository status are time-sensitive and not evidence of a defence advantage or of the user's experience. If reused, retain the evaluation ideas and omit any implication of live trading or demonstrated edge.

## Historical ideas vs. synthesis vs. implementation

- **Historical themes represented in the source register:** workflow/computer-use automation; graph-based knowledge and research handoffs; forecasting and calibration; simulation; prerecorded sensor/platform material; resource/compute contracts; and human–AI coordination. Because S01/S05/S06 are incomplete or not content-reviewed here, the exact wording and provenance of each theme should remain qualified.
- **Prior assistant synthesis, not verbatim user evidence:** the common capability loop in `portfolio/THESIS.md`, the “AI Systems / Product Engineer” positioning, and the mapping of historical topics into the current workstreams. These are useful framing proposals, not proof of a user-authored unified strategy or of employment capability.
- **Inspected artifacts:** the four S04 research-note contents were read at their fixed commits; S02/S03 path existence was checked but their contents were not read; the task registry and portfolio thesis were read in the defence-workbench clone.
- **Implemented result:** per the current README, the repository has planning metadata/contracts, a task backlog, a worktree planner, and a structural validator/tests. The domain workstreams remain proposed or research-stage. No application capability, field deployment, partner, funding award, clearance, or performance result is established.
- **New proposals below:** authored for this audit; do not relabel them as historical user ideas.

## New cross-workstream connections to consider

All items below are **new design proposals**, not existing systems or claims about military operations. Keep any first demo synthetic/public and non-operational.

1. **Source-to-brief evidence chain:** connect staff-work automation → source/provenance records → knowledge/evidence brief → human review. Track citation coverage, stale/missing sources, reviewer corrections, and turnaround time. This is the most coherent small portfolio slice because it links automation and knowledge without needing sensitive data.
2. **Forecast-to-simulation evaluation loop:** connect timestamped public/synthetic forecasts to repeatable simulation scenarios and an independent assurance report. Freeze inputs and baselines; report calibration, scenario pass/fail, and failure cases. This converts the S04 interest in forecasting and simulation into an evaluable experiment, without market trading or operational recommendations.
3. **Sensor-to-evidence quality path:** define metadata and quality checks for prerecorded or synthetic observations, then link accepted observations to a scenario or brief. Measure missing/stale data handling, timestamp integrity, and transformation traceability. No real sensor feeds or operational locations are assumed.
4. **Compute/readiness lineage:** attach resource estimates, job versions, outputs, and failure/recovery records to the same evidence contract. This links compute, resource trade-offs, and resilience while avoiding unsupported readiness or platform-performance claims.

The public Force Transformation Command description makes the first and fourth connections thematically relevant: it describes staff/support use, a chain from data/situational awareness to decisions, and tested, secure, monitored, traceable use. It does **not** validate these proposed designs or establish that the user has implemented them. [Official page](https://mil.ee/en/landforces/force-transformation-command/)

## Recommended corrections before any public reuse

1. Restore S01 as a user-reviewed, sanitized source record or official employer URL; verify whether the vacancy remains relevant before repeating the 2026-10-31 deadline.
2. Replace every ephemeral search-result marker in S04 with a stable URL/DOI, exact paper version, publication/revision date, claim-to-source mapping, and retrieval date.
3. Correct the OpenMAIC attribution; mark the 80%/100-step claim unknown unless its primary source is identified.
4. Replace the Anthropic role labels with the source's actual descriptions; present counts as one-task observations only.
5. Label all S04 results as research evidence, all thesis integrations as prior assistant synthesis, and the four connections above as new proposals.
6. Keep S05's weaponization material out of the public workbench. Add no S05 technical claim unless a human-reviewed, nonsensitive excerpt and its source provenance are explicitly authorized.

## Stable references

### S04 note snapshots inspected

- [Prediction-markets branch note](https://github.com/IsleOf/agentic-universe/blob/0381f69626567b72339e2432442486ed678e558c/knowledge/notes/prediction-markets-branch-2026-09.md)
- [Human–LLM hybrid-cycle note](https://github.com/IsleOf/agentic-universe/blob/5e4c943aec047066f119ac06fc6cb216b5eda4ab/knowledge/notes/human-llm-hybrid-cycle-2026.md)
- [Attack-surface and supply-chain note](https://github.com/IsleOf/agentic-universe/blob/78b93572f507632c64cc6f234a2bf06ffe90e8e2/knowledge/notes/attack-surface-supply-chain-2026.md)
- [Role-specialization and decentralized-coordination note](https://github.com/IsleOf/agentic-universe/blob/efcf734a8bb956b0ae16307d251a84526b88079d/knowledge/notes/role-specialization-decentralized-2026.md)

### Primary checks

The linked arXiv papers, official OpenMAIC repository, Anthropic report, and Estonian Defence Forces page are linked inline at the claims they support. The S04 note snapshots above are fixed to the exact commits read for this audit.

## Universal handoff

- **Task/stream:** G01 / knowledge-evidence.
- **Actor:** ChatGPT; G01 scope selected by the product owner. Not Gemini-authored.
- **Base and branch:** `760a5344707db6297462bd8578f17dee49d8d737`; local `work/knowledge-evidence/chatgpt/g01`.
- **Artifact:** `evidence/gemini-audit.md` (this file, local only).
- **Sources inspected:** repository onboarding/portfolio/task files; four S04 notes at recorded historical commits; metadata only for the named S05 swarm file; official public source pages and selected primary papers listed above.
- **Tests:** `python scripts/validate.py` passed (10 workstreams, 4 tasks, 6 sources); `python -m unittest discover -s tests -v` passed (7 tests); `git diff --check` passed. These checks validate repository scaffolding, not domain capability claims.
- **Limitations:** S01 ad text and S05 energy document not available in the audited packet; S05 swarm file not read; S04 audit is selective; Gemini conversation content inaccessible; no independent candidate-experience evidence; not a blind independent review because C01 had been seen earlier.
- **Decision required:** product-owner review before this draft is copied, committed, pushed, or published. No remote changes made.
