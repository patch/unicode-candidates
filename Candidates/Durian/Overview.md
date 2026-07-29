---
title: Durian overview
last_reviewed: 2026-07-29
tags:
  - candidate
  - durian
  - project-context
---

This note records the current project decisions and intentions needed by collaborators working at different times. It is not a research log, a proposal draft, or a fixed plan for the vault’s structure.

## Current objective

Research whether a durian character has a sound case for encoding, including evidence and reasoning both for and against it, and prepare a proposal if the evidence continues to support that conclusion. My present judgement favours encoding, particularly because of durian’s repeated use on signage in Southeast Asia, but the research remains open to disconfirming evidence and better interpretations. The signage establishes a prima facie visual convention; it does not yet establish need for public interchange in plain text.

## Submission strategy

Prepare the character case through the Unicode Script Encoding Working Group’s character-proposal process. Treat emoji re-review as a separate, later step whose eligibility timing remains unresolved under the public record; the evidence and date interpretations are documented at [Unicode history and proposal status](<Research/Unicode history and proposal status.md>).

Once emoji re-review is confirmed eligible, the intended emoji proposal may cross-reference any public L2 document assigned to the character proposal. The two paths should share evidence without implying that either process guarantees the other outcome.

## Research status

I have already conducted years of research, but not all of it has been contributed or reviewed. Contribution and source review are in progress, and the prior Unicode history has been reconstructed from its external sources at [Unicode history and proposal status](<Research/Unicode history and proposal status.md>).

The candidate-specific [evidence-to-encoding-question map](<Research/Evidence to encoding-question map.md>) distinguishes evidence that bears on character identity, usage, stability, equivalence or public interchange from contextual material that may be well sourced but has little encoding relevance. It currently supports continued research and deferral rather than proposal drafting: functional signage supplies the strongest support, while plain-text public-interchange need remains the strongest gap.

The evidence-led [Durian geographic survey](<Research/Durian geographic survey.md>) is a first-pass dataset with explicit confidence tiers and open research leads, not a closed worldwide census. Its reusable lessons are maintained separately in [Geographic evidence research for symbol proposals](<../../Methods/Geographic evidence research for symbol proposals.md>) so later symbol projects can repeat and refine the process without importing durian-specific conclusions.

The bounded review at [Existing Unicode characters with fruit referents](<../../Research/Existing Unicode characters with fruit referents.md>) covers fruit-referent characters in Unicode 17.0.0. It leads with the contemporary emoji comparison, separates weak legacy and historical material, distinguishes encoded characters from emoji presentation and sequences, and preserves botanical and culinary disagreement. The reusable repertoire-audit method is at [Comparative Unicode repertoire research](<../../Methods/Comparative Unicode repertoire research.md>).

## Strongest current non-encoding model

The strongest credible alternative is that the observed durian graphics are ordinary pictograms or illustrations embedded in physical signs, not uses of an abstract character in textual interchange. On this model, a venue commissions or selects a recognizable fruit image, combines it with a prohibition circle or slash, words, colour and layout, and communicates through the resulting sign as a visual artefact. Repetition of the referent and regulatory function can establish an icon convention without establishing that operators, designers or readers preserve a durian unit when the artwork and layout are removed.

The presently documented functions have plausible existing representations. Ordinary text can name durian and state a rule; an image or icon asset can preserve the exact pictogram; markup, metadata and higher-level sign systems can associate that asset with a category or prohibition; and existing characters already represent the letter and punctuation functions in the documented inline brand uses. No reviewed fruit-referent character or sequence represents durian, but the absence of such a representation does not itself show that the physical-sign pictogram must become plain text. This is the candidate-specific application of the project’s [character-identity and encoding method](<../../Methods/Character identity and encoding analysis.md>), not a conclusion that the model has been proved.

## Evidence presently supporting or weakening that model

- **Functional signage:** [Durian signage](<Research/Durian signage.md>) verifies prohibition use in six Southeast Asian territories across transit, accommodation and building rules. That independent, stable function is the strongest current evidence against a merely decorative-illustration account and may support a reusable semantic identity. The reviewed records nevertheless establish displayed signs, not transcription, search, indexing, quotation or cross-system exchange of a durian character. The latter is a present absence in the reviewed evidence, not adverse evidence that such interchange does not occur.
- **Marketing and inline integration:** [Durian visual use](<Research/Durian visual use.md>) records character-scale forms, but the clearest examples are directly explainable as a stylized LATIN CAPITAL LETTER O (`U+004F`), FULL STOP (`U+002E`) or a letter–image hybrid. This positively supports the logo or glyph-treatment branch of the non-encoding model for those occurrences; it does not decide the different functional-signage evidence. One example is a design project rather than verified sustained deployment.
- **Repertoire comparison:** the [fruit-referent review](<../../Research/Existing Unicode characters with fruit referents.md>) finds a large contemporary emoji neighbourhood and no durian representation in its bounded Unicode 17.0.0 corpus. This weakens the claim that an existing fruit character already supplies the same referent, but repertoire fit, category completion and visual recognizability do not establish plain-text need. Legacy terminal symbols and historical commodity signs arose from materially different encoding requirements.
- **Subject importance and geographic reach:** the [geographic survey](<Research/Durian geographic survey.md>) establishes a substantial biological, commercial and cultural footprint. This makes the referent important and the signage geographically meaningful, but importance, trade, consumption and exposure are background evidence rather than evidence that the pictogram is an abstract textual unit.
- **Prior Unicode treatment:** the [Unicode history](<Research/Unicode history and proposal status.md>) supplies no item-specific reason for the 2022 emoji decline, while the earlier records concern an expired item and a duplicate. Those outcomes are therefore neither three adverse merits findings nor favourable character-route evidence. The missing reasons are an evidential limit, not evidence for the non-encoding model.

## Decision-changing evidence

| Possible finding | Likely effect on the working decision |
|---|---|
| Independent sign systems use varied durian forms as the same named semantic unit, and users must enter, exchange, quote, search, index or preserve that unit outside the source artwork; words, images, markup or existing representations cause a documented loss in those workflows | Materially strengthen support for encoding |
| The sign-photo catalogue shows chiefly copied or commissioned artwork, context-dependent generic fruit images, or forms whose identity depends on wording, colour, layout or one exact design; a bounded interchange audit finds that words, accessible image metadata and higher-level sign assets preserve every demonstrated function | Materially strengthen opposition to encoding |
| A conventionally used existing character or standardized sequence is found to carry the same identity and behave adequately in the relevant workflows | Materially weaken a separate-character case and redirect it towards the existing representation |
| A stable visual convention is established but its plain-text users, operations, losses or representative-glyph range remain unproved | Support deferral rather than either submission or final opposition |
| Evidence supports a generic durian-fruit unit across renderings, while the prohibition circle, slash, wording and brand treatments remain ordinary composition | Narrow the model to a generic durian character; exclude a separately encoded “no durian” sign, exact artwork, logos and species-level semantics |

## Current dependencies and unresolved questions

The project owner’s private sign-photo collection must be catalogued before broader image collection or a settled identity judgement. Preserve its originals, provenance and rights; code independence, venue, wording, form and composition; and identify gaps without inferring anything from photographs not yet assessed. After that catalogue is available, conduct the deferred systematic plain-text-interchange and counterargument audit. The present section frames that later work but does not perform it.

Two questions require evidence not yet in the project. Sign-system designers, operators or wayfinding specialists should establish whether organizations treat the recurring durian pictogram as a reusable semantic token independent of its artwork, or simply select an illustrative asset for each displayed sign. Relevant users and text-system implementers must identify any real workflow in which the unit needs plain-text input, interchange, fallback, search, indexing, quotation or archival retrieval, then test words, existing characters or sequences, images, metadata and higher-level protocols in that workflow. Until those questions and the form variation in the private corpus are assessed, the project cannot settle representative-glyph boundaries, small monochrome recognizability, possible confusion with other spiky fruits, or proposal-stage character properties.

## 2026 emoji-submission timing and eligibility

The Unicode Consortium’s [emoji-proposal guidelines](https://www.unicode.org/emoji/proposals.html), last updated 20 May 2026, state that the current submission window closes at the end of 31 July 2026. They also state: ‘Emoji declined within the last four years are not eligible for re-review.’ Both points were rechecked on 22 July 2026.

The latest durian entry was submitted on 24 July 2022. Official committee records say that the 2022 review was complete by 31 October, that authors would be notified shortly after the 1–3 November Unicode Technical Committee meeting, and an Internet Archive capture shows the durian row publicly marked ‘Declined’ by 2 December 2022. The published status record does not give an item-specific decision or notification date.

The historical rule also matters: archived guidance still said two years in November 2022 and November 2023, but said four years by November 2024. The public wording does not say whether the later rule applies retroactively or whether its period runs from submission, decision, notification, or publication. For planning, 24 July 2026 is the earliest plausible anniversary, shortly after 3 November 2026 is the likely batch-notification anniversary, and 3 December 2026 is a conservative backstop if the present rule is applied retroactively from no later than the archived public record. None is an official eligibility determination. Use the 2026 window only if the Emoji Standard & Research Working Group confirms eligibility. Character research and preparation can continue independently. See [Unicode history and proposal status](<Research/Unicode history and proposal status.md>).

## Research archive and public-facing material

The project will accumulate a larger archive of images than will appear in the formal proposal. Only a select set of the strongest representative images is intended for the proposal. A larger, but still curated, subset may be used for a general-audience project page at `novapatch.ie/en/durian`.

Research from this and other character-proposal projects may become source material for corresponding pages on my personal website, whether or not a proposal is approved.

Original project text and assets are intended for publication under CC BY-SA 4.0. Third-party reference material remains excluded from that blanket licence and must retain its own rights record. Creative Commons works, separately licensed Shutterstock material, permission-cleared material, and narrowly used non-free references require different handling under [Evidence storage and publication](<../../Project/Evidence storage and publication.md>); the evidence archive must not imply that everything stored locally can be redistributed.

## Version control

The parent project is a local Git repository with Git LFS support available, but no files are currently tracked through LFS and no tracking rules have been chosen. LFS may later support large public, distributable assets when actual storage and transfer needs justify a rule; it is not a rights, confidentiality, privacy, or publication boundary. Private or restricted material must remain outside the public repository and its history whether or not LFS is available.

## Collaboration context

When a durable project decision or research finding is not already captured, update the most relevant current note. Use Git history or a dedicated changelog for superseded wording and routine changes of direction.

## Status

Durian is in the `researching` phase. The case for encoding is being developed and tested, but no proposal has yet been drafted for submission. Organization, data formats, and supporting files should continue to be introduced only when the work creates a real need for them.
