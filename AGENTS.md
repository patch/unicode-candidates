# Unicode Candidate Research Project Guidance

## Purpose

This project researches the case for and against encoding prospective Unicode characters and repertoires. Inclusion in the project records a subject for evaluation, not an official Unicode status or a presumption that a proposal should be submitted. Research may support encoding, oppose encoding, or remain unresolved.

Initial parallel work prioritizes the Durian, All Gender Symbol, and Urinal projects, with Inverted Cross as another near-term project. The current working judgement favours encoding a durian character, particularly because of repeated use on signage in Southeast Asian countries, but research remains open to a different conclusion. A proposed character may also receive official emoji treatment; emoji status is not a separate character encoding.

## Working principles

- Use en-GB as the baseline dialect, following Oxford University Press and UK academic-journal practice; in particular, use `-ize` rather than `-ise` in Greek-derived verbs where applicable.
- In Markdown prose, use LEFT SINGLE QUOTATION MARK (`U+2018`), RIGHT SINGLE QUOTATION MARK (`U+2019`), LEFT DOUBLE QUOTATION MARK (`U+201C`), and RIGHT DOUBLE QUOTATION MARK (`U+201D`) for English quotation and apostrophe punctuation. Retain APOSTROPHE (`U+0027`) and QUOTATION MARK (`U+0022`) only where syntax, code, identifiers, or URLs require them.
- Treat a country as any territory assigned an ISO 3166-1 alpha-2 code, including dependent territories, and use that alpha-2 code as the primary country identifier in project data. Name the property `country_code` and define its standard in the relevant data documentation.
- Use Unicode CLDR English (`en`) names for territories at every level, including macroregions such as Southeast Asia. Prefer the `alt="short"` territory name when present, except when that value is itself a two-letter abbreviation; in that case use the unqualified name. When naming a language, include its lowercase ISO 639-1 alpha-2 code when assigned, otherwise its lowercase ISO 639-3 alpha-3 code. Keep ISO 3166-1 alpha-2 country codes uppercase. Where the expanded form is useful, write `Country Name (CC)` and `Language Name (ll/lll)`.
- Name standards precisely on first use. Do not use ambiguous phrases such as “ISO country code”, “ISO language code”, “ISO entities”, or standalone “ISO”. After defining the applicable standard, prefer “country code”, “language code”, or Unicode’s term “territory”, as context requires.
- Treat this directory as part of an Obsidian vault. Prefer portable Markdown notes, internal links, clear titles, and ordinary files that work without plugins.
- Where Obsidian’s inline title already displays a note’s frontmatter title or filename, omit an identical Markdown H1. Use a body H1 only when it supplies materially different information.
- Within a directory that functions as a coded lookup list, such as territories, languages, or currencies, use the relevant code as the filename and store the human-readable `Name (code)` form in the note’s `title` property.
- Use Obsidian Bases only where structured filtering or comparison is genuinely useful; do not force narrative research, source notes, or evidence archives into a Base.
- Keep the public `README.md` focused on the project’s purpose, methods, scope, and participation context. Maintain the candidate inventory in `Candidates.md`, not in the README, so the repository’s primary view does not imply that listed subjects are established or official candidates.
- At the project level, name and analyse the prospective encoded entity as a character or symbol, not a sign. Use “sign” for a physical or displayed artefact and “signage” for the real-world usage context that supplies evidence of symbol use.
- Treat a single prospective character, a repertoire of inseparable characters, and a related set of independently researchable characters as different scopes. Give independently viable candidates separate project folders even when a later proposal may group them; in particular, keep All Gender Symbol and Urinal separate.
- Treat “Cross of St. Peter” as an earlier project name for Inverted Cross. Treat “Nonbinary restroom symbol” as an earlier project name for the All Gender Symbol project; determine the final proposed character name from the evidence rather than assuming that working label is final.
- For formal background research, the user’s questions may be reframed into a more defensible methodology when that better serves future publication. State material changes in scope or framing, distinguish verified results from leads, and prefer explicit inclusion criteria and limitations over false exhaustiveness.
- Treat user prompts as concise statements of intent rather than publication-ready wording. Preserve their substantive direction while translating them into the terminology, evidential framing, structure, and register most appropriate to formal Unicode and academic work. Surface any material reinterpretation; do not reproduce informal prompting language merely for verbal consistency.
- Capture reusable research methods and cross-project lessons separately from durian-specific findings so future symbol or emoji investigations can repeat and improve the process. Research must be capable of supporting, opposing, or leaving unresolved a case for encoding; publish useful findings even when the conclusion is not to propose a character. Maintain a brief refinement log when the method changes.
- Use import and diaspora research to document global availability, repeated exposure, and possible comprehension beyond the core region. Keep availability, observed use, and demonstrated symbol comprehension as separate evidential steps.
- Keep organization deliberately light. Create a file or folder only when there is an actual item to place in it; avoid numbered folder names and unnecessary nesting.
- When research material is judged clearly out of scope but retains evidential or methodological value, preserve it in an archive rather than deleting it. Create archive structure only when there is material to place there.
- Reassess organization as material accumulates. Reorganize conservatively when it makes retrieval meaningfully easier.
- Preserve original evidence unchanged. When creating crops, annotations, resized images, or other derivatives, keep them separate from the original and retain a link to it.
- Catalogue the project owner’s existing sign-photo collection before commissioning or broadly collecting further sign images. Defer the systematic plain-text-interchange and counterargument audit until that collection can be shared and assessed.
- For each evidence item, record available provenance: source or creator, URL or origin, access/capture date, location and context of use, and rights or permission status.
- When a useful public web source has changed or disappeared, check the Internet Archive Wayback Machine. Record the original URL, capture URL and timestamp, access date, and limitations; inspect separately captured embedded resources where necessary. Archival availability does not alter the material’s rights status.
- Do not assume locally stored material is suitable for public submission. Track whether an image or other asset is safe to publish or license for proposal use.
- Treat functional or non-marketing symbol use and marketing or brand use as distinct evidence categories. Functional use is normally stronger evidence of an independent communicative convention, but repeated marketing use across unrelated organizations and territories remains relevant. Track inline integration with text, such as a durian form substituting for a letter or punctuation mark, as its own observation.
- Interpret a proposed character’s referent from popular real-world use, much like a dictionary sense, rather than forcing it to match biological nomenclature. The referent may cover a genus, higher-level or vernacular category, or even a polyphyletic popular grouping. Where one species is the strongest popular exemplar, call it the “popular representative species”, not a “type species”.
- The project owner intends to license original project text and assets under CC BY-SA 4.0, while excluding third-party reference material governed by other terms. Record exact Creative Commons licences, attribution and share-alike duties, and compatibility before reuse. The project owner can license Shutterstock assets; record the asset ID and applicable licence and do not assume the subscription permits repository redistribution.
- Non-free material may be retained as reference evidence and considered for limited, low-resolution reproduction in critical commentary under an explicitly documented fair-use or fair-dealing rationale. Treat this as a rights-review category rather than an automatic permission or a substitute for legal review.
- Treat character encoding and emoji treatment as distinct research and submission processes for the same proposed character. Link shared evidence rather than duplicating it.
- When a candidate-specific task produces a reusable method, cross-candidate finding, or finding about another defined candidate, integrate each result at the corresponding project level and link it rather than duplicating it.

## Version control

- Do not create a commit unless the user explicitly requests it.
- When integrating the former `patch/unicode-candidates` repository, preserve both repositories’ commit histories and original dates. Move the historical `README.md` to `Candidates.md` in a rename-only commit before overhauling its contents, so the candidate-list history remains discoverable without placing the inventory in the new README. Do not create a milestone tag for the former repository tip unless the user requests one.
- Public access may be opened before contribution policies or a `CONTRIBUTING.md` are prepared. Do not delay an otherwise ready initial publication merely to design a mature contribution model.
- A minor or single-purpose commit may use only a concise imperative subject.
- A comprehensive or multi-issue commit should also have a body that summarizes its material scope. When the body records two or more distinct outcomes, format them as one compact Markdown bullet list; do not place each outcome in a separate prose paragraph. Reserve a prose body for a genuinely cohesive explanation, and describe meaningful outcomes rather than repeating the subject line.

## Unicode research and proposals

- In any table that lists Unicode characters or character sequences, include a column displaying the literal character or sequence alongside its code-point notation and name, and use one extended grapheme cluster per row.
- On first prose reference to a Unicode character or sequence on a page, include its literal form unless a table on that page already displays it. Always retain code-point notation and names because font support and glyph rendering vary.
- Organize repertoire comparisons by proposal relevance and source history. Keep contemporary emoji or general symbols separate from legacy source-set and historical-script material.
- Treat former candidates that have since been encoded as comparative and process precedents rather than active candidates. Coconut 🥥 (`U+1F965 COCONUT`) is encoded; future fruit-repertoire research should review it and other fruit or closely comparable emoji added after the initial Unicode emoji repertoire.
- Prefer the latest official Unicode Consortium resources as the source of truth for process, criteria, templates, status, and submission requirements. Treat older forms and past proposals as historical references unless current official guidance confirms they remain applicable.
- Before scheduling an emoji re-review, verify the current waiting-period rule and how Unicode applies it, including the event from which the period runs and any transitional treatment of older decisions. Unicode’s emoji-status spreadsheet labels its date column `Date Submitted`; do not assume that it is the controlling date or present an inferred eligibility date as settled.
- Record useful, durable findings from official Unicode resources in project notes when they will help future work. Cite the official page or document and the access date; summarize rather than reproducing large source text.
- Check current official guidance before presenting a Unicode-process claim as settled.
- Maintain a clear distinction between observed evidence, sourced claims, working inferences, and proposal decisions.

## Maintaining this guidance

- When the user gives a durable project preference, decision, or workflow direction that would help future work, update this `AGENTS.md` without needing a separate request.
- Keep updates concise and limited to enduring guidance. Do not use this file as a research log, source register, or proposal draft.
- Mention material updates to this file in the final handoff for the task that made them.
