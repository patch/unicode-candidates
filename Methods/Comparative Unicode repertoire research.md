---
title: Comparative Unicode repertoire research
last_reviewed: 2026-07-22
tags:
  - method
  - unicode
  - repertoire
  - symbols
---

## Purpose

This method supports bounded claims about ‘all existing Unicode characters’ for a semantic class. It was first applied in [[Existing Unicode characters with fruit referents]]. The objective is an auditable repertoire result that can reveal supportive, adverse or ambiguous comparisons without treating resemblance to encoded subjects as an encoding criterion.

## Workflow

1. **Freeze the cut-off.** Name the latest stable Unicode Standard version, the associated Unicode Emoji version and any CLDR release used for annotations. Exclude drafts and beta data.
2. **Define the unit.** Keep assigned characters, standardized variation sequences, emoji sequences, representative glyphs and private-use mappings distinct. Use one extended grapheme cluster per table row and display it literally beside code-point notation and names. Count code points and semantic referents separately when several characters share a referent.
3. **Define the semantic union.** When the request supplies parallel definitions, generate candidates from the union and classify each candidate under every definition. Do not use one scheme to pre-filter another.
4. **Search independent official surfaces.** Review `UnicodeData.txt`, `NamesList.txt`, name aliases, code charts, emoji property and sequence files, and CLDR annotations. Search names and annotations, but also inspect relevant blocks and complete emoji subgroups so vocabulary choice is not the sole discovery method.
5. **Handle source strata explicitly.** Lead with the contemporary comparison relevant to the proposal, then separate legacy source-set symbols and historical scripts. Exclude ordinary letters, syllables and ideographs that merely write a name. Include a historical sign only when a dedicated non-phonetic symbol, commodity or classificatory function is established and falls within the approved rule.
6. **Maintain a boundary register.** Record plausible false positives, lexical collisions, depicted ingredients, derived objects, plants without the relevant part, and sequences mistaken for characters. This makes exclusions reviewable and helps detect inconsistent rules.
7. **Classify from subject authorities.** Unicode establishes encoded identity and presentation properties, not botanical, zoological or culinary truth. Use appropriate domain authorities and retain qualified or mixed outcomes.
8. **Cross-check counts.** Reconcile character count, unique-referent count, presentation status and sequence count before publication. Inspect the final note for duplicated code points and unaccounted candidates.

## Completeness language

Claim completeness only for the named, versioned corpus and inclusion rules. Do not claim exhaustive knowledge of every cultural meaning attached to arbitrary script characters, glyph variants or private fonts. A character name is discovery evidence, not by itself proof of real-world semantics; conversely, a representative glyph is informative but non-prescriptive.

## Refinement log

- **2026-07-22:** Added separate counts for characters and referents after apple, cherry, strawberry, fig, grain and olive produced multiple encoded characters. Added an explicit historical-sign stratum and boundary register after NamesList searches recovered Aegean commodity signs, including a syllable with a separately documented ideogram value, and script-internal false positives. Extended the botanical pass to cereal commodity signs after recognizing that a grain is a caryopsis even though culinary classification keeps cereals apart from fruit. Added presentation-property and sequence checks after the lime ZWJ sequence demonstrated that an emoji referent need not be an encoded character.
- **2026-07-22:** Reorganized the result by proposal relevance after review showed that contemporary emoji fruit are materially stronger comparisons than legacy terminal symbols or historical Aegean signs. Adopted one extended grapheme cluster per row, literal display backed by code-point notation and names, and separate treatment of the represented subject from the mechanism used to encode or sequence it.
