---
title: Evidence to encoding-question map
research_status: candidate-specific decision map
official_guidance_cutoff: 2026-07-29
evidence_cutoff: 2026-07-29
last_reviewed: 2026-07-29
tags:
  - durian
  - character-identity
  - encoding-analysis
  - evidence-map
---

This note maps the current Durian evidence to the questions that actually govern a character-encoding decision. It is a research-prioritization and review record, not a proposal draft or a cumulative score. Multiple sources may make a contextual fact well established without making that fact materially probative of character identity, stability, or public interchange in plain text.

The prospective entity under test is a **generic durian-fruit symbol that retains its identity across suitable renderings**. It is not provisionally defined as one exact artwork, a biological species identifier, a brand mark, or the composite of fruit, prohibition circle, slash, wording and sign layout. That boundary is candidate judgement derived from the [Durian overview](../Overview.md), the [geographic survey](<Durian geographic survey.md>) and the project’s [character-identity and encoding-analysis method](<../../../Methods/Character identity and encoding analysis.md>); it is not yet an observed user definition.

## Official frame and analytical labels

The official-guidance cut-off is **29 July 2026**. The current Script Encoding Working Group [Submission Guidelines and Process](https://sew.unicode.org/guidelines) were checked on that date ([U07](Sources.md#u07)), together with the [Unicode pipeline](https://www.unicode.org/alloc/Pipeline.html), last updated 27 July 2026 ([U20](Sources.md#u20)), and the [Archive of Notices of Non-Approval](https://www.unicode.org/alloc/nonapprovals.html) ([U21](Sources.md#u21)). Neither complete current list contained a ‘durian’ entry on that date.

The map uses the following labels:

- **[Official — eligibility]**: the proposed addition must be a character, must not already be encoded and must not be a duplicate representation expressible as an existing character sequence. Possible existing equivalents must be examined.
- **[Official — usage]**: existing use by a community must be demonstrated, independently of a creator where applicable.
- **[Official — stability]**: the character or proposed repertoire must be stable and not in active development.
- **[Official — interchange]**: encoding must be needed for public interchange of information in plain text.
- **[Official — proposal material]**: a proposal is expected to compare visually similar characters and provide other technical material. This is a submission requirement, not a fourth basic criterion.
- **[Project analysis]**: character-versus-icon classification, semantic boundaries, form convergence, representative-glyph independence, recognition, workflow loss, evidence independence, alternative representations, rights and falsification questions developed by this project.
- **[Counterargument]**: the strongest candidate-specific non-encoding explanation stated in the [Durian overview](../Overview.md).

Geographic spread, referent importance, repertoire fit, visual appeal, recognition and the number of sources are not presented below as official criteria. Rights status governs whether and how evidence can be published; it does not determine whether an abstract character exists.

## Decision map

| Evidence class or finding | Direction | Current strength for the proposition that matters | Main decision link | Principal gap |
|---|---|---|---|---|
| Provisional generic durian identity and boundary | Mixed | Coherent working hypothesis, but not yet user-validated | Eligibility; project identity analysis | Whether users preserve the base durian unit apart from sign composition |
| Repeated functional prohibition signage | Supports encoding | Strong for verified functional occurrence; moderate for a reusable abstract-unit inference | Usage; stability; character-versus-icon question | No demonstrated plain-text operation or independent-token workflow |
| Geographic breadth of observed symbol use | Supports encoding | Moderate for regional distribution; limited for prevalence or independent textual use | Usage; independence | Sparse occurrences, venue imbalance and web-selection bias |
| Form convergence and recognizability | Mixed | Preliminary only; no coded form corpus or recognition test | Stability; representative-glyph independence | Private corpus audit, variant coding and small monochrome testing |
| Marketing and brand use | Mixed | Limited supplementary evidence | Usage; icon/logo counterargument | Small corpus, deployment and public-comprehension evidence |
| Inline letter or punctuation substitution | Supports non-encoding for the documented occurrences | Clear for the underlying `O`, full-stop and letter–image analyses; weak for a wider durian convention | Eligibility; glyph/logo alternative | Independent uses in which the durian unit, rather than the replaced character, must be preserved |
| Production, trade, consumption and cultural importance | Contextual only | Often strong for the contextual fact; low relevance to encoding | Background and semantic scope | No evidential bridge from importance to textual use |
| Contemporary fruit and emoji repertoire | Mixed | Strong and versioned for the bounded repertoire; limited relevance to the character decision | Existing-representation check; route distinction | Candidate-specific equivalence and interchange analysis |
| Legacy terminal fruit symbols | Contextual only | Strong source-set finding; weak analogy | Route distinction; possible precedent counterargument | No comparable durian source-encoding requirement |
| Historical Aegean fruit or commodity signs | Contextual only | Strong historical identification; very weak analogy | Repertoire comparison | Different script, notation and interchange needs |
| Previous emoji submissions and committee history | Contextual only | Strong for the recoverable chronology; weak for merits | Prior-related-document context; route distinction | Missing submissions, response letters and 2022 item-specific reason |
| Visual distinctiveness and possible confusion | Mixed | Weak and preliminary | Visually similar-character comparison; recognizability | Systematic comparison and user testing |
| Plain-text public-interchange need | Supports non-encoding provisionally | Strong as a documented gap in the current case, not as proof that no need exists | Interchange | Named users, systems, operations and losses |
| Existing characters and ordinary text | Mixed | Strong for known brand uses and the bounded fruit review; incomplete as a full equivalence matrix | Eligibility; equivalence | Exhaustive candidate-specific semantic and technical comparison |
| Existing or possible character sequences | Mixed | Strong for the absence of a durian representation in the bounded fruit/emoji corpus; incomplete for all sequence models | Eligibility; duplicate representation | Explicit sequence inventory and behaviour testing |
| Images, words, metadata and higher-level systems | Supports non-encoding for presently documented functions | Strong fit to the observed sign and brand artefacts; untested against any proved external workflow | Interchange; strongest non-encoding model | A workflow in which these alternatives cause a concrete loss |
| Pending private photo-corpus audit | Contextual only | No finding may be inferred from unaudited material | Usage; stability; identity; independence | Catalogue, provenance, form coding and rights review |
| Rights-cleared versus reference-only evidence | Contextual only | Strong for current publication-readiness distinctions | Evidence usability, not encoding merits | Item-level clearance and selection after the corpus audit |

## Evidence records

### Provisional generic durian identity and boundary

- **Finding or class:** The present hypothesis is one generic durian-fruit unit across suitable whole-fruit or durian-pictogram renderings. A prohibition circle or slash, sign wording, venue layout, a particular brand treatment and species-level taxonomy remain outside the proposed identity.
- **Canonical source:** [Durian overview](../Overview.md), especially “Decision-changing evidence”; [Durian geographic survey](<Durian geographic survey.md>), especially “Symbol referent”; and [Character identity and encoding analysis](<../../../Methods/Character identity and encoding analysis.md>).
- **Relevance:** [Official — eligibility]; [Project analysis] semantic boundary, identity across glyphs and decomposition of physical signs.
- **Direction:** **Mixed.** The boundary makes a character hypothesis testable, but it is currently project-authored rather than an attested community definition.
- **Current strength:** Coherent and appropriately narrow as an analytical hypothesis; unverified as a user-recognized textual unit.
- **Exact proposition it can support:** The project is evaluating the generic popular referent “durian”, not a separately encoded “no durian” composite, exact sign artwork or *Durio zibethinus* taxonomic symbol.
- **What it cannot establish:** That users treat the generic pictogram as a character, distinguish it from an icon or need to interchange it in plain text.
- **Contradictions or alternatives:** The signs may communicate only through the complete artwork, wording and venue context; brand examples may preserve a brand or an existing letter rather than a durian unit.
- **Verification and rights:** This is candidate judgement synthesized from reviewed project notes; no rights conclusion follows from it.
- **Unresolved dependency:** Audit form variation and ask designers, operators and users what unit they regard as reusable outside the sign.
- **Likely proposal use:** A future scope and exclusions statement only if the evidence validates the boundary.

### Repeated functional prohibition signage

- **Finding or class:** Traceable signs use a durian image or name to prohibit the fruit in transport, accommodation and building contexts.
- **Canonical source:** [Durian signage](<Durian signage.md>) and the itemized [signage and policy source records](Sources.md#signage-and-policy).
- **Relevance:** [Official — usage] and [Official — stability]; [Project analysis] function-bearing use; [Counterargument] physical signs may still be icons or illustrations.
- **Direction:** **Supports encoding.**
- **Current strength:** Strong for verified functional occurrence and a repeated regulatory meaning within the bounded corpus; moderate for the inference that the base pictogram is a reusable abstract unit; no direct strength for interchange.
- **Exact proposition it can support:** By the evidence cut-off, durian-prohibition signs were traceably photographed or documented in mass-transit, hotel and building-rule contexts in six Southeast Asian territories, with the recurring function “durian is prohibited here”.
- **What it cannot establish:** Frequency, universal comprehension, a named symbol, transcription or data exchange, a separate “no durian” character, or independence of the fruit pictogram from wording, slash, colour and layout.
- **Contradictions or alternatives:** A venue can select an illustrative fruit asset and compose a complete visual rule without treating any component as plain text. Some forms may be copied, generic spiky-fruit images or intelligible only because of words and context.
- **Verification and rights:** Eight occurrence rows are verified at the level stated in the signage register. The Singapore and 1998 Thai photographs have Creative Commons reuse routes; the Bangkok footage requires licensing; several hotel or traveller photographs are reference-only or rights-unverified; the Indonesian occurrence is supported by a citable scholarly corpus but image rights remain separate.
- **Unresolved dependency:** Catalogue the private photo collection for provenance, independence, form, wording and composition, then test whether the base unit survives removal from the source artwork.
- **Likely proposal use:** Core usage evidence if the independence and identity tests hold; reproduce only a small rights-cleared set and present the prohibition overlay as composition rather than the proposed character.

### Geographic breadth of observed symbol use

- **Finding or class:** Verified or scholarly documented prohibition occurrences currently cover Indonesia, Cambodia, Malaysia, Singapore, Thailand and Vietnam.
- **Canonical source:** [Durian geographic survey](<Durian geographic survey.md>) and [Durian signage](<Durian signage.md>).
- **Relevance:** [Official — usage]; [Project analysis] independent distribution and corpus bias.
- **Direction:** **Supports encoding.**
- **Current strength:** Moderate for a geographically repeated Southeast Asian convention; limited for prevalence, community size or independence because several territories have only one reviewed occurrence and venue types are uneven.
- **Exact proposition it can support:** The documented convention is not confined to one organization, venue or territory; it occurs in six ISO 3166-1 territories within Southeast Asia.
- **What it cannot establish:** A worldwide distribution, national prevalence, independent invention, broad public recognition, plain-text use, or absence of signs in unverified territories.
- **Contradictions or alternatives:** Shared tourism, transit and accommodation practices may diffuse an icon convention through copied artwork or common sign suppliers. Web-visible evidence is biased towards cities, hotels, tourists and indexed photographs.
- **Verification and rights:** The aggregate is verified against the occurrence register; its rights status is inherited item by item and does not make every underlying image reproducible.
- **Unresolved dependency:** Determine design lineage and independent commissioning in the private corpus; verify present leads only where they fill a material geographic or venue gap.
- **Likely proposal use:** A bounded map or concise usage-distribution statement, never an “all countries” claim or a popularity score.

### Form convergence and recognizability

- **Finding or class:** Signs and the preliminary inline examples suggest that designers can reduce durian to a compact spiky-fruit form, but the project has not yet coded invariant and variable features across the main corpus.
- **Canonical source:** [Durian signage](<Durian signage.md>), [Durian visual use](<Durian visual use.md>) and the unresolved questions in the [Durian overview](../Overview.md).
- **Relevance:** [Official — stability] and [Official — proposal material] comparison with similar characters; [Project analysis] representative-glyph independence and form variation.
- **Direction:** **Mixed.**
- **Current strength:** Preliminary. The examples make convergence plausible, but there is no complete form inventory, independence analysis or recognition study.
- **Exact proposition it can support:** At least some unrelated sign and design contexts use compact spiky forms intended or described as durian.
- **What it cannot establish:** The invariant glyph features, acceptable whole/cut-fruit range, recognition at small monochrome sizes, independence from colour or wording, or stability across communities.
- **Contradictions or alternatives:** A contextually labelled generic spiky fruit can be understood without a stable durian glyph; one exact silhouette may recur through copying rather than convergence.
- **Verification and rights:** Form observations can be checked in the registered sources, but several images remain reference-only and the private collection is unaudited.
- **Unresolved dependency:** Code the photo corpus for spikes, stalk, silhouette, cut/whole fruit, colour, overlay, wording and probable lineage; then test unlabelled small monochrome forms.
- **Likely proposal use:** Representative-glyph rationale and visual-comparison material only after the acceptable range and confusions are evidenced.

### Marketing and brand use

- **Finding or class:** Preliminary research records a university design project, a deployed transnational commercial wordmark and a United States trademark lead using durian-like forms.
- **Canonical source:** [Durian visual use](<Durian visual use.md>) and [V01–V03](Sources.md#marketing-and-inline-visual-use).
- **Relevance:** [Official — usage] only weakly; [Project analysis] visual conventionalization; [Counterargument] logo, illustration and brand-asset models.
- **Direction:** **Mixed.**
- **Current strength:** Limited supplementary evidence. The corpus is small, includes one student or university design project, and does not establish public comprehension independent of each brand.
- **Exact proposition it can support:** More than one designer has used a simplified durian-like form as a compact component of visual identity.
- **What it cannot establish:** A generic community convention, non-marketing use, textual semantics, public interchange or an encoding gap.
- **Contradictions or alternatives:** Marketing relies on product context and can intentionally create novel artwork; the relevant identity may be the brand, not the fruit unit.
- **Verification and rights:** V01 and V02 supply direct design rationales; V03 remains a secondary lead pending current official trademark verification. Branding is generally reference-only unless permission or a destination-specific non-free-use review permits reproduction.
- **Unresolved dependency:** Prefer evidence of independent sustained deployment and unaided comprehension over additional portfolio concepts.
- **Likely proposal use:** At most a short supplementary form-convergence example; omit weak or redundant marketing material.

### Inline letter or punctuation substitution

- **Finding or class:** A durian form replaces LATIN CAPITAL LETTER O (`U+004F`) in “Ducoff”; a durian-like star functions as FULL STOP (`U+002E`) in “Forbidden”; and a trademark lead combines a spiky band with LATIN SMALL LETTER D (`U+0064`).
- **Canonical source:** [Durian visual use](<Durian visual use.md>) and [V01–V03](Sources.md#marketing-and-inline-visual-use).
- **Relevance:** [Official — eligibility] character-versus-glyph distinction; [Project analysis] inline integration; [Counterargument] existing-character and logo explanations.
- **Direction:** **Supports non-encoding for the documented occurrences.**
- **Current strength:** Clear for the designers’ stated letter or punctuation roles in V01 and V02; weak as evidence of a broader durian textual convention.
- **Exact proposition it can support:** Durian-like art can remain recognizable at approximately character scale while functioning as a stylistic rendition or hybrid of already encoded characters.
- **What it cannot establish:** That the durian identity must be retained in the underlying text, that readers treat it as a separate character, or that letter and punctuation substitution is widespread.
- **Contradictions or alternatives:** The same occurrences modestly support recognizability, but ordinary `O`, full stop or `d` preserves their explicit textual role.
- **Verification and rights:** The V01 and V02 roles are stated by their designers; deployment is not established for V01, and the images remain subject to their own rights.
- **Unresolved dependency:** Find, if it exists, independent inline use where substituting the apparent underlying character loses information that users need to preserve.
- **Likely proposal use:** An adverse example distinguishing a durian character from brand glyphs, with only secondary value for small-scale recognizability.

### Production, trade, consumption and cultural importance

- **Finding or class:** The geographic survey documents a compact native range, market cultivation or active commercial projects in 19 territories, at-large consumption in 16, and a wider import and cultural footprint.
- **Canonical source:** [Durian geographic survey](<Durian geographic survey.md>), [Cultivation and native range](<Cultivation and native range.md>), [Consumption and fruit rankings](<Consumption and fruit rankings.md>) and [Diaspora import markets](<Diaspora import markets.md>).
- **Relevance:** [Project analysis] referent scope and geographic context only; it is not an official encoding criterion.
- **Direction:** **Contextual only.**
- **Current strength:** Often strong for the bounded biological, production or consumption fact, with source-specific qualifications; low relevance to whether a character exists or needs encoding.
- **Exact proposition it can support:** Durian is a biologically, commercially and culturally significant fruit with a centre in Southeast Asia and substantial distribution beyond it.
- **What it cannot establish:** Symbol use, recognition, community use of a character, form stability, public-interchange need or entitlement to category completion.
- **Contradictions or alternatives:** A socially important object can be named in ordinary language and depicted by images without having an independent plain-text symbol.
- **Verification and rights:** The survey distinguishes official statistics, scholarly or specialist evidence, supported inferences and leads. Most facts can be cited without reproducing third-party visual assets.
- **Unresolved dependency:** Recheck figures before formal publication, but do not expand this background unless a specific identity or user-community question requires it.
- **Likely proposal use:** One concise context paragraph and support for the broad popular referent; detailed ranks and trade tables are unnecessary to the encoding decision.

### Contemporary fruit and emoji repertoire

- **Finding or class:** At Unicode 17.0.0, the bounded review finds 29 contemporary emoji-capable fruit-referent characters and the RGI lime sequence 🍋‍🟩 (`U+1F34B U+200D U+1F7E9` — LEMON, ZERO WIDTH JOINER, LARGE GREEN SQUARE). No durian representation was found in that corpus.
- **Canonical source:** [Existing Unicode characters with fruit referents](<../../../Research/Existing Unicode characters with fruit referents.md>) and the versioned Unicode 17.0 and Emoji 17.0 source families [U19](<../../../Research/Sources.md#u19>) and [U20](<../../../Research/Sources.md#u20>).
- **Relevance:** [Official — eligibility] bounded existing-representation check; [Project analysis] character/emoji route and comparison-set selection.
- **Direction:** **Mixed.**
- **Current strength:** Strong, reproducible and versioned for the defined repertoire; limited for the wider encoding decision.
- **Exact proposition it can support:** Within the Unicode 17.0.0 fruit-referent corpus, durian is not represented and belongs to a readily intelligible contemporary fruit comparison neighbourhood.
- **What it cannot establish:** Plain-text need, a new-character precedent, distinctiveness, popularity or a right to fill a repertoire gap.
- **Contradictions or alternatives:** Lime shows that a fruit subject can be represented by a standardized sequence; it neither represents durian nor establishes that a sequence or separate character is appropriate for durian. Emoji representation and the character-proposal route answer distinct selection questions.
- **Verification and rights:** The result is based on versioned official Unicode data and has no dependency on reproducing third-party sign photographs.
- **Unresolved dependency:** Complete the Durian-specific existing-character and sequence analysis and recheck the then-current Unicode repertoire before any submission.
- **Likely proposal use:** A short, carefully bounded comparison and no-existing-fruit-referent statement; avoid a long category-completion inventory.

### Legacy terminal fruit symbols

- **Finding or class:** APPLE SYMBOL 𜺽 (`U+1CEBD`), CHERRY SYMBOL 𜺾 (`U+1CEBE`) and STRAWBERRY SYMBOL 𜺿 (`U+1CEBF`) are explicitly non-emoji characters disunified to preserve a legacy terminal source set.
- **Canonical source:** [Existing Unicode characters with fruit referents](<../../../Research/Existing Unicode characters with fruit referents.md>) and [U21](<../../../Research/Sources.md#u21>)–[U23](<../../../Research/Sources.md#u23>).
- **Relevance:** [Project analysis] repertoire comparison and character-versus-emoji distinction; possible but weak precedent argument.
- **Direction:** **Contextual only.**
- **Current strength:** Strong for their encoded identity and source-set history; weak as an analogy to Durian.
- **Exact proposition it can support:** Unicode can encode non-emoji fruit-referent symbols where a legacy source-encoding and disunification requirement establishes the interchange need.
- **What it cannot establish:** A modern generic fruit pictogram convention or a comparable legacy interchange requirement for Durian.
- **Contradictions or alternatives:** Their exceptional source-set history is a reason not to generalize them into a rule that any fruit merits encoding.
- **Verification and rights:** The non-emoji labels are at `U+1CEBD`–`U+1CEBF` in the Unicode 17.0 Symbols for Legacy Computing Supplement chart; the Miscellaneous Symbols and Pictographs chart supplies the reciprocal fruit-character cross-references, and L2/23-252 supplies the source-set and disunification history.
- **Unresolved dependency:** None likely to change the Durian decision unless a comparable durian source encoding is discovered.
- **Likely proposal use:** Usually omit; retain only for a narrowly qualified explanation that character encoding and emoji presentation are separable.

### Historical Aegean fruit or commodity signs

- **Finding or class:** The bounded review records nine Linear A or Linear B fruit, grain or commodity signs under its inclusion rule.
- **Canonical source:** [Existing Unicode characters with fruit referents](<../../../Research/Existing Unicode characters with fruit referents.md>) and [U22](<../../../Research/Sources.md#u22>).
- **Relevance:** [Project analysis] repertoire comparison and historical counterexample control.
- **Direction:** **Contextual only.**
- **Current strength:** Strong for the historical sign identifications within Unicode; very weak as an analogy to a modern Durian symbol.
- **Exact proposition it can support:** Unicode contains historical non-phonetic commodity signs whose identities and interchange needs arise within specific scripts and source traditions.
- **What it cannot establish:** Modern durian usage, recognizability, stability or plain-text need.
- **Contradictions or alternatives:** Their historical notational functions are materially different from a contemporary physical-sign pictogram and should not be treated as category precedent.
- **Verification and rights:** Verified from Unicode 17.0 Chapter 8’s Linear B discussion and the code-chart entries for `U+1001B`, `U+1008E`–`U+10090`, `U+10093`, `U+1061D`, and `U+10649`–`U+1064B`.
- **Unresolved dependency:** None likely to change the present decision.
- **Likely proposal use:** Omit unless needed to rebut an overbroad claim about “all fruit symbols”.

### Previous emoji submissions and committee history

- **Finding or class:** The public record supports one expired 2017 item, one 2018 item ultimately recorded as a duplicate, and one standalone 2022 decline whose item-specific reason has not been recovered.
- **Canonical source:** [Unicode history and proposal status](<Unicode history and proposal status.md>) and the exact current or archived source record cited for each event.
- **Relevance:** [Official — proposal material] prior related documents where identifiable; [Project analysis] route distinction and adverse-history reconstruction.
- **Direction:** **Contextual only.**
- **Current strength:** Strong for the documented chronology and limits; weak for any inference about the merits of the current character case.
- **Exact proposition it can support:** Durian has prior emoji-process history, but the record does not support describing it as three independent adverse merits decisions.
- **What it cannot establish:** Why the 2022 submission was declined, what evidence any submission contained, that a character proposal was rejected, or that previous intermediate treatment endorsed Durian.
- **Contradictions or alternatives:** “Expired”, “duplicate”, “needs modification” and “added to larger set” were different workflow states. The undisclosed 2022 reason could be relevant, but the present record cannot supply it.
- **Verification and rights:** The chronology is reconstructed from official documents, current and archived status sheets and period guidance. No recovered proposal text is available to reproduce or assess.
- **Unresolved dependency:** Author-held proposals or response letters, a new public archive, and official clarification of emoji re-review timing.
- **Likely proposal use:** A concise, neutral related-history note if the specific documents are relevant; never use the missing reason as either favourable or adverse evidence.

### Visual distinctiveness and possible confusion

- **Finding or class:** A 2015 Unicode Mail List exchange raised possible small monochrome confusion with lychee, while other participants considered durian distinctive and contrasted sharp durian tips with round lychee tips.
- **Canonical source:** [Unicode history and proposal status](<Unicode history and proposal status.md>) and the later 2015 mail-list exchange [U19](Sources.md#u19), supplemented only cautiously by [Durian visual use](<Durian visual use.md>).
- **Relevance:** [Official — proposal material] comparison with visually similar characters; [Project analysis] recognizability and confusability.
- **Direction:** **Mixed.**
- **Current strength:** Weak and preliminary. The exchange identifies a real question and possible discriminating feature but is not a recognition study or committee finding.
- **Exact proposition it can support:** Durian–lychee confusion at small monochrome sizes was publicly raised and disputed; spike shape is a plausible feature to test.
- **What it cannot establish:** Reliable recognition, a stable glyph range, confusion rates, safety implications or distinction from every other spiky fruit.
- **Contradictions or alternatives:** Wording, colour, a stalk or cultural familiarity may drive recognition more than the outline; a generic spiky fruit may be sufficient inside a labelled sign.
- **Verification and rights:** The discussion is publicly verifiable; image-based testing remains subject to the source assets’ rights and the private-corpus protocol.
- **Unresolved dependency:** Systematic visual comparison and unlabelled user testing after representative forms are selected from an independently coded corpus.
- **Likely proposal use:** A balanced visually similar-character section only after empirical or well-documented comparative evidence replaces the informal exchange.

### Plain-text public-interchange need

- **Finding or class:** No reviewed project evidence currently identifies users who enter, exchange, quote, search, index, parse or archive a durian symbol as plain text independently of sign artwork or brand design.
- **Canonical source:** The strongest non-encoding model and unresolved questions in the [Durian overview](../Overview.md), tested under [Character identity and encoding analysis](<../../../Methods/Character identity and encoding analysis.md>).
- **Relevance:** [Official — interchange].
- **Direction:** **Supports non-encoding provisionally.**
- **Current strength:** Strong as a gap in the present case and therefore as a reason not to draft or submit a proposal; it is not evidence that such workflows do not exist.
- **Exact proposition it can support:** The current research has not yet demonstrated the official public-interchange criterion for a Durian character.
- **What it cannot establish:** That no community has such a need, that future evidence cannot satisfy it, or that images and higher-level systems are adequate for every possible workflow.
- **Contradictions or alternatives:** Repeated functional use suggests a stable semantic target may exist, but displayed communication is not the same as interchanging the target as plain text.
- **Verification and rights:** This is a bounded negative finding from the reviewed project record; it requires an explicit search boundary in any later publication. Rights are not the cause of the analytical gap, although private evidence has not yet been assessed.
- **Unresolved dependency:** After the photo audit, interview operators, sign-system designers, relevant users and text-system implementers; name sender, recipient, systems, operations and concrete loss.
- **Likely proposal use:** None until affirmative workflow evidence exists. If a bounded audit still finds no loss, this becomes a central reason not to submit.

### Existing characters and ordinary text

- **Finding or class:** The Unicode 17.0.0 fruit-referent review found no character representing durian. Ordinary text can write “durian” or state a rule, while the documented inline designs are directly expressible with LATIN CAPITAL LETTER O (`U+004F`), FULL STOP (`U+002E`) or LATIN SMALL LETTER D (`U+0064`) according to their stated roles.
- **Canonical source:** [Existing Unicode characters with fruit referents](<../../../Research/Existing Unicode characters with fruit referents.md>), [Durian visual use](<Durian visual use.md>) and the [Durian overview](../Overview.md).
- **Relevance:** [Official — eligibility] and equivalence; [Official — interchange] alternative adequacy.
- **Direction:** **Mixed.**
- **Current strength:** Strong within the bounded fruit repertoire and for the known brand cases; incomplete as a standalone matrix of every semantically or visually plausible Unicode character.
- **Exact proposition it can support:** No Unicode 17.0 fruit-referent character reviewed by the project denotes durian, and existing characters adequately preserve the explicit textual role of the three preliminary inline-brand examples.
- **What it cannot establish:** That no existing character outside the bounded fruit corpus could be proposed as an equivalent, or that the word “durian” preserves every possible compact symbol function.
- **Contradictions or alternatives:** Lack of an equivalent removes one possible objection but does not create interchange need. Ordinary words may preserve the known rule even if they do not preserve source-faithful pictographic text.
- **Verification and rights:** Based on versioned Unicode data and directly documented design rationales; no sign-image reproduction is needed for the basic equivalence claims.
- **Unresolved dependency:** Produce a candidate-specific equivalence matrix covering semantic, glyph-range and behavioural candidates, then recheck the current Standard, pipeline and non-approval archive.
- **Likely proposal use:** Required eligibility and alternatives analysis, with explicit reasons for rejecting any plausible equivalent.

### Existing or possible character sequences

- **Finding or class:** The bounded Unicode 17.0 fruit and emoji review found no standardized character sequence representing durian. The lime sequence represents lime, not durian; ordinary letter sequences can spell the word and phrases can state the prohibition.
- **Canonical source:** [Existing Unicode characters with fruit referents](<../../../Research/Existing Unicode characters with fruit referents.md>), the [Durian overview](../Overview.md) and [Character identity and encoding analysis](<../../../Methods/Character identity and encoding analysis.md>).
- **Relevance:** [Official — eligibility] duplicate-representation rule; [Official — interchange] alternative adequacy.
- **Direction:** **Mixed.**
- **Current strength:** Strong for the absence of a durian representation in the bounded standardized fruit/emoji corpus; incomplete for every compositional, combining-mark, shaped or ad hoc sequence model.
- **Exact proposition it can support:** No currently reviewed standardized fruit or emoji sequence carries the durian identity, and 🍋‍🟩 is not a semantic substitute.
- **What it cannot establish:** Completion of the official sequence check, that a visually similar ad hoc sequence represents the same abstract entity, or that spelling “durian” is inadequate in a named workflow.
- **Contradictions or alternatives:** A standardized sequence can represent a subject without a separate character, as lime demonstrates; an invented visual approximation does not automatically carry the required semantics.
- **Verification and rights:** The standardized-sequence finding is reproducible from official versioned Unicode data.
- **Unresolved dependency:** Write and test every plausible candidate sequence by literal form, code points, names, semantics, normalization, fallback, searching and segmentation where material.
- **Likely proposal use:** A concise official-eligibility analysis only after the explicit candidate-specific sequence test is complete.

### Images, words, metadata and higher-level systems

- **Finding or class:** Exact sign or brand appearance can be preserved as an image or icon asset; the known rules can be expressed in words; metadata, markup or a sign-management system can associate the asset with a category or prohibition; private-use or icon-font mappings can serve coordinated closed systems.
- **Canonical source:** The strongest non-encoding model in the [Durian overview](../Overview.md) and the alternative-representation framework in [Character identity and encoding analysis](<../../../Methods/Character identity and encoding analysis.md>).
- **Relevance:** [Official — interchange]; [Counterargument] the documented need concerns appearance, layout or closed-system exchange rather than a new textual unit.
- **Direction:** **Supports non-encoding for presently documented functions.**
- **Current strength:** Strong fit to the observed physical signs and brand assets; untested against any demonstrated requirement to preserve the generic unit outside those artefacts.
- **Exact proposition it can support:** Every currently reviewed occurrence can be explained and stored as a sign, image, logo, ordinary text or higher-level composition without evidence of a lost plain-text Durian unit.
- **What it cannot establish:** That these alternatives remain adequate for an as-yet-undocumented public workflow involving input, quotation, search, indexing, parsing, accessibility or archival retrieval.
- **Contradictions or alternatives:** Independent users preserving the same semantic token across artwork, systems and operations would weaken this model; independent private mappings could expose an interoperability failure rather than settle it.
- **Verification and rights:** Image and logo assets carry item-specific rights; textual descriptions and metadata can often be published even when the source image is reference-only.
- **Unresolved dependency:** Test the strongest alternative in each real workflow, including what survives font loss, plain-text extraction, fallback and exchange without prior agreement.
- **Likely proposal use:** The principal counterargument and alternatives section; a convincing proposal would need to show a concrete loss rather than dismiss images as inconvenient.

### Pending private photo-corpus audit

- **Finding or class:** The project owner’s existing private Durian sign-photo collection has not yet been catalogued and assessed in the canonical research record.
- **Canonical source:** [Durian overview](../Overview.md), [Durian geographic survey](<Durian geographic survey.md>) and candidate [AGENTS.md](../AGENTS.md).
- **Relevance:** [Project analysis] provenance, independence, form stability, semantic boundary and falsification; indirectly [Official — usage] and [Official — stability].
- **Direction:** **Contextual only until audited.**
- **Current strength:** None for the unseen contents. The collection’s existence establishes a research dependency, not favourable evidence.
- **Exact proposition it can support:** A potentially decision-relevant body of evidence remains outside the reviewed corpus and should be audited before broad new image collection.
- **What it cannot establish:** Additional countries, independent usage, form convergence, recognizability, rights clearance or support for encoding.
- **Contradictions or alternatives:** The audit may reveal broad independent convergence, or chiefly copied artwork, repeated visits to the same signs, context-dependent generic fruit images or rights restrictions.
- **Verification and rights:** Preserve originals privately. [Contributor rights](<Contributor rights.md>) records Sandy Patch’s CC BY-SA 4.0 permission for photographs already shared within the stated scope, but each file still needs provenance, item-level linkage, suitability and publication review.
- **Unresolved dependency:** Create the private catalogue and safe public evidence records; code venue, date, wording, form, composition, independence, creator and separate rights, privacy and publication status.
- **Likely proposal use:** Only audited, independently probative and appropriately cleared items should enter a proposal evidence set.

### Rights-cleared versus reference-only evidence

- **Finding or class:** Evidential value and permission to reproduce are separate. Two current Wikimedia sign examples have identifiable Creative Commons reuse routes; most other located sign and brand images are licensed stock, rights-unverified or reference-only. A contributor permission record exists but does not replace item-level review.
- **Canonical source:** [Durian signage](<Durian signage.md>), [Durian visual use](<Durian visual use.md>), [Contributor rights](<Contributor rights.md>) and [Evidence storage and publication](<../../../Project/Evidence storage and publication.md>).
- **Relevance:** [Project analysis] verification, auditability and proposal publication; not an official encoding criterion.
- **Direction:** **Contextual only.**
- **Current strength:** Strong for the present rights-status distinctions; incomplete for the unaudited private corpus and any future derivative or destination-specific use.
- **Exact proposition it can support:** Some current occurrences may be cited as evidence but cannot presently be reproduced, while the Singapore and older Thai Wikimedia photographs have documented reuse routes subject to their exact attribution and share-alike terms.
- **What it cannot establish:** That rights-cleared evidence is stronger on the merits, that reference-only evidence is false, or that a low-resolution reproduction is automatically lawful.
- **Contradictions or alternatives:** A reference-only photograph may be highly probative, while a cleared image may be old, atypical or redundant. Clearance should shape publication selection, not evidence weighting.
- **Verification and rights:** Apply item-specific licence, permission, privacy, stock and derivative records. Keep restricted originals and private catalogues outside public Git history; publish safe evidence records where possible.
- **Unresolved dependency:** Complete item-level rights and provenance review after the corpus audit and seek permission or commission new photographs only for material evidential gaps.
- **Likely proposal use:** Reproduce a small, representative, independently probative and rights-cleared set; cite other sources without reproducing their images where appropriate.

## Research-prioritization consequence

Later work should follow the decision dependencies rather than the easiest available source volume:

1. **Audit before expanding.** Catalogue the private corpus, establish provenance and independence, code form and composition, and separate rights from evidential value.
2. **Resolve the entity.** Use the audited corpus to decide whether a generic base durian unit persists across renderings or whether the complete sign artefact is the stable communicative object.
3. **Test interchange with named users.** Interview operators, designers, wayfinding specialists and relevant users about actual systems and operations; record both successful alternatives and concrete losses.
4. **Complete equivalence and sequence checks.** Only once the identity and workflow are specific should the project test existing characters, explicit sequences, words, images, metadata, fonts, private mappings and higher-level protocols against that requirement.
5. **Collect only decision-bearing gaps.** Commission or seek rights clearance for sign evidence that fills a missing venue, territory, form, independence or workflow cell. Do not accumulate images or contextual statistics as an implicit vote.

The current map therefore supports **continued research and deferral**, not proposal drafting: the usage case is plausible, but the identity, representative-glyph range and official interchange criterion remain unresolved.

## Decision summary

- **Strongest current support:** Repeated functional durian-prohibition signage with the same regulatory meaning is traceably documented across six Southeast Asian territories and several venue types. This is the best evidence that the referent participates in a stable visual convention rather than appearing only as decoration.
- **Strongest current weakness:** The project has not demonstrated a public need to preserve and interchange a generic durian unit in plain text. Every reviewed occurrence can still be explained as a physical sign, image, logo, existing letter or punctuation mark, ordinary wording or higher-level composition.
- **Most consequential unresolved dependency:** The private photo-corpus audit. It can materially change the assessments of independence, copying, form convergence, semantic boundary, recognizability and publication readiness, and it is the necessary evidence base for a proportionate interchange and counterargument audit.
- **Research that now appears lower value:** Further production, trade or consumption accumulation; additional fruit-category enumeration; more speculative portfolio branding; renewed bounded searches for the same unrecovered emoji submissions without a new archive or contact; broad sign collection before the private corpus reveals actual gaps; and historical or legacy comparisons without a comparable source-encoding requirement.
- **Next evidence that could genuinely change the decision:** A documented workflow in which independent sign operators, designers or users treat varied durian forms as the same reusable semantic token and need to enter, exchange, quote, search, index, parse or preserve it outside the source artwork, with a concrete loss under words, existing characters or sequences, images, metadata and higher-level systems. The contrary result—a well-bounded audit showing artwork-dependent icons and adequate alternatives—would genuinely change the decision towards non-encoding.
