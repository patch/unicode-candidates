---
title: Character identity and encoding analysis
method_status: reusable working method
last_reviewed: 2026-07-29
tags:
  - method
  - unicode-research
  - character-identity
  - plain-text
---

Use this method to answer the central technical question in a character project:

> What abstract entity, if any, is being proposed, and why is character encoding the appropriate representation?

The method applies to modern symbols, historical repertoires, notational systems, and investigations of possible equivalence to an existing character. It can support a new-character case, unification with an existing character, use of an existing sequence or higher-level representation, deferral for specialist review, or a conclusion that no encodable character has been established. It is a research and review method, not a substitute for the current submission form or a presumption that a proposal should be written.

## Authority and analytical status

Keep three levels distinct in every output:

| Level | What belongs here |
|---|---|
| **Current official guidance** | Definitions, eligibility rules, submission criteria, required proposal material, process, and property terminology stated in current Unicode Consortium material, including Script Encoding Working Group and Emoji Standard & Research Working Group guidance |
| **Project analysis** | Reusable questions, comparison models, evidence classifications, falsification tests, and review procedures developed by this project |
| **Candidate judgement** | The proposed identity, semantic boundary, evidence weighting, unification decision, repertoire contents, likely properties, route, and final recommendation for one candidate |

The official baseline, checked on 29 July 2026, is as follows:

- The Unicode Standard defines an abstract character as a unit of information used to organize, control, or represent textual data; it has no concrete form and is not a glyph. The Standard distinguishes character identity from rendered glyphs and defines plain text as a sequence of character codes. ([Unicode 17.0, Chapter 3, D7](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G2212); [Chapter 2, §§2.2.3 and 2.2.5](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-2/))
- The current [Script Encoding Working Group submission guidance](https://sew.unicode.org/guidelines) requires a proposed addition to be a character and not already encoded. It states that a character expressible as an existing character sequence would be a duplicate representation and is not suitable for encoding. Its three basic criteria are existing use by a community independent of the script creator where applicable, a repertoire whose characters are stable and not in active development, and need for public interchange in plain text. The guidance deliberately leaves the exact amount and form of evidence to case-by-case review and warns that meeting all three criteria does not guarantee acceptance.
- The current guidance requires comparison with possible existing equivalents and visually similar characters. A proposal is also expected to address character properties and ordering; at least the applicable `UnicodeData.txt` values are required through the submission process. ([Unicode properties in character proposals](https://www.unicode.org/pending/properties.html))
- The current process accepts a single proposal PDF through the Script Encoding Working Group submission form. The form collects proposed property data, ISO/IEC 10646 summary information, and, where applicable, a font; the working group will not recommend a proposal without a suitably licensed font. The form contains more detailed requirements and must be rechecked before submission.
- Unicode character names identify characters but do not necessarily express their full meaning. Once a character is encoded, its Unicode Name property value will not change, so naming errors cannot normally be repaired by renaming the character. ([Unicode Character Encoding Stability Policies](https://www.unicode.org/policies/stability_policy.html))
- The Script Encoding Working Group does not accept emoji or flag proposals. The current [emoji-proposal guidance](https://www.unicode.org/emoji/proposals.html), last updated 20 May 2026, defines a separate process and multi-factor selection framework; it directs a widely used symbol that does not require colour towards the character-proposal process. Its inclusion factors include Usage level, supported by prescribed Frequency evidence, while its exclusion factors include Transient and Already representable. It also automatically declines several proposed identities, including signage, while noting that symbols used on signage may be encoded for reasons unconnected with emoji use.

The sections below are the project’s analytical extension of that official baseline. They do not create new Unicode requirements. Every conclusion produced by applying them remains candidate-specific editorial judgement unless an official source is cited for it.

### Route and analytical labels for evidence maps

Use one shared label system when mapping evidence to official processes, project questions and candidate-specific adverse interpretations. In this system, **Character** and **Emoji** identify proposal routes, not disjoint kinds of encoded entity. Character refers to the general character-proposal route handled through the Script Encoding Working Group. Emoji refers to the specialized emoji-proposal route reviewed by the Emoji Standard & Research Working Group. Emoji characters and emoji sequences remain plain text.

The labels are project navigation aids. They do not create Unicode terminology or convert project questions into official requirements. Keep the labels short and put the specific official factor, category or requirement in the application text:

| Label | Definition |
|---|---|
| **Character eligibility** | Official character-status, already-encoded, sequence-duplication and possible-equivalent checks that precede the three basic criteria |
| **Character usage** | The official basic Usage criterion requiring existing use by a community, independently of a creator where applicable |
| **Character stability** | The official basic Stability criterion requiring a stable character or repertoire that is not in active development |
| **Character need for interchange** | The official basic Need for interchange criterion requiring public interchange of information in plain text |
| **Character proposal requirement** | Officially requested proposal material or technical data that is not one of the three basic criteria |
| **Emoji eligibility** | Current submission-window, re-review waiting-period, public-availability, completeness and other threshold rules not captured by a more specific label |
| **Emoji inclusion factor** | A current official factor weighing in favour of emoji selection; identify the applicable factor in the following prose, such as Usage level or Distinctiveness |
| **Emoji exclusion factor** | A current official factor weighing against emoji selection; identify the applicable factor in the following prose, such as Already representable or Transient |
| **Emoji automatic-decline category** | A current proposal subject or condition listed under “Automatically Declined”; identify the applicable heading or clear listed subcategory in the following prose, such as Signage |
| **Emoji proposal requirement** | Officially requested emoji-proposal material that is not itself a selection factor; identify the requirement in the following prose, such as Image Rights & Licenses |
| **Project analytical question** | A reusable question or distinction developed by this project rather than an official Unicode requirement |
| **Candidate counterargument** | The strongest credible candidate-specific adverse or non-encoding interpretation to which the evidence is relevant |

Use bold noun phrases to bound labels. Square brackets are reserved for Markdown links and citations. Do not use an em dash, parenthetical qualifier or internal colon to extend a label. The colon after the bold label separates it from its application. Name any specific factor, category or requirement in the following prose, retaining the source’s spelling and capitalization for an exact official name. For example:

> **Relevance:** **Character usage:** direct support; **Emoji inclusion factor:** Usage level, but only as indirect background; **Project analytical question:** geographic breadth; **Candidate counterargument:** subject importance is not symbol use.

Where an evidence class bears differently on the routes, state the direction separately as **Character:** and **Emoji:**. Omit a route that is not materially implicated rather than importing one route’s favourable or adverse effect into the other. An emoji usage-level assessment concerns frequency of the concept or term under the current prescribed method; it is not equivalent to evidence that a character is already used by a community. Conversely, existing functional symbol use does not by itself satisfy the Emoji Usage level factor.

## Decision frame

State the strongest credible versions of two competing models before choosing between them.

**Encoding model:** a community uses a stable abstract character, or stable repertoire of characters, with identifiable semantics or notational functions; existing Unicode characters, sequences, fonts, markup, images, higher-level protocols, and private agreements do not adequately support the demonstrated need for public interchange in plain text.

**Non-encoding model:** the observed material is better represented as a glyph variant, icon, image, illustration, logo, physical sign, stylistic treatment, existing character, existing sequence, ordinary word or phrase, font behaviour, markup, higher-level protocol, or private convention. Any remaining need concerns appearance, layout, branding, or closed-system exchange rather than a new plain-text unit.

Do not weaken the non-encoding model merely because the project began with a candidate name. Conversely, do not treat a workable closed-system substitute as automatically adequate for public interchange. The analysis must identify the actual users, data, contexts, and losses on both sides.

## Workflow

### 1. State an identity hypothesis

Begin with a provisional identity record. Do not start with a code point or representative glyph.

| Field | Question |
|---|---|
| Proposed abstract entity | What unit of textual information is claimed to recur? |
| Unit type | Is this one character, an inseparable repertoire, a related set of independently viable characters, an existing-character question, or no demonstrated character? |
| Semantic scope | What dictionary-like referent, operator, sound, number, category, instruction, or other function does it carry? |
| Observed functions | What does it do in running text, notation, labels, diagrams, signs, interfaces, or other evidence? |
| Exclusions | What similar meanings, objects, forms, or functions are outside the proposed identity? |
| Invariant features | Which semantic or structural features must persist across uses? |
| Variable features | Which differences in shape, colour, orientation, style, context, or composition may be glyph variation? |
| Working names | What names are attested, translated, ambiguous, contested, overly broad, overly narrow, or visually prescriptive? |
| Intended interchange | Who needs to send what plain-text data to whom, through which systems and operations? |
| Alternatives | What are the best existing-character, sequence, textual, visual, font, markup, protocol, and private-use models? |

Treat this as a hypothesis to test, not a proposal decision. If the identity can be stated only as ‘the exact image shown here’, the image or logo model is presently stronger. If the identity can survive several appropriate glyphs while retaining its meaning or function, a character analysis remains plausible.

For a real-world object, distinguish the dictionary-like referent from a scientific, legal, commercial, or ideological classification unless actual use supports that narrower scope. For a historical or notational character, define its function from the relevant writing or notation system rather than from modern visual association. Record homographs and later reinterpretations separately.

### 2. Build a function-bearing use corpus

Collect evidence capable of showing what unit users communicate, not merely that the subject exists or matters.

For each occurrence, record:

- source, date, place or community, language or notation, and access or capture date;
- exact context, with enough surrounding material to interpret the mark;
- whether the occurrence is functional, non-marketing, marketing, brand, decorative, illustrative, or integrated with ordinary text;
- for platform emoji, reaction, and rich-media material, whether the source establishes only platform capability, public asset or search availability, a local inventory, a provider metric, rich-media sharing, or a context-bearing inline or reaction occurrence, and whether the item is an encoded character or sequence, custom image, alias, sticker, or proprietary built-in reaction;
- the claimed reading or function, and whether it is stated by the source, inferred by the project, or confirmed by a user or specialist;
- whether an existing character, sequence, word, image, or protocol could replace it without loss in that context;
- independence from the creator, commissioning organization, font, source set, or previously copied example;
- visual form and material variants, without treating a crop or redraw as new evidence; and
- provenance, rights, and whether the item may be reproduced or only cited.

For scripts and notational systems, prioritize strings, paradigms, inventories, teaching material, reference works, and evidence of productive use. For modern symbols, distinguish functional communication from subject depiction and branding. A physical sign is an artefact: it may contain text, a pictogram, a logo, or a candidate character, but the existence of the sign does not decide which of those is encoded.

Use [Geographic evidence research for symbol proposals](<Geographic evidence research for symbol proposals.md>) where territory, language, signage, diaspora, biological referents, or evidence-corpus design is material. Preserve observed evidence, sourced claims, working inferences, and proposal decisions as separate statement types.

### 3. Distinguish character identity from visual objects

Classify each relevant use by its best current explanation:

| Model | Diagnostic question | Typical implication |
|---|---|---|
| Abstract character | Does a repeatable information unit retain identity across appropriate renderings and contexts? | Continue the encoding analysis |
| Glyph or glyph variant | Is this one rendering, contextual form, stylistic alternate, ligature, or abbreviation of an existing character or sequence? | Use fonts or rendering unless independent character semantics are established |
| Icon or pictogram | Does the graphic label an action, category, object, or interface function primarily as a visual asset? | Test whether the identity is also used as plain text; otherwise an icon system may be sufficient |
| Image or illustration | Is the exact depiction, composition, or scene the information being exchanged? | Store or exchange an image with appropriate textual metadata |
| Logo or brand mark | Is identity tied to an organization, product, protected design, or prescribed artwork? | Use the logo asset and brand rules; separately test any generic character embedded in it |
| Physical or displayed sign | Is this an artefact that combines graphics, words, layout, colour, or an overlay to communicate in place? | Decompose its content and test the base symbol independently |
| Font behaviour | Can an encoded string plus ordinary shaping, ligature, stylistic-set, or alternate-glyph behaviour produce the form? | Encoding another character may duplicate presentation |
| Character sequence | Do existing characters conventionally and interoperably express the same textual unit? | Prefer the sequence unless a distinct identity and need remain |

These categories are diagnostic, not mutually exclusive. An icon can depict an abstract character; a logo can contain ordinary characters; and a physical sign can provide evidence of a wider convention. The question is what must be preserved as textual data when the original artwork, font, layout, or venue is removed.

The Unicode code charts provide representative glyphs for identification, not prescribed designs, as the official [Where is my Character?](https://www.unicode.org/standard/where/) explanation also emphasizes. Apply an **independence test**: substitute several attested or technically suitable glyphs that preserve the hypothesized invariant features. If the meaning survives, document the acceptable range. If only one exact artwork, colour scheme, orientation, or composition is acceptable, explain why this is not better handled as an image, logo, or higher-level representation.

### 4. Test form stability, variation, and mirroring

Form stability does not require one frozen outline. Code independent occurrences for potentially meaningful features, then distinguish:

- invariant identity features;
- ordinary typeface, handwriting, scale, stroke, or simplification differences;
- contextual shaping or joining;
- stylistic or regional variants;
- orientation, rotation, reflection, or mirroring;
- optional colour, frame, enclosure, overlay, or annotation;
- forms that may instead be separate characters; and
- ambiguous or falsely grouped forms.

Ask whether reflection or direction:

1. is merely an interchangeable glyph variant;
2. is selected by layout or bidirectional context;
3. marks a semantic or notational contrast;
4. distinguishes two members of a repertoire; or
5. is an unsupported modern editorial interpretation.

Do not infer a separate character from a mirrored glyph alone, and do not infer `Bidi_Mirrored=Yes` merely because a shape can be reflected. If direction changes meaning, seek paired use and specialist analysis. If software is expected to mirror the glyph in bidirectional text, record the observed behaviour for later property review.

For modern creator-led systems, test whether use and form have stabilized outside the creator. For historical material, distinguish scribal variation, damaged forms, palaeographic classifications, and editorial sign lists. For notation, distinguish stable semantic tokens from renderer-selected constructions.

### 5. Test existing-character equivalence and possible unification

Freeze the Unicode version and other relevant repertoire cut-offs. Search:

- the Unicode Character Database, code charts, NamesList annotations, name aliases, and relevant core-specification chapters;
- relevant Unicode Standard Annexes and technical standards;
- current pipeline characters and the Archive of Nonapproval Notices;
- standardized variation sequences, named sequences, emoji data, and other applicable sequence registries;
- source encodings, domain standards, scholarly sign lists, and community mappings; and
- semantically related as well as visually similar characters.

Use [Comparative Unicode repertoire research](<Comparative Unicode repertoire research.md>) when a bounded claim about a whole Unicode semantic class is needed. Its repertoire result discovers candidates for comparison; the present method decides whether one of them represents the same abstract entity.

For each plausible equivalent, compare:

| Dimension | Questions |
|---|---|
| Encoded identity | What do the Unicode name, annotations, properties, block context, and standard text establish? |
| Attested semantics | Do users give the existing and proposed forms the same reading or function? |
| Substitutability | Are they interchanged in actual text without loss, or only visually confusable? |
| Glyph range | Does the requested form fit a documented glyph range of the existing character? |
| Behaviour | Would normalization, shaping, segmentation, bidirectionality, mirroring, collation, or identifiers treat them compatibly? |
| Community distinction | Do relevant users or specialists consistently distinguish them as textual units? |
| Historical relation | Is the difference palaeographic, stylistic, semantic, source-set based, or a later reinterpretation? |
| Remaining gap | What public-interchange failure persists if the existing character is used? |

Visual difference alone does not establish a new character. Visual identity alone does not prove unification either: characters with the same or overlapping glyphs may differ by script membership, semantics, properties, or conventional use. The candidate analysis should conclude **represented by an existing character**, **plausible unification requiring review**, **distinct from the compared character**, or **unresolved**, and state the evidence and specialist authority needed.

Do not use the mere existence of superficially similar encoded characters as precedent that another one should be encoded. Compatibility characters, legacy source-set symbols, and historical-script characters may answer different interchange needs.

### 6. Test representation by an existing sequence

Write every candidate sequence explicitly by literal form, code points, and names. Identify its type:

- ordinary character sequence;
- base plus combining mark;
- standardized variation sequence;
- emoji modifier or emoji ZWJ sequence;
- named character sequence;
- shaped or ligated sequence; or
- an ad hoc visual approximation with no standardized semantic identity.

Then test:

1. whether relevant users already use the sequence for the proposed meaning;
2. whether Unicode or another applicable standard gives it that meaning;
3. its NFC, NFD, NFKC, and NFKD behaviour where normalization is material;
4. rendering and fallback across representative implementations;
5. copying, pasting, searching, indexing, editing, and interchange;
6. grapheme, word, and line-boundary behaviour where relevant;
7. whether exposed components create a materially different reading; and
8. whether the sequence preserves semantics without a particular font or private agreement.

Current Script Encoding Working Group guidance states that a proposed character which can be expressed as an existing character sequence would be a duplicate representation and is not suitable for separate encoding. Applying that rule requires the project to distinguish a sequence that represents the hypothesized abstract character from one invented only because its rendered glyph resembles the desired mark. A visual approximation does not automatically encode the same abstract entity; a standardized sequence does not automatically meet every non-emoji interchange need.

### 7. Compare non-character representations

Evaluate the strongest workable alternative rather than listing weak substitutes.

| Representation | What it can preserve | Principal limitation to test |
|---|---|---|
| Existing word or phrase | Lexical meaning in ordinary text | May not preserve a compact symbol, operator, language-neutral label, or source-faithful transcription |
| Existing character | Standard plain-text identity and behaviour | May collapse a conventionally distinct meaning or fall outside its legitimate glyph range |
| Existing sequence | Standard components and possibly a standardized combined representation | May expose components, normalize, segment, or behave differently from the claimed unit |
| Font, ligature, or stylistic alternate | Desired appearance from an existing string | Semantics usually remain those of the underlying string and depend on the font or renderer |
| Markup or higher-level protocol | Structure, styling, semantics, layout, and rich notation | May not survive plain-text extraction or be available across the demonstrated interchange contexts |
| Image, icon, or logo asset | Exact appearance, colour, composition, and branding | Is not searchable or editable as the proposed textual unit without separate metadata |
| Private-use character or icon-font mapping | Efficient exchange inside a coordinated system | Unicode semantics are defined only by private agreement; unrelated recipients cannot infer them |
| Custom emoji or reaction asset | A compact, named image usable inline or as a reaction inside a platform, server, or workspace | Identity depends on a local asset, shortcode or provider ID, platform support, access rights, and prior agreement; directory availability alone does not show public-interchange need |
| Sticker, GIF, or emote asset | Animated or exact visual expression distributed through rich-media search, a picker, an API, or a pack | Farther from plain text than custom emoji; identity depends on the media file, tags, placement, and platform, while search visibility does not establish a textual unit |
| Local transliteration or transcription convention | Reproducible scholarly or community text | May be adequate for the specialist corpus but not preserve the original character identity |

For each alternative, name:

- sender and recipient;
- data format and systems;
- whether prior agreement is required;
- required operations such as input, display, search, copy and paste, quotation, collation, parsing, or archival retrieval;
- what information survives font loss, plain-text extraction, conversion, and fallback;
- accessibility and discoverability effects; and
- the concrete loss, if any, compared with character encoding.

Plain-text need is not demonstrated by asserting that an image is inconvenient or that a desired glyph is absent from a keyboard. It is demonstrated by a public-interchange requirement for the abstract textual unit that existing standard representations do not adequately meet. Conversely, a private-use mapping is not evidence that Unicode must encode the item, but independent mappings of the same stable entity may document a recurring interoperability problem.

### 8. Define semantic and repertoire boundaries

For a single character, produce a dictionary-like definition with positive examples, exclusions, and ambiguous edge cases. Separate:

- referent from representative glyph;
- core meaning from metaphorical or context-dependent readings;
- generic category from named subtype or instance;
- conventional semantics from one author’s interpretation; and
- the character itself from enclosing circles, prohibition strokes, labels, decorations, or other composed sign elements.

For a multi-character system, maintain a repertoire boundary register:

| Status | Meaning |
|---|---|
| Core | Independently attested character with stable identity and function |
| Variant or unified | Attested form currently analysed as a glyph variant or existing-character equivalent |
| Sequence or construction | Represented compositionally rather than proposed as a separate character |
| Disputed | Character status, reading, or distinction is contested |
| Peripheral | Borrowed punctuation, numeral, symbol, or logogram whose inclusion needs a separate rationale |
| Excluded | Outside the stated corpus or inclusion rule |
| Unresolved | Requires specified evidence or specialist review |

State the corpus, dates, source traditions, inclusion rules, and treatment of rare, obsolete, reconstructed, unattested, creator-proposed, or still-developing forms. Do not make a repertoire look stable by silently dropping disagreements, and do not inflate it by encoding every documented glyph.

Distinguish an inseparable repertoire from a related set of independently viable characters. Shared scholarship or a possible joint proposal does not by itself make every member dependent on the others.

### 9. Assess names without allowing them to decide identity

Maintain three separate name fields where useful:

1. **working project name** — an editorial retrieval label;
2. **attested names and aliases** — community, language, scholarly, standard, or source-set terms with provenance; and
3. **possible Unicode name** — a proposal-stage identifier subject to official review.

Test naming risks:

- a name that prescribes one glyph rather than the abstract identity;
- a biological, historical, religious, political, gender, or technical scope narrower or broader than attested use;
- an English label mistaken for a universal community name;
- collision or confusion with an existing Unicode name, formal alias, CLDR short name, or different established concept;
- a name that treats a working reconstruction or disputed reading as settled;
- an eponym, brand, trademark, or current institutional terminology likely to obscure generic use; and
- multiple repertoire names that conceal unification or one name that collapses distinct characters.

Because an encoded Unicode name is stable and may not express the full semantics, do not attempt to make it a complete definition. Put qualifications in proposal prose, names-list annotations, aliases where officially appropriate, or later descriptive text. Final naming remains candidate-specific and committee-reviewed.

### 10. Describe expected behaviour before assigning properties

Character properties affect software behaviour, so they are evidence-bearing technical claims, not proposal decoration. At research stage, describe the observed behaviour and closest analogues before recommending property values.

Review only materially relevant dimensions:

| Dimension | Early analytical question |
|---|---|
| Basic type | Letter, mark, number, punctuation, symbol, separator, format control, or another role? Spacing, combining, or enclosing? |
| Script relation | Script-specific, script-common, inherited, or part of a notation rather than a script? |
| Case and numeric behaviour | Does it participate in case pairs, digits, numeric values, or numeric syntax? |
| Shaping | Does it join, stack, ligate, reorder, stretch, or take contextual forms? |
| Normalization | Is any canonical or compatibility relation actually established, and what happens to plausible existing sequences? |
| Segmentation | How should grapheme, word, sentence, and line boundaries behave in attested strings? |
| Bidirectionality | How does it behave among left-to-right and right-to-left text, numbers, punctuation, or neutrals? |
| Mirroring | Is reflection a rendering behaviour in bidirectional context, a semantic contrast, or irrelevant? |
| Ordering | Is there dictionary, sign-list, numerical, or other conventional order? |
| Identifiers | Is identifier use attested or required, and what restrictions would be expected? |
| Confusability and security | Which existing characters or sequences could be mistaken for it, in which fonts and contexts, and with what practical consequence? |
| Presentation | Is text or emoji presentation relevant, or is variation ordinary font design? |

Consult the current official property guidance and the applicable Unicode Standard Annexes before producing proposal data, including [UAX #9](https://www.unicode.org/reports/tr9/) for bidirectionality, [UAX #15](https://www.unicode.org/reports/tr15/) for normalization, [UAX #29](https://www.unicode.org/reports/tr29/) for text segmentation, [UAX #31](https://www.unicode.org/reports/tr31/) for identifiers, [UAX #44](https://www.unicode.org/reports/tr44/) for the Unicode Character Database, and [UTS #39](https://www.unicode.org/reports/tr39/) for security mechanisms where applicable.

Do not:

- invent a decomposition because the glyph looks composite;
- infer mirroring, directionality, identifier status, or segmentation from appearance alone;
- copy every property from a merely similar character;
- assign a code point as if it were settled; or
- fill uncertain fields only to make the analysis look complete.

Instead, record **observed behaviour**, **proposed analogue**, **tentative implication**, **contrary evidence**, and **specialist question**. At proposal stage, convert supported conclusions into the current required data format and leave committee-assigned matters to the committees.

### 11. Keep the character and emoji routes distinct

Resolve the abstract-identity and representation questions before assuming a route.

For the character-proposal route, apply the Script Encoding Working Group’s use, stability, and plain-text public-interchange criteria. A character may be encoded as a text symbol without emoji presentation. A desire for a colourful or platform-designed image does not by itself establish a character case.

For the emoji-proposal route, apply the current emoji selection factors and exclusions, including whether the concept is already represented, overly specific, open-ended, transient, or justified only by resemblance to an existing emoji. The current guidance also excludes requests for an exact image and several categories such as logos, brands, user-interface icons, and signage. Evidence discovered on a physical sign does not necessarily make the proposed entity ‘signage’; classify the entity rather than the evidence venue.

An emoji character or emoji sequence is plain text, but emoji treatment does not encode a second abstract character. Existing emoji representation may answer one use case while leaving a separately evidenced non-emoji character question unresolved; equally, a character case does not guarantee emoji selection or presentation. State which evidence and requirement belongs to which route.

Popularity, subject importance, repertoire similarity, visual appeal, category completion, or the existence of a pictogram does not independently establish character-encoding need. Current emoji guidance uses its own multi-factor selection framework; do not import one favourable emoji factor as if it satisfied the character criteria.

Unicode emoji characters and standardized emoji sequences are plain text. A platform’s “custom emoji” may instead be a named image asset handled by a higher-level protocol; its entry, inline display, and reaction behaviour may align with emoji without making the asset plain text. Stickers, GIFs, and emotes are normally still farther removed: rich-media objects selected through search, a picker, an API, or a pack. Using any of these in a reaction position does not change its encoding status.

Keep platform capability, directory or sticker-search availability, installation, provider-defined metrics, inline use, rich-media sharing, and actual reaction occurrences distinct; see [Custom emoji, reaction, and sticker sources](<../Research/Custom emoji, reaction, and sticker sources.md>).

### 12. Seek disconfirming evidence

For each model, record observations that would materially weaken or overturn it.

Evidence that may falsify or substantially weaken the **encoding model** includes:

- relevant users consistently identify the mark as artwork, a logo, a stylistic glyph, or an illustration rather than a textual unit;
- an existing character is routinely used interchangeably without semantic or behavioural loss;
- an existing standardized sequence already carries the identity and behaves adequately in the demonstrated workflows;
- the requested distinction depends on one precise shape, colour, orientation, font, or brand design;
- the repertoire or meaning remains in active development or lacks defensible boundaries;
- use is confined to a creator, one private agreement, or copied derivatives rather than a community;
- the claimed need disappears when the actual interchange task is specified; or
- the evidence establishes only popularity, importance, similarity to encoded subjects, or visual recognizability.

Evidence that may falsify or substantially weaken the **non-encoding model** includes:

- independent communities repeatedly use a stable semantic unit across media, renderings, and contexts;
- users preserve the unit in transcription, indexing, quotation, search, or data exchange even when the original image or layout is unavailable;
- the proposed and existing characters are conventionally distinguished by meaning, behaviour, repertoire membership, or attested substitution;
- an apparently adequate sequence has different semantics, unstable fallback, unsuitable boundaries, or a demonstrated loss in the relevant interchange;
- multiple independent private or font encodings converge on the same entity and expose a recurring public-interchange failure; or
- images, markup, or higher-level protocols demonstrably fail in environments where the stable unit must remain plain text.

Absence of disconfirming evidence is not proof. Record the search boundary, negative findings, unresolved contradictions, and evidence that could still change the result.

### 13. Record a proportionate outcome

Choose the smallest useful output:

| Level | Use | Minimum output |
|---|---|---|
| Screening | Early candidate or obvious equivalence question | Identity hypothesis, strongest non-encoding model, principal evidence, existing-character and sequence checks, unresolved issue, provisional outcome |
| Full single-character analysis | Material evidence and a plausible encoding question | Function corpus, semantic boundary, equivalence matrix, sequence and alternative-representation tests, form analysis, plain-text interchange cases, property sketch, falsifiers, and recommendation |
| Repertoire analysis | Historical, created, or notational multi-character system | Shared model plus per-character boundary register, variant/unification decisions, ordering and behaviour, source-tradition limits, and specialist questions |
| Proposal review | Candidate approaching submission | Recheck current official guidance and form; map every criterion and technical field to evidence; identify unsupported assignments, rights dependencies, and open review issues |

Use one of these candidate-specific outcomes:

- prima facie case for a new character or stable repertoire;
- represented by an existing character;
- likely unification, pending specified review;
- represented by an existing sequence;
- better represented by text, font behaviour, markup, a higher-level protocol, an image, or private agreement;
- no stable abstract character demonstrated;
- defer pending named evidence or specialist questions; or
- route-specific result, such as a character case remaining open while emoji treatment is separately resolved.

For every unresolved specialist issue, state the exact question, the relevant discipline or community, the evidence or review needed, and which identity, unification, property, or route decision the answer could change. ‘Needs expert review’ by itself is not an actionable result.

Do not change a candidate conclusion merely to demonstrate the method. Applying the method may confirm, qualify, defer, or overturn a conclusion only when candidate evidence warrants that change.

## Review checklist

- [ ] The proposed entity is stated independently of a code point and exact glyph.
- [ ] Semantic scope, observed functions, exclusions, and ambiguous cases are explicit.
- [ ] Evidence types and statement status are kept separate.
- [ ] Community use and independence are assessed under current official guidance.
- [ ] Form and repertoire stability are assessed without demanding one frozen glyph.
- [ ] Character, glyph, icon, image, illustration, logo, sign, font, and sequence explanations are distinguished where material.
- [ ] The latest stable Unicode repertoire, pipeline, and nonapproval notices have been checked.
- [ ] Possible existing-character equivalents and unification have been tested semantically and technically, not only visually.
- [ ] Every plausible existing sequence is written explicitly and tested where material.
- [ ] The strongest existing-text, font, markup, protocol, image, and private-agreement alternatives are assessed.
- [ ] Plain-text public interchange names users, systems, operations, and concrete loss.
- [ ] Representative-glyph independence and recognizable identity have been tested.
- [ ] Names and repertoire boundaries expose uncertainty rather than settling it editorially.
- [ ] Expected behaviour is described before property values are proposed.
- [ ] Normalization, segmentation, bidirectionality, mirroring, identifiers, confusability, and security are addressed only when material.
- [ ] Character and emoji implications are kept distinct.
- [ ] Both encoding and non-encoding models have credible falsifiers.
- [ ] Unresolved specialist questions identify the required expertise and decision.
- [ ] The output is proportionate and states its evidence cut-off and official-guidance check date.

## Relationship to other project methods

This method is consistent with and complementary to:

- [Geographic evidence research for symbol proposals](<Geographic evidence research for symbol proposals.md>), which establishes semantic, geographic, and function-bearing evidence without treating popularity or distribution as encoding need;
- [Comparative Unicode repertoire research](<Comparative Unicode repertoire research.md>), which produces versioned and auditable existing-character or sequence corpora without treating repertoire resemblance as precedent; and
- [Recovering changed and unavailable web sources](<Recovering changed and unavailable web sources.md>), which supports historical and procedural reconstruction without turning archive availability into stronger provenance or reuse rights.

The present method consumes those results to decide what textual unit they establish and whether character encoding is the appropriate representation. It does not duplicate their geographic, repertoire-discovery, archive, or rights procedures.

## Illustrative examples only

- A pictorial form substituted for LATIN CAPITAL LETTER O (`U+004F`) or FULL STOP (`U+002E`) in a logo can show recognizable reduction to character scale while remaining a glyph or brand treatment of the existing character. It does not by itself demonstrate an encoding gap. See [Durian visual use](<../Candidates/Durian/Research/Durian visual use.md>).
- The lime emoji 🍋‍🟩 (`U+1F34B U+200D U+1F7E9`) shows that a subject may have a standardized representation as a sequence without a separately encoded character for that subject. It neither supplies a representation for another fruit nor establishes that another fruit should be encoded. See [Existing Unicode characters with fruit referents](<../Research/Existing Unicode characters with fruit referents.md>).

These examples illustrate distinctions in the method; they are not a Durian identity analysis or a change to that candidate’s working judgement.

## Refinement log convention

Append a dated refinement only after applying this method reveals a reusable change. State the trigger, the change, why it improves the analysis, and which earlier outputs may need review. Do not record routine editing, candidate conclusions, or a refinement that has not actually occurred.

### 29 July 2026: custom emoji, reaction, and sticker evidence

Registering public custom-emoji directories and sticker search revealed a reusable ambiguity between platform capability, asset or search availability, and actual inline, sharing, or reaction use. The method now distinguishes those evidence levels and places Unicode emoji plain text, platform custom emoji, and richer sticker, GIF, or emote assets in separate representation layers. This prevents a directory or search result from being mistaken for encoding evidence while retaining its value for discovering variants, local conventions, representative forms, and context-bearing occurrences.
