---
title: Existing Unicode characters with fruit referents
research_status: bounded complete repertoire review
unicode_cutoff: 17.0.0
emoji_cutoff: 17.0
cldr_version: 48.2
last_reviewed: 2026-07-29
tags:
  - unicode
  - fruit
  - repertoire
  - emoji
  - classification
---

## Finding

At the Unicode Standard, Version 17.0.0 cut-off, the defined review finds **41 encoded characters covering 33 fruit-referent categories**, but their relevance to a prospective durian character is highly asymmetric:

| Stratum                                            | Encoded characters | Presentation status                                                                  |
| -------------------------------------------------- | -----------------: | ------------------------------------------------------------------------------------ |
| Contemporary emoji-capable characters meeting the fruit-referent inclusion rules |                 29 | Emoji-capable: 28 have default emoji presentation; one has default text presentation |
| Legacy terminal fruit symbols                      |                  3 | Explicitly non-emoji                                                                 |
| Historical Aegean commodity or logographic signs   |                  9 | Non-emoji script characters                                                          |
| **Total**                                          |             **41** | Emoji status is not the criterion for membership                                     |

For proposal work, the principal comparison set is the **29 contemporary emoji-capable characters plus the lime sequence (🍋‍🟩)**. The three legacy terminal symbols are weak supplementary comparisons, and the nine historical Aegean signs are weaker still. They remain documented because they satisfy the stated repertoire rule, not because they are likely precedents for a final proposal.

Lime is represented by the single extended grapheme cluster 🍋‍🟩, an RGI emoji ZWJ sequence, rather than by a separately encoded lime character. Its significance here is that Unicode’s emoji repertoire represents lime as a subject; the sequence mechanism is secondary. It is not counted among the 41 encoded characters. The sequence is recorded in Emoji 17.0’s `emoji-zwj-sequences.txt` and `emoji-test.txt` files ([U20](Sources.md#u20)).

The encoded characters therefore cover 33 referent categories; adding the sequence-only lime category brings the represented total to 34.

This is the complete result within the corpus and inclusion rules below. It is not a claim that every arbitrary letter, ideograph or culturally reinterpreted glyph with an undocumented fruit association has been found.

## Definitions and inclusion rules

The **botanical** classification treats a fruit as a ripened ovary with its seeds and recognizes accessory tissue, aggregate and multiple fruits, dry fruits, and fruit-bearing structures. The **culinary** classification follows common food grouping and use rather than plant morphology. ‘Fruit’, ‘vegetable’, ‘nut’, ‘pulse’ and ‘grain’ are therefore parallel culinary categories, not botanical opposites. Botanical types and difficult cases follow university botany and extension sources; culinary labels use FAO groupings designed around foods’ roles in diets and common dietary categories. ([F01](Sources.md#f01), [F02](Sources.md#f02), [F03](Sources.md#f03), [F04](Sources.md#f04), [F05](Sources.md#f05))

A character or sequence is included when its encoded identity, established non-phonetic commodity-sign value, or standardized emoji identity directly denotes:

- a whole fruit, cluster of fruits, cut fruit or generic fruit class;
- a structure or cereal commodity whose edible units are botanical fruits, such as maize kernels or rice grains; or
- an intact pod or nut that is itself botanically a fruit, even when ordinary culinary language instead emphasizes its seeds.

Ordinary script characters that spell a fruit name are excluded. A historical sign qualifies only when Unicode identifies a separately established non-phonetic ideographic, logographic or monogrammatic commodity use, even if the same encoded character also has a syllabic use. A phonetic spelling or one lexical reading of a general script character is insufficient. Processed foods, drinks, incidental garnishes, flowers, leaves, fruit-bearing plants without depicted fruit, private-use glyphs and arbitrary icon-font mappings are excluded.

## Contemporary emoji comparison

This is the principal proposal-facing comparison. Each row contains one extended grapheme cluster: either one encoded character or, for lime, one multi-character emoji sequence perceived as a single symbol. Literal forms are included for visual reference, but code points and names remain necessary because font and platform support vary.

The code-point identities and names resolve to the displayed entries in Unicode 17.0 `UnicodeData.txt` and `NamesList.txt` ([U19](Sources.md#u19)). Emoji properties, standardized presentation sequences and the RGI lime sequence resolve respectively to Emoji 17.0 `emoji-data.txt`, `emoji-variation-sequences.txt`, `emoji-zwj-sequences.txt` and `emoji-test.txt`; CLDR 48.2 supplies only the stated English annotation and ordering cross-checks ([U20](Sources.md#u20)). The source-group keys retain release packages, while each table row supplies the exact code point or sequence to inspect.

‘Qualified’ records that the familiar object contains botanical fruits or combines ovary and non-ovary tissue; it does not mean that one definition overrides the other.

| Character or sequence | Code point(s) and name(s) | Referent | Encoding and presentation | Botanical classification | Common culinary classification |
|---|---|---|---|---|---|
| 🍇 | `U+1F347 GRAPES` | Grapes | Encoded character; default emoji presentation | Fruit: a cluster of simple berries | Fruit |
| 🍈 | `U+1F348 MELON` | Melon | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Fruit |
| 🍉 | `U+1F349 WATERMELON` | Watermelon | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Fruit |
| 🍊 | `U+1F34A TANGERINE` | Tangerine | Encoded character; default emoji presentation | Fruit: citrus hesperidium | Fruit; the glyph and CLDR keywords can also support a more generic orange or citrus reading |
| 🍋 | `U+1F34B LEMON` | Lemon | Encoded character; default emoji presentation | Fruit: citrus hesperidium | Fruit |
| 🍋‍🟩 | `U+1F34B U+200D U+1F7E9` — LEMON, ZERO WIDTH JOINER, LARGE GREEN SQUARE | Lime | RGI emoji ZWJ sequence since Emoji 15.1; **not a separately encoded lime character** | Fruit: citrus hesperidium | Fruit |
| 🍌 | `U+1F34C BANANA` | Banana | Encoded character; default emoji presentation | Fruit: berry | Fruit |
| 🍍 | `U+1F34D PINEAPPLE` | Pineapple | Encoded character; default emoji presentation | Qualified fruit: multiple fruit formed from coalesced fruits and associated tissue | Fruit |
| 🥭 | `U+1F96D MANGO` | Mango | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍎 | `U+1F34E RED APPLE` | Apple | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit; the ovary forms the core and much of the flesh is hypanthium | Fruit |
| 🍏 | `U+1F34F GREEN APPLE` | Apple | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit; the ovary forms the core and much of the flesh is hypanthium | Fruit |
| 🍐 | `U+1F350 PEAR` | Pear | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit | Fruit |
| 🍑 | `U+1F351 PEACH` | Peach | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍒 | `U+1F352 CHERRIES` | Cherry | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍓 | `U+1F353 STRAWBERRY` | Strawberry | Encoded character; default emoji presentation | Qualified fruit: aggregate accessory structure; the surface achenes are the botanical fruits and the red flesh is receptacle | Fruit |
| 🫐 | `U+1FAD0 BLUEBERRIES` | Blueberries | Encoded character; default emoji presentation | Fruit: berries | Fruit |
| 🥝 | `U+1F95D KIWIFRUIT` | Kiwifruit | Encoded character; default emoji presentation | Fruit: berry | Fruit |
| 🍅 | `U+1F345 TOMATO` | Tomato | Encoded character; default emoji presentation | Fruit: berry | Usually vegetable in culinary and dietary grouping; mixed popular labelling. CLDR places it under ‘food-fruit’ and supplies both ‘fruit’ and ‘vegetable’ keywords |
| 🫒 | `U+1FAD2 OLIVE` | Olive | Encoded character; default emoji presentation | Fruit: drupe | Mixed: FAO groups table olives with fruits, while ordinary use often treats them as a savoury ingredient or condiment |
| 🥥 | `U+1F965 COCONUT` | Coconut | Encoded character; default emoji presentation | Qualified fruit: the whole coconut is a fibrous drupe; a dehusked or split coconut foregrounds the endocarp and seed | Mixed fruit/nut usage; FAO’s dietary grouping places coconut with nuts and seeds |
| 🥑 | `U+1F951 AVOCADO` | Avocado | Encoded character; default emoji presentation | Fruit: single-seeded berry | Mixed: widely called a fruit but normally used as a savoury vegetable; CLDR orders it under ‘food-vegetable’ |
| 🍆 | `U+1F346 AUBERGINE` | Aubergine or eggplant | Encoded character; default emoji presentation | Fruit: berry | Vegetable |
| 🌽 | `U+1F33D EAR OF MAIZE` | Maize or corn ear | Encoded character; default emoji presentation | Qualified fruit-bearing structure: each kernel is a caryopsis, a dry one-seeded fruit | Mixed: sweetcorn is used as a vegetable; mature maize is a cereal grain |
| 🌶 | `U+1F336 HOT PEPPER` | Hot pepper | Encoded character; emoji-capable with default text presentation | Fruit: berry | Vegetable when fresh and often spice when dried; not normally a culinary fruit |
| 🫑 | `U+1FAD1 BELL PEPPER` | Bell pepper | Encoded character; default emoji presentation | Fruit: berry | Vegetable |
| 🥒 | `U+1F952 CUCUMBER` | Cucumber | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Vegetable |
| 🥜 | `U+1F95C PEANUTS` | Peanuts | Encoded character; default emoji presentation | Qualified and glyph-sensitive: an intact peanut pod is a legume fruit; a shelled peanut is its seed | Nut or legume, not culinary fruit |
| 🌰 | `U+1F330 CHESTNUT` | Chestnut | Encoded character; default emoji presentation | Fruit: a true botanical nut, a dry indehiscent fruit; the edible portion is principally the seed | Nut |
| 🫛 | `U+1FADB PEA POD` | Pea pod | Encoded character; default emoji presentation | Fruit: a dry legume containing seeds | Vegetable |
| 🌾 | `U+1F33E EAR OF RICE` (CLDR short name ‘sheaf of rice’) | Rice sheaf | Encoded character; default emoji presentation | Qualified fruit-bearing structure: each rice grain is a caryopsis | Cereal grain |

Unicode Emoji subgroup labels match neither classification. ‘food-fruit’ includes TOMATO, OLIVE and COCONUT, while ‘food-vegetable’ includes AVOCADO, AUBERGINE, EAR OF MAIZE, both peppers, CUCUMBER, PEANUTS, CHESTNUT and PEA POD; EAR OF RICE is under ‘plant-other’. These are chart-ordering categories, not botanical or culinary determinations. ([U20](Sources.md#u20))

Botanical terminology in the table follows the structural classifications in [F01](Sources.md#f01) and [F02](Sources.md#f02). Fig, avocado, coconut, mango, peanuts, chestnuts and the cereal grains were separately checked in [F03](Sources.md#f03) and [F04](Sources.md#f04). The culinary column deliberately retains disagreements between FAO food groups and Unicode CLDR/emoji ordering rather than treating either as a biological authority. ([F05](Sources.md#f05), [U20](Sources.md#u20))

### Presentation variants of HOT PEPPER

Of the 29 emoji-capable encoded characters, 28 have `Emoji_Presentation=Yes` and normally display in emoji style. HOT PEPPER has `Emoji=Yes` but `Emoji_Presentation=No`. Its standardized variation sequences request text or emoji style; they are presentations of the same encoded hot-pepper character, not further fruit characters. Each sequence is shown on its own row. ([U20](Sources.md#u20))

| Character sequence | Code-point sequence | Requested presentation |
|---|---|---|
| 🌶︎ | `U+1F336 U+FE0E` — HOT PEPPER, VARIATION SELECTOR-15 | Text style |
| 🌶️ | `U+1F336 U+FE0F` — HOT PEPPER, VARIATION SELECTOR-16 | Emoji style |

The lime sequence’s components retain their own encoded identities. LARGE GREEN SQUARE (🟩, `U+1F7E9`) is not independently a fruit character, and an implementation that does not support 🍋‍🟩 may expose its components rather than one lime glyph. This limits interoperability, but the main comparative fact is that lime itself has a standardized emoji representation. The sequence does not show that durian has an adequate existing representation.

## Legacy terminal fruit symbols

These three explicitly non-emoji characters came from a legacy terminal source set. They are interesting repertoire findings but weak comparisons for either a modern character proposal or an emoji re-review, so they are kept outside the principal table.

| Character | Code point and name | Referent | Encoding and presentation | Botanical classification | Common culinary classification |
|---|---|---|---|---|---|
| 𜺽 | `U+1CEBD APPLE SYMBOL` | Apple | Encoded legacy symbol; explicitly non-emoji | Qualified fruit: pome or accessory fruit | Fruit |
| 𜺾 | `U+1CEBE CHERRY SYMBOL` | Cherry | Encoded legacy symbol; explicitly non-emoji | Fruit: drupe | Fruit |
| 𜺿 | `U+1CEBF STRAWBERRY SYMBOL` | Strawberry | Encoded legacy symbol; explicitly non-emoji | Qualified fruit: aggregate accessory structure | Fruit |

Their only durable comparative point is narrow: character encoding and emoji presentation are separable. Their source-set history does not provide a close precedent for durian.

The non-emoji labels and cross-references resolve to the Unicode 17.0 Symbols for Legacy Computing Supplement entries `U+1CEBD`–`U+1CEBF` and the corresponding Miscellaneous Symbols and Pictographs entries ([U21](Sources.md#u21)); the source-set and disunification rationale resolves to L2/23-252, especially its proposal summary and rationale ([U23](Sources.md#u23)).

## Historical Aegean commodity signs

These nine non-emoji script characters qualify under the deliberately broad botanical rule because Unicode documents a non-phonetic commodity, logographic or monogrammatic value. They are the weakest proposal comparisons in this review and are unlikely to belong in a final proposal except for a narrowly qualified point.

| Character | Code point and name | Referent | Established sign value | Botanical classification | Common culinary classification |
|---|---|---|---|---|---|
| 𐂓 | `U+10093 LINEAR B MONOGRAM B127 KAPO` | Generic fruit | Monogram glossed ‘fruit’ | Generic fruit value; no structure or taxon is specified | Fruit, but the Unicode gloss does not define the precise historical commodity scope |
| 𐙉 | `U+10649 LINEAR A SIGN AB120` | Generic cereal grain | Sign annotated ‘grain’ | Qualified fruit: Unicode does not specify the cereal; cereal grains are caryopses | Cereal grain, not culinary fruit |
| 𐙊 | `U+1064A LINEAR A SIGN A120B` | Generic cereal grain | Sign annotated ‘grain’ | Qualified fruit: Unicode does not specify the cereal; cereal grains are caryopses | Cereal grain, not culinary fruit |
| 𐂎 | `U+1008E LINEAR B IDEOGRAM B120 WHEAT` | Wheat | Commodity ideogram | Qualified fruit-bearing commodity: wheat grains are caryopses | Cereal grain, not culinary fruit |
| 𐂏 | `U+1008F LINEAR B IDEOGRAM B121 BARLEY` | Barley | Commodity ideogram | Qualified fruit-bearing commodity: barley grains are caryopses | Cereal grain, not culinary fruit |
| 𐀛 | `U+1001B LINEAR B SYLLABLE B030 NI` | Fig | Separately documented ideogram B030 value ‘figs’ | Qualified fruit: a syconium of receptacle tissue enclosing many small fruits | Fruit |
| 𐘝 | `U+1061D LINEAR A SIGN AB030` | Fig | Sign annotated ‘figs’ | Qualified fruit: a syconium of receptacle tissue enclosing many small fruits | Fruit |
| 𐂐 | `U+10090 LINEAR B IDEOGRAM B122 OLIVE` | Olive | Commodity ideogram | Fruit: drupe | Mixed: fruit in FAO grouping; often a savoury ingredient or condiment in ordinary use |
| 𐙋 | `U+1064B LINEAR A SIGN AB122` | Olive | Sign annotated ‘olives’ | Fruit: drupe | Mixed: fruit in FAO grouping; often a savoury ingredient or condiment in ordinary use |

The Aegean inclusions are narrow exceptions to the script-character exclusion. Unicode describes Linear B ideograms as logographs used mainly as counters for commodities, documents a separate ideogram B030 ‘figs’ use for the encoded NI syllable, names the wheat, barley and olive ideograms, and glosses the dedicated B127 KAPO monogram as ‘fruit’. The corresponding Linear A signs are officially annotated ‘figs’, ‘grain’ and ‘olives’. Their qualifying function is therefore a separately documented commodity sign, not the ordinary sequential spelling of a fruit name. ([U22](Sources.md#u22))

## Boundary and exclusion register

- KANGXI RADICAL MELON (⽠, `U+2F60`), the radicals named GRAIN (⽲, `U+2F72`), RICE (⽶, `U+2F76`), BEAN (⾖, `U+2F96`) and WHEAT (⿆, `U+2FC6`; ⻨, `U+2EE8`), and ordinary ideographs or script letters used to write food names are excluded. Their conventional role is script structure or lexical writing, not independently established food pictograms; the Kangxi radicals have compatibility mappings to unified ideographs.
- Egyptian hieroglyphs annotated with fig, fruit, emmer or mixed plant-classifier values—including 𓺦 (`U+13EA6`), 𓺱 (`U+13EB1`), 𓺹 (`U+13EB9`), 𓻀 (`U+13EC0`), 𔊡 (`U+142A1`) and 𔊢 (`U+142A2`)—are excluded. These are logographic or classifier readings inside Egyptian writing; no independent fruit-symbol use was established under the approved rule.
- PHAISTOS DISC SIGN VINE (𐇳, `U+101F3`) is a vine sign, not a fruit, and the script is undeciphered.
- MAHJONG TILE PLUM (🀢, `U+1F022`) and CHERRY BLOSSOM (🌸, `U+1F338`) refer to flowers or flower tiles, not plum or cherry fruit.
- The vine-leaf fleurons 🙘 🙙 🙚 🙛 🙜 🙝 🙞 🙟 (`U+1F658`–`U+1F65F`) are ornamental leaves, not fruit.
- BEANS (🫘, `U+1FAD8`) conventionally denotes loose edible seeds. PEA POD (🫛, `U+1FADB`) is separately encoded and included as the fruit.
- JACK-O-LANTERN (🎃, `U+1F383`) is a derived lantern and Halloween symbol made from a pumpkin, not conventionally a fruit character.
- POPCORN (🍿), rice dishes (🍘 🍙 🍚 🍛), PIE (🥧), drinks, juice containers and fruit garnishes are excluded as processed foods, generic containers or incidental ingredients whose encoded referent is not a fruit.
- Private-use characters and arbitrary icon-font substitutions are excluded because they are not assigned Unicode characters and have no standard interchange semantics.

## Completeness method

The result uses four independent passes:

1. freeze the versioned Unicode 17.0.0 `UnicodeData.txt`, `NamesList.txt`, name aliases and block data;
2. review every Emoji 17.0 Food & Drink entry plus plant entries, then distinguish single characters, presentation sequences and ZWJ sequences from `emoji-test.txt` and the property files;
3. search Unicode names, aliases and NamesList annotations with a broad fruit and botanical vocabulary, then inspect surrounding block annotations and cross-references; and
4. reverse-check the accepted set against CLDR 48.2 English annotations, official code charts and the historical-script descriptions, retaining a boundary register for false positives.

This method makes the completeness claim reproducible for the defined standard corpus. It cannot prove the absence of undocumented symbolic use attached to an arbitrary script character, and representative glyphs are not prescriptive. The reusable workflow is recorded at [Comparative Unicode repertoire research](<../Methods/Comparative Unicode repertoire research.md>).

## Interpretation for the durian project

The principal finding is the contemporary emoji neighbourhood: Unicode already represents many fruit subjects, including botanical fruits commonly treated as vegetables, nuts, pulses or grains, and lime has a standardized representation even though it is implemented as a sequence. This makes a durian referent semantically intelligible within the repertoire and is directly relevant to an emoji re-review.

Lime is an informative but probably inconsequential comparison for the character proposal. Its sequence confirms representation of the subject but neither supplies an adequate representation for durian nor establishes that another fruit should receive a character. The legacy terminal symbols and historical Aegean signs are still weaker: they arose from source-set and historical-script requirements unlike the prospective durian case and should not be presented as precedent that any additional fruit merits encoding.

None of these comparisons establishes plain-text need, widespread symbolic use, distinctiveness or any other encoding criterion. The repertoire documents the set a prospective durian character could join; it does not prove the case for joining it.

## Limits and next use

- Literal character display is visually important but depends on font, shaping and platform support; code-point notation and names are the stable identifiers.
- Culinary categories vary by territory, language and preparation. The table records a defensible common English/international grouping, not a universal taxonomy.
- COCONUT and PEANUTS are especially sensitive to whether the intended object is the whole fruit, its shell or pod, or the edible seed.
- The maize and rice emoji represent fruit-bearing structures rather than isolated fruits; the Aegean wheat, barley and grain signs denote cereal commodities. Their inclusion follows the botanical status of cereal grains as fruits, not culinary usage.
- The historical Aegean signs document ancient commodity notation, not modern public comprehension.
- This dataset should feed the deferred plain-text-need and counterargument audit after the owner’s sign-photo collection is available; it does not supersede that evidence dependency.
