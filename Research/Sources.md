---
title: Shared research sources
last_reviewed: 2026-07-29
tags:
  - sources
  - research-register
  - shared-research
---

IDs are local citation keys. Descriptions state what a source is used for; they are not blanket endorsements of every claim on the page.

## Citation-key granularity

A citation key normally identifies one independently citable document or evidence item. It may instead identify a **narrowly described source group** when several related documents jointly serve one background-research function—for example, one versioned standard with its data files, companion pages in one statistical release, or captures that document changes to the same web publication. The register must name every member used and distinguish their roles and limitations.

Create separate keys when documents are independently citable and support different propositions, or when their authority, dates, rights, provenance, or evidential limitations differ materially. In particular:

- a key must not imply that every member supports a claim when only one does; identify that member in the claim and register, cite it directly, or give it a separate key;
- proposal-facing and other formal-publication claims must resolve to the exact document and supporting location, even when a source-group key is retained;
- the supporting location should be recorded as precisely as the medium permits: page and section, table or figure, paragraph or heading, timestamp, image region, dataset release and table/series/query, code-point or data-file entry, or archival capture timestamp and archived-page location;
- dynamic or negative findings should also record the version or review date, search boundary and search term or field where applicable.

Do not split established keys merely to normalize their appearance. Split a current bundle only when its members already support materially distinct proposal-facing claims, the change has a clear immediate benefit, and all internal references can be migrated safely. Otherwise retain the bundle and record the condition that should trigger a later split. When a key has been published or is widely referenced, preserve a stable alias where the system permits it or add an explicit migration note stating which new key now carries each former member.

## Unicode repertoire, process, and naming

Sources U19–U23 were accessed on **22 July 2026**. Sources U24–U27 were accessed on **28 July 2026**.

### U19

Unicode Consortium, [*The Unicode Standard, Version 17.0.0*](https://www.unicode.org/versions/Unicode17.0.0/), published 9 September 2025, with the versioned Unicode Character Database files [`UnicodeData.txt`](https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt), [`NamesList.txt`](https://www.unicode.org/Public/17.0.0/ucd/NamesList.txt), [`NameAliases.txt`](https://www.unicode.org/Public/17.0.0/ucd/NameAliases.txt) and [`Blocks.txt`](https://www.unicode.org/Public/17.0.0/ucd/Blocks.txt). Authoritative repertoire cut-off, character names, annotations and block boundaries. Version 17.0.0 supersedes earlier standards; draft Unicode 18 data is outside the review.

### U20

Unicode Consortium, [UTS #51, *Unicode Emoji*, Version 17.0](https://www.unicode.org/reports/tr51/), with versioned [`emoji-data.txt`](https://www.unicode.org/Public/17.0.0/ucd/emoji/emoji-data.txt), [`emoji-variation-sequences.txt`](https://www.unicode.org/Public/17.0.0/ucd/emoji/emoji-variation-sequences.txt), [`emoji-test.txt`](https://www.unicode.org/Public/17.0.0/emoji/emoji-test.txt), [`emoji-sequences.txt`](https://www.unicode.org/Public/17.0.0/emoji/emoji-sequences.txt) and [`emoji-zwj-sequences.txt`](https://www.unicode.org/Public/17.0.0/emoji/emoji-zwj-sequences.txt). Primary sources for emoji properties, default presentation, qualification and the RGI lime sequence. Unicode CLDR [48.2 release data](https://unicode.org/Public/cldr/48.2/) supplied English annotations and ordering as semantic discovery and cross-check evidence; annotations do not create additional encoded characters.

### U21

Unicode Consortium, complete Unicode 17.0 code charts for [Symbols for Legacy Computing Supplement](https://www.unicode.org/charts/PDF/U1CC00.pdf) and [Miscellaneous Symbols and Pictographs](https://www.unicode.org/charts/PDF/U1F300.pdf). The former expressly labels `U+1CEBD APPLE SYMBOL`, `U+1CEBE CHERRY SYMBOL` and `U+1CEBF STRAWBERRY SYMBOL` as non-emoji terminal graphic characters and cross-references their emoji counterparts. The latter supplies the official fruit and vegetable symbol names and reciprocal cross-references. Representative chart glyphs are not prescriptive.

### U22

Unicode Consortium, [Chapter 8, ‘Europe-II’](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-8/), and Unicode 17.0 code charts for the [Linear B Syllabary](https://unicode.org/charts/PDF/U10000.pdf), [Linear B Ideograms](https://unicode.org/charts/PDF/U10080.pdf) and [Linear A](https://unicode.org/charts/PDF/U10600.pdf). The core specification says Linear B ideographic signs were used mainly as counters for commodities and explains that agreed meanings appear in character names. The charts document ideogram B030 ‘figs’ as a use of `U+1001B LINEAR B SYLLABLE B030 NI`; name the B120 WHEAT, B121 BARLEY and B122 OLIVE ideograms; gloss `U+10093 LINEAR B MONOGRAM B127 KAPO` as ‘fruit’; and annotate Linear A signs `U+1061D AB030`, `U+10649 AB120`, `U+1064A A120B` and `U+1064B AB122` as ‘figs’, ‘grain’, ‘grain’ and ‘olives’.

### U23

Rebecca Bettencourt and Doug Ewell for the Terminals Working Group, *[Proposal to disunify Symbols for Legacy Computing from emoji](https://www.unicode.org/L2/L2023/23252-legacy-disunification.pdf)*, L2/23-252, 14 October 2023. Primary proposal history for the separately encoded APPLE SYMBOL, CHERRY SYMBOL and STRAWBERRY SYMBOL. It explains that the source-set characters had previously been unified with emoji and were separated because using emoji characters as non-emoji terminal graphics was considered inappropriate. The proposal reports rare contemporary use by specialists and hobbyists; it is not evidence of a general-purpose fruit-symbol convention.

### U24

Unicode Consortium, [*Guidelines for Submitting Unicode Emoji Proposals*](https://unicode.org/emoji/proposals.html), last updated 20 May 2026. Current guidance states that the Consortium no longer accepts proposals for flags and that flags corresponding to assigned ISO 3166-1 alpha-2 region codes are added automatically without proposals. It also directs widely used symbols that do not require colour towards the character-proposal process. The [Script Encoding Working Group proposal guidelines](https://sew.unicode.org/guidelines) likewise state that the group does not accept flag proposals.

### U25

Jennifer Daniel for the Unicode Emoji Subcommittee, [‘The Past and Future of Flag Emoji’](https://blog.unicode.org/2022/03/the-past-and-future-of-flag-emoji.html), 28 March 2022, updated 12 December 2024. Official explanatory background for the decision to stop processing flag proposals, the automatic treatment of flags based on ISO 3166-1 alpha-2 codes, and the distinction between valid subdivision-flag sequences and emoji recommended for general interchange.

### U26

Unicode Consortium, Unicode 17.0 [Egyptian Hieroglyphs names list](https://www.unicode.org/charts/nameslist/n_13000.html), [Unikemet data](https://www.unicode.org/Public/17.0.0/ucd/Unikemet.txt), and [UAX #57, *Unicode Egyptian Hieroglyph Database (Unikemet)*](https://www.unicode.org/reports/tr57/). The names list identifies 𓂀 (`U+13080 EGYPTIAN HIEROGLYPH D010`) as a logogram for the udjat eye. Unikemet describes an eye with the markings of a falcon’s head. Unlike entries explicitly marked `kEH_NoMirror=Y`, D010 has the property’s default value of `N`; taken together with UAX #57, this means mirroring is not prohibited. The official data checked does not identify the character specifically as the Eye of Horus or Eye of Ra.

### U27

Unicode Consortium, [Section 4.8, ‘Name’, in *The Unicode Standard*, Version 17.0](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-4/#G1353). Formal Unicode character names are immutable identifiers and contain only uppercase Latin letters, digits, spaces, and hyphen-minuses. This formal syntax does not require a research project to typeset provisional working names in uppercase.

## Comparative fruit classification

The sources in this section were accessed on **22 July 2026**.

### F01

University of Minnesota, *The Science of Plants*, [‘Fruit Morphology’](https://open.lib.umn.edu/horticulture/chapter/8-1-fruit-morphology/). University horticulture text defining fruit structure and distinguishing berries, pepos, hesperidia, legumes, caryopses, multiple fruits and accessory fruits. It specifically treats tomato, grapes and blueberries as berries; cucumber as a pepo; peas as legumes; pineapple as multiple fruit; apple and pear as pomes; and strawberry as an aggregate accessory structure whose achenes are the botanical fruits.

### F02

Virginia Cooperative Extension, [*Extension Gardener Handbook*, Chapter 1, ‘Botany’](https://pressbooks.lib.vt.edu/emgtraining/chapter/1/). University extension classification cross-check for berries, drupes, pepos, legumes, achenes, pomes, nuts, aggregate fruits and multiple fruits. It identifies tomato, grape, aubergine and blueberry as berries; cucumber and watermelon as pepos; peanut as a legume fruit; chestnut as a true nut; apple as a pome; peach as a drupe; strawberry as aggregate-accessory fruit; and pineapple as multiple fruit.

### F03

University of California Agriculture and Natural Resources, [‘Fig Fact Sheet’](https://ucanr.edu/site/fruit-nut-research-information-center/fig-fact-sheet); University of California, Riverside, [‘What Kind of Fruit is an Avocado?’](https://avocado.ucr.edu/what-kind-fruit-avocado); University of Florida IFAS, [‘Coconut’](https://gardeningsolutions.ifas.ufl.edu/mastergardener/resources/plantid/fruits-and-nuts/coconut/), [`Mangifera indica`: Mango](https://edis.ifas.ufl.edu/publication/ST404/pdf) and [`Musa` spp.: Banana](https://ask.ifas.ufl.edu/publication/ST409); Oregon State University Extension, [*Growing kiwifruit*](https://extension.oregonstate.edu/catalog/pnw-507-growing-kiwifruit-guide-kiwiberries-fuzzy-kiwifruit-pacific-northwest-producers); and University of Illinois, [Integrative Biology 335 plant-systematics laboratory manual](https://www.life.illinois.edu/downie/IB335_Lab%20Manual_Spring%202015.pdf), p. 116. University sources for the special cases: the fig as a syconium of receptacle tissue enclosing its small true fruits; banana, kiwifruit and avocado as berries; coconut as a fibrous drupe; mango as a drupe; and coconut, olive, cherry and peach as drupes whose edible structures differ.

### F04

University of Florida IFAS, [‘Peanuts’](https://gardeningsolutions.ifas.ufl.edu/plants/edibles/vegetables/peanuts/) and [*Rice Handbook 2021*](https://erec.ifas.ufl.edu/media/erecifasufledu/Rice-Handbook_2021.pdf); University of Wyoming, [Rocky Mountain Herbarium plant-family handout](https://www.uwyo.edu/barnbackyard/_files/documents/resources/nativeplants/rmherbplantfamilies.pdf); Virginia Tech, [common barley profile](https://weedid.cals.vt.edu/profile/677); and North Carolina State Extension, [*Arachis hypogaea*](https://plants.ces.ncsu.edu/plants/arachis-hypogaea/common-name/peanuts/). University sources confirming peanut pods as legume fruits; rice, maize, wheat and barley grains as caryopses; and the distinction between a peanut pod and its edible seeds.

### F05

Food and Agriculture Organization of the United Nations, [FAO/WHO GIFT food groups and subgroups](https://www.fao.org/gift-individual-food-consumption/methodology/food-groups-and-sub-groups/en), [the adapted FAOSTAT classification](https://files-faostat.fao.org/production/FB/food_group_classification_e.pdf), and [fruit and vegetable processing guidance](https://www.fao.org/4/v5030E/V5030E05.htm). Official international food-group evidence for culinary classification. The system is designed around foods’ roles in diets and common dietary groupings rather than botany; it separates cereals, pulses/nuts/seeds, vegetables and fruits, treats rice and maize as cereals, cucumber and tomato as fruiting vegetables, table olives as fruit, and coconut with nuts and seeds. The processing guidance describes culinary fruit generally as acidic or sugary and often served as dessert, while classifying peas, sweetcorn, cucumber, tomato, aubergine and avocado as ‘fruit vegetables’.

## Data method and file format

### M01

International Organization for Standardization, [Online Browsing Platform](https://www.iso.org/obp/ui/#search/code/). Authority for ISO 3166-1 and ISO 3166-2 identifiers. Codes should be rechecked before publication.

### M02

Obsidian Help, [Bases syntax](https://help.obsidian.md/bases/syntax) and [Base views](https://help.obsidian.md/bases/views). Official syntax used for the country index.

### M03

Unicode Consortium, CLDR, [English territory names in JSON](https://raw.githubusercontent.com/unicode-org/cldr-json/refs/heads/main/cldr-json/cldr-localenames-full/main/en/territories.json), [Country/Region (Territory) Names](https://cldr.unicode.org/translation/displaynames/countryregion-territory-names), [Territory Subdivisions](https://www.unicode.org/cldr/charts/48/supplemental/territory_subdivisions.html), and [Territory Containment](https://www.unicode.org/cldr/charts/48/supplemental/territory_containment_un_m_49.html). Terminology and Unicode CLDR English (`en`) display-name reference for territories at all levels. The project prefers a non-abbreviated `alt="short"` value when available. Use machine-readable CLDR data, rather than scraping charts, when generating publication data. JSON reviewed 22 July 2026.

### M04

Library of Congress, [ISO 639 frequently asked questions](https://www.loc.gov/standards/iso639-2/faq). Authoritative language-code overview identifying ISO 639-1 as the alpha-2 code and ISO 639-3 as the alpha-3 code for comprehensive coverage of individual languages. Reviewed 22 July 2026.

## Source-quality notes

- Government statistical agencies, current botanical authorities, and official commodity definitions are preferred.
- Government news releases are often timely but may use promotional language or unreconciled estimates.
- Trade interfaces derived from UN Comtrade are suitable for screening; raw reporter/partner data should replace them in a publication dataset.
- Farm, nursery, travel, and stock-image pages can establish a lead or a physical occurrence, but rarely establish a national total.
- A source can be credible evidence that a sign existed while still being unusable for image reproduction.

## Bundled-key audit

Reviewed on **29 July 2026**. “Retain” describes the present research use, not permanent permission to cite the group without identifying the supporting member.

| Key or keys | Decision | Reason and future split condition |
|---|---|---|
| U19 | Retain | The Unicode 17.0 standard page and its versioned Unicode Character Database files form one release package. Name the exact data file and entry for a proposal-facing property or repertoire claim; split if a file begins to support an independent proposition. |
| U20 | Retain | UTS #51 and its Emoji 17.0 data files form one versioned source family; CLDR 48.2 is explicitly only an annotation and ordering cross-check. Split CLDR from the emoji family if it supports an independent proposal or publication claim, and meanwhile name the relevant report section, file and entry. |
| U21 | Retain | The two Unicode 17.0 code charts form a narrow contemporary-versus-legacy comparison. Proposal-facing use must identify the Symbols for Legacy Computing Supplement entries `U+1CEBD`–`U+1CEBF` or the relevant Miscellaneous Symbols and Pictographs entry; split if the charts support separate substantive claims. |
| U22 | Retain | The core chapter and three Aegean code charts jointly define one bounded historical-sign comparison. Existing claims identify the relevant signs by code point; split if one document is used independently in a proposal rather than as background comparison. |
| U24 | Retain | The current emoji and Script Encoding Working Group guidance jointly support one narrow flag-route background finding. Split if a claim turns on only one group’s remit, wording or revision date. |
| U26 | Retain | The names list, Unikemet data and UAX #57 are needed together for the current D010 identity-and-mirroring analysis. Record the exact name-list entry, Unikemet field and UAX section before proposal use; split if any surface supports a separate proposition. |
| F03–F05 | Retain | These are background botanical and culinary source groups assembled to classify difficult cases, not proposal evidence groups. Split an individual document when its specific taxon, definition or table becomes independently citable in a proposal or formal publication. |
| M02 | Retain | The two Obsidian Help pages are one software-documentation family used only for the project method. Split only if version-specific behaviour requires separate records. |
| M03 | Retain | The CLDR JSON and explanatory charts form one terminology and publication-data family. Cite the exact release, file, path or chart row for a published data claim; split subdivision, containment or display-name sources if they acquire independent uses. |
