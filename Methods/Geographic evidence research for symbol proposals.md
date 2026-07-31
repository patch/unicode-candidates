---
title: Geographic evidence research for symbol proposals
method_status: reusable working method
last_reviewed: 2026-07-31
tags:
  - method
  - unicode-research
  - geographic-evidence
---

This note extracts a repeatable method from the durian background survey. It applies to any unencoded subject under evaluation, including cases that begin with little more than the knowledge that a concept is unencoded. The research may support encoding, oppose encoding, or remain unresolved; none of those outcomes makes the research a failure.

## Principle

Start with the communicative use that may justify a symbol, then build outward to historical, biological, commercial, social, and geographic context. Actively seek counterevidence and competing interpretations. Do not let popularity, production, imports, or visual appeal substitute for evidence that the proposed symbol has a repeatable meaning or use.

Keep four kinds of statement visibly separate:

- **Observed evidence:** a photographed sign, official statistic, survey result, or other directly inspectable item.
- **Sourced claim:** a statement made by a traceable source but not independently observed in the project.
- **Working inference:** an interpretation derived from several facts, such as a likely diaspora-market relationship.
- **Proposal decision:** a later editorial judgement about what evidence belongs in a submission.

## Repeatable workflow

### 1. Define the research object

Record:

- scientific taxon or other formal identity;
- common names, scripts, spellings, and possible confusions;
- what visual forms might count as the symbol;
- intended semantic function, such as prohibition, wayfinding, category label, or expressive emoji;
- character-encoding and emoji-treatment questions as related but distinct workstreams.

For biological subjects, describe the scientific taxa involved, but derive the prospective character’s semantic scope from popular real-world use. Unicode characters are not biological nomenclature: the useful dictionary-like referent may be a genus, higher-level taxon, vernacular category, product class, or polyphyletic grouping. One species may be the strongest **popular representative species** without constraining the character to that species; avoid “type species”, which has a formal taxonomic meaning.

### 2. Fix identifiers and units

Use durable identifiers as primary keys. A **territory** follows Unicode CLDR usage and may be a macroregion, country, dependent territory, or subdivision. Territory and language names use Unicode CLDR English (`en`) forms. Prefer a territory’s `alt="short"` name when present, except when it is itself a two-letter abbreviation; use the unqualified name in that case. This rule gives Hong Kong, Myanmar, and Macao, while retaining United States and United Kingdom ([M03](../Research/Sources.md#m03)).

The `country_code` property stores the ISO 3166-1 alpha-2 code assigned to an included country or dependent territory ([M01](../Research/Sources.md#m01)). Country codes are uppercase. Language codes are lowercase: use ISO 639-1 alpha-2 when assigned and fall back to ISO 639-3 alpha-3 otherwise. Store the result as `language_code` ([M04](../Research/Sources.md#m04)). For subdivisions, use ISO 3166-2 codes where applicable and identify every alternate code namespace explicitly.

In prose, use `Country Name (CC)` and `Language Name (ll/lll)` where both the label and identifier improve clarity. Macroregion codes such as `035` need not be displayed unless the macroregion is being treated as data. After a standard has been defined in an asset, “country code” or “language code” is usually sufficient. Avoid ambiguous shorthand such as “ISO entities”.

Define each quantitative unit before collecting it:

- planted area versus bearing area;
- production mass versus sales;
- fresh product versus frozen, prepared, or processed product;
- apparent consumption versus household purchase, dietary recall, preference, or import value;
- resident population, ethnicity, citizenship, ancestry, or country of birth.

### 3. Design evidence layers before searching

A useful default for geographic object research is:

1. native range;
2. introduced or naturalized range;
3. market-oriented cultivation or manufacture;
4. consumption/use among national or substantial regional populations;
5. diaspora-oriented or specialist markets;
6. observed functional or non-marketing symbol use;
7. observed marketing or brand use;
8. inline integration with ordinary text, such as a pictorial letter substitution or punctuation-like mark;
9. policy or textual context without an observed symbol;
10. unresolved leads and negative searches.

These layers should not be collapsed into one country list.

### 4. Set inclusion tiers

Define thresholds before interpreting search results. The durian survey used:

- industrial or statistically established production;
- niche commercial production;
- emerging commercial project;
- candidate/unverified;
- national/territorial consumption;
- substantial regional-population consumption;
- emerging general-market niche;
- diaspora-oriented or mixed market;
- verified photographed sign;
- verified scholarly documented sign;
- policy-only context;
- unverified signage lead.

Thresholds may change for another subject, but the change and reason should be recorded.

### 5. Search from authoritative cores outward

Preferred source order:

1. current taxonomic authority, standards body, statistical agency, or regulator;
2. ministry, local government, intergovernmental body, or official survey;
3. peer-reviewed research and university extension;
4. industry or specialist reporting with named methods and sources;
5. first-person field reports and identifiable photographs;
6. commercial listings, social media, and search snippets as leads only.

Search in relevant local languages and scripts. When naming a language, give its Unicode CLDR English (`en`) name and its ISO 639-1 alpha-2 code, such as English (en), or its ISO 639-3 alpha-3 code if no alpha-2 code is assigned. Preserve the exact term used, not only an English translation.

### 6. Map claims rather than pages

For each claim, record:

- exact proposition supported;
- territory and local subdivision;
- date or reference period;
- source and access date;
- whether the support is direct or inferential;
- confidence and unresolved contradiction;
- whether the source is suitable to cite publicly;
- whether an associated image is licensed to reproduce.

One source can support several claims, and one claim may require several sources. A bibliography alone is not a claim-to-source map.

Apply the shared source register’s [citation-key granularity policy](<../Research/Sources.md#citation-key-granularity>). In proposal-facing work, a source-group key does not replace an exact document-and-location citation.

### 7. Treat “all countries” as an auditable search

Worldwide exhaustiveness is rarely provable for signs, local crops, or informal practices. Report:

- the inclusion definition;
- databases, languages, and date range searched;
- verified occurrences;
- plausible leads;
- named exclusions and why they failed;
- jurisdictions searched without a result;
- the review date.

Use “verified in these territories as of [date]” instead of implying that no other territory qualifies.

### 8. Separate measurement systems

Never merge:

- production rank with consumption rank;
- import value with consumption mass;
- respondent preference with annual dietary intake;
- a selected-commodity table with an all-fruit universe;
- one-day dietary recall with a seasonal annual measure.

Every published rank should read: “rank within [source universe], measured by [metric], [period]”.

### 9. Investigate diaspora markets without ecological fallacy

The purpose of this layer is to investigate wider global availability, exposure, use, and possible comprehension beyond the object’s core region. Trade data establish distribution, not symbol comprehension, and do not identify buyers. Census geography can identify fieldwork areas but cannot prove that a population caused an import flow.

Use a staged inference:

1. screen trade scale and product form;
2. identify re-export hubs;
3. map relevant population geography;
4. document retail channels, packaging, signs, and languages;
5. identify local-language media and public references that show exposure beyond a single shop;
6. interview wholesalers/retailers;
7. if appropriate and ethical, test unaided and aided recognition among both diaspora and non-diaspora residents;
8. label the conclusion as direct evidence, supported inference, or hypothesis.

Do not ascribe a preference to an individual from neighbourhood, ethnicity, birthplace, or citizenship.

Use an explicit evidence ladder:

| Level | What can be claimed |
|---|---|
| Imported/distributed | The object is commercially available in the country |
| Repeated local exposure | Residents plausibly encounter it through stable retail, media, events, or public display |
| Observed local symbol use | A graphic representation performs a communicative function in that country |
| Demonstrated comprehension | A defined population recognizes the object or meaning under a recorded test method |

Do not move from the first level to the fourth by implication.

### 10. Build a sign corpus fit for evidence and publication

For every sign, capture:

- original uncropped image;
- close and contextual views;
- ISO 3166-1 alpha-2 country code and local subdivision code, with the subdivision code’s standard or namespace identified;
- coordinates/address and venue type;
- capture date and photographer;
- exact wording, `Language Name (language_code)`, transcription, and translation;
- graphic features and semantic function;
- source chain and authenticity notes;
- copyright owner, licence, permission, and publication status;
- derivative files linked back to the original.

Evidence value and reuse rights are separate. A web photograph may prove occurrence while remaining unsuitable for a proposal.

Record rights using categories that preserve the relevant distinction:

- public domain;
- Creative Commons, with exact licence, attribution, adaptation, and share-alike requirements;
- separately licensed stock, with the provider, stable asset ID, governing licence or agreement, acquisition date, permitted use, required attribution, restrictions, intended context, covered derivatives and distribution channels, and material-change review triggers;
- permission granted, with scope and evidence of permission;
- non-free reference or reproduction, with the source, creator, use context, amount, market-substitution assessment, and fair-use, fair-dealing, or other legal basis recorded to the level warranted by the uncertainty; and
- rights unknown or not publishable.

The project’s CC BY-SA 4.0 licence for original work does not override third-party rights or automatically make every compatible-looking asset redistributable.

Apply [Evidence storage and publication](<../Project/Evidence storage and publication.md>) to public assets, private originals, and safe public records for privately held material. Record the standard provenance and publication fields for ordinary uses; add a fuller rationale only when a geographic source or use is materially ambiguous or consequential. Apply [Content sources and licensing](<../Project/Content sources and licensing.md>) when comparing acquisition routes or checking a provider.

### 11. Store according to information shape

Use ordinary Markdown for:

- analysis and methodological argument;
- source evaluations;
- sign narratives and provenance;
- limitations, contradictions, and decisions.

Use a Base or table only when records have stable repeated fields and useful filters, such as country-code-keyed status. Follow the current official Bases syntax for those views ([M02](../Research/Sources.md#m02)). Do not force sources or unique evidence items into a table if that hides qualifications.

In an Obsidian vault with inline titles enabled, do not repeat an identical H1 below frontmatter. Use ordinary relative Markdown links for source citations and navigational relationships so they remain portable across Obsidian and GitHub and do not introduce wiki-link alias delimiters into tables.

### 12. Validate and freeze a research release

Before publication or proposal use:

- recheck current official Unicode guidance;
- recheck identifiers and taxonomic status;
- update the newest complete production/trade year;
- verify every numerical transcription;
- test every external URL and preserve durable copies where lawful;
- confirm that every substantive claim maps to a source;
- separate permitted, restricted, and unresolved images;
- record the review date, dataset version, and known gaps.

## Reusable output set

A proportionate project usually needs:

- a short research hub and synthesis;
- thematic notes for evidence types that require different methods;
- a stable source register;
- primary-keyed geographic records where cross-filtering helps;
- an evidence archive with originals and rights metadata;
- a method note and refinement log;
- a proposal evidence map later, without duplicating source material.

Do not create every component in advance. Add it when actual material needs it.

## Decision outcomes and cross-project comparison

Use the same evaluation dimensions across subjects, while allowing any of four editorial outcomes: support encoding; oppose encoding; defer because the evidence is unresolved; or publish a background finding without pursuing a proposal. Record the strongest counterarguments even when the working judgement supports encoding.

| Dimension | Question |
|---|---|
| Functional semantic use | Is the object independently used to communicate a repeatable meaning in non-marketing contexts? |
| Marketing semantic use | Do unrelated organizations in different territories use the object consistently in brands, packaging, or category marks? |
| Inline integration | Does the graphic replace or accompany a letter, word, or punctuation mark within otherwise ordinary text? |
| Geographic breadth | In how many territories is that use directly observed? |
| Venue breadth | Does it occur across transport, accommodation, public buildings, packaging, maps, or other domains? |
| Form stability | Do independent signs converge on a recognizable visual form? |
| Lexical gap | Is text or an existing symbol inadequate for the observed function? |
| Cultural breadth | Is use national/regional, specialist, or predominantly diaspora-based? |
| Confusability | Could viewers mistake it for an existing character or a generic fruit/object? |
| Evidence quality | Are examples dated, located, independent, and lawfully usable or documented with an explicit publication status? |

A negative or weaker case is still a valid research result and may support a useful public article explaining why encoding is not warranted. Do not lower thresholds merely to make projects look comparable.

## Refinement log

### 2026-07-21 — initial method extracted from the durian survey

- Split genus-native range from cultivated-species native range.
- Replaced binary “commercially grown” with scale/evidence tiers.
- Replaced a universal fruit-ranking request with source-defined rankings.
- Added a redistribution control and explicit inference labels to diaspora-market research.
- Reframed diaspora/import research as a global-reach pathway and separated distribution, exposure, observed use, and demonstrated comprehension.
- Recast worldwide signage as a verified-occurrence register with leads and negative searches.
- Made image publication rights a separate field from evidential credibility.
- Restricted Obsidian Bases to genuinely repeated, filterable country fields.
- Quoted ISO 3166-1 alpha-2 values in YAML frontmatter after validation showed that YAML 1.1 can parse `NO` as Boolean “no”. Treat identifiers as strings even when most unquoted codes appear safe.
- Added a final small-producer gap audit after it found official Taiwanese niche-farm evidence and a Venezuelan commercialization project absent from the first source screen. Do not freeze an “all countries” result before a dedicated edge-case search.
- Reframed the method as an open evaluation that can support, oppose, or defer encoding, rather than as a procedure for strengthening a predetermined proposal.
- Separated functional, marketing, and inline-text uses while retaining marketing evidence as relevant.
- Replaced species-bound character semantics with a dictionary-like common-use referent and the term “popular representative species”.
- Standardized territory and language labels on Unicode CLDR English (`en`) names, preferring non-abbreviated `alt="short"` territory forms and using ISO 3166-1 alpha-2, ISO 639-1 alpha-2, and fallback ISO 639-3 alpha-3 identifiers precisely.
- Renamed the country primary-key property to `country_code`; coded lookup records use the country code as the filename and store `Country Name (CC)` in the `title` property.
- Replaced informal descriptions of quotation-mark shapes with Unicode character names and code points.
- Expanded the rights ladder to include Creative Commons, separately licensed stock, permission, and reviewable non-free reference use.
- Recorded Obsidian title, table-link, and vault-relative Base-filter pitfalls discovered during review; source and note links use ordinary relative Markdown links, while Bases use `this.file.folder` where a query should follow its own folder.

### 2026-07-22 — pre-commit consistency review

- Distinguished territories with documented market output from active projects intended to establish commercial production; do not hide that evidential difference inside an umbrella count.
- Standardized source citations and note navigation as portable relative Markdown links.
- Revalidated the country-record schema, source-key coverage, Markdown tables, inline-title treatment, and Base folder query before treating the research set as commit-ready. The revised Base was confirmed to return records in Obsidian on 22 July 2026.

### 2026-07-28 — stock-licence review

- Replaced the generic stock-licence field with an acquisition- and use-specific record, and routed public/private storage decisions to the project evidence-governance note.

### 2026-07-29 — citation-key granularity review

- Routed source groups through a conservative project-wide policy: retain practical background bundles, separate independently citable documents when they support materially distinct proposal-facing claims, and require exact document-and-location records for formal use.

### 2026-07-29 — content-source governance

- Retained provider-neutral stock fields in this method and routed potential-source availability and provider-specific checks to [Content sources and licensing](<../Project/Content sources and licensing.md>); actual use remains item-specific.

### 2026-07-31 — managed-risk publication review

- Adopted the project-wide source-sensitive managed-risk standard, including scoped decisions, genuine-equivalence and fit-for-purpose tests, and proportionate records. The operative policy and its source distinctions are maintained in [Evidence storage and publication](<../Project/Evidence storage and publication.md>).

Future research should append concise refinements here when a method changes, including why it changed and which earlier results may need review.
