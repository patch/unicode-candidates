---
title: Recovering changed and unavailable web sources
last_reviewed: 2026-07-22
tags:
  - method
  - web-archives
  - provenance
---

Use web archives to recover public evidence whose original page has changed, disappeared, become inaccessible, or lost embedded content. Archive recovery supports provenance and historical reconstruction; it does not make the recovered material free to republish.

## Workflow

1. Check the live URL and record the access date and observed failure or change. Preserve the original URL even when it no longer works.
2. Query the Internet Archive Wayback Machine near the date relevant to the research question. Try justified URL variants, including HTTP and HTTPS, `www` and bare hostnames, and historically encoded forms.
3. Inspect the archived page itself. If it depended on an iframe, spreadsheet, image, script, or other embedded resource, check that resource’s URL and captures separately; the wrapper page and its contents may have been archived at different times.
4. Record the exact capture URL and timestamp. Treat a capture as evidence that the archived representation contained the information **no later than** that timestamp. It does not by itself prove the page’s creation date, first publication, decision date, or continuous availability.
5. Compare snapshots on both sides of a suspected change to establish a date bracket. Keep the wording found in each snapshot separate from any inference about the changeover.
6. Cite both the original source identity and the archive capture. Record the date on which the archive was accessed and any missing assets, replay problems, redirect behaviour, or uncertain page state.
7. Preserve only what the research needs. Quote sparingly and retain a clear distinction between source content, observations about the capture, and the project’s inference.
8. Apply the original rights analysis. Internet Archive availability does not grant a reuse licence or make commercial artwork, photographs, or documents safe to redistribute.

The Internet Archive documents its [Wayback Machine APIs](https://archive.org/help/wayback_api.php), including lookup by target timestamp and interfaces for broader capture discovery.

## Common limitations

- A nearest capture after the target date supplies only a no-later-than bound.
- The first available capture need not be the first time the page was public.
- Dynamic pages may replay incompletely or show a shell without their original data.
- Embedded resources may have different capture timestamps from the page that displayed them.
- Redirects, robots exclusions, removed captures, and URL canonicalization can leave gaps.
- An archived search-results page is usually less reproducible and less authoritative than an archived underlying source.

## Refinement log

- 2026-07-22: Added this method after separate Wayback captures recovered the 2022 durian status row, the historical Unicode emoji-submission page, and a CafePress listing behind an unavailable source link. Comparing archived Unicode guidance also exposed a change from a two-year to a four-year re-review period, requiring the project to preserve administrative uncertainty rather than impose a single inferred eligibility date.
- 2026-07-22: Extended the embedded-resource check after an archived Unicode wrapper page replayed a live spreadsheet rather than its historical state. Inspect retired page names and every historical iframe target separately, use the resource’s Memento time map, and verify the timestamp actually returned: a requested old date may silently redirect to the nearest later capture. This recovered the 2018–2020 durian workflow labels that the current summary sheet omits.
