---
title: Unicode terminology profile
method_status: maintained project reference
last_reviewed: 2026-07-29
tags:
  - method
  - unicode
  - terminology
---

This profile records the Unicode terms whose distinctions materially recur in this project. The current official [Glossary of Unicode Terms](https://www.unicode.org/glossary/) is the default terminology authority; where a glossary entry points to a normative definition or specification, that cited source controls the exact technical rule. The entries below are project-oriented paraphrases, not replacement definitions or a copy of the glossary.

## Loading and maintenance rule

Use this local profile for routine writing and review. Open only the relevant official glossary entry when:

- a material term is absent here;
- an exact definition or source citation is required;
- local usage appears to conflict with the current glossary; or
- a Unicode release or scheduled review gives reason to revalidate the entry.

Do not load the external glossary wholesale for routine work. When an official check produces a durable clarification, update the relevant entry and `last_reviewed` date here. Preserve exact official capitalization for formal names, property names, proposal factors, and quoted labels; glossary heading capitalization does not require title case in ordinary prose.

## Character identity and encoding

| Term | Project usage and boundary | Official entry |
| --- | --- | --- |
| abstract character | A unit of textual information, independent of any one concrete appearance. State a candidate’s hypothesized abstract identity before discussing a code point or representative glyph. | [Abstract Character](https://www.unicode.org/glossary/#abstract_character) |
| character | Use as a synonym for abstract character where the context is clear, including for a prospective entity whose character status is being tested. Do not use it for an exact image, font-specific shape, or code point. | [Character](https://www.unicode.org/glossary/#character) |
| encoded character | The association between an abstract character and a code point. A prospective character is not an encoded character; an existing encoded character may be compared with it. | [Encoded Character](https://www.unicode.org/glossary/#encoded_character) |
| assigned character | A code point assigned to an abstract character. Freeze the Unicode version when making repertoire or count claims about assigned characters. | [Assigned Character](https://www.unicode.org/glossary/#assigned_character) |
| base character | Any graphic character whose General Category is not a combining mark. In a combining character sequence, it is the initial character to which the combining marks apply. | [Base Character](https://www.unicode.org/glossary/#base_character) |
| code point | A numerical value or position in a codespace. Give it in `U+XXXX` notation where applicable; do not treat it as the character or glyph itself. | [Code Point](https://www.unicode.org/glossary/#code_point) |
| character name | The unique string identifying an encoded abstract character. Prefer ‘character name’ or, when qualification helps, ‘Unicode character name’; avoid the imprecise short form ‘Unicode name’. A proposal-stage possible character name remains provisional. | [Character Name](https://www.unicode.org/glossary/#character_name) |
| character properties | Property names and values associated with individual characters. Distinguish a technical character property from an ordinary descriptive property, and verify proposal data against the current applicable source. | [Character Properties](https://www.unicode.org/glossary/#character_properties) |
| character repertoire; repertoire | A collection of characters included in a character set. ‘Proposed repertoire’ may describe the intended character collection in a proposal. When a research corpus also contains sequences or non-character representations, call it a ‘character-and-sequence set’, ‘corpus’, or another explicit mixed term rather than treating the sequences as repertoire members. | [Character Repertoire](https://www.unicode.org/glossary/#character_repertoire); [Repertoire](https://www.unicode.org/glossary/#repertoire) |
| unification | Identifying characters as common across writing systems or source traditions. In candidate analysis, use it only for a possible shared abstract character or existing-character identity; visual resemblance alone does not establish unification. | [Unification](https://www.unicode.org/glossary/#unification) |
| private-use character | A character assigned to a private-use code point by private agreement. Its project-relevant semantics come from that agreement, not from a standardized Unicode assignment of the proposed identity. | [Private-Use Character](https://www.unicode.org/glossary/#private_use_character) |
| script | A collection of letters and other written signs used to represent textual information in one or more writing systems. Do not use ‘script’ as an automatic synonym for ‘writing system’. | [Script](https://www.unicode.org/glossary/#script) |

## Text units and representations

| Term | Project usage and boundary | Official entry |
| --- | --- | --- |
| glyph | A form or glyph image selected to depict one or more characters. Treat representative glyphs, variants, and font behaviour separately from character identity. | [Glyph](https://www.unicode.org/glossary/#glyph) |
| pictograph; pictogram | A symbol denoting an object through a more or less conventional visual likeness. A pictogram may be evidence for a character, an icon convention, or merely an image; the label does not decide encoding status. | [Pictograph](https://www.unicode.org/glossary/#pictograph) |
| character sequence | An ordered sequence of abstract characters. Write a materially compared sequence by literal form, code points, and character names, and do not imply that it is one encoded character. | [Character Sequence](https://www.unicode.org/glossary/#character_sequence) |
| combining mark | The commonly used synonym for ‘combining character’. Keep it distinct from a base character when describing candidate sequences and rendering. | [Combining Mark](https://www.unicode.org/glossary/#combining_mark) |
| grapheme | A minimally distinctive unit in a particular writing system; the glossary also records the user-perceived-character sense. Do not use it as an unrestricted synonym for encoded character. | [Grapheme](https://www.unicode.org/glossary/#grapheme) |
| grapheme cluster; extended grapheme cluster | A segmentation unit bounded under Unicode Standard Annex #29. The project’s one-extended-grapheme-cluster-per-row display rule keeps a sequence visually together; it does not make the cluster one character or one code point. | [Grapheme Cluster](https://www.unicode.org/glossary/#grapheme_cluster); [UAX #29](https://www.unicode.org/reports/tr29/) |
| plain text | Computer-encoded text consisting only of a sequence of code points from a given standard, without additional formatting or structural information. Demonstrated need for public interchange in plain text requires users, systems, operations, and concrete loss under existing representations. | [Plain Text](https://www.unicode.org/glossary/#plain_text) |
| higher-level protocol | An explicit or implicit agreement about interpreting Unicode characters beyond the Standard. Markup, platform conventions, private mappings, and contextual agreements may therefore provide representations without creating another character. | [Higher-Level Protocol](https://www.unicode.org/glossary/#higher_level_protocol) |
| rich text | Plain text with added information such as styling, structure, or annotation. Use the more specific ‘rich-media object’ for a sticker, GIF, or other media asset rather than treating every non-plain-text representation as rich text. | [Rich Text](https://www.unicode.org/glossary/#rich_text) |

## Emoji and sequences

| Term | Project usage and boundary | Official entry |
| --- | --- | --- |
| emoji | The glossary covers both certain Unicode-encoded symbols with customary colourful or playful presentation and unencoded graphics commonly called emoji. Qualify the layer when it matters: ‘Unicode emoji character’, ‘emoji sequence’, ‘platform custom emoji’, or another specific representation. | [Emoji](https://www.unicode.org/glossary/#emoji) |
| emoji character; emoji sequence | A Unicode emoji character is an encoded character; an emoji sequence contains multiple code points. Both are plain text when defined by the applicable Unicode data. Emoji treatment or presentation does not encode a second abstract character. Use the current Unicode Emoji specification for exact sequence classes. | [Emoji](https://www.unicode.org/glossary/#emoji); [UTS #51](https://www.unicode.org/reports/tr51/) |
| RGI | ‘Recommended for General Interchange’, a subset of emoji or emoji sequences intended for broad cross-platform support. Do not imply that every emoji or possible sequence is RGI. | [RGI](https://www.unicode.org/glossary/#RGI) |
| variation selector | A character used with a base to select a defined subset of potential graphic presentations. It has no independent graphic shape and must not be described as a freestanding presentation glyph. | [Variation Selector](https://www.unicode.org/glossary/#variation_selector) |
| variation sequence | Exactly two code points: a base character or spacing mark followed by one variation selector. Do not use the term for an arbitrary variant sequence. | [Variation Sequence](https://www.unicode.org/glossary/#variation_sequence) |
| standardized variation sequence | A variation sequence defined in `StandardizedVariants.txt`; distinguish it from emoji variation sequences and registered ideographic variation sequences where the source distinction matters. | [Standardized Variation Sequence](https://www.unicode.org/glossary/#standardized_variation_sequence) |

## Standards and potentially ambiguous language

| Term | Project usage and boundary | Official entry |
| --- | --- | --- |
| Unicode Character Database; UCD | The collection of files providing normative and informative character properties and mappings. Cite the exact version, file, and entry for a proposal-facing data claim. | [Unicode Character Database](https://www.unicode.org/glossary/#unicode_character_database) |
| canonical | Reserve the Unicode technical senses for conformance, normative mappings, and forms of equivalence. Describe project materials as ‘authoritative’, ‘integrated’, ‘current’, or ‘project-approved’ rather than ‘canonical’. | [Canonical](https://www.unicode.org/glossary/#canonical) |
| normalization | In the Unicode sense, processing that gives canonically or compatibility-equivalent strings the specified representations used for equivalence comparison. Qualify ordinary statistical or editorial normalization where confusion is possible. | [Normalization](https://www.unicode.org/glossary/#normalization) |
| property | Use ‘character property’ for the Unicode technical sense. Ordinary uses such as a property of an evidence corpus, a venue property, or a metadata field are not Unicode terminology and should remain clear from context. | [Property](https://www.unicode.org/glossary/#property) |

## Project-specific working terms

These terms are not supplied as Unicode glossary definitions. They organize the investigation without asserting official status:

- **candidate** or **prospective character:** a subject being evaluated for possible encoding, not an official Unicode candidate or an assumption that it is a character;
- **symbol:** the project-level working subject where ‘character’ would prematurely decide the abstract-character question;
- **sign:** a physical or displayed artefact that may combine text, pictograms, layout, colour, and other elements;
- **signage:** the usage context or body of signs supplying evidence;
- **icon:** a visual asset or interface representation whose possible independent plain-text identity still requires testing;
- **character-proposal route** and **emoji-proposal route:** project navigation labels for separate official submission and review processes, not different ontological kinds of plain text; and
- **authoritative project record** or **integrated project research:** current project material that has passed the applicable verification and approval gates. These expressions avoid the Unicode-specific ambiguity of ‘canonical’.

## Conformance audit of 29 July 2026

The initial corpus comprised all 71 tracked Markdown files in the working tree, totalling 5,258 lines, at Git `333de7b3603dc902891fb1c7024e877bfabf4b92`, with the already approved uncommitted `AGENTS.md` terminology rule included. The audit also screened project-authored labels in the other tracked text files where relevant.

The official glossary page was retrieved once into temporary working data and was not added to the repository. Its 190,153-byte HTML representation had SHA-256 `3803680631c16f4d19f9f35e725e1fc7a452a7e19a5a311266bd065207738d45`. A deterministic extraction found 487 glossary headings; a case-insensitive exact-term scan found 78 headings in the initial Markdown corpus. Exact matching generated review candidates only: ordinary-English homonyms, URLs, quotations, and formally named properties or documents required contextual classification.

The semantic review:

- reserved ‘canonical’ for its Unicode technical senses and replaced 51 project-record uses with ‘authoritative’, ‘integrated’, or another explicit term;
- standardized ‘character name’ where ‘Unicode name’ or an unqualified ‘name’ could be ambiguous;
- corrected private-use wording that had treated private-use characters as simply unassigned rather than privately interpreted;
- reserved ‘repertoire’ for character collections and renamed mixed character-and-sequence or proprietary reaction sets where necessary;
- aligned the project’s compact plain-text definition with the glossary’s sequence-of-code-points wording; and
- retained ordinary-English homonyms only where their context does not imply the Unicode technical term.

The audit establishes conformance for the defined working-tree corpus and the reviewed term matches, not for Git history, quoted third-party wording, future files, or every concept that could be expressed without using a glossary heading.
