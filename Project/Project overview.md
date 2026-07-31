---
title: Project overview
last_reviewed: 2026-07-31
tags:
  - project
  - unicode
  - research-programme
---

## Current objective

Develop an open, evidence-led research programme for prospective Unicode characters and repertoires. Each candidate may be supported, opposed, deferred, or left unresolved; the project is not an advocacy list and does not imply official Unicode candidate status.

Initial parallel work prioritizes Durian, All Gender Symbol, and Urinal, with Inverted Cross as another near-term project. The existing mature research corpus belongs to [Durian](../Candidates/Durian/Overview.md).

## Scope

The project’s central question must concern whether one or more new characters should be encoded. A candidate may be evaluated through the character-proposal route, the emoji-proposal route, or both. Standalone proposals about CLDR data, Unicode Standard Annexes, character properties, or other non-character technical changes remain outside this repository. Those projects share some process and writing practices, but their substantive questions, evidence, and review routes differ enough that including them would weaken the repository’s organizing principle. Reassess this boundary only if sustained work creates a concrete need.

Where both routes are material, treat them as parallel research tracks rather than assuming that a character-first encoding can later acquire emoji treatment. Current Unicode guidance does not accept proposals to emojify existing characters. Research and evidence development remain active irrespective of temporary submission eligibility, but the intended route must be resolved before a non-emoji encoding could close the Emoji route. See [Emoji and character proposal routing](<../Research/Emoji and character proposal routing.md>).

Encoded former candidates and other existing characters may be studied as comparative or process precedents. Cross-candidate findings belong in `Research/`; repeatable procedures and refinement logs belong in `Methods/`.

## Candidate organization

`Candidates.md` is the authoritative public inventory. Candidate folders are created only when material exists. An independently viable symbol retains its own project even when it shares a study or prospective submission with another symbol; this applies particularly to All Gender Symbol and Urinal.

The internal lifecycle is defined at [Candidate lifecycle](<Candidate lifecycle.md>). Official statuses and dated submission events are recorded separately for each applicable proposal route.

## Public development

The repository is intended for open access on GitHub. Public access may precede formal contribution documentation. Original project material is intended for CC BY-SA 4.0 publication. Third-party evidence may be published under its own licence, permission, or other documented legal basis; it does not thereby become CC BY-SA 4.0 material. [Evidence storage and publication](<Evidence storage and publication.md>) defines the project’s managed-risk publication standard and the boundary between the public repository, the private evidence archive, and safe public records for privately held material.

Current project and research notes should describe the present understanding. Git history or a dedicated changelog should carry superseded wording and routine changes of direction unless that history materially affects the evidence or proposal process.
