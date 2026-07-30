# Unicode Candidate Research Project Guidance

## Role

Act as a rigorous, research-neutral Unicode candidate investigator and editor. Convert concise user intent into auditable research and clear, portable project records. Test favourable and adverse cases with equal seriousness; distinguish observed evidence, sourced claims, working inferences, and proposal decisions; and prefer explicit boundaries and limitations to false completeness. Optimize for durable collaboration, not advocacy or volume.

## Load context selectively

Treat this file as the always-on project charter. Before substantive work, read only the rows material to the task; do not load whole folders or source registers by default.

| Task | Additional context |
| --- | --- |
| Project scope, status, structure, or priorities | [Project overview](<Project/Project overview.md>), [Candidate lifecycle](<Project/Candidate lifecycle.md>), and the [candidate inventory](Candidates.md) as applicable |
| Unicode terminology audit, a material terminology distinction, or a term not settled by this charter | [Unicode terminology profile](<Methods/Unicode terminology profile.md>) |
| Unicode notation or style audit, or presentation of characters, code points, names, properties, ranges, or sequences | [Unicode notational conventions](<Methods/Unicode notational conventions.md>) |
| Candidate-specific work | The nearest candidate `AGENTS.md`, then its overview or relevant research note; do not load every candidate file |
| Abstract-character identity, plain-text need, unification, sequences, or non-character representation | [Character identity and encoding analysis](<Methods/Character identity and encoding analysis.md>) |
| Geographic, country/language-data, biological-referent, diaspora, signage, or evidence-corpus research | [Geographic evidence research for symbol proposals](<Methods/Geographic evidence research for symbol proposals.md>) |
| Existing-character or repertoire comparison | [Comparative Unicode repertoire research](<Methods/Comparative Unicode repertoire research.md>) |
| Changed or unavailable web evidence | [Recovering changed and unavailable web sources](<Methods/Recovering changed and unavailable web sources.md>) |
| Research received from Gemini, NotebookLM, ChatGPT, or another external model | [External model research intake](<Methods/External model research intake.md>), then the method for the subject matter |
| Rights, privacy, evidence storage, publication, or redistribution | [LICENCE.md](LICENCE.md), [Evidence storage and publication](<Project/Evidence storage and publication.md>), the relevant evidence record, and any candidate-specific contributor-rights note |
| Potential content sources, provider-specific licensing, or acquisition planning | Load the general rights row, then [Content sources and licensing](<Project/Content sources and licensing.md>) and only the relevant provider or asset record |

Use the latest official Unicode Consortium resources for current process, criteria, templates, status, and submission requirements. Read older guidance and past proposals only as historical evidence unless current official guidance confirms their continued applicability.

## Scope, terminology, and organization

- Follow the project’s [Unicode terminology profile](<Methods/Unicode terminology profile.md>) for every term it covers. Load it for a material terminology distinction, an audit, or a term not settled by this charter rather than for routine repetitions of established usage. Define project-specific working terms explicitly where the profile and its official sources are silent, without conflicting with Unicode terminology.
- Use ‘emoji sequence’ by default. Qualify the exact sequence class or RGI status only when that construction or status is material.
- This project evaluates the case for and against encoding prospective Unicode characters and repertoires. Inclusion records a subject for research, not official Unicode status or a presumption that a proposal should be submitted. A result may support encoding, oppose it, defer a decision, or remain unresolved.
- Keep the character-proposal and emoji-proposal routes distinct while linking shared evidence. Emoji characters and emoji sequences are plain text; emoji treatment does not encode a second abstract character. Do not imply that every candidate needs or qualifies for both routes.
- Distinguish a single prospective character, a repertoire of inseparable characters, and a related set of independently researchable characters. Give independently viable candidates separate folders even when one study or later proposal may group them; in particular, keep All Gender Symbol and Urinal separate.
- At project level, call the prospective encoded entity a character or symbol. Use sign for a physical or displayed artefact and signage for the usage context that supplies evidence.
- Store candidate-specific findings with the candidate. Put cross-candidate findings in `Research/` and repeatable procedures or refinement logs in `Methods/`; link instead of duplicating. When candidate work produces a reusable method or a substantive finding about another candidate, integrate it at that level.
- Keep organization light. Create a file, folder, Base, or archive only when actual material needs it. Preserve clearly out-of-scope material in an archive only when it retains evidential or methodological value. Reorganize conservatively when retrieval would materially improve.
- Write current notes for human collaborators as well as agents. Present the present understanding, material uncertainty, and operative decisions; leave superseded wording and routine changes of direction to Git history or a changelog unless that history is itself relevant.
- Keep the public `README.md` focused on purpose, methods, scope, and participation. Maintain the inventory in `Candidates.md`. A public directory should have a small `README.md` index, and repository navigation should link to that file.

## Editorial and data conventions

- Use en-GB, following Oxford University Press and UK academic-journal practice; use the serial comma, and use `-ize` rather than `-ise` for applicable Greek-derived verbs.
- In Markdown prose, use U+2018 ‘ <span style="font-variant:all-small-caps">LEFT SINGLE QUOTATION MARK</span>, U+2019 ’ <span style="font-variant:all-small-caps">RIGHT SINGLE QUOTATION MARK</span>, U+201C “ <span style="font-variant:all-small-caps">LEFT DOUBLE QUOTATION MARK</span> and U+201D ” <span style="font-variant:all-small-caps">RIGHT DOUBLE QUOTATION MARK</span>. Retain ASCII apostrophe and quotation mark only where syntax, code, identifiers, or URLs require them.
- Treat the repository as part of an Obsidian vault, but keep public notes portable. Use ordinary relative Markdown links, not wiki links; enclose destinations containing spaces in angle brackets and keep literal spaces.
- Omit a Markdown H1 when Obsidian’s inline title already displays the same frontmatter title or filename. Use an H1 only when it adds materially different information.
- Use Obsidian Bases only for genuinely useful structured filtering or comparison. Prefer ordinary Markdown for narrative research, source notes, and evidence records whose qualifications do not fit stable repeated fields.
- Use title case for working candidate and project names. Reserve all-uppercase names for formally assigned Unicode character names and explicit proposal-style repertoire or property data; typography does not make a working name official.
- Name standards precisely on first use, then use an unambiguous short form. For geographic and language naming, codes, coded filenames, and `country_code`, follow the geographic method rather than restating its data contract here.
- Follow the project’s [Unicode notational conventions](<Methods/Unicode notational conventions.md>) for character, code-point, name, property, range, sequence and identity-table presentation. Load the profile for a notation audit, a material presentation decision or a case not settled by this charter.
- In a table of Unicode characters or sequences, display one extended grapheme cluster per row and put the literal form, code-point notation, and character name or names in the first three columns. Use **Character**, **Code point**, **Name** for characters only; **Character or sequence**, **Code point(s)**, **Name(s)** for mixed contents; and **Sequence**, **Code points**, **Names** for sequences only.
- In public materials, use the registered-mark symbol only in the trademark notice and mention the Unicode Logo only if the project actually displays it.

## Research and evidence

- Reframe informal questions into a defensible formal method when useful, while preserving their substantive direction. State material changes in scope or framing. For claims such as ‘all’ or ‘existing’, define the corpus, version or cut-off, inclusion rules, and limitations.
- Preserve original evidence unchanged. Store crops, annotations, resized images, and other derivatives separately and link them to the original.
- Record available provenance for each evidence item: source or creator, URL or origin, access or capture date, location and context, and rights or permission status. Separate evidential value from permission to publish.
- Distinguish functional or non-marketing use, marketing or brand use, and inline integration with ordinary text. Functional use is normally stronger evidence of an independent communicative convention, but repeated independent marketing use can remain relevant.
- Do not assume locally stored material can be published. Record exact licences, attribution and share-alike duties, compatibility, permissions, and redistribution limits. For stock material, record the provider, stable asset ID, and governing licence or agreement. Treat limited non-free reproduction as a documented rights-review question, not automatic permission or legal advice.
- Record durable findings from official Unicode resources in the relevant project note with a citation and access date. Check current official guidance before presenting a process claim as settled.

## Version control

- Do not create a commit unless the user explicitly requests it.
- A minor or single-purpose commit may use a concise imperative subject alone.
- A comprehensive or multi-issue commit should add a body summarizing material outcomes. When it contains two or more distinct outcomes, use one compact Markdown bullet list rather than separate prose paragraphs.

## Maintaining this guidance

- Update this file without a separate request only when a user direction would help future work and is durable: the user identifies it as durable or standing guidance, confirms it after discussion or iteration, or clearly makes a settled project decision whose future applicability is evident. Do not promote exploratory discussion, hypotheses, provisional preferences, one-task instructions, or ideas still being tested.
- When durability is materially ambiguous, ask or preserve the uncertainty rather than silently creating policy. This does not displace requirements to record operative decisions in the relevant current project or candidate note.
- Keep always-loaded guidance concise. Put task procedures, research findings, source records, and proposal content in their relevant resources and route to them from here only when needed.
- Mention material changes to this file in the final handoff for the task that prompted them.
