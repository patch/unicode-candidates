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

A finding enters canonical project research only after a reviewer opens the underlying source, evaluates it, and records the claim in the project’s own words and terminology. The reviewer must also apply the relevant project method and [Evidence storage and publication](<../Project/Evidence storage and publication.md>). The report may remain available for audit, but it does not become an intermediary authority between the project and the source.

An external model cannot make a canonical project decision by producing persuasive prose. Decisions about character identity, unification, plain-text need, evidence weighting, proposal route, candidate status, properties, or submission remain project judgements made through the applicable method and human review.

The exception is when the model or its behaviour is itself the research object. Its exact output may then be observed evidence of what that system produced under recorded conditions, but it still does not prove the external-world claims contained in the output.

## Statement classes

Classify every candidate finding before verification. Do not let fluent synthesis erase the boundary between source content and interpretation.

| Class | Meaning | Intake treatment |
| --- | --- | --- |
| **Observed evidence** | A reviewer can directly inspect the relevant object, text, data, image, recording, or source state | Record what is visible or measurable, the exact location, provenance, and material limits |
| **Sourced claim** | An identifiable source states the proposition, but the project has not independently observed the underlying event or condition | Attribute the claim to the source and evaluate its authority, date, method, scope, and context |
| **Model inference** | The external system derives, classifies, reconciles, predicts, or generalizes beyond an explicit source statement | Retain as a lead; never cite the model as factual support |
| **Proposed project inference** | A reviewer considers an inference that may follow from checked evidence | Test contrary explanations and identify it as a project inference if integrated |
| **Project decision** | An authorized editorial judgement about the candidate, method, or proposal | Make only after the applicable human review gates; the model may suggest but cannot decide it |

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

Do not use `verified` as a vague synonym for confidence. Record who performed a `checked`, `qualified`, or `rejected` review and when. A later source change may require rechecking under the archive-recovery method.

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

### 4. Open and evaluate every underlying source

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
| **Translation** | Preserve the original text and script; record the model-produced translation as provisional; check terminology, ambiguity, named entities, negation, modality, and culturally or technically specialized meanings with a competent human or authoritative translation where material |
| **Classification** | Verify the underlying observations separately, then apply the project’s declared definitions and boundary rules; do not import the model’s category labels as facts |
| **Negative finding** | Require a bounded search record: exact queries, languages, scripts, spelling variants, corpora, jurisdictions, date range, search dates, exclusions, access failures, and tool limits; report ‘not found within this search’ rather than absence |
| **Bibliographic entry** | Confirm that the work exists and that author, title, venue, date, edition, DOI or other identifier, and publication type are correct; then read the work before using it for a claim |
| **Numerical or tabular result** | Recalculate material totals, rankings, conversions, and filters from the underlying data; preserve the source universe, unit, period, missing values, and revisions |
| **Technical interpretation** | Check the current official standard, specification, data file, or process document directly; distinguish official requirements from project analysis and candidate judgement; obtain named specialist review where interpretation exceeds the project’s competence |

Project terminology and current official standards take precedence over common online explanations and the model’s preferred wording. For Unicode process, criteria, properties, names, and repertoire status, use the latest applicable official Unicode Consortium material. Older documents remain historical evidence unless current guidance confirms that they still govern.

### 6. Integrate only the checked result

After a finding passes the applicable gates:

- write the canonical claim from the underlying evidence, not by lightly editing the model’s paragraph;
- retain the statement class and any uncertainty or contradiction;
- add the underlying source to the relevant candidate or shared source register, describing its precise use rather than giving blanket endorsement;
- cite the exact source from the destination note;
- update the relevant candidate, shared-research, or method note; and
- record the intake finding’s disposition as integrated, narrowed, rejected, deferred, or retained only as a lead.

The canonical note should remain intelligible if the raw model report disappears. Do not cite the private packet as the authority for an external fact.

## Research roles and their limits

| Role | Proper use | Additional intake requirement |
| --- | --- | --- |
| **Broad open-web discovery** | Find candidate sources, vocabulary, jurisdictions, controversies, and overlooked adverse cases | Preserve queries or the available activity log; identify inaccessible, duplicated, derivative, search-snippet, and citation-laundering results; open the original source before use |
| **Multilingual discovery** | Generate local-language terms and search relevant languages and scripts | Record exact queries, scripts, variants, language identifiers, and who checked meanings; verify translations and false friends; do not equate lack of English results with absence |
| **Closed-corpus source analysis** | Locate passages, compare supplied documents, and develop questions within a defined set | Inventory the exact corpus, versions, synchronization state, exclusions, and context window; open the original document at every cited location; do not generalize beyond the supplied corpus |
| **Scan or image analysis** | Locate possible text, symbols, layouts, or repeated visual features | Inspect the original at useful resolution; separate OCR, description, object identification, classification, and inference; record page or image region and derivative relationship; apply the evidence-storage boundary |
| **Bibliography construction** | Discover and deduplicate possibly relevant works | Verify bibliographic identity and source type, then obtain and evaluate the work; a plausible title or DOI is not evidence for a substantive claim |
| **Summarization** | Reduce a checked source or corpus into a reviewable outline | Check representativeness, omissions, source disagreement, and whether model wording is more definite than the source |
| **Technical interpretation** | Surface relevant clauses, data fields, comparison points, and questions for experts | Current official material and project terminology control; require direct inspection and specialist judgement for material ambiguity |

The same system may perform several roles in one run. Record the role of each finding rather than assigning one evidential status to the whole report.

## Intake packet

One packet may cover one report and many candidate findings. The report-level record establishes provenance and scope; each finding-level record maps one proposed claim to its possible support. Negative searches and access failures may be recorded once at report level when they apply to the whole run, or under the affected finding.

The following copyable template has immediate practical value and is kept inside this method to avoid creating an empty intake structure. Store a completed copy in the appropriate private area unless the public-preservation test below is met.

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
reviewer:
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
- **Verification reviewer and date:**
- **Reason for status or supported narrower wording:**
- **Intended project destination:**
- **Canonical disposition:** pending | integrated | narrowed | rejected | deferred | lead only
- **Unresolved questions requiring expert judgement:**

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
- **Rights and publication gate:**
- **Canonical-integration gate:**
- **Project-decision gate, if applicable:**
```

Use `not applicable`, `not disclosed`, or `not yet checked` rather than leaving a material ambiguity implicit. The template is a review aid, not a universal public schema; proportionate intake may omit fields that genuinely do not apply.

## Human review gates

1. **Scope gate:** a human confirms the question, corpus, definitions, context boundary, exclusions, and permitted data supplied to the system.
2. **Source-verification gate:** a human opens each underlying source and checks exact support, source identity, date or version, authority, and context.
3. **Interpretation gate:** a human applies project terminology and methods, checks quotations, translations, classifications, calculations, negative findings, and contradictions, and obtains named expertise where needed.
4. **Rights and publication gate:** a human classifies storage and proposed publication under [Evidence storage and publication](<../Project/Evidence storage and publication.md>) and the relevant evidence record.
5. **Canonical-integration gate:** a human writes the supported finding into its proper destination, adds the underlying source to the appropriate register, and preserves qualifications and rejected excess.
6. **Project-decision gate:** the project owner or authorized editor decides any resulting change to candidate judgement, proposal strategy, status, or submission. Passing earlier gates does not predetermine this decision.

A reviewer may combine gates in a small, low-risk intake, but none may be silently delegated to the model whose output is under review.

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

## Brief Durian intake test

Suppose a model reports: ‘Singapore law expressly prohibits durian on the MRT’, citing the Rapid Transit Systems Regulations ([S02](<../Candidates/Durian/Research/Sources.md#s02>)). The packet records the claim as `unverified` and as a sourced claim. A reviewer opens the cited legislation and finds that it supplies general transit context but does not appear to name durian; the exact legal claim is therefore `rejected` as non-supporting. The separate 2015 photograph recorded as [S01](<../Candidates/Durian/Research/Sources.md#s01>) directly documents a durian-prohibition pictogram on the Singapore MRT. That observed sign occurrence can be `checked` and integrated through [Durian non-marketing signage](<../Candidates/Durian/Research/Durian signage.md>), with the warning not to present it as an express statutory durian offence.

This example exercises all material distinctions: the model report is a lead; the citation is checked for exact support; observed evidence is separated from legal interpretation; the excessive claim is rejected; the source and image rights remain independently recorded; and no new conclusion about encoding follows without candidate-level review.

## Review checklist

- [ ] The approved question, scope, context boundary, corpus, tool, model where known, prompt, and research date are recorded.
- [ ] The raw report is stored outside canonical research and classified under the evidence-storage boundary.
- [ ] Every material proposition has a candidate finding identifier, exact proposed wording, and statement class.
- [ ] Every cited source has been opened and checked for identity, date or version, authority, exact support, and context.
- [ ] Summaries, quotations, translations, classifications, calculations, technical interpretations, and negative findings received their specific checks.
- [ ] Independent corroboration, contradictory evidence, access failures, and unresolved leads are recorded where material.
- [ ] A `checked` finding is not confused with a canonical acceptance or project decision.
- [ ] Integrated prose is written from the underlying evidence using project terminology.
- [ ] The underlying source, not the model report, is entered in the appropriate source register and cited from the destination note.
- [ ] Human reviewers have passed the applicable scope, verification, interpretation, rights, integration, and decision gates.
