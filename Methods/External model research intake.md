---
title: External model research intake
method_status: reusable working method
last_reviewed: 2026-07-29
tags:
  - method
  - research-intake
  - model-assisted-research
  - provenance
---

Use this method when research has been performed by an external artificial-intelligence system, including an open-web research agent, a source-grounded notebook, a multimodal model, or an ordinary chat model. It governs how the project receives the result; it does not endorse a particular tool.

## Governing principle

A model output is a **research lead or analytical artefact, not a source for the external facts it describes**. A citation supplied by a model points towards a possible underlying source. It does not establish that the source exists, has been identified correctly, says what the model claims, carries the claimed date or authority, or supports the claim in context.

A finding enters canonical project research only after the underlying source has been opened and checked by a process independent of the model output being evaluated. The verifier must have direct access to the source and record exact support, date or version, authority, context, material contradictions, and limitations. This independent source verification may be performed by the central ChatGPT/Sol or Codex workflow when it can inspect the source directly. It does not require the project owner to repeat every uncomplicated source check.

The output under review must never certify itself. The output-producing run or unsupported context cannot turn a claim into a checked finding by restating it, generating another citation card, or rechecking only the material already present there. A central verification process must return to the underlying evidence and disclose what it checked. The report may remain available for audit, but it does not become an intermediary authority between the project and the source.

After source verification, the central workflow may apply project terminology and methods, identify unsupported inferences, and write canonical prose from the evidence. It must also apply [Evidence storage and publication](<../Project/Evidence storage and publication.md>) and disclose unresolved matters. Material technical or specialist interpretation, consequential translation, disputed classification, rights or privacy judgement, candidate-level evidence weighting, and other decision-relevant uncertainty require proportionate human expert review. Passing source verification does not predetermine that review or any project decision.

Neither an external model nor the central workflow can approve a canonical project decision merely by producing persuasive prose. The project owner remains the final approval authority for changes to candidate judgement, project strategy, lifecycle status, proposal route, submission readiness, publication of restricted or legally sensitive material, and accepted repository commits. The central workflow may prepare source-verified canonical changes for the owner to approve, reject, narrow, or return for revision.

The exception is when the model or its behaviour is itself the research object. Its exact output may then be observed evidence of what that system produced under recorded conditions, but it still does not prove the external-world claims contained in the output.

## Statement classes

Classify every candidate finding before verification. Do not let fluent synthesis erase the boundary between source content and interpretation.

| Class | Meaning | Intake treatment |
| --- | --- | --- |
| **Observed evidence** | A reviewer can directly inspect the relevant object, text, data, image, recording, or source state | Record what is visible or measurable, the exact location, provenance, and material limits |
| **Sourced claim** | An identifiable source states the proposition, but the project has not independently observed the underlying event or condition | Attribute the claim to the source and evaluate its authority, date, method, scope, and context |
| **Model inference** | The external system derives, classifies, reconciles, predicts, or generalizes beyond an explicit source statement | Retain as a lead; never cite the model as factual support |
| **Proposed project inference** | A reviewer considers an inference that may follow from checked evidence | Test contrary explanations and identify it as a project inference if integrated |
| **Project decision** | An authorized editorial judgement about the candidate, method, or proposal | The central workflow may analyse or draft it, but only the identified human decision authority may approve it |

These classes describe statements, not whole documents. One report paragraph may contain a checked quotation, an inaccurate summary, and an unsupported inference.

## Verification outcomes

Use a small vocabulary and keep verification separate from canonical acceptance:

| Status | Meaning |
| --- | --- |
| `unverified` | The source or support has not been checked directly. This is the default for every imported model claim. |
| `located` | The likely underlying source has been opened and identified, but exact support, context, or another material element has not yet been checked. |
| `checked` | A reviewer has verified source identity, exact support, date or version, authority, and relevant context, and has recorded material qualifications. This does not by itself mean that the finding has been integrated. |
| `qualified` | The source supports only a narrower, differently framed, or more uncertain claim. Record the supported wording and reject the excess. |
| `rejected` | The cited source is fabricated, misidentified, non-supporting, materially contradicted, or presented so misleadingly that the proposed claim must not be used. State the reason. |
| `unresolved` | Verification requires unavailable access, a missing original, language or subject expertise, or another named condition. The finding must not enter canonical research meanwhile. |

Do not use `verified` as a vague synonym for confidence. Record the `verification_reviewer`, the independence basis, and the date for every `checked`, `qualified`, or `rejected` review. The output-producing run or unsupported context is not an eligible verification reviewer. A later source change may require rechecking under the archive-recovery method.

## Intake workflow

### 1. Freeze the research brief and context boundary

Before sending work to an external system, or retrospectively where necessary, record:

- the research question, approved scope, exclusions, corpus boundary, and stopping condition;
- the repository commit and snapshot date supplied to the system, or an exact list of supplied files and instructions when the system had no repository access;
- any uncommitted or private context supplied in addition to that snapshot;
- the tool, research mode, displayed model or model family where known, enabled web or connector sources, and material settings;
- the original prompt or research brief; and
- the research date and time zone.

If the system is allowed to choose or expand sources, say so. If its search history, retrieval method, corpus coverage, or model identity is not disclosed, record that limitation rather than reconstructing it from the prose.

Do not upload private, restricted, personal, or account-linked material merely because a model can accept it. Decide whether the service and intended use are appropriate before upload, then apply the project’s evidence-storage boundary to the returned report and any source copies.

### 2. Receive the report as non-canonical intake

Preserve the raw report unchanged when audit value justifies retention. Assign a packet identifier and retain the prompt, report, export date, and available activity or source list together. Do not paste the report wholesale into a candidate note or source register.

Raw reports normally belong in an appropriate private intake area outside the public repository and its Git history. They may contain confidential context, third-party excerpts, personal account data, unstable source links, invented citations, or unreviewed claims. A safe canonical finding can be public even when the raw report remains private.

### 3. Decompose prose into candidate findings

Give each material proposition its own candidate finding identifier. Rewrite it as an exact claim that could be accepted, narrowed, or rejected. Separate:

- a source’s statement from the model’s summary of it;
- direct observation from interpretation;
- each source in a compound citation;
- evidence for occurrence from evidence for frequency, recognition, completeness, or encoding need;
- character-proposal implications from emoji-proposal implications; and
- evidential value from publication permission.

Do not assign a canonical source-register key at intake. A checked underlying source receives a key only if and when it is integrated into the relevant source register.

### 4. Independently open and evaluate every underlying source

The verification reviewer may be a human or a central model-assisted process, but must be independent of the output under review and must inspect the underlying evidence directly. Record enough of the verification path to distinguish a source check from a repetition of the report.

For each candidate finding:

1. open the original source rather than relying on a search snippet, model quotation, citation card, cached extract, or bibliography entry;
2. confirm source identity, authorship or issuing body, title, publication or revision date, edition or version, URL or stable identifier, and source type;
3. locate the exact page, passage, table, cell, timestamp, image region, record, or data row that is claimed to support the finding;
4. compare the proposed claim with the source’s exact scope, definitions, method, population, date range, and surrounding context;
5. assess authority for that particular claim rather than treating a reputable domain as universal endorsement;
6. record independent corroboration and contradictory evidence where material; and
7. record access, provenance, rights, privacy, and publication limits by linking to the evidence-storage policy rather than duplicating its rules.

If a citation resolves to a secondary article summarizing an identifiable primary source, evaluate both. Prefer the primary source for the canonical claim when it is available and appropriate, while retaining the secondary source if its interpretation is itself material.

### 5. Apply output-specific checks

Different output forms require different verification:

| Output | Required check |
| --- | --- |
| **Summary** | Map each material proposition to exact support; inspect omitted qualifications, adverse findings, source disagreement, and whether the report converts a selected-source result into a general claim |
| **Quotation or transcription** | Compare character-for-character with the original; record page or location, speaker where applicable, original language, ellipses, editorial insertions, OCR uncertainty, and enough context to avoid changing the sense |
| **Translation** | Preserve the original text and script; record the model-produced translation as provisional; check terminology, ambiguity, named entities, negation, and modality against authoritative resources; obtain competent human review when a consequential conclusion depends on a culturally, linguistically, or technically specialized meaning |
| **Classification** | Verify the underlying observations separately, then apply the project’s declared definitions and boundary rules; do not import the model’s category labels as facts |
| **Negative finding** | Require a bounded search record: exact queries, languages, scripts, spelling variants, corpora, jurisdictions, date range, search dates, exclusions, access failures, and tool limits; report ‘not found within this search’ rather than absence |
| **Bibliographic entry** | Confirm that the work exists and that author, title, venue, date, edition, DOI or other identifier, and publication type are correct; then read the work before using it for a claim |
| **Numerical or tabular result** | Recalculate material totals, rankings, conversions, and filters from the underlying data; preserve the source universe, unit, period, missing values, and revisions |
| **Technical interpretation** | Check the current official standard, specification, data file, or process document directly; distinguish official requirements from project analysis and candidate judgement; where a material ambiguity depends on specialist judgement, state the exact question, required expertise, and decision it could change, then obtain human expert review |

Project terminology and current official standards take precedence over common online explanations and the model’s preferred wording. For Unicode process, criteria, properties, names, and repertoire status, use the latest applicable official Unicode Consortium material. Older documents remain historical evidence unless current guidance confirms that they still govern.

### 6. Integrate only the checked result

After a finding passes independent source verification and any expert review required for its intended use, the central workflow may prepare or apply canonical changes within the approved task. Where a change requires human approval, keep its status explicit and do not treat the proposed judgement or decision as operative until the decision authority approves it.

- write the canonical claim from the underlying evidence, not by lightly editing the model’s paragraph;
- retain the statement class and any uncertainty or contradiction;
- add the underlying source to the relevant candidate or shared source register, describing its precise use rather than giving blanket endorsement;
- cite the exact source from the destination note;
- update the relevant candidate, shared-research, or method note; and
- record the intake finding’s disposition as integrated, narrowed, rejected, deferred, or retained only as a lead.

The canonical note should remain intelligible if the raw model report disappears. Do not cite the private packet as the authority for an external fact. Source support, project interpretation, and human approval remain separate: success at one stage does not silently supply either of the others.

## Research roles and their limits

| Role | Proper use | Additional intake requirement |
| --- | --- | --- |
| **Broad open-web discovery** | Find candidate sources, vocabulary, jurisdictions, controversies, and overlooked adverse cases | Preserve queries or the available activity log; identify inaccessible, duplicated, derivative, search-snippet, and citation-laundering results; open the original source before use |
| **Multilingual discovery** | Generate local-language terms and search relevant languages and scripts | Record exact queries, scripts, variants, language identifiers, and who checked meanings; verify translations and false friends; do not equate lack of English results with absence |
| **Closed-corpus source analysis** | Locate passages, compare supplied documents, and develop questions within a defined set | Inventory the exact corpus, versions, synchronization state, exclusions, and context window; open the original document at every cited location; do not generalize beyond the supplied corpus |
| **Scan or image analysis** | Locate possible text, symbols, layouts, or repeated visual features | Inspect the original at useful resolution; separate OCR, description, object identification, classification, and inference; record page or image region and derivative relationship; apply the evidence-storage boundary |
| **Bibliography construction** | Discover and deduplicate possibly relevant works | Verify bibliographic identity and source type, then obtain and evaluate the work; a plausible title or DOI is not evidence for a substantive claim |
| **Summarization** | Reduce a checked source or corpus into a reviewable outline | Check representativeness, omissions, source disagreement, and whether model wording is more definite than the source |
| **Technical interpretation** | Surface relevant clauses, data fields, comparison points, and questions for experts | Current official material and project terminology control; the central workflow may perform ordinary standards analysis, but material ambiguity requires an exact question and human expert review |

The same system may perform several roles in one run. Record the role of each finding rather than assigning one evidential status to the whole report.

## Intake packet

One packet may cover one report and many candidate findings. The report-level record establishes provenance and scope; each finding-level record maps one proposed claim to its possible support. Negative searches and access failures may be recorded once at report level when they apply to the whole run, or under the affected finding.

The following copyable template has immediate practical value and is kept inside this method to avoid creating an empty intake structure. Store a completed copy in the appropriate private area unless the public-preservation test below is met.

Use `intake_reviewer` for the person or central process that decomposes and manages the packet. `verification_reviewer` identifies the independent process that directly checked an underlying source and must include its independence basis. `expert_review` records `not required`, or the exact pending or completed question, reviewer, outcome, and decision it could change. `approval_status` applies to the specified canonical change or project decision, not to the truth of a source claim. `decision_authority` names the human authorized to approve that change; neither the external report nor the central workflow can occupy that field.

```markdown
---
packet_id:
research_question:
approved_scope:
context_boundary:
repository_commit:
snapshot_date:
tool:
research_mode:
model:
enabled_sources_or_connectors:
research_date:
time_zone:
intake_reviewer:
packet_status: unverified
---

## Original brief

[Exact prompt or research brief, or a safe reference to a privately retained original.]

## Corpus and limits

- Included sources, files, languages, scripts, territories, dates, and definitions:
- Exclusions and stopping condition:
- Undisclosed or uncertain tool behaviour:

## Candidate finding [ID]

- **Exact proposed claim:**
- **Statement class:** observed evidence | sourced claim | model inference | proposed project inference
- **Underlying source:**
- **Source type and authority:**
- **Source identity, date, edition, or version:**
- **Exact supporting location:** page | passage | table | cell | timestamp | image region | record
- **Exact support and context:**
- **Independent corroboration:**
- **Contradictory evidence:**
- **Source, access, and publication-rights limitations:**
- **Verification status:** unverified | located | checked | qualified | rejected | unresolved
- **Verification reviewer, independence basis, and date:**
- **Reason for status or supported narrower wording:**
- **Expert review:** not required | pending | completed — exact question, reviewer, outcome, and decision affected
- **Intended project destination:**
- **Canonical disposition:** pending | integrated | narrowed | rejected | deferred | lead only

## Negative searches

- **Question or target:**
- **Queries and spelling variants:**
- **Languages and scripts:**
- **Corpora, databases, territories, and date range:**
- **Search dates and tools:**
- **Exclusions, access gaps, and limits:**
- **Permitted conclusion:** not found within this search

## Access failures and unresolved leads

- **Source or lead:**
- **URL or identifier:**
- **Failure and date observed:**
- **Alternative route attempted:**
- **Next evidence or authority required:**

## Review record

- **Scope gate:**
- **Source-verification gate:**
- **Interpretation gate:**
- **Human expert-review gate:**
- **Rights and publication gate:**
- **Canonical-integration gate:**
- **Approval subject and requirement:**
- **Decision authority:**
- **Approval status:** not required | pending | approved | rejected | narrowed | revision requested
```

Use `not applicable`, `not disclosed`, or `not yet checked` rather than leaving a material ambiguity implicit. The template is a review aid, not a universal public schema; proportionate intake may omit fields that genuinely do not apply.

## Review and approval gates

Gates attach to acts and decisions, not to an assumption that every act must be performed manually by the project owner. The central workflow may perform independent source verification, ordinary project interpretation, and canonical drafting or integration when the conditions below are met. Human expert review and human approval remain distinct controls.

1. **Scope and context gate:** the project owner approves the bounded external assignment, context boundary, and any private-data exposure when the governing workflow requires advance approval. A retrospective intake records an unknown or unapproved boundary rather than inventing approval.
2. **Independent source-verification gate:** a human or central model-assisted process independent of the output under review opens each underlying source and checks exact support, source identity, date or version, authority, context, contradictions, and limitations. The verifier records what it checked and cannot rely on the report as support.
3. **Interpretation gate:** the central workflow applies project terminology and the relevant method, distinguishes source content from inference, and checks quotations, classifications, calculations, negative findings, and contradictions. Passing this gate does not convert an interpretation into a project decision.
4. **Human expert-review gate:** obtain review from the project owner or an identified specialist where the intended result depends materially on Unicode or standards interpretation, specialist linguistic or disciplinary judgement, consequential translation, disputed classification, rights or privacy judgement, candidate-level evidence weighting, or another issue for which human expertise is decision-relevant. Record the exact question, the reviewer or required expertise, and what candidate, property, route, publication, or other decision the answer could change. Do not use an unqualified ‘human review required’ label.
5. **Rights and publication gate:** the central workflow may record source terms, storage facts, and a routine policy classification. Material rights or privacy ambiguity requires human expert review; publication of restricted or legally sensitive material requires the project owner’s approval under [Evidence storage and publication](<../Project/Evidence storage and publication.md>) and the relevant evidence record.
6. **Canonical-integration gate:** the central workflow may write source-based prose, update the appropriate register and destination, and preserve qualifications and rejected excess. If the change contains a judgement or action reserved for human approval, present it as proposed and keep the approval status explicit.
7. **Human approval and project-decision gate:** the project owner or other identified human decision authority approves, rejects, narrows, or requests revision of changes to candidate judgement, project strategy, lifecycle status, proposal route, submission readiness, publication of restricted or legally sensitive material, and accepted repository commits. Approval may rely on the disclosed source-verification record; it does not require the approver to repeat uncomplicated mechanical checks. Passing any earlier gate does not predetermine this decision.

One process may combine proportionate source-verification, interpretation, rights-recording, and integration gates for a small, low-risk intake. It must still disclose which checks it performed, preserve any required human gate, and expose rather than hide material ambiguity. The same output under review must never perform its own source-verification gate.

The [`next-research` workflow](<../.agents/skills/next-research/SKILL.md>) governs execution-lane selection, advance approval of the bounded task and context, and return to the central lane. This intake method governs the evidential and decision gates after an external result returns; it does not duplicate the full lane policy.

## Public preservation of reports and prompts

A raw external-model report should normally remain private and non-canonical. Preserve a report or prompt publicly only when it has a concrete methodological purpose, such as reproducing a documented research procedure, auditing a material model failure, comparing tool behaviour, or studying the model output itself, and only when:

- the public artefact is necessary for that purpose rather than merely convenient;
- private, sensitive, account-linked, and confidential material has been excluded;
- third-party quotations, images, source extracts, and other incorporated material have passed the evidence-storage and publication review;
- the exact prompt, context boundary, tool or mode, displayed model where known, research date, export format, and material settings are recorded;
- the report is labelled as a non-canonical analytical artefact whose external claims require the underlying sources; and
- a stable snapshot and integrity information are retained when exact reproduction matters.

A project-authored prompt may be publishable even when the resulting report is not, provided the prompt contains no restricted context and materially improves reproducibility. Public preservation does not upgrade the report into a source for the subject matter.

Place an approved public artefact beside the method, research note, or evidence record that gives it meaning, and link to it there. Do not create a general public model-report archive in anticipation of future material.

## Brief gate tests

### Straightforward official-source finding

Suppose Gemini discovers a current official Unicode Consortium page that states a procedural submission requirement and returns its URL and supporting location. The packet treats the report as an `unverified` lead. In the central lane, Sol opens the official page directly, confirms the issuing authority, current date or version, exact clause, scope, and any nearby qualification, checks for a material contradiction in the current official guidance, and records those actions under `verification_reviewer`. Sol then writes a narrow canonical statement from the official page in project terminology and presents the resulting change for the project owner’s approval. No separate human expert review is required if the source and its application are unambiguous, and the owner may approve the change without repeating the source check.

This flow does not make Gemini an authority and does not let Sol treat Gemini’s summary as support. It also does not turn the verified procedural statement into a candidate judgement.

### Technically disputed Unicode interpretation

Suppose an external report claims that a reflected form must be a separate character because a superficially similar encoded character has a particular bidirectional or mirroring property. The central workflow can open the current Unicode Standard, Unicode Character Database files, applicable Unicode Standard Annex, and candidate evidence; it can check what each source actually says and reject any fabricated or overbroad factual claim. If the checked sources do not settle whether the relevant community treats reflection as a semantic distinction, a glyph convention, or bidirectional rendering behaviour, source verification has passed but the interpretation remains unresolved.

The packet must state the expert question—for example, ‘Does the attested use distinguish the reflected form as an abstract textual unit, or is reflection renderer-selected glyph behaviour?’—identify the required script-community and bidirectional-text expertise, and state that the answer could change the unification, separate-character, or property recommendation. The project owner or an identified specialist reviews that question, and the owner approves any resulting candidate judgement. Neither the external report nor the central workflow may close the dispute by asserting confidence.

## Review checklist

- [ ] The approved question, scope, context boundary, corpus, tool, model where known, prompt, and research date are recorded.
- [ ] The raw report is stored outside canonical research and classified under the evidence-storage boundary.
- [ ] Every material proposition has a candidate finding identifier, exact proposed wording, and statement class.
- [ ] Every cited source has been independently opened and checked for identity, date or version, authority, exact support, context, contradictions, and limitations.
- [ ] The verification reviewer, independence basis, and date are recorded; the output under review has not verified itself.
- [ ] Summaries, quotations, translations, classifications, calculations, technical interpretations, and negative findings received their specific checks.
- [ ] Independent corroboration, contradictory evidence, access failures, and unresolved leads are recorded where material.
- [ ] A `checked` finding is not confused with a canonical acceptance or project decision.
- [ ] Integrated prose is written from the underlying evidence using project terminology.
- [ ] The underlying source, not the model report, is entered in the appropriate source register and cited from the destination note.
- [ ] Each material expert-review question identifies the required human expertise and the decision it could change.
- [ ] Human approval has been recorded for every reserved project decision, restricted or legally sensitive publication, and accepted repository commit.
