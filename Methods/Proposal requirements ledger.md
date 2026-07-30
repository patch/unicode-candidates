---
title: Proposal requirements ledger
method_status: reusable working method
official_guidance_cutoff: 2026-07-30
last_reviewed: 2026-07-30
tags:
  - method
  - unicode-proposals
  - proposal-readiness
  - requirements
---

Use this ledger to accumulate the exact answers, evidence, technical data and submission artefacts that a prospective Unicode character or repertoire may require. It complements the analytical checklist in [Character identity and encoding analysis](<Character identity and encoding analysis.md>): that method tests whether an encoding case is defensible, while this ledger records what could actually be entered into a submission and what remains unsupported.

Completing a ledger does not presume that a proposal should be submitted. It may expose a decisive weakness, support deferral or opposition, or show that only one proposal route is viable. A candidate can use the ledger during `researching` without entering `drafting`; the phase changes only when a formal proposal document is actually being prepared.

## Use and placement

Keep this file as the reusable project template. Create a candidate-specific copy only when there are substantive answers or gaps to record, normally at:

`Candidates/<Candidate>/Research/Proposal requirements ledger.md`

Store candidate facts and judgements in that copy. Link to underlying candidate research rather than duplicating evidence, long rationales or source records. If several candidates may later share one submission, keep their ledgers independent until a joint submission is an operative decision; then add a separate submission-level mapping rather than collapsing their identities.

Maintain separate character-proposal and emoji-proposal sections. Shared evidence may support both, but one route’s eligibility, requirements or outcome does not satisfy or decide the other.

Do not create empty ledgers for every subject in `Candidates.md`. Once a ledger exists, retain every stable field ID from this template so automated reconciliation and validation remain possible. Mark a genuinely irrelevant field `not applicable` and record why; retain route-level sections even when one route is presently deferred or inapplicable.

## Maintenance and automatic reconciliation

Treat each candidate ledger as a **maintained projection of integrated candidate research**. The authoritative source for a finding remains the relevant research note, evidence register, source record or operative project decision. Do not update a ledger directly from an unintegrated lead, model output, private item not yet assessed, or unsupported inference.

Every task that integrates candidate-specific research for a candidate with a ledger must finish with this sequence:

1. integrate the new evidence, source correction or decision into its authoritative candidate note;
2. identify every ledger field whose answer, support, state, rights boundary, refresh condition or destination may change;
3. reconcile those fields in the same task, including downstream summary-form mappings rather than updating only the first matching row;
4. update the route readiness summary if the balance of evidence, a blocker or a submission-time dependency changes;
5. advance `evidence_cutoff`, `official_guidance_cutoff` and `last_reviewed` only to the dates actually covered; and
6. run `python3 scripts/validate_proposal_ledgers.py`.

If integrated research has no ledger consequence, leave the ledger unchanged and report `Ledger impact: none` in the final handoff. Otherwise report the affected IDs and whether each answer was added, strengthened, qualified, replaced, blocked, unblocked or prepared for project-owner approval.

### Update classes

| Change | Default treatment |
| --- | --- |
| Explicit sourced fact, date, count, link, official status or completed artefact | Apply automatically after integration and cite the authoritative project record |
| New exact answer to an `unknown` or `blocked` field | Apply when the integrated evidence supports that exact answer and no material interpretation is concealed |
| Stronger evidence for the same answer | Replace or qualify the support, update the state and refresh every dependent field |
| Contradictory or superseding evidence | Preserve the live alternatives, normally set the answer to `provisional` or `blocked`, and identify the decision or evidence needed; do not use last-write-wins |
| Character identity, semantic scope, candidate grouping, route strategy, readiness, lifecycle phase or submission decision | Prepare the coordinated changes for project-owner approval |
| Consequential rights, privacy, contributor-role or publication judgement | Prepare the coordinated changes for project-owner approval and keep restricted details out of the public ledger |
| Unicode guidance, repertoire, pipeline, nonapproval, request status or route eligibility | Recheck at the row’s refresh trigger and propagate the dated result across every affected candidate field |

An automatic update may be adverse. For example, new evidence can change a favourable `provisional` answer to a supported non-encoding conclusion, or turn a formerly `supported` answer into `blocked` because its source or rights basis has failed.

### Replacement and audit history

Keep the ledger’s prose current. When better evidence replaces an earlier entry, write the present answer and material qualification rather than appending a chronological log to the cell. Git history preserves routine superseded wording. Retain a dated history in the candidate record only when the change itself is evidentially, procedurally or methodologically material.

Update the authoritative research note before or with the ledger. A ledger citation must never point only to another ledger row when an underlying source record or analytical note is available. Cross-references between ledger rows may reduce duplication, but they do not replace evidential support.

### Handoff record

Use a compact final handoff:

```text
Ledger impact:
- Updated: C-E05, C-SF-C4, C-SF-C5
- Qualified: C-E06
- Readiness: Character blocker narrowed; route decision unchanged
- Approval required: none
```

For a task with no material effect:

```text
Ledger impact: none
```

### Structural validation

Run the project validator from the repository root:

```sh
python3 scripts/validate_proposal_ledgers.py
```

The validator checks the stable template IDs, duplicate, malformed or missing fields, table structure, permitted states, unexplained blank values, support and refresh cells, local links and heading fragments, control metadata, frontmatter cut-offs, possible public e-mail addresses and route-readiness summaries. It also warns when a candidate evidence cut-off is newer than the ledger, when the template’s official-guidance cut-off is newer than a candidate ledger’s, or when a literal refresh date in `YYYY-MM-DD` form has passed. A note’s `last_reviewed` date alone does not imply ledger impact: the note may have received an editorial or methodological revision without new candidate evidence.

These checks detect drift; they cannot determine whether evidence supports the answer, whether a replacement judgement is sound, whether rights permit publication, or whether a candidate should proceed.

## Official baseline and change control

The requirements below were reconciled on 30 July 2026 against:

- the Script Encoding Working Group’s current [Submission Guidelines and Process](https://sew.unicode.org/guidelines) and the read-only preview of its New Proposal Submission form;
- Unicode’s current [Proposal Summary Form](https://www.unicode.org/L2/summary.html) page and the linked [N4502-F form](https://www.unicode.org/L2/L2014/14232-n4502-form.html);
- [Unicode Properties in Character Proposals](https://www.unicode.org/pending/properties.html); and
- the [Guidelines for Submitting Unicode Emoji Proposals](https://www.unicode.org/emoji/proposals.html), last updated there on 20 May 2026.

These sources can change independently. The current Unicode summary-form page still links N4502-F despite its 2014 document path, and the SEW form permits the same information to be entered directly. Record both the official source and the operative submission mechanism instead of inferring obsolescence from a filename or date.

At the start of drafting, and again immediately before submission:

1. re-open the current official guidance and live submission form;
2. record their displayed revision dates or the absence of one, the access date and material changes;
3. reconcile added, removed or reworded requirements without silently overwriting the earlier record;
4. recheck the applicable Unicode release, pipeline, nonapproval notices, proposal history and route-specific eligibility;
5. refresh time-sensitive search evidence, dates, statuses, authorship, rights and submission packaging; and
6. preserve the submitted snapshot under [Evidence storage and publication](<../Project/Evidence storage and publication.md>).

Past proposals are examples, not current templates. Where current guidance and a historical proposal differ, follow the current guidance and retain the historical difference only when it has analytical value.

## Answer states

Use one state for the present answer and a separate refresh instruction where necessary.

| State | Meaning |
| --- | --- |
| `unknown` | No defensible answer has yet been recorded |
| `provisional` | A working value or answer exists, but its evidence, technical review or project approval is incomplete |
| `supported` | The answer is supported by integrated evidence or an applicable current source, with material qualifications recorded |
| `not applicable` | The requirement does not apply, and the reason is recorded |
| `blocked` | A named missing condition prevents a defensible answer or artefact |
| `submission-ready` | The exact answer or artefact is in the required form, its dependencies and rights have been checked, and no known gap remains; this is not official acceptance |

Do not use a tick alone to mean both ‘answered’ and ‘satisfied’. A technically valid value may remain `provisional`; an adverse answer may be fully `supported`; and an item may be `submission-ready` while the project still decides not to submit.

Use `not applicable` or `unknown` rather than an unexplained blank. Where non-disclosure is itself the supported answer, record `not disclosed` as the current value and explain the public/private boundary. Administrative blanks that Unicode permits may remain blank only after that has been checked.

## Ledger row contract

Each candidate ledger should use the following columns:

| Column | Record |
| --- | --- |
| **ID** | Stable project identifier from this template |
| **Required answer or artefact** | The exact question, value, file or decision needed |
| **Current value** | The candidate-specific answer, proposed data line, filename or link |
| **State** | One answer state from above |
| **Support and destination** | Evidence or rationale, reviewer where material, and the proposal section, form field, data file or appendix that will consume it |
| **Rights or privacy** | Publication, licence, permission, personal-data or restricted-source limits |
| **Refresh** | A date, Unicode version or trigger such as `before drafting` or `immediately before submission` |

When the official form asks for a yes/no answer and a proposal reference, record both. A bare ‘yes’ is not complete if the form also expects a section, source, artefact or rationale.

## Candidate ledger template

Copy the following sections into the candidate-specific record and replace the instructional text with candidate data. Add frontmatter `title`, `last_reviewed`, `evidence_cutoff` and `official_guidance_cutoff` values in `YYYY-MM-DD` form, plus appropriate candidate tags. Record the ledger’s own evidence cut-off separately from the access date of each official requirement.

### Ledger control

| Field | Value |
| --- | --- |
| Candidate or repertoire |  |
| Scope | Single prospective character, inseparable repertoire, or submission-level set |
| Candidate phase |  |
| Routes under evaluation | Character proposal, emoji proposal, or both |
| Evidence cut-off |  |
| Stable Unicode version checked |  |
| Emoji version checked, if applicable |  |
| Official-guidance check | Source revisions or displayed dates; access date; reviewer |
| Ledger revision |  |
| Principal unresolved decision |  |

### Shared candidate record

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| S-01 | Proposed entity and unit type, stated independently of a code point and exact glyph |  | `unknown` | Link to the identity analysis |  | When scope changes |
| S-02 | Working name, proposed submission name and material alternative names |  | `unknown` | Distinguish attested names, translations and project naming decisions |  | Before drafting |
| S-03 | Semantic and functional scope, including explicit exclusions |  | `unknown` | Link to the candidate overview or identity section |  | When evidence changes the boundary |
| S-04 | Number of independently viable characters and any proposed grouping |  | `unknown` | Explain why the unit is single, inseparable or only submission-related |  | Before drafting |
| S-05 | Community or communities using the entity and the relevant languages, notations or systems |  | `unknown` | Link to bounded community and usage evidence | Protect personal data | Before drafting |
| S-06 | Current and historical use contexts, including functional, inline, freestanding, marketing and decorative distinctions |  | `unknown` | Link to classified evidence rather than copying the corpus | Check reproduction rights item by item | At evidence cut-off |
| S-07 | Previous submissions, requests, related proposals, official documents and exact status history |  | `unknown` | Record route, title, date, identifier, status wording and source separately |  | Immediately before submission |
| S-08 | Existing Unicode versions, pipeline entries and nonapproval notices checked |  | `unknown` | Record corpus and negative-search limits |  | Immediately before submission |
| S-09 | Authors, substantive data or exhibit contributors, sponsors, submitter and main contact identified |  | `unknown` | Public ledger may record names and roles approved for publication; keep contact details separately | Do not publish private e-mail addresses or account data | When contributors change |
| S-10 | Potential rights holders or claimants in the proposed entity identified |  | `unknown` | Record the nature of any claim and the action it requires | Keep legal correspondence and personal contact details private unless publication is approved | Before drafting and submission |
| S-11 | Evidence and artefact rights review complete for material contemplated for submission |  | `unknown` | Link to evidence records, permissions and the prospective public manifest | Separate evidential value from permission to reproduce | Before each draft freeze |
| S-12 | Route-neutral adverse case and named conditions that would support deferral or non-submission |  | `unknown` | Link to disconfirming evidence and unresolved questions |  | At each readiness review |

## Character-proposal route

Use this section for the current Script Encoding Working Group route. The SEW does not accept emoji or flag proposals through this process.

### Administrative and legal data

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| C-A01 | Submission purpose: new script, new character for an existing script, new symbol, change to existing character data, or other in-scope request |  | `unknown` | SEW subject field |  | Before drafting |
| C-A02 | Proposal title; for a single character, the proposed character name |  | `unknown` | SEW administrative field and proposal heading |  | With each revision |
| C-A03 | Submitter name, submitter type and private e-mail address |  | `unknown` | SEW account and N4502-F A.2–A.3 | Keep e-mail and account data outside the public ledger | At submission |
| C-A04 | Submission date, requester reference if any, and whether the proposal is complete |  | `unknown` | N4502-F A.4–A.6 |  | With each submitted revision |
| C-A05 | Every proposal author’s name, private e-mail address and applicable Unicode Contributor License Agreement status |  | `unknown` | SEW author confirmation | Record only non-sensitive status publicly; do not store CLA files or private e-mail addresses here | When authorship changes and at submission |
| C-A06 | Sponsors or endorsing bodies and their exact role, if any |  | `unknown` | Proposal acknowledgement or SEW correspondence as applicable | Obtain publication approval for non-public endorsements | Before submission |
| C-A07 | Every potential intellectual-property holder or claimant, applicable CLA or other licence, and formal written endorsement |  | `unknown` | SEW rights-holder field and private support record | Keep contact details and correspondence private unless publication is approved | Before submission |
| C-A08 | Contributor and font ownership: individual, employer or other entity |  | `unknown` | Determines individual or corporate CLA and font licence path | Treat as a rights determination, not legal advice | Before material drafting by that contributor |
| C-A09 | Consortium retention and permitted use of submitted proposals and related material reviewed as part of the publication decision |  | `unknown` | Submission-rights review | Do not submit restricted support material merely because Unicode can retain submissions | Before public draft and submission |

### Eligibility and core criteria

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| C-E01 | Why the proposed entity is an abstract character rather than a glyph, ligature, conjunct, abbreviation, icon, image, logo or exact design |  | `unknown` | Proposal identity and eligibility sections |  | Before drafting |
| C-E02 | Confirmation that the entity is not already encoded or on track for encoding |  | `unknown` | Stable repertoire, pipeline and related-proposal search |  | Immediately before submission |
| C-E03 | Every plausible existing-character equivalent and why it does or does not preserve the claimed identity and use |  | `unknown` | Existing-character comparison and N4502-F C.8/C.10 |  | When Unicode version changes |
| C-E04 | Every plausible existing or proposed character sequence, normalization result and reason the sequence does or does not suffice |  | `unknown` | Sequence analysis and N4502-F C.9/C.11 |  | When Unicode version changes |
| C-E05 | Evidence for every proposed character and for use by a community independent of the creator where applicable |  | `unknown` | SEW usage criterion; identify independent sources and running-text evidence. The current form describes at least two independently published print sources showing running-text use as good evidence, while the general guidance leaves the exact amount case-dependent | Confirm reproduction rights separately | At evidence cut-off |
| C-E06 | Historic or scholarly versus modern use; repertoire and form stability; five-year form history for modern use; recent changes and justification |  | `unknown` | SEW stability field and proposal history |  | At evidence cut-off and submission |
| C-E07 | Concrete public plain-text interchange need: users, systems, operations and loss without encoding |  | `unknown` | SEW interchange criterion and proposal section | Do not expose private user data | At evidence cut-off |
| C-E08 | Why the entity must remain distinguishable in plain text from existing characters, words, images, markup, fonts, protocols and private agreements |  | `unknown` | Eligibility synthesis |  | Before drafting |
| C-E09 | Strongest adverse eligibility finding and whether it supports opposition, deferral or unresolved status |  | `unknown` | Readiness decision, not advocacy text |  | At each readiness review |
| C-E10 | For a currency sign: running-text use and any supporting letter from a national bank or similar institution relied on to show intended public-commerce use |  | `unknown` | Conditional SEW evidence field | Confirm authority, endorsement scope and publication permission | At evidence cut-off |

### Proposal content

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| C-P01 | Short summary of the exact action requested |  | `unknown` | Beginning of proposal |  | With each revision |
| C-P02 | Introduction to the character or script using appropriate modern and historical sources |  | `unknown` | Proposal introduction | Check quotation and figure rights | At evidence cut-off |
| C-P03 | Prior related Unicode documents, including proposals by other authors |  | `unknown` | Proposal history section |  | Immediately before submission |
| C-P04 | Proposed script or existing block, number of characters and ISO/IEC 10646 proposal category: A-Contemporary, B.1-Specialized (small collection), B.2-Specialized (large collection), C-Major extinct, D-Attested extinct, E-Minor extinct, F-Archaic Hieroglyphic or Ideographic, or G-Obscure or questionable usage symbols |  | `unknown` | N4502-F B.1–B.3; record category rationale | Code-point allocation remains a committee decision | Before drafting |
| C-P05 | Repertoire with proposed names and legible representative shapes |  | `unknown` | Character table, names list and N4502-F B.4 | Proposed names are not formally assigned names | With each repertoire revision |
| C-P06 | Existing characters similar in appearance or function, confusability analysis and rationale for separate encoding |  | `unknown` | Proposal comparison and N4502-F C.10 |  | When Unicode version changes |
| C-P07 | References and published examples of use included or cited, with source information and proposal references |  | `unknown` | Evidence section and N4502-F B.6 | Confirm public reproduction or use a citation-only record | Before each draft freeze |
| C-P08 | Community information, consultations, available documents, use context, frequency and current-use locations |  | `unknown` | N4502-F C.2–C.5 | Do not publish private contact details or identifiable community data without approval | At evidence cut-off |
| C-P09 | Preferred character ordering and collation behaviour, including placement relative to existing characters |  | `unknown` | Proposal ordering section |  | Before technical review |
| C-P10 | Input, presentation, sorting, searching, indexing, transliteration and other processing issues |  | `unknown` | N4502-F B.7 and proposal behaviour section |  | Before technical review |
| C-P11 | Contextual shaping, ligatures, conjuncts, stacking, joining or other rendering behaviour, with sufficient examples for implementation |  | `unknown` | Proposal shaping section | Check example rights | Before technical review |
| C-P12 | For a new script: punctuation, word and line breaking, existing characters used by the script, and proposed Core Specification introduction |  | `unknown` | New-script proposal sections |  | Before technical review |
| C-P13 | BMP placement rationale, contiguous-range preference and any recommended code-point location |  | `unknown` | N4502-F C.6–C.7 | Distinguish recommendation from assigned allocation | Before submission |
| C-P14 | Special semantics or control-like behaviour, syntax suitability, identifier implications and security considerations where material |  | `unknown` | N4502-F C.12 and technical sections |  | Before technical review |
| C-P15 | Combining-character or composite-sequence inventory with corresponding glyph images and rationale, if applicable |  | `unknown` | N4502-F C.11 | Check glyph-image rights | Before technical review |
| C-P16 | Ideographic compatibility equivalents and sources, if applicable |  | `unknown` | N4502-F C.13 |  | Before technical review |

### Character and property data

Record expected behaviour before selecting property values. For each proposed character, retain the exact proposed data lines and cite comparator characters or other rationale. A syntactically valid line is not automatically a correct assignment.

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| C-T01 | `UnicodeData.txt` line for every proposed character: code point or placeholder, name, General_Category, Canonical_Combining_Class, Bidi_Class, decomposition mapping, decimal/digit/numeric values, Bidi_Mirrored, Unicode_1_Name, ISO_Comment and simple case mappings |  | `unknown` | Required SEW property data; record comparable encoded characters and UAX #44 validation |  | Against the stable UCD used for drafting and before submission |
| C-T02 | Code-point or block recommendation, if useful, with roadmap or allocation rationale |  | `unknown` | Proposal and property data | The committees normally assign code points | Immediately before submission |
| C-T03 | `NamesList.txt` data: display line, annotations, aliases, cross-references and subsection placement where applicable |  | `unknown` | SEW optional data file and proposal character table |  | Against the stable UCD used for drafting |
| C-T04 | `LineBreak.txt` value or an explicit textual account of line-breaking behaviour |  | `unknown` | SEW property data or proposal behaviour section |  | Before technical review |
| C-T05 | `Script` property value and, where applicable, `ScriptExtensions.txt` data when characters are used in multiple scripts or a new script uses existing characters |  | `unknown` | SEW property data |  | Before technical review |
| C-T06 | `ArabicShaping.txt` data for joining scripts |  | `unknown` | SEW property data |  | Before technical review |
| C-T07 | `IndicSyllabicCategory.txt` and `IndicPositionalCategory.txt` data for an applicable Indic encoding model |  | `unknown` | SEW property data |  | Before technical review |
| C-T08 | Identifier treatment, including whether use is customary, whether the character may start an identifier and any special handling |  | `unknown` | Proposal property section |  | Before technical review |
| C-T09 | Bidirectional and mirroring behaviour in mixed-direction text |  | `unknown` | `UnicodeData.txt`, other applicable data and proposal explanation |  | Before technical review |
| C-T10 | Normalization, decomposition, composition, case, numeric, whitespace, combining, paired-punctuation, mathematical or other special behaviour |  | `unknown` | Property rationale and applicable data files |  | Before technical review |
| C-T11 | Preferred ordering and any expected collation tailoring, with comparable characters or authoritative ordering sources |  | `unknown` | Proposal ordering section |  | Before technical review |
| C-T12 | Machine validation of every proposed data line against the current file format and permitted property values |  | `unknown` | Record validator, Unicode version, date and result |  | After each technical change and before submission |

### ISO/IEC 10646 proposal-summary mapping

The live SEW form can collect this information directly, or a completed current summary form can be included. Record an exact answer and proposal reference for every applicable question. Earlier ledger rows may be referenced instead of repeating their rationale.

| ID | N4502-F item to answer | Current answer and proposal reference | State | Refresh |
| --- | --- | --- | --- | --- |
| C-SF-A1 | Title |  | `unknown` | With each revision |
| C-SF-A2 | Requester name |  | `unknown` | At submission |
| C-SF-A3 | Requester type |  | `unknown` | At submission |
| C-SF-A4 | Submission date |  | `unknown` | With each submitted revision |
| C-SF-A5 | Requester reference, if any |  | `unknown` | At submission |
| C-SF-A6 | Complete proposal or more information to follow |  | `unknown` | At submission |
| C-SF-B1 | New script and proposed script name, or addition to a named existing block |  | `unknown` | Before submission |
| C-SF-B2 | Number of characters |  | `unknown` | When repertoire changes |
| C-SF-B3 | Proposed category |  | `unknown` | Before submission |
| C-SF-B4 | Named repertoire, naming-guideline conformity and legible shapes |  | `unknown` | Before submission |
| C-SF-B5 | Font provider and party granting the publishing licence |  | `unknown` | Before recommendation |
| C-SF-B6 | References and attached published examples |  | `unknown` | Before submission |
| C-SF-B7 | Special processing issues |  | `unknown` | Before technical review |
| C-SF-B8 | Additional properties needed for correct processing |  | `unknown` | Before technical review |
| C-SF-C1 | Previous submission and explanation |  | `unknown` | Immediately before submission |
| C-SF-C2 | Community or expert contact and relevant documents |  | `unknown` | At evidence cut-off |
| C-SF-C3 | User-community information and reference |  | `unknown` | At evidence cut-off |
| C-SF-C4 | Common or rare use context and reference |  | `unknown` | At evidence cut-off |
| C-SF-C5 | Current use, location and reference |  | `unknown` | At evidence cut-off |
| C-SF-C6 | Whether BMP placement is necessary and rationale |  | `unknown` | Before submission |
| C-SF-C7 | Whether contiguous encoding is preferred |  | `unknown` | Before submission |
| C-SF-C8 | Possible presentation form and inclusion rationale |  | `unknown` | Before submission |
| C-SF-C9 | Possible representation by a composed character sequence and inclusion rationale |  | `unknown` | Before submission |
| C-SF-C10 | Similarity or confusability with an existing character and inclusion rationale |  | `unknown` | Before submission |
| C-SF-C11 | Combining characters or composite sequences, rationale and glyph list |  | `unknown` | Before submission |
| C-SF-C12 | Control function or other special semantics |  | `unknown` | Before submission |
| C-SF-C13 | Ideographic compatibility characters and unified equivalents |  | `unknown` | Before submission |
| C-SF-MODE | Summary information entered in the SEW form, embedded in the proposal, or supplied as a separate current PDF |  | `unknown` | At submission |

### Font and character-route packaging

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| C-F01 | Font availability, provider, filename, version and mapped proposed characters |  | `unknown` | SEW font upload | Keep working fonts private unless distribution is approved | With each font revision |
| C-F02 | Representative glyphs at suitable code-chart scale and style |  | `unknown` | Font and proposal character table | Do not derive them from restricted stock material | With each glyph revision |
| C-F03 | Font licence permits the uses, embedding and modification required by the current Unicode Font Submission Policy |  | `unknown` | Licence record and SEW upload | Preserve the exact licence or permission reviewed | Before upload |
| C-F04 | Single proposal PDF in English with author, title and date at the top and an opening summary |  | `unknown` | SEW proposal upload | Exclude private information | With each revision |
| C-F05 | Pages or lines numbered; every figure numbered and sourced |  | `unknown` | Editorial review | Verify figure reproduction rights separately | Before each draft freeze |
| C-F06 | Proposal and images contain no private names, phone numbers, addresses or other private community information |  | `unknown` | Privacy review | Acknowledgements may identify approved contributors without exposing private data | Before each public draft |
| C-F07 | Fonts embedded in the PDF and rendering checked on another system |  | `unknown` | PDF validation |  | After every final render |
| C-F08 | PDF is not password-protected or restricted for editing, copying or printing |  | `unknown` | PDF validation |  | After every final render |
| C-F09 | Proposal PDF, property data, summary information and font are mutually consistent |  | `unknown` | Final package review |  | Immediately before submission |
| C-F10 | Applicable CLAs are in place and every declared author has confirmed the submission |  | `unknown` | Private submission administration | Record only status publicly | At submission |

## Emoji-proposal route

Use this section only for the current emoji-proposal process. Record the exact current submission window and procedural eligibility; do not generalize one year’s dates or waiting period into a durable rule.

### Eligibility, administration and first-page data

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| E-A01 | Current submission window, route availability and official-guidance revision date |  | `unknown` | Current emoji guidelines |  | Immediately before drafting and submission |
| E-A02 | Approved-emoji list, Emoji Requests status and any declined-item re-review restriction checked |  | `unknown` | Record exact status wording, source and relevant dates |  | Immediately before submission |
| E-A03 | Automatic-decline screen: logo or brand; third-party rights; UI icon; signage; specific person, building, landmark or deity; ineligible flag; included text; exact-image request; direction variation; or inadequate image rights |  | `unknown` | Answer each applicable category separately | Rights analysis may require private records | Before drafting and submission |
| E-A04 | Proposal title in the current `Proposal for Emoji <name>` form using a descriptive proposed name |  | `unknown` | Top of first page | Proposed name remains subject to change | With each revision |
| E-A05 | Submitter names separated by semicolons when there are multiple authors; one main point of contact; and current proposal date |  | `unknown` | Top of first page and submission form | Keep private contact details outside the public ledger | With each revision |
| E-A06 | Suggested keywords that do not merely repeat the proposed name |  | `unknown` | Identification section and top of first page |  | Before drafting |
| E-A07 | Proposed emoji category, group and subgroup under the current emoji ordering |  | `unknown` | Identification section and top of first page |  | Against the emoji version used for drafting |
| E-A08 | Emoji Proposal Agreement and License reviewed and an eligible rights holder identified to give the required warranty and licence |  | `unknown` | Submission administration | Keep signed agreements and personal account data private unless publication is approved | Before commissioning final images |
| E-A09 | Proposal does not rely on furthering a cause as a selection justification |  | `unknown` | Eligibility and editorial review; independently compelling factors may still be assessed |  | Before submission |

### Example images and rights

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| E-I01 | Colour example image at 18 × 18 pixels |  | `unknown` | Top of first page | Record creator and rights basis | With each image revision |
| E-I02 | Colour example image at 72 × 72 pixels |  | `unknown` | Top of first page | Record creator and rights basis | With each image revision |
| E-I03 | Black-and-white, not greyscale, example image at 18 × 18 pixels |  | `unknown` | Top of first page | Record creator and rights basis | With each image revision |
| E-I04 | Black-and-white, not greyscale, example image at 72 × 72 pixels |  | `unknown` | Top of first page | Record creator and rights basis | With each image revision |
| E-I05 | Image provenance: original creator or source, creation or acquisition method, stable source URL where applicable and any artificial-intelligence assistance |  | `unknown` | Image-rights statement | Preserve private source files only where permitted | Before public draft |
| E-I06 | Ownership, assignment, work-for-hire, public-domain status or appropriate open-source licence established for every example image |  | `unknown` | Required image certification and source URL where applicable | Do not use restricted stock or merely viewable web images | Before public draft and submission |
| E-I07 | Images remain legible and visually distinctive at required sizes without prescribing one exact vendor design |  | `unknown` | Inclusion-factor analysis |  | With each image revision |

### Factors for inclusion and exclusion

Address every current factor, including adverse or neutral answers. A factor is not ‘satisfied’ merely because a favourable paragraph can be written.

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| E-FI01 | Multiple meanings, including notable metaphorical uses or symbolism |  | `unknown` | Inclusion section with empirical support |  | At evidence cut-off |
| E-FI02 | Use in sequences with existing emoji to convey additional concepts |  | `unknown` | Inclusion section with exact examples |  | Against the emoji version used for drafting |
| E-FI03 | How the candidate breaks new ground in the repertoire |  | `unknown` | Inclusion section and comparative repertoire research |  | When emoji version changes |
| E-FI04 | Distinctiveness: legibility, recognition and visual distinctiveness |  | `unknown` | Inclusion section, image tests and comparator set | Check comparator-image rights | With each image revision |
| E-FI05 | Usage level: high expected usage supported by the required Frequency evidence |  | `unknown` | Inclusion and Frequency sections |  | Refresh as a submission-time snapshot |
| E-FI06 | Completes an incomplete category, if claimed |  | `unknown` | Inclusion section with a bounded current category |  | When emoji version changes |
| E-FI07 | Compatibility with a popular existing system, if claimed |  | `unknown` | Inclusion section with exact system and evidence | Check platform-data and screenshot rights | At evidence cut-off |
| E-FE01 | Already representable: whether another emoji character or emoji sequence can represent the concept |  | `unknown` | Exclusion section with semantic and repertoire comparison |  | When emoji version changes |
| E-FE02 | Whether the proposed identity is overly specific |  | `unknown` | Exclusion section with the appropriate semantic level |  | Before drafting |
| E-FE03 | Whether acceptance would create an unjustified open-ended category |  | `unknown` | Exclusion section with a bounded comparator corpus |  | When emoji version changes |
| E-FE04 | Whether the concept or visual convention is transient |  | `unknown` | Exclusion section with dated evidence |  | At evidence cut-off |
| E-FE05 | Faulty comparison: whether the principal justification is merely resemblance to, association with or precedent from an existing emoji |  | `unknown` | Exclusion section |  | Before drafting |
| E-OT01 | Other useful information, including design considerations and material limitations |  | `unknown` | Other-information section | Check rights for any figures | Before submission |

### Required frequency record

Treat frequency data as a reproducible public snapshot, not a stable fact. Record the exact query, qualifiers, language, corpus, geography, date range, access date, displayed value, screenshot and limitations. Use the widest available range where the current guidance requires it. The current guidance requires the candidate concept and ‘elephant’ as a comparison in the Trends and Ngram evidence; recheck that comparator before any later submission.

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| E-Q01 | Search concept, exact term variants, category qualifiers, grouped multiword queries and non-English queries with rationale |  | `unknown` | Frequency-method pre-registration; record the exact syntax required by the current guidance | Avoid account-personalized or private query data | Before running the snapshot |
| E-Q02 | Personalization minimized, normally through a private browsing context, with material limitations recorded |  | `unknown` | Frequency-method record | Do not capture account identifiers | With each snapshot |
| E-Q03 | Google Search query, displayed result count, date and screenshot |  | `unknown` | Required frequency evidence | Review screenshot for personal or account data | Refresh near submission |
| E-Q04 | Google Video Search query, displayed result count, date and screenshot |  | `unknown` | Required frequency evidence | Review screenshot for personal or account data | Refresh near submission |
| E-Q05 | Google Trends Web Search using the required comparison term, widest range and relevant geography; screenshot and date |  | `unknown` | Required frequency evidence | Review screenshot for personal or account data | Refresh near submission |
| E-Q06 | Google Trends Image Search using the required comparison term, widest range and relevant geography; screenshot and date |  | `unknown` | Required frequency evidence | Review screenshot for personal or account data | Refresh near submission |
| E-Q07 | Google Books Ngram Viewer using the required comparison term and widest range; corpus, smoothing, screenshot and date |  | `unknown` | Required frequency evidence | Review screenshot for personal or account data | Refresh near submission |
| E-Q08 | Alternative frequency method and reproducibility justification where a prescribed service is unavailable in the researcher’s location |  | `unknown` | Frequency section | Record access constraint without exposing private location data unnecessarily | At snapshot |
| E-Q09 | Ambiguous-result exclusions, likely false positives, unavailable ranges and other limitations |  | `unknown` | Frequency interpretation |  | At snapshot |
| E-Q10 | Petitions, calls for the emoji, unsupported anecdotes and other expressly unacceptable evidence excluded from the frequency claim |  | `unknown` | Method review |  | Before submission |

### Emoji packaging

| ID | Required answer or artefact | Current value | State | Support and destination | Rights or privacy | Refresh |
| --- | --- | --- | --- | --- | --- | --- |
| E-P01 | Proposal contains every current required section and addresses every question |  | `unknown` | Editorial review against current format |  | Immediately before submission |
| E-P02 | All empirical claims have screenshots or citations and the frequency section contains every required snapshot |  | `unknown` | Evidence audit | Check rights and personal data in screenshots | Immediately before submission |
| E-P03 | Image-rights certification and stable licence or public-domain URLs included where required |  | `unknown` | Image section and submission form | Preserve exact rights record | Immediately before submission |
| E-P04 | Complete proposal rendered as a PDF |  | `unknown` | Submission artefact | Exclude private information not intended for publication | With each final render |
| E-P05 | PDF hosted at a publicly accessible link without sign-in or access request |  | `unknown` | Emoji Submission Form | Public availability is an intentional publication action | At submission |
| E-P06 | Submission made through the current official form by an eligible submitter under the required agreement and licence |  | `unknown` | Private submission administration | Keep account and contact details private | At submission |
| E-P07 | Public PDF, source, example images, evidence manifest and submitted version frozen consistently |  | `unknown` | Submission snapshot | Apply the project’s publication and rights policy | At submission |

## Readiness summary

End every candidate ledger with a concise route-by-route summary. Readiness is a project assessment, not an official status.

| Route | Present assessment | Strongest supported requirement | Strongest adverse finding | Blocking items | Submission-time refreshes | Project decision |
| --- | --- | --- | --- | --- | --- | --- |
| Character proposal |  |  |  |  |  | Pursue, defer, oppose or unresolved |
| Emoji proposal |  |  |  |  |  | Pursue, defer, oppose or unresolved |

Also record:

- the reviewer and date of the latest readiness assessment;
- whether a candidate phase change is proposed and why;
- any specialist review question, the required expertise and the decision it could change;
- the exact source and evidence cut-off; and
- the next smallest useful action, if any.

Do not convert missing evidence into favourable boilerplate. A substantially complete ledger may justify a decision not to submit; an incomplete ledger may still identify a high-value next research task.

## Privacy and public-template rule

The project-level template and public candidate ledgers must not contain private e-mail addresses, CLA files, account screenshots, signatures, private correspondence or form captures populated from a signed-in account. Record the existence, status and private storage pointer only where that pointer itself is safe to publish.

Before committing a downloaded or printed submission-form preview, inspect every page for autofilled account information. A form’s assurance that an address will remain private does not make a locally printed capture safe for a public repository.
