---
title: Emoji and character proposal routing
last_reviewed: 2026-07-31
tags:
  - unicode
  - emoji
  - proposal-route
  - shared-research
---

This note records the current Unicode rule and the project interpretation for a prospective character that may have both a general character case and an Emoji case. It distinguishes property semantics, proposal routing, submission eligibility and research priority.

## Current official position

The Unicode Consortium’s current *Emoji Submission FAQ* states that proposals to emojify existing characters are no longer accepted. It says that such proposals were accepted in the past but proved problematic, without specifying all the problems or declaring emoji data technically immutable. ([U28](Sources.md#u28))

The rule is broader and differently framed than a prohibition on adding `Emoji_Presentation=Yes`. UTS #51 defines an emoji character as a character with `Emoji=Yes`; `Emoji_Presentation=Yes` identifies an emoji character that should default to emoji presentation. An emoji character may instead have `Emoji_Presentation=No` and use a standardized variation sequence to request emoji presentation. If `Emoji=No`, then `Emoji_Presentation=No`. ([U20](Sources.md#u20))

UTS #51 says emoji properties are stable within a version but may change between versions, and gives the historical emojification of U+265F ♟ <span style="font-variant:all-small-caps">BLACK CHESS PAWN</span> as an example. That technical allowance and historical example do not override the current proposal policy. ([U20](Sources.md#u20))

The current policy also informs committee property work. In January 2025, supporting analysis for the Unicode Technical Committee stated that assigned non-emoji characters would not be emojified and recommended removing `Extended_Pictographic` values that had preserved forward compatibility for possible future emojification. The committee then approved removal from 672 assigned characters without `Emoji=Yes` for Unicode 17.0. This directly changed `Extended_Pictographic`, not `Emoji_Presentation`, but corroborates the current expectation that an assigned non-emoji character will not later become an emoji character. ([U29](Sources.md#u29), [U30](Sources.md#u30))

## Project interpretation

Treat Character and Emoji as alternative proposal routes for the same prospective encoded entity, not two cumulative encodings. If a new emoji-character proposal succeeds, the resulting encoded character is both a Unicode character and an emoji character. Emoji treatment does not encode a second abstract character.

Where a candidate has a material, credible Emoji objective, prefer an emoji-first submission approach or obtain route-specific guidance before a non-emoji encoding can foreclose later emoji treatment. The trigger is the substantive Emoji objective and evidence, not a visual prediction that an implementation would probably use colour. A character can be emoji-capable while retaining default text presentation, and a colourful appearance alone does not satisfy the Emoji selection factors.

Parallel research remains appropriate. The project may develop the Character case and Emoji case simultaneously, distinguish their evidence and criteria, and use findings from each to test identity, representation and adverse interpretations. It must not assume that a completed character-first encoding can be followed by a proposal to add emoji treatment.

Submission eligibility gates submission, not research priority. A closed window, waiting period or known future bar does not by itself justify delaying or deprioritizing Emoji research. Non-volatile evidence, adverse-factor analysis, query design, example-image research and dated baselines may all remain useful; requirements and frequency snapshots that are intended to be current should be refreshed near an eligible submission.

## Route decision

| Situation | Project treatment |
|---|---|
| Material and credible Emoji objective | Prefer Emoji-first submission or obtain working-group guidance before non-emoji encoding |
| Independent character case without a material Emoji objective | Use the character-proposal route if its own criteria are met |
| Both routes remain unresolved | Keep both research tracks active and resolve routing before encoding |
| Emoji submission is temporarily ineligible | Continue Emoji research; gate only the submission event |
| Emoji proposal is declined | Preserve the independent Character analysis; do not treat the Emoji outcome as deciding plain-text character need |

## Limits

- The public FAQ does not define the precise procedural point at which a prospective addition counts as an ‘existing character’. Resolve the route before acceptance or encoding rather than relying on a narrow pipeline-stage interpretation.
- The checked sources do not establish that Unicode could never correct an emoji property internally. The actionable rule is that proposals to emojify existing characters are not accepted, reinforced by current committee practice.
- The rule does not show that every pictographic candidate should be Emoji-first. Each route still requires its own eligibility and evidential case.
- A waiting period expressed as a number of years must not be converted to an exact eligibility date unless the source defines the controlling event and calculation. Where proposals operate in annual cycles, cycle-based and elapsed-time readings should both remain open if the published wording does not choose between them.
