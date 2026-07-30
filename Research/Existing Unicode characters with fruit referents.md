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

For proposal work, the principal comparison set is the **29 contemporary emoji-capable characters plus the lime emoji sequence**, 🍋‍🟩 \<U+1F34B 🍋 <span style="font-variant:all-small-caps">LEMON</span>, U+200D <span style="font-variant:all-small-caps">ZERO WIDTH JOINER</span>, U+1F7E9 🟩 <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span>\>. The three legacy terminal symbols are weak supplementary comparisons, and the nine historical Aegean signs are weaker still. They remain documented because they satisfy the stated repertoire rule, not because they are likely precedents for a final proposal.

Lime is represented by this single extended grapheme cluster, an RGI emoji ZWJ sequence, rather than by a separately encoded lime character. Its significance here is that Unicode emoji data represent lime as a subject; the sequence mechanism is secondary. It is not counted among the 41 encoded characters. The sequence is recorded in Emoji 17.0’s `emoji-zwj-sequences.txt` and `emoji-test.txt` files ([U20](Sources.md#u20)).

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

This is the principal proposal-facing comparison. Each row contains one extended grapheme cluster: either one encoded character or, for lime, one multi-character emoji sequence perceived as a single symbol. Literal forms are included for visual reference, but code points and character names remain necessary because font and platform support vary.

The code points and character names resolve to the displayed entries in Unicode 17.0 `UnicodeData.txt` and `NamesList.txt` ([U19](Sources.md#u19)). Emoji properties, standardized presentation sequences, the lime emoji sequence and its RGI status resolve respectively to Emoji 17.0 `emoji-data.txt`, `emoji-variation-sequences.txt`, `emoji-zwj-sequences.txt` and `emoji-test.txt`; CLDR 48.2 supplies only the stated English annotation and ordering cross-checks ([U20](Sources.md#u20)). The source-group keys retain release packages, while each table row supplies the exact code point or sequence to inspect.

‘Qualified’ records that the familiar object contains botanical fruits or combines ovary and non-ovary tissue; it does not mean that one definition overrides the other.

| Character or sequence | Code point(s) | Name(s) | Referent | Encoding and presentation | Botanical classification | Common culinary classification |
| --- | --- | --- | --- | --- | --- | --- |
| 🍇 | U+1F347 | <span style="font-variant:all-small-caps">GRAPES</span> | Grapes | Encoded character; default emoji presentation | Fruit: a cluster of simple berries | Fruit |
| 🍈 | U+1F348 | <span style="font-variant:all-small-caps">MELON</span> | Melon | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Fruit |
| 🍉 | U+1F349 | <span style="font-variant:all-small-caps">WATERMELON</span> | Watermelon | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Fruit |
| 🍊 | U+1F34A | <span style="font-variant:all-small-caps">TANGERINE</span> | Tangerine | Encoded character; default emoji presentation | Fruit: citrus hesperidium | Fruit; the glyph and CLDR keywords can also support a more generic orange or citrus reading |
| 🍋 | U+1F34B | <span style="font-variant:all-small-caps">LEMON</span> | Lemon | Encoded character; default emoji presentation | Fruit: citrus hesperidium | Fruit |
| 🍋‍🟩 | \<U+1F34B, U+200D, U+1F7E9\> | \<<span style="font-variant:all-small-caps">LEMON</span>, <span style="font-variant:all-small-caps">ZWJ</span>, <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span>\> | Lime | RGI emoji ZWJ sequence since Emoji 15.1; **not a separately encoded lime character** | Fruit: citrus hesperidium | Fruit |
| 🍌 | U+1F34C | <span style="font-variant:all-small-caps">BANANA</span> | Banana | Encoded character; default emoji presentation | Fruit: berry | Fruit |
| 🍍 | U+1F34D | <span style="font-variant:all-small-caps">PINEAPPLE</span> | Pineapple | Encoded character; default emoji presentation | Qualified fruit: multiple fruit formed from coalesced fruits and associated tissue | Fruit |
| 🥭 | U+1F96D | <span style="font-variant:all-small-caps">MANGO</span> | Mango | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍎 | U+1F34E | <span style="font-variant:all-small-caps">RED APPLE</span> | Apple | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit; the ovary forms the core and much of the flesh is hypanthium | Fruit |
| 🍏 | U+1F34F | <span style="font-variant:all-small-caps">GREEN APPLE</span> | Apple | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit; the ovary forms the core and much of the flesh is hypanthium | Fruit |
| 🍐 | U+1F350 | <span style="font-variant:all-small-caps">PEAR</span> | Pear | Encoded character; default emoji presentation | Qualified fruit: pome or accessory fruit | Fruit |
| 🍑 | U+1F351 | <span style="font-variant:all-small-caps">PEACH</span> | Peach | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍒 | U+1F352 | <span style="font-variant:all-small-caps">CHERRIES</span> | Cherry | Encoded character; default emoji presentation | Fruit: drupe | Fruit |
| 🍓 | U+1F353 | <span style="font-variant:all-small-caps">STRAWBERRY</span> | Strawberry | Encoded character; default emoji presentation | Qualified fruit: aggregate accessory structure; the surface achenes are the botanical fruits and the red flesh is receptacle | Fruit |
| 🫐 | U+1FAD0 | <span style="font-variant:all-small-caps">BLUEBERRIES</span> | Blueberries | Encoded character; default emoji presentation | Fruit: berries | Fruit |
| 🥝 | U+1F95D | <span style="font-variant:all-small-caps">KIWIFRUIT</span> | Kiwifruit | Encoded character; default emoji presentation | Fruit: berry | Fruit |
| 🍅 | U+1F345 | <span style="font-variant:all-small-caps">TOMATO</span> | Tomato | Encoded character; default emoji presentation | Fruit: berry | Usually vegetable in culinary and dietary grouping; mixed popular labelling. CLDR places it under ‘food-fruit’ and supplies both ‘fruit’ and ‘vegetable’ keywords |
| 🫒 | U+1FAD2 | <span style="font-variant:all-small-caps">OLIVE</span> | Olive | Encoded character; default emoji presentation | Fruit: drupe | Mixed: FAO groups table olives with fruits, while ordinary use often treats them as a savoury ingredient or condiment |
| 🥥 | U+1F965 | <span style="font-variant:all-small-caps">COCONUT</span> | Coconut | Encoded character; default emoji presentation | Qualified fruit: the whole coconut is a fibrous drupe; a dehusked or split coconut foregrounds the endocarp and seed | Mixed fruit/nut usage; FAO’s dietary grouping places coconut with nuts and seeds |
| 🥑 | U+1F951 | <span style="font-variant:all-small-caps">AVOCADO</span> | Avocado | Encoded character; default emoji presentation | Fruit: single-seeded berry | Mixed: widely called a fruit but normally used as a savoury vegetable; CLDR orders it under ‘food-vegetable’ |
| 🍆 | U+1F346 | <span style="font-variant:all-small-caps">AUBERGINE</span> | Aubergine or eggplant | Encoded character; default emoji presentation | Fruit: berry | Vegetable |
| 🌽 | U+1F33D | <span style="font-variant:all-small-caps">EAR OF MAIZE</span> | Maize or corn ear | Encoded character; default emoji presentation | Qualified fruit-bearing structure: each kernel is a caryopsis, a dry one-seeded fruit | Mixed: sweetcorn is used as a vegetable; mature maize is a cereal grain |
| 🌶 | U+1F336 | <span style="font-variant:all-small-caps">HOT PEPPER</span> | Hot pepper | Encoded character; emoji-capable with default text presentation | Fruit: berry | Vegetable when fresh and often spice when dried; not normally a culinary fruit |
| 🫑 | U+1FAD1 | <span style="font-variant:all-small-caps">BELL PEPPER</span> | Bell pepper | Encoded character; default emoji presentation | Fruit: berry | Vegetable |
| 🥒 | U+1F952 | <span style="font-variant:all-small-caps">CUCUMBER</span> | Cucumber | Encoded character; default emoji presentation | Fruit: pepo, a modified berry | Vegetable |
| 🥜 | U+1F95C | <span style="font-variant:all-small-caps">PEANUTS</span> | Peanuts | Encoded character; default emoji presentation | Qualified and glyph-sensitive: an intact peanut pod is a legume fruit; a shelled peanut is its seed | Nut or legume, not culinary fruit |
| 🌰 | U+1F330 | <span style="font-variant:all-small-caps">CHESTNUT</span> | Chestnut | Encoded character; default emoji presentation | Fruit: a true botanical nut, a dry indehiscent fruit; the edible portion is principally the seed | Nut |
| 🫛 | U+1FADB | <span style="font-variant:all-small-caps">PEA POD</span> | Pea pod | Encoded character; default emoji presentation | Fruit: a dry legume containing seeds | Vegetable |
| 🌾 | U+1F33E | <span style="font-variant:all-small-caps">EAR OF RICE</span> (CLDR short name ‘sheaf of rice’) | Rice sheaf | Encoded character; default emoji presentation | Qualified fruit-bearing structure: each rice grain is a caryopsis | Cereal grain |

Unicode Emoji subgroup labels match neither classification. ‘food-fruit’ includes <span style="font-variant:all-small-caps">TOMATO</span>, <span style="font-variant:all-small-caps">OLIVE</span> and <span style="font-variant:all-small-caps">COCONUT</span>, while ‘food-vegetable’ includes <span style="font-variant:all-small-caps">AVOCADO</span>, <span style="font-variant:all-small-caps">AUBERGINE</span>, <span style="font-variant:all-small-caps">EAR OF MAIZE</span>, both peppers, <span style="font-variant:all-small-caps">CUCUMBER</span>, <span style="font-variant:all-small-caps">PEANUTS</span>, <span style="font-variant:all-small-caps">CHESTNUT</span> and <span style="font-variant:all-small-caps">PEA POD</span>; <span style="font-variant:all-small-caps">EAR OF RICE</span> is under ‘plant-other’. These are chart-ordering categories, not botanical or culinary determinations. ([U20](Sources.md#u20))

Botanical terminology in the table follows the structural classifications in [F01](Sources.md#f01) and [F02](Sources.md#f02). Fig, avocado, coconut, mango, peanuts, chestnuts and the cereal grains were separately checked in [F03](Sources.md#f03) and [F04](Sources.md#f04). The culinary column deliberately retains disagreements between FAO food groups and Unicode CLDR/emoji ordering rather than treating either as a biological authority. ([F05](Sources.md#f05), [U20](Sources.md#u20))

### Presentation variants of the hot pepper character

Of the 29 emoji-capable encoded characters, 28 have `Emoji_Presentation=Yes` and normally display in emoji style. <span style="font-variant:all-small-caps">HOT PEPPER</span> has `Emoji=Yes` but `Emoji_Presentation=No`. Its standardized variation sequences request text or emoji style; they are presentations of the same encoded hot-pepper character, not further fruit characters. Each sequence is shown on its own row. ([U20](Sources.md#u20))

| Sequence | Code points | Names | Requested presentation |
| --- | --- | --- | --- |
| 🌶︎ | \<U+1F336, U+FE0E\> | \<<span style="font-variant:all-small-caps">HOT PEPPER</span>, <span style="font-variant:all-small-caps">VS15</span>\> | Text style |
| 🌶️ | \<U+1F336, U+FE0F\> | \<<span style="font-variant:all-small-caps">HOT PEPPER</span>, <span style="font-variant:all-small-caps">VS16</span>\> | Emoji style |

The lime sequence’s components retain their own encoded identities. U+1F7E9 🟩 <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span> is not independently a fruit character, and an implementation that does not support 🍋‍🟩 may expose its components rather than one lime glyph. This limits interoperability, but the main comparative fact is that lime itself has a standardized emoji representation. The sequence does not show that durian has an adequate existing representation.

## Legacy terminal fruit symbols

These three explicitly non-emoji characters came from a legacy terminal source set. They are interesting repertoire findings but weak comparisons for either a modern character proposal or an emoji re-review, so they are kept outside the principal table.

| Character | Code point | Name | Referent | Encoding and presentation | Botanical classification | Common culinary classification |
| --- | --- | --- | --- | --- | --- | --- |
| 𜺽 | U+1CEBD | <span style="font-variant:all-small-caps">APPLE SYMBOL</span> | Apple | Encoded legacy symbol; explicitly non-emoji | Qualified fruit: pome or accessory fruit | Fruit |
| 𜺾 | U+1CEBE | <span style="font-variant:all-small-caps">CHERRY SYMBOL</span> | Cherry | Encoded legacy symbol; explicitly non-emoji | Fruit: drupe | Fruit |
| 𜺿 | U+1CEBF | <span style="font-variant:all-small-caps">STRAWBERRY SYMBOL</span> | Strawberry | Encoded legacy symbol; explicitly non-emoji | Qualified fruit: aggregate accessory structure | Fruit |

Their only durable comparative point is narrow: character encoding and emoji presentation are separable. Their source-set history does not provide a close precedent for durian.

The non-emoji labels and cross-references resolve to the Unicode 17.0 Symbols for Legacy Computing Supplement entries U+1CEBD–U+1CEBF and the corresponding Miscellaneous Symbols and Pictographs entries ([U21](Sources.md#u21)); the source-set and disunification rationale resolves to L2/23-252, especially its proposal summary and rationale ([U23](Sources.md#u23)).

## Historical Aegean commodity signs

These nine non-emoji script characters qualify under the deliberately broad botanical rule because Unicode documents a non-phonetic commodity, logographic or monogrammatic value. They are the weakest proposal comparisons in this review and are unlikely to belong in a final proposal except for a narrowly qualified point.

| Character | Code point | Name | Referent | Established sign value | Botanical classification | Common culinary classification |
| --- | --- | --- | --- | --- | --- | --- |
| 𐂓 | U+10093 | <span style="font-variant:all-small-caps">LINEAR B MONOGRAM B127 KAPO</span> | Generic fruit | Monogram glossed ‘fruit’ | Generic fruit value; no structure or taxon is specified | Fruit, but the Unicode gloss does not define the precise historical commodity scope |
| 𐙉 | U+10649 | <span style="font-variant:all-small-caps">LINEAR A SIGN AB120</span> | Generic cereal grain | Sign annotated ‘grain’ | Qualified fruit: Unicode does not specify the cereal; cereal grains are caryopses | Cereal grain, not culinary fruit |
| 𐙊 | U+1064A | <span style="font-variant:all-small-caps">LINEAR A SIGN A120B</span> | Generic cereal grain | Sign annotated ‘grain’ | Qualified fruit: Unicode does not specify the cereal; cereal grains are caryopses | Cereal grain, not culinary fruit |
| 𐂎 | U+1008E | <span style="font-variant:all-small-caps">LINEAR B IDEOGRAM B120 WHEAT</span> | Wheat | Commodity ideogram | Qualified fruit-bearing commodity: wheat grains are caryopses | Cereal grain, not culinary fruit |
| 𐂏 | U+1008F | <span style="font-variant:all-small-caps">LINEAR B IDEOGRAM B121 BARLEY</span> | Barley | Commodity ideogram | Qualified fruit-bearing commodity: barley grains are caryopses | Cereal grain, not culinary fruit |
| 𐀛 | U+1001B | <span style="font-variant:all-small-caps">LINEAR B SYLLABLE B030 NI</span> | Fig | Separately documented ideogram B030 value ‘figs’ | Qualified fruit: a syconium of receptacle tissue enclosing many small fruits | Fruit |
| 𐘝 | U+1061D | <span style="font-variant:all-small-caps">LINEAR A SIGN AB030</span> | Fig | Sign annotated ‘figs’ | Qualified fruit: a syconium of receptacle tissue enclosing many small fruits | Fruit |
| 𐂐 | U+10090 | <span style="font-variant:all-small-caps">LINEAR B IDEOGRAM B122 OLIVE</span> | Olive | Commodity ideogram | Fruit: drupe | Mixed: fruit in FAO grouping; often a savoury ingredient or condiment in ordinary use |
| 𐙋 | U+1064B | <span style="font-variant:all-small-caps">LINEAR A SIGN AB122</span> | Olive | Sign annotated ‘olives’ | Fruit: drupe | Mixed: fruit in FAO grouping; often a savoury ingredient or condiment in ordinary use |

The Aegean inclusions are narrow exceptions to the script-character exclusion. Unicode describes Linear B ideograms as logographs used mainly as counters for commodities, documents a separate ideogram B030 ‘figs’ use for the encoded NI syllable, names the wheat, barley and olive ideograms, and glosses the dedicated B127 KAPO monogram as ‘fruit’. The corresponding Linear A signs are officially annotated ‘figs’, ‘grain’ and ‘olives’. Their qualifying function is therefore a separately documented commodity sign, not the ordinary sequential spelling of a fruit name. ([U22](Sources.md#u22))

## Boundary and exclusion register

- U+2F60 ⽠ <span style="font-variant:all-small-caps">KANGXI RADICAL MELON</span>, U+2F72 ⽲ <span style="font-variant:all-small-caps">KANGXI RADICAL GRAIN</span>, U+2F76 ⽶ <span style="font-variant:all-small-caps">KANGXI RADICAL RICE</span>, U+2F96 ⾖ <span style="font-variant:all-small-caps">KANGXI RADICAL BEAN</span>, U+2FC6 ⿆ <span style="font-variant:all-small-caps">KANGXI RADICAL WHEAT</span>, U+2EE8 ⻨ <span style="font-variant:all-small-caps">CJK RADICAL SIMPLIFIED WHEAT</span>, and ordinary ideographs or script letters used to write food names are excluded. Their conventional role is script structure or lexical writing, not independently established food pictograms; the Kangxi radicals have compatibility mappings to unified ideographs.
- Egyptian hieroglyphs annotated with fig, fruit, emmer or mixed plant-classifier values—including U+13EA6 𓺦 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-13EA6</span>, U+13EB1 𓺱 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-13EB1</span>, U+13EB9 𓺹 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-13EB9</span>, U+13EC0 𓻀 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-13EC0</span>, U+142A1 𔊡 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-142A1</span> and U+142A2 𔊢 <span style="font-variant:all-small-caps">EGYPTIAN HIEROGLYPH-142A2</span>—are excluded. These are logographic or classifier readings inside Egyptian writing; no independent fruit-symbol use was established under the approved rule.
- U+101F3 𐇳 <span style="font-variant:all-small-caps">PHAISTOS DISC SIGN VINE</span> is a vine sign, not a fruit, and the script is undeciphered.
- U+1F022 🀢 <span style="font-variant:all-small-caps">MAHJONG TILE PLUM</span> and U+1F338 🌸 <span style="font-variant:all-small-caps">CHERRY BLOSSOM</span> refer to flowers or flower tiles, not plum or cherry fruit.
- The vine-leaf fleurons 🙘 🙙 🙚 🙛 🙜 🙝 🙞 🙟 (U+1F658–U+1F65F) are ornamental leaves, not fruit.
- U+1FAD8 🫘 <span style="font-variant:all-small-caps">BEANS</span> conventionally denotes loose edible seeds. <span style="font-variant:all-small-caps">PEA POD</span> is separately encoded and included as the fruit.
- U+1F383 🎃 <span style="font-variant:all-small-caps">JACK-O-LANTERN</span> is a derived lantern and Halloween symbol made from a pumpkin, not conventionally a fruit character.
- POPCORN (🍿), rice dishes (🍘 🍙 🍚 🍛), PIE (🥧), drinks, juice containers and fruit garnishes are excluded as processed foods, generic containers or incidental ingredients whose encoded referent is not a fruit.
- Private-use characters and arbitrary icon-font substitutions are excluded because their semantics depend on private agreement or font mapping rather than assignment by the Unicode Standard, so they do not provide standard interchange semantics for the represented fruit identity.

## Completeness method

The result uses four independent passes:

1. freeze the versioned Unicode 17.0.0 `UnicodeData.txt`, `NamesList.txt`, name aliases and block data;
2. review every Emoji 17.0 Food & Drink entry plus plant entries, then distinguish single characters, presentation sequences and ZWJ sequences from `emoji-test.txt` and the property files;
3. search character names, aliases and NamesList annotations with a broad fruit and botanical vocabulary, then inspect surrounding block annotations and cross-references; and
4. reverse-check the accepted set against CLDR 48.2 English annotations, official code charts and the historical-script descriptions, retaining a boundary register for false positives.

This method makes the completeness claim reproducible for the defined standard corpus. It cannot prove the absence of undocumented symbolic use attached to an arbitrary script character, and representative glyphs are not prescriptive. The reusable workflow is recorded at [Comparative Unicode repertoire research](<../Methods/Comparative Unicode repertoire research.md>).

## Interpretation for the durian project

The principal finding is the contemporary emoji neighbourhood: Unicode already represents many fruit subjects, including botanical fruits commonly treated as vegetables, nuts, pulses or grains, and lime has a standardized representation even though it is implemented as a sequence. This makes a durian referent semantically intelligible within the combined character-and-sequence set and is directly relevant to an emoji re-review.

Lime is an informative but probably inconsequential comparison for the character proposal. Its sequence confirms representation of the subject but neither supplies an adequate representation for durian nor establishes that another fruit should receive a character. The legacy terminal symbols and historical Aegean signs are still weaker: they arose from source-set and historical-script requirements unlike the prospective durian case and should not be presented as precedent that any additional fruit merits encoding.

None of these comparisons establishes plain-text need, widespread symbolic use, distinctiveness or any other encoding criterion. The repertoire documents the set a prospective durian character could join; it does not prove the case for joining it.

## Limits and next use

- Literal character display is visually important but depends on font, shaping and platform support; code-point notation and character names are the stable identifiers.
- Culinary categories vary by territory, language and preparation. The table records a defensible common English/international grouping, not a universal taxonomy.
- <span style="font-variant:all-small-caps">COCONUT</span> and <span style="font-variant:all-small-caps">PEANUTS</span> are especially sensitive to whether the intended object is the whole fruit, its shell or pod, or the edible seed.
- The maize and rice emoji represent fruit-bearing structures rather than isolated fruits; the Aegean wheat, barley and grain signs denote cereal commodities. Their inclusion follows the botanical status of cereal grains as fruits, not culinary usage.
- The historical Aegean signs document ancient commodity notation, not modern public comprehension.
- This dataset should feed the deferred plain-text-need and counterargument audit after the owner’s sign-photo collection is available; it does not supersede that evidence dependency.
