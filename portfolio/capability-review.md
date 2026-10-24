# C01 — Capability architecture review

- **Repository:** IsleOf/defence-ai-workbench
- **Reviewed base:** `760a5344707db6297462bd8578f17dee49d8d737`
- **Date:** 24 October 2026
- **Actor:** ChatGPT
- **State:** Review artifact; not accepted conclusions or implemented capability
- **Independent review:** Perplexity review posted by IsleOf on PR #1, comment 6382047456, inspected for this revision. This is not completed P01 reconciliation or product-owner acceptance.
- **Final approver:** Product owner

## 1. Overall assessment

The portfolio has a coherent organizing thesis: turn information and human expertise into bounded, verifiable work, preserve human decision authority, and improve procedures through reviewed evidence. This connects staff automation, knowledge, forecasting, simulation, sensor data and resilience without making drones the umbrella.

The strongest common foundation is **traceable task execution and evaluation**, not a universal AI platform. The proposed streams become a capability architecture only when they exchange named, versioned artifacts and demonstrate a useful outcome for a specified user. At the reviewed base, their integration remains a design proposal.

The three-layer distinction in THESIS is useful. Platform and assurance are shared foundations; staff, knowledge, forecasting, training, sensors and resilience are applications; coordination research supplies optional alternatives. Coordination research should not become a prerequisite for delivering an ordinary useful workflow.

A concise application thesis would be: **I propose to connect workflow discovery, source-linked knowledge and bounded evaluation so that a user can see what an AI-assisted process did, why its output is supported, and whether it actually helped.** This is proposed positioning, not evidence of prior delivery or employment.

The job advertisement supports this direction through its emphasis on user benefit, reliable data, traceability, testing and human decisions. It does not validate this project's usefulness, the applicant's experience, or any field-readiness claim.

## 2. Evidence scope and availability

Project evidence was inspected at the base above. Upstream sources were inspected separately at `IsleOf/agentic-universe@5927fb9426fe9475c8c97846f63b60f9f640f128`. That is the revision retrieved during C01; it is not established as the revision used by the scaffold author.

| Source | C01 access and inspection | What it establishes; what it does not |
|---|---|---|
| S01 | Job advertisement available in this conversation | Supplied requirements and scope; employer verification remains outstanding |
| S02 | Read `architecture/foundations.md` at the upstream revision | Documented bounded-loop, artifact-edge and knowledge-promotion principles; no operational implementation established |
| S03 | Read both named August 31 archives | Conceptual handoffs, approval and evaluation patterns. The measured-loops archive explicitly says the original X article was not fully retrieved and no experiments ran |
| S04 | Read all four named notes | Documented research directions. External papers, vendor status, numerical results and comparative claims were not independently verified |
| S05 | **Unavailable to the C01 author:** private Drive documents `estonian_fpv_swarm.md` and the unnamed energy document were not supplied/read | Their descriptions in SOURCES/THESIS are available; their contents and alleged errors are not independently established by C01. Perplexity reports access and observations in review comment 6382047456; those are separately attributed reviewer evidence, not direct C01 inspection |
| S06 | **Unavailable as an original source packet:** the named April/July/August/October conversations and retrieval records are not attached or uniquely addressable here | The source-register summary is available. It cannot establish exact wording, authorship or full historical coverage |

S02–S04 are no longer unavailable to this reviewer. Their underlying external research and implementation evidence remain unverified. References to a tool or schema inside a note do not establish that its code exists, runs correctly or implements the claimed ability.

Project files inspected: README.md, AGENTS.md, COLLABORATION.md, GEMINI.md, portfolio/THESIS.md, evidence/SOURCES.json, workstreams/REGISTRY.json, collaboration/TASKS.json, scripts/validate.py, scripts/setup_worktrees.py, tests/test_project.py, .github/pull_request_template.md and .gitignore. The recursive tree listing was not truncated and confirmed 13 files at the reviewed base. The earlier local portfolio/ZIP was not used as repository evidence. No other reviewer's conclusions were consulted for the initial first pass. Perplexity comment 6382047456 was subsequently read to prepare this revision.

## 3. Findings

Priority: **P1** before making consequential application claims or implementing the selected slice; **P2** before extending the architecture. Classification separates observed document properties from unproven runtime behavior.

### C01-F01 — Map lifecycle abstraction levels and define a user outcome
- **Priority:** P1 for user/outcome definition; P2 for lifecycle mapping.
- **Affected artifact:** README, THESIS, REGISTRY.
- **Evidence:** README uses capture/structure/coordinate/produce/verify/human decision/controlled learning; THESIS uses observe/normalize/split/execute/verify/correct/gate/merge/learn. REGISTRY's intended user is explicitly unvalidated.
- **Classification:** Different abstraction levels and missing user validation; no demonstrated lifecycle contradiction or architectural failure. A mapping is sufficient.
- **Consequence:** Streams can satisfy local paperwork while optimizing different ideas of success.
- **Recommended change:** Map the two descriptions to shared semantic stages, retaining appropriate abstraction levels and optional stages and a user/problem/outcome for each selected pilot. Separate artifact verification from user-benefit evaluation.
- **Verification criterion:** Both thesis descriptions map to the same lifecycle; each selected pilot names a user, a task, baseline and measured outcome. Uninterviewed users remain hypothetical.

### C01-F02 — Claim-level provenance is missing
- **Priority:** P1.
- **Affected artifact:** SOURCES, THESIS history table, proposed ResultRecord.
- **Evidence:** S03 and S04 group multiple documents; S05 lacks a unique identifier for the energy document; S06 groups conversations. ResultRecord lists claims/evidence without a claim-edge schema.
- **Classification:** Demonstrated traceability gap; not evidence that the underlying historical claims are false.
- **Consequence:** Reviewers cannot reliably distinguish original user ideas, assistant elaborations, document existence and validated performance.
- **Recommended change:** Give each consequential claim an ID, category, exact statement, source revision/locator, support relation, verification status and limitations. Distinguish unavailable, not inspected and inspected-but-unverified.
- **Verification criterion:** Every demonstration headline can be traced to an exact passage or reproducible result; absent original sources produce an explicit gap, not an invented attribution.

### C01-F03 — Cross-stream outputs lack reproducibility and invalidation rules
- **Priority:** P1.
- **Affected artifact:** THESIS interfaces; platform-core.
- **Evidence:** SourceRecord has a digest and TaskRecord a base commit, but the proposed interfaces do not explicitly bind an artifact digest, schema version, model/tool configuration, parent inputs and review to one result version.
- **Classification:** Specification gap; no stale-result incident demonstrated.
- **Consequence:** An upstream change can leave downstream summaries, forecasts or approvals appearing current.
- **Recommended change:** Define a ResultEnvelope with artifact reference/digest, schema version, input versions, producer/configuration versions, test evidence and review reference. Mark dependent outputs stale when relevant inputs change.
- **Verification criterion:** Declare each result's relevant dependencies and invalidation policy. A changed dependency digest, schema, computation-affecting configuration or evaluation/approval policy marks affected outputs stale; cosmetic metadata and unrelated configuration edits do not. Test both an invalidating change and an irrelevant change. Unchanged inputs can be replayed with declared deterministic or stochastic limits.

### C01-F04 — Authority and approval semantics need separate contracts
- **Priority:** P1.
- **Affected artifact:** shared_contract, TaskRecord, ResultRecord, platform-core.
- **Evidence:** REGISTRY says humans approve scope/consequential outputs; interfaces do not specify permitted actions, approving identity, scope, expiry, revocation or approval invalidation.
- **Classification:** Specification gap; no security bypass demonstrated.
- **Consequence:** “Reviewed” may be mistaken for authorization to execute or reuse data.
- **Recommended change:** Separate task permission, evidence handling and artifact review. Define a synthetic ApprovalRecord bound to an exact artifact/action and authorized reviewer. For the record-only first slice, use self-declared synthetic reviewer records and rejection fixtures; defer production identity and authorization enforcement. Passing those fixtures does not establish authenticated authority.
- **Verification criterion:** Fixtures reject wrong-scope, revoked and changed-artifact approvals; a review verdict alone never authorizes an external action.

### C01-F05 — Reviewed learning has no promotion or rollback interface
- **Priority:** P1.
- **Affected artifact:** THESIS lifecycle; knowledge-evidence; assurance.
- **Evidence:** S02 forbids silent runtime rewrites of canonical knowledge; THESIS includes learning but does not define a KnowledgeChangeProposal or retirement procedure.
- **Classification:** Missing interface; no observed memory contamination.
- **Consequence:** A useful lesson, anecdote or model assertion can become a permanent rule without a clear evidential threshold.
- **Recommended change:** Specify proposed change, supporting/contradicting evidence, applicability, regression results, reviewer, version and reversal procedure. Repeated evaluation must include protection against overfitting to the test set.
- **Verification criterion:** First slice: runtime output can create only a proposal artifact, and stable knowledge remains unchanged. Promotion and executable rollback are later bounded tasks with separate authorization; their eventual tests must cover rejection, version-specific review and restoration of a named prior version.

### C01-F06 — Evaluation independence and forecasting/simulation validity are underspecified
- **Priority:** P1.
- **Affected artifact:** forecasting, simulation-training, assurance, coordination-research.
- **Evidence:** REGISTRY asks for point-in-time evidence, baseline scoring and measured transfer; it does not specify dataset splits, leakage checks, hidden labels or reviewer independence. COLLABORATION correctly says model agreement is not factual verification.
- **Classification:** Experimental-design gap; no demonstrated forecasting failure or simulation-transfer defect.
- **Consequence:** Hindsight, shared context or tuned synthetic cases can create misleading gains.
- **Recommended change:** Freeze cases, source cutoffs, scoring and baselines before evaluation. Assign whole scenario families to development or held-out sets using a versioned, seeded group manifest; variants of one underlying episode stay in one group. Keep outcome/fault labels in a separate scorer-only file/store, excluded from worker inputs, retrieval and prompts; log the input manifest. Preserve a held-out set; give independent checks access to source evidence rather than merely another model's conclusion.
- **Verification criterion:** A seeded post-cutoff record is excluded; outcome labels are hidden until scoring; results include all cases and failures. Synthetic success is labeled synthetic and does not establish operational transfer.

### C01-F07 — Upstream research contains claims unsuitable for promotion
- **Priority:** P1.
- **Affected artifact:** SOURCES S04 and any downstream application narrative.
- **Evidence:** The hybrid-cycle note asserts creativity unreachable by humans or LLMs alone; role-specialization notes contain 80%/100-step and roughly 95% reuse claims plus general “IQ gain” language. The threat-model note recommends removing zero-catch gates. These statements were read, but their external evidence and applicability were not verified.
- **Classification:** Observed strong assertions and a questionable proposed rule; not a finding that cited studies are fabricated or that a gate was removed.
- **Consequence:** Research leads can become unsupported superiority, reliability or safety claims.
- **Recommended change:** Preserve them as attributed hypotheses pending primary-source checks. Remove imported percentages and “IQ gain” from portfolio promises. Replace zero-catch removal with threat coverage, detection quality, missed-event and consequence analysis; an unused control may still be necessary.
- **Verification criterion:** No portfolio advantage claim rests only on these notes. Control retirement requires explicit threat/risk justification and human review, not a zero-catch count alone.

### C01-F08 — Readiness needs a neutral decision model, not a preferred-technology conclusion
- **Priority:** P2.
- **Affected artifact:** readiness-resilience, THESIS energy/fuel row, S05.
- **Evidence:** REGISTRY requires transparent inputs and neutral alternatives; the underlying energy document is unavailable. No defined decision owner, outage scenario, recovery horizon or validated dataset is supplied.
- **Classification:** Missing evidence and model scope, not a demonstrated energy-model error.
- **Consequence:** Broad advocacy could be presented as a defence-readiness result.
- **Recommended change:** Start with a fictional civilian support-service continuity problem and explicit dependency assumptions. Compare concentration, maintainability, replacement, inputs, costs and recovery; record what would change the preferred option.
- **Verification criterion:** Each ranking is traceable to assumptions; sensitivity tests expose ranking changes; no conclusion is generalized to actual Estonian readiness.

### C01-F09 — Structural checks do not validate the proposed runtime contracts
- **Priority:** P2.
- **Affected artifact:** README current status; validate.py; tests/test_project.py.
- **Evidence:** Seven bundled tests pass. The validator checks IDs, selected fields, states, source membership and some paths; it does not verify source truth, ResultRecord behavior, runtime permissions or functional benefit. Its docstring already states this limitation.
- **Classification:** Demonstrated bounded test coverage, not a defect against the validator's stated structural purpose.
- **Consequence:** “Contracts implemented” can be read more broadly than the actual planning checks support.
- **Recommended change:** Describe current code as planning-record validation/worktree planning. Add contract fixtures and behavior tests only for the chosen implementation slice; keep content verification and authorization separate.
- **Verification criterion:** Status text distinguishes planning checks from runtime capabilities; each new implemented behavior has appropriate positive and failure-case evidence.

### C01-F10 — Applicant evidence must remain separate from architecture breadth
- **Priority:** P1.
- **Affected artifact:** THESIS application positioning and future application material.
- **Evidence:** THESIS explicitly says five years' experience and clearance eligibility are unverified; README describes the role as proposed. Neither supplies a career ledger, shipped outcomes or language evidence.
- **Classification:** Missing applicant evidence; no invented experience identified in the reviewed scaffold.
- **Consequence:** A broad research portfolio may be mistaken for established responsibility across every domain.
- **Recommended change:** Add only user-confirmed employment/project dates, personal contribution, inspectable outputs and measured results. Separate AI-assisted drafting from work independently understood and demonstrated by the applicant.
- **Verification criterion:** Every career or delivery statement has a user-confirmed source; credentials and clearance claims remain absent unless established. Missing proof is not described as proof of ineligibility.

## 4. Proposed cross-workstream contracts

These are C01 proposals, not implemented schemas.

| Exchange | Producer → consumer | Minimum content and failure behavior |
|---|---|---|
| EvidencePacket | ingestion/sensor-data → knowledge/forecasting | Source ID, observed/acquired/available-at times, handling/rights, digest, locator, quality flags; reject or quarantine invalid inputs |
| ResultEnvelope | any worker → assurance/human review | Task/input versions, artifact digest, producer/configuration, claims, checks, errors and uncertainty; never convert a transport success into semantic acceptance |
| ForecastRecord | knowledge/forecasting → resilience/evaluation | Question, probability, cutoff, horizon, resolution rule, evidence versions and baseline; unresolved outcomes stay unresolved |
| ScenarioRecord | simulation → staff/sensor/assurance | Generator/version/seed, assumptions, permitted use, training/test split and hidden labels; synthetic lineage remains visible |
| ApprovalRecord | authorized human → narrowly scoped action | Actor, scope, artifact/action digest, decision, time and invalidation/revocation; fail closed where approval is required |
| KnowledgeChangeProposal | evaluated results → curated knowledge | Change, support, counterevidence, applicability, reviewer and rollback target; no automatic promotion |

Worktree isolation is a development convenience, not an authorization or data-security boundary. E01 should implement one narrow exchange rather than all six records.

## 5. Three bounded experiments

All thresholds below are proposed decision gates, not achieved results or statistical guarantees. Freeze the protocol before inspecting held-out outcomes. No paid runs, real operational data, external actions or participant recruitment are authorized by this review.

### C01-X01 — Source-linked support brief with reviewed procedure learning

**Streams:** staff-automation → knowledge-evidence → assurance; platform-core carries the task/result boundary.

- **User problem:** A hypothetical support administrator repeatedly reconciles inconsistent requests and explains the resulting procedure to another worker.
- **Inputs:** Twenty synthetic maintenance-request packets: ten development and ten held-out. Include duplicates, missing fields, conflicting dates and instructions embedded as untrusted source text. An independently authored answer key records expected omissions/conflicts.
- **Output:** A structured brief with claim-to-source links, exceptions, corrections, review verdict and one proposed procedure update. No real submission or canonical-memory modification.
- **Baseline:** A deterministic pipeline already validates required fields, normalizes dates, identifies exact duplicates, applies fixed conflict rules, preserves locators and renders a fixed brief template. Compare the same person's completion of that template against the assisted variant using matched packets and counterbalanced order. An optional AI component may propose a draft explanation or procedure summary only; record its input/output versions and incremental quality/time effects. No model is required for the first slice or added merely for presentation.
- **Acceptance:** Every consequential factual statement has a correct supporting locator or is explicitly unknown; every seeded critical conflict is surfaced; no embedded instruction causes an action; changed evidence marks the brief stale; an unapproved lesson does not enter curated knowledge. The 20% net-time-saving target is a provisional product hypothesis without a validated empirical basis, not a universal acceptance standard. Before held-out use, freeze critical-error classes (unsupported consequential assertion, missed critical conflict, incorrect disposition or unauthorized action), per-packet critical opportunities and all denominators. Report absolute baseline/assisted times, paired differences, drafting/checking/correction time separately, quality failures and every held-out case. Preserve a failed target as a result; do not retune or replace held-out cases to achieve it. A newly revised method requires a new untouched evaluation set.
- **Interpretation:** A small exploratory user trial cannot establish general workforce productivity. Without an independent participant, report only engineering behavior and author self-test timing.

### C01-X02 — Point-in-time continuity forecasts with transparent decisions

**Streams:** knowledge-evidence → forecasting → readiness-resilience → assurance.

- **User problem:** A hypothetical equipment-support coordinator must decide which routine fictional service dependencies deserve follow-up before a scheduled maintenance window.
- **Inputs:** A seeded synthetic event timeline for fictional services; thirty development and thirty held-out service-window outcomes, grouped to avoid train/test leakage. Each event has availability time. Reveal evidence only up to each forecast cutoff; hold outcome labels separately.
- **Output:** Versioned probability forecasts, supporting/counterevidence, unresolved assumptions, resolved outcomes and a scored comparison. A fictional follow-up recommendation uses a predeclared decision threshold, separate from the probability estimate.
- **Baseline:** An unconditional base-rate estimate fitted only on development data and a simple predeclared status rule. Freeze the primary comparison before scoring.
- **Acceptance:** No post-cutoff evidence is used; every forecast precedes resolution; excluded/unresolved cases are counted and explained; rerunning the same ledger reproduces scores. Report mean Brier score against both baselines and counts by group. Continue the improvement hypothesis only if it beats both on the fixed held-out set without raising the predeclared missed-critical-case count.
- **Interpretation:** Synthetic results test ledger/scoring mechanics only, not forecasting advantage, real forecasting skill, deployed calibration or national readiness. A developer-authored generator can reward assumptions embedded by that developer; score improvements remain mechanics findings until independently designed, untouched scenario families and suitable real point-in-time data support broader interpretation. Small samples do not support fine-grained calibration claims.

### C01-X03 — Fault-injected observation-to-handover pipeline

**Streams:** sensor-data → simulation-training → staff workflow → assurance; platform-core supplies versioning.

- **User problem:** A hypothetical facilities reviewer needs a clear handover when prerecorded benign observations are missing, old or contradictory.
- **Inputs:** Synthetic environmental measurements for a fictional training room. Use eight development and twelve held-out scenarios covering clean, single-fault and combined-fault cases, with missing intervals, duplicates, out-of-order records, stale values, incompatible units and conflicting sensors. Freeze a case/fault manifest and report scenarios, injected fault instances, detected/missed instances and false alarms with denominators by fault class; a combined-fault case can contribute to multiple class counts. Preserve generator version/seeds and hidden fault labels.
- **Output:** A quality-checked observation packet, source-linked handover, explicit unavailable/uncertain states and a reproducible fault report. No physical control or real flight/video data.
- **Baseline:** Deterministic parsing, approved unit conversions, exact-event deduplication, identity/revision checks, timestamp/freshness rules, fixed thresholds and a source-linked checklist already perform the integrity work. Compare any optional AI explanation against this identical pipeline plus template handover; AI is not the authority for validity, timestamps or quarantine. Keep X03 as a later extension, not part of the first implementation slice.
- **Acceptance:** All seeded critical integrity failures are flagged or quarantined; a stale observation is never labeled current; every accepted value has source/unit/time; clean fixtures have no critical false alarms. Repeat runs reproduce deterministic quality verdicts; human reviewers can locate each fault's supporting record. Report missed faults, false alarms, review time and abstentions.
- **Predeclared data policy:** Store observation time, arrival time and evaluation time separately. For the fictional room fixtures, require UTC times and declare freshness as evaluation time minus observation time no greater than a fixed protocol value (proposed: five minutes); arrival delay is a separate flag, and recent arrival never refreshes an old observation. Predeclare clock-skew handling (proposed: observations more than 30 seconds in the future are quarantined), and freeze values before evaluation. Identical event ID/revision/payload is a duplicate; same ID/revision with different payload is a conflict and is quarantined; a higher revision explicitly supersedes an earlier record and invalidates dependent results. Normalize only recognized, dimension-compatible units with a versioned conversion table; quarantine unknown/incompatible units while preserving originals.
- **Interpretation:** Zero misses on finite fixtures is not a reliability guarantee. Training transfer is not established. If later tested with volunteers, use held-out scenario families, consent and a predeclared rubric; measure explanation accuracy rather than claiming operational competence.

## 6. Two demonstrations to prioritize

### 6.1 First implementation slice — proposed, not authorized

Implement only an X01 record-only vertical slice after separate authorization: synthetic support request → deterministic EvidencePacket → fixed-template brief and ResultEnvelope → self-declared human review record. Use one composite serialized record with these small sections rather than six generalized schemas. Include task ID, source locators/digests, relevant dependency/configuration versions, artifact digest, limitations and a review verdict bound to that digest. Negative fixtures cover malformed input, changed relevant evidence and a review referring to the wrong artifact. Baseline behavior is the deterministic pipeline in X01; no AI-benefit claim is made unless an optional model condition is later justified and measured separately.

Explicitly out of the first slice: executable actions, production authentication/authorization, graph updates, learning promotion/rollback, forecasting, live sensor ingestion, distributed scheduling and platform construction. A procedure-learning output may be a proposal document only. X03 is the second demonstration direction, reusing this record once the first slice works; X02 remains deferred.

No implementation is authorized by approval to revise C01.


**First: X01, the evidence-backed support brief.** It is closest to the supplied job's staff/support work, explainability and product-engineering expectations. It demonstrates a user problem, data handling, human checking, artifact versioning and net utility in one inspectable workflow. Keep the first version deterministic where possible; add model assistance only as a measured comparison.

**Second: X03, the fault-aware observation handover.** It demonstrates data engineering, uncertainty, simulation-derived tests and traceability without weapon integration or live operational data. It broadens the portfolio beyond document automation while remaining bounded.

Use one shared ResultEnvelope/evidence contract across both. Two deep demonstrations are more credible than separate partial interfaces for every workstream. X02 remains a documented experiment for a later phase: its evaluation discipline matters, but credible real forecasting evidence needs time, outcome definitions and leakage controls.

Neither demonstration has been implemented or executed by C01.

## 7. Defer, remove or retain as context

**Defer implementation:** a universal AgentOS, GraphRAG by default, autonomous role emergence, large agent fleets, live integrations, a full sensor platform and production identity/security services. Adopt them only if a simple baseline exposes a specific need.

**Keep as research context:** forecasting, alternative coordination, infrastructure/energy/food dependencies and benign robotics/sensing. These help explain the applicant's systems thinking; they are not extra products promised for the application deadline.

**Remove from application claims:** inherited percentages, profit-to-defence analogies, “swarm IQ,” untested creativity superiority, fixed simulation-transfer rates, “jam-proof” claims, funding promises, broad deployment/readiness language and suggestions that multiple models agreeing establish truth.

**Do not import:** weaponization details, private raw conversations, unavailable source contents, classified/operational data or unverified career assertions. The current scaffold already excludes these; this review recommends maintaining that boundary.

Keep agentic-universe canonical. Any generic insight from C01 is a proposal for separate upstream review, not an instruction to change its graph. No new platform dependencies, paid services or automation are required to evaluate this review.

## 8. Verification actually performed

A local reconstruction of all 13 base files was obtained through exact-revision GitHub reads; it is separate from the earlier local portfolio and is not represented as a Git clone.

- `python scripts/validate.py`: PASS; 10 workstreams, 4 tasks, 6 sources.
- `python -m unittest discover -s tests -v`: PASS; 7 tests.
- The three experiments above: NOT RUN.
- User interviews, model benchmarks, security testing and functional capability tests: NOT RUN.
- External citations inside S03/S04 and linked implementation code: NOT independently verified or executed.
- No canonical upstream files, domain implementations or main-branch records were changed by this review.

These checks support scaffold consistency only. They do not establish the truth of historical claims, operational security, applicant qualifications or user benefit.

## 9. Review disposition and separate decisions

Review source: [Perplexity independent review](https://github.com/IsleOf/defence-ai-workbench/pull/1#issuecomment-6382047456), posted by IsleOf, created/updated 24 October 2026; reviewed artifact d66244b04aad8c8ac3fd5466832570ba464086fd. Attribution to Perplexity is supplied by the product owner and the comment heading, not inferred from the GitHub account.

### 9.1 Requested-change disposition

“Addressed” means incorporated into this report, not that a finding has been accepted or its recommendation implemented. No requested changes are disagreed with in this revision.

| Request | Disposition | Relevant section / change |
|---|---|---|
| F01 lifecycle severity | Addressed | §3 F01: user/outcome remains P1; abstraction mapping P2, no contradiction alleged |
| F02 consequential provenance scope | Addressed | §3 F02 already targets consequential claims and demonstration headlines; no every-sentence provenance requirement |
| F03 dependency-scoped invalidation | Addressed | §3 F03: declared relevant dependencies; invalidating and irrelevant-change fixtures |
| F04 synthetic review versus real authority | Addressed | §3 F04; §6.1: record-only review, production enforcement deferred |
| F05 staged learning | Addressed | §3 F05; §6.1: proposal only; executable promotion/rollback later |
| F06 reproducible groups/label isolation | Addressed | §3 F06: seeded versioned family manifest, scorer-only labels and worker-input manifest |
| F07 unverified claims and zero-catch gates | Addressed | §3 F07 retains documented proposed rule versus unobserved removal; retirement requires threat/risk review |
| F08 retain broad resilience context | Addressed | §3 F08 and §7 retain energy/resilience research with neutral alternatives |
| F09 planning tests versus capability | Addressed | §3 F09 and §8 keep structural checks separate from functional/security evidence |
| F10 career ledger/ineligibility distinction | Addressed | §3 F10 preserves user confirmation; absence of documentation is not ineligibility |
| X01 timing/20%/errors/denominators | Addressed | §5 X01: provisional threshold, absolute/paired times, burden, predefined critical errors, frozen denominators and no held-out retuning |
| X03 clean/single/combined faults and policies | Addressed | §5 X03: case/fault counts, three clocks, freshness/skew, duplicates versus revisions, conversion/quarantine and finite-fixture limits |
| X01/X03 deterministic versus AI benefit | Addressed | §5 X01/X03 and §6.1 enumerate deterministic behavior; optional AI contribution evaluated separately |
| X02 generator bias | Addressed | §5 X02: mechanics only until independent scenario-family evidence; no advantage claim |
| One thin first slice | Addressed | §6.1: one record-only X01 path with EvidencePacket/ResultEnvelope/review; no platform or six-schema implementation |
| S05 access is reviewer-specific | Addressed | §2 and §9.2: unavailable to this author; separately attributed Perplexity observations |
| Separate acceptance and authorization | Addressed | §9.3: three decisions; revision approval authorizes no implementation |
| Preserve independent G01 and explicit disagreement | Addressed | §9.4: G01 remains separate; no completed P01 reconciliation claimed |

### 9.2 Additional reviewer evidence

Perplexity reports direct access to staged S05 documents: a drone draft describes a pipeline as production-ready alongside prospective milestones, and an energy document frames its purpose around a preferred technology's advantages. These are the reviewer's content observations, not direct source inspection by this author, verified performance, a blanket technical refutation, or a basis to copy weaponization material. Obtain sanitized exact-revision passages if claim-level adjudication requires them. S06 original-history coverage remains incomplete; reviewer agreement does not fill that gap.

### 9.3 Three independent product-owner decisions

1. **Report acceptance:** receive/approve C01 as an adequately scoped review artifact, including its limitations. This does not accept every finding or threshold.
2. **Finding acceptance:** record accept/revise/reject/defer per finding ID, supporting reasons and any demonstration priorities. A reviewer recommendation or merge is not blanket substantive acceptance.
3. **Implementation authorization:** separately approve one task's artifact, allowed files/data, baseline, acceptance tests, owner and review. Accepting C01 or a finding does not authorize E01, model runs, integrations, paid services, deployment, canonical-graph edits or merges.

The current user instruction authorizes this report revision on its existing branch only. No product-owner finding dispositions or implementation authorization are inferred.

### 9.4 Next review

Request Perplexity's revision check through the existing review process; no separate message or assignment is sent by this revision. Gemini's G01 remains a separately attributable evidence audit. P01 reconciliation remains outstanding and must preserve concrete agreements, disagreements and source limits. The broader portfolio remains intact; only the proposed first implementation is narrowed.

## 10. Universal handoff

- **Task ID:** C01.
- **Stream:** portfolio.
- **Actor:** ChatGPT; bounded review authorized by the user in this conversation.
- **Base commit:** `760a5344707db6297462bd8578f17dee49d8d737`.
- **Revision parent:** `d66244b04aad8c8ac3fd5466832570ba464086fd`; existing branch `work/portfolio/chatgpt/c01`, draft PR #1.
- **Upstream snapshot:** `IsleOf/agentic-universe@5927fb9426fe9475c8c97846f63b60f9f640f128`; not assumed to be the scaffold author's source revision.
- **Files inspected:** the 13 project files and seven upstream files listed in section 2.
- **Sources:** S01 supplied advertisement; S02–S04 inspected documents; S05 unavailable to this author, with Perplexity's reported observations separately attributed; S06 original packets unavailable. External research claims remain unverified. Review comment 6382047456 inspected for this revision.
- **Artifact:** `portfolio/capability-review.md`.
- **Factual claims and evidence:** document/interface observations in F01–F10, source availability in section 2 and actual test results in section 8. Recommendations and experiment thresholds are new proposals.
- **Tests actually run:** structural validator and seven bundled unit tests; all passed in the reconstructed base snapshot and were repeated successfully with the revised review document. These checks do not validate experimental outcomes or source truth.
- **Limitations:** no source-wide implementation audit, domain experiments, interviews, operational assessment, qualification verification or current defence-capability research validation.
- **Disagreements:** initial first pass was independent; this revision addresses all requests in Perplexity comment 6382047456 with no disagreements. See §9.1. G01/P01 reconciliation remains outstanding.
- **Proposed next step:** revision review, separate report/finding dispositions, then separately scoped implementation authorization if desired. No E01 implementation is authorized.
- **Human decision required:** separate report acceptance, per-finding dispositions, demonstration priorities, implementation authorization and any merge. No acceptance is implied.
- **Repository delivery status:** report separately alongside this artifact; a branch/commit/PR must be confirmed by actual tool results.
