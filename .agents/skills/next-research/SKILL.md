---
name: next-research
description: Scope an approval-gated, bounded Unicode candidate-research task, select its proportionate execution lane, and execute and integrate it after approval. Apply to a specific character, a set or repertoire, shared or method-supporting character-agnostic research, or the highest-priority actionable project topic. Use when the user invokes `$next-research` with or without a target, asks Codex to choose or plan the next project research task or execution approach, or approves a task and lane previously proposed through this workflow.
---

# Next Research

Run an approval-gated, bounded research cycle that chooses one task and the most appropriate execution lane. Apply `AGENTS.md`, including its selective context routing, throughout. The result may support, weaken, or leave unresolved a candidate case. Keep the central model responsible for project continuity, standards reasoning, interpretation, independent source verification, and canonical integration. Preserve the human expert-review and project-owner approval gates assigned by [External model research intake](<../../../Methods/External model research intake.md>).

## Choose the mode

- If the user approves a task and execution lane previously proposed through this workflow, proceed to execution. If the earlier proposal did not include a lane, or the user materially changes the task, lane, context boundary, or private-data exposure, revise the proposal and obtain approval before execution.
- If the user supplies a character, candidate set or repertoire, character-agnostic topic, or research task, use directed mode.
- If the target is undefined, use selection mode to choose the highest-priority actionable task across candidate-specific, cross-candidate, and methodological work.

Identify the target as a candidate, related set or repertoire, shared/methodological topic, or—until selection resolves it—undefined.

## Scope the task

### Selection mode

1. Read the project context and candidate inventory, then inspect outstanding tasks, leads, unresolved claims, negative findings, and any ranked future-research list. Use local evidence first. Limit any pre-approval external check to determining whether a task is actionable; do not collect substantive findings.
2. Exclude candidates that require unavailable private material, fieldwork, paid acquisition, external contact, a material user decision, or authority not supplied by the user. Treat those as future tasks rather than actionable now.
3. Rank actionable tasks by declared priority and dependencies; ability to resolve a consequential uncertainty or counterargument; cross-candidate reuse or dependency-unlocking value; time sensitivity; and likely evidential return within a bounded pass.
4. Recommend exactly one task.

### Directed mode

1. Treat the user’s target and topic as the substantive direction; do not re-rank the backlog or replace them with another target.
2. Inspect relevant candidate-specific and shared context, then translate the topic into a defensible research question and scope while preserving its direction. State any material reinterpretation.
3. Preserve requested parallel definitions or classifications; treat overlap and disagreement as data. For a candidate set, distinguish shared questions from candidate-specific branches and where each result belongs.
4. If the task is blocked, propose the closest actionable subset rather than switching targets.

## Choose the execution lane

Choose the lane after scoping the task and before proposing or executing it. Select by evidential and operational fit, not by brand preference. Default to one central lane; use an external, human, or mixed lane only when a named task characteristic supplies a material advantage.

Assess:

- whether the main work is project reasoning, source discovery, closed-corpus analysis, repeatable computation, visual/private-evidence review, first-hand acquisition, or specialist judgement;
- the source universe, languages, scripts, jurisdictions, modalities, access conditions, and corpus boundary;
- whether reproducible transformations or calculations matter more than open-ended interpretation;
- privacy, rights, account, cost, contact, and tool-access constraints;
- what context the lane needs and what can safely be supplied; and
- which decisions must remain with the project owner and which analytical or integration duties remain with the central model.

| Lane | Choose when | Do not use it as |
| --- | --- | --- |
| **Central ChatGPT/Sol or Codex reasoning and canonical integration** | The task is small or medium, depends on repository continuity, current official standards, close comparison, source verification, interpretation, or editorial judgement. This is the default and always owns final integration. | A reason to omit specialist review or deterministic analysis when the evidence genuinely requires either |
| **Gemini Deep Research** | Bounded discovery requires broad open-web coverage across many terms, languages, scripts, jurisdictions, or obscure and difficult-to-locate sources, and a source-map or lead set is the useful deliverable. | An authority for verified facts, Unicode interpretation, candidate decisions, or direct repository editing |
| **NotebookLM** | The question must be answered against a deliberately selected, versioned source corpus and passage-level comparison, contradiction mapping, or corpus-bounded synthesis is more important than open-web discovery. | A completeness claim beyond the supplied corpus or a substitute for opening and checking the originals |
| **Scripted or structured-data analysis** | Versioned data, stable rules, repeated transformations, enumeration, deduplication, counts, reconciliation, or reproducible tests dominate the task. | A substitute for defining semantic boundaries, evaluating source authority, or making candidate judgements |
| **Private-evidence or image-corpus review** | Permitted local material, original-resolution inspection, provenance-aware visual coding, OCR triage, or comparison of an existing private collection is central. | Permission to upload restricted material, alter originals, publish private metadata, or treat image classification as character analysis |
| **Human fieldwork, source acquisition, or permission work** | The needed evidence is first-hand, unindexed, paywalled, privately held, location-dependent, or available only through contact, purchase, capture, interview, or a rights grant. Use only with the user’s authority and available resources. | An actionable selection-mode task when the required access, authority, or resources are unavailable |
| **Specialist consultation** | A precisely stated question requires disciplinary, linguistic, community, legal, palaeographic, technical, or other expertise that project methods cannot responsibly supply. State which decision the answer could change. | A vague request for endorsement or a replacement for evidence that the project can check directly |
| **Mixed workflow** | Two or more genuinely distinct stages depend on different lanes, such as scripted corpus extraction followed by central interpretation, or broad discovery followed by source verification and canonical analysis. Order the stages and minimize transfers. | Routine multi-model duplication, an unbounded second opinion, or automatic escalation of a small task |

Apply these constraints:

1. Keep ordinary project reasoning, direct source checking, ordinary Unicode standards interpretation, and canonical writing in the central lane.
2. Choose the fewest lanes that can answer the approved question. Do not send a task to another model merely to repeat work or add apparent consensus.
3. Treat a mixed workflow as an ordered dependency: name the output passed between stages and keep the central model at the beginning and end.
4. Minimize supplied context. Prefer an exact file list or bounded extract to a repository dump, and classify private or restricted material before any external upload.
5. Do not imply that ChatGPT, Codex, Gemini, NotebookLM, or another system communicates directly with another one or can update the repository. Unless a separately configured automation explicitly provides that capability, the user remains the intermediary and approval authority.
6. A lane does not make unavailable evidence actionable. In selection mode, defer work that still needs unsupplied authority or access; in directed mode, propose the closest actionable subset.

## Propose the plan

Present:

- the proposed research question;
- the target scope and affected candidate projects, if any;
- in selection mode, why it outranks the nearest alternatives;
- in directed mode, any material scoping or reframing;
- material definitions, corpus boundaries, and inclusion rules;
- a high-level method and intended project outputs;
- principal uncertainties and counterarguments;
- the selected lane or ordered lanes and why each fits the task;
- the exact context, files, corpus, data, or private-evidence category to provide to each lane;
- the expected deliverable from each lane;
- source, provenance, citation, adverse-evidence, and verification requirements;
- stopping conditions and the limits of the bounded pass;
- how each result will return through the user to the central model and then to the canonical project; and
- a request for approval or optional changes.

Keep this proposal compact enough for a user with limited capacity. Make clear that approval covers both the bounded task and the stated lane, including the context to be supplied. Do not begin substantive research, send a handoff, upload context, contact anyone, acquire material, or run the substantive analysis before approval.

### External-model handoff brief

When Gemini Deep Research, NotebookLM, or another external model is selected, include a bounded, paste-ready handoff brief in the proposal so the user can approve the exact delegation and context boundary. Adapt this structure without adding irrelevant fields:

```markdown
## Role and bounded question

[State the discovery or corpus-analysis role, the exact question, and that project decisions remain outside the assignment.]

## Scope and exclusions

- Included sources, corpus, languages, scripts, territories, dates, and definitions:
- Excluded adjacent questions and prohibited generalizations:
- Supplied files or context, with snapshot date or commit where applicable:

## Source and method requirements

- Prefer original and authoritative sources; give exact URLs or stable identifiers and supporting locations.
- Separate observed material, source claims, model inferences, negative searches, contradictions, and access failures.
- Record queries, language or spelling variants, and corpus limits where discovery or a negative finding is material.
- Do not treat the report as verification or claim repository access or editing capability.

## Deliverable

[Specify a source map, finding table, passage comparison, bounded synthesis, or other reviewable artefact and its required fields.]

## Stopping conditions

[State coverage target, saturation rule, time or result bound, and conditions that must be returned as unresolved.]

## Return path

Return the prompt, raw report, source or activity list, and disclosed tool details to the user. The user will bring them back to the central model for intake, source verification, interpretation, and possible canonical integration.
```

For NotebookLM, inventory the exact supplied corpus and forbid extrapolation beyond it. For Gemini Deep Research, define the open-web discovery surfaces, languages, and search record expected. Do not place private or restricted material in either handoff unless the proposal explicitly classifies the service and upload as appropriate and the user approves it.

## Execute after approval

Execute only the approved question, lane order, and context boundary:

- In the central lane, research the approved question and directly material evidential branches.
- In an external-model lane, unless an approved, separately configured automation is part of the proposal, give the approved brief and context package to the user to run in that system. Pause that lane until the user returns the raw result and available source or activity list. Receive it through [External model research intake](<../../../Methods/External model research intake.md>) before any canonical use.
- In a scripted lane, freeze input versions and rules, preserve a reproducible method and validation record, and keep interpretation separate from computed output.
- In a private-evidence or image-corpus lane, work only within the approved access and storage boundary, preserve originals unchanged, and record derivatives and provenance separately.
- In a human or specialist lane, provide the approved acquisition instrument or exact consultation questions, then wait for the user to return the resulting evidence, response, rights record, or field notes with provenance.
- In a mixed workflow, follow the approved order. Pass only the stated deliverable between stages and return to the central lane for verification and integration.

Initial approval covers the planned stages; seek fresh approval before a material lane change, a new external system or contact, paid acquisition, expanded private-context disclosure, or a substantially broadened question. Within the approved plan, follow useful evidence without seeking permission for every search, but:

- allow at most one material methodological reframing and record why it was necessary;
- do not turn an adjacent lead into a separate full investigation;
- stop when the planned questions are answered, the next step needs unavailable evidence or new authority, or further searching produces marginal repetition; and
- add a materially different lead to future research instead of expanding the approved task.

## Integrate the result

Before reporting back:

1. Verify returned evidence proportionately. For external-model work, apply every applicable intake gate: the central lane may perform the gates the intake method assigns to it, but it cannot replace required human expert review or project-owner approval. Integrate only checked underlying sources, never the report as factual authority. For scripts, inspect inputs, rules, outputs, and material calculations. For human, specialist, private, or visual evidence, preserve provenance, qualifications, rights, and the boundary between evidence and judgement.
2. Integrate candidate-specific findings into the corresponding candidate project notes and source records, updating affected summaries, data, and review dates where necessary.
3. Put cross-candidate findings in shared research and reusable methodological lessons in methods. Store a substantive finding about another candidate with that candidate, or add a scoped lead if its project has not begun.
4. Re-rank the canonical project-wide future-research list when one exists. Otherwise update relevant local leads without creating a competing project-wide ranking.
5. Check internal links and inspect the final diff.

In the final handoff, lead with the research conclusion. Identify the lane or lane sequence used, material reframing, important limitations, the effect on the encoding case, files changed, and any newly prioritized lead.
