---
title: Evidence storage and publication
last_reviewed: 2026-07-31
tags:
  - project
  - governance
  - evidence
  - rights
---

This policy separates evidential value from rights, privacy, publication, and storage decisions. It applies to originals, derivatives, metadata, correspondence, and proposal snapshots. The three zones describe where a particular file or record may be held; a private original and its safe public evidence record can therefore occupy different zones.

Classify material before it enters public Git history. A source being visible online, locally available, purchased, or technically storable does not make it publishable. [LICENCE.md](../LICENCE.md) governs the project’s blanket licence; third-party terms and item-specific permissions remain controlling for their material.

## Risk posture and decision standard

The project uses a source-sensitive managed-risk standard with a rebuttable presumption in favour of publishing authentic, well-provenanced public-interest evidence. The objective is to advance open research, open standards, freedom of information, and common human knowledge while respecting creators, copyright, licences, safety, and proportionate harm reduction. An informed, correctable decision is sufficient; zero residual risk is not the objective.

Public-world evidence—including publicly displayed signs, logos, packaging, property, and incidental people—is normally eligible for truthful descriptive, documentary, critical, or other editorial use. A non-free asset or absent model or property release does not by itself require private-only treatment. Private or unpublished material, private-message and account-derived content, sensitive people or settings, and contract-bound source files receive closer review because their provenance, privacy, access, or agreed-use conditions differ materially. Closer review is not a presumption against publication.

Publish when:

- the project has a licence, permission, or other documented legal basis covering the use;
- the material meaningfully supports a research claim, identification, comparison, criticism, or explanation and is used in relevant context rather than as decoration, advertising, merchandising, or an endorsement;
- attribution, notices, modification limits, special restrictions, and access conditions can be met;
- the presentation is accurate and does not materially misrepresent, defame, or expose a person to disproportionate privacy or safety harm; and
- the asset is incorporated into the research work rather than offered as a reusable substitute for the source asset.

The absence of a release can limit promotional or other commercial exploitation without prohibiting every editorial use. Likewise, the fact that a newspaper, magazine, research platform, or standards body is corporate-owned, revenue-generating, or professionally produced does not by itself make a descriptive use advertising or merchandising. Classify the function and context of the use under the actual governing terms.

Prefer public-domain, openly licensed, permissioned, or otherwise more reusable material when it is genuinely equivalent. A generic substitute is not equivalent when the particular artefact’s appearance, occurrence, provenance, age, location, or context is itself evidence. Use fit-for-purpose quality and context: enough resolution, extent, and surrounding detail for a reader to inspect the claim, without copying material that adds no research value or unnecessarily substitutes for the source.

English Wikipedia’s [image-use policy](https://en.wikipedia.org/wiki/Wikipedia:Image_use_policy) and [non-free-content policy](https://en.wikipedia.org/wiki/Wikipedia:Non-free_content), checked on 31 July 2026, inform the project’s attention to provenance, contextual significance, market substitution, privacy, and clear rights labelling. Wikipedia deliberately applies rules stricter than United States fair use to maximize unrestricted downstream reuse. This smaller research project does not adopt Wikipedia’s absolute no-free-equivalent rule, routine low-resolution presumption, ten-part test, per-use rationale, or namespace controls.

Where United States fair use is the basis, apply the purpose, nature, amount, and market-effect factors summarized by the [United States Copyright Office](https://www.copyright.gov/fair-use/more-info.html), checked on 31 July 2026. The Copyright Office identifies research, scholarship, criticism, and commentary as potentially qualifying purposes and rejects fixed percentage or amount rules. Other jurisdictions may provide different exceptions.

Escalate when the terms or legal basis are materially ambiguous; the proposed use is promotional, out of context, or a plausible market substitute; an alteration could change meaning; a private or restricted setting is involved; the material concerns a child, vulnerable person, allegation, medical or other sensitive context; precise personal or location data are unnecessary; or a complaint, special restriction, or jurisdiction-specific issue creates a concrete concern. Record only the reason and decision needed for collaborators to understand the result. Do not require extra permission merely because third-party content is depicted when no governing term, applicable rule, or material contextual risk calls for it.

## Zone 1: public repository material

The public repository may contain:

- original project text and assets intended for distribution under the project licence;
- public-domain, Creative Commons, permission-cleared, or otherwise distributable evidence when the exact rights basis and every applicable attribution, adaptation, notice, and share-alike duty are recorded and met;
- third-party material incorporated into a permitted editorial, documentary, critical, or other limited use, with its own rights notice and without representing it as a reusable project asset;
- metadata, citations, and evidence records that are safe to publish;
- public derivatives covered by an item-specific or scoped publication decision; and
- exact submitted-proposal snapshots and other intentionally public release artefacts.

“Rights-cleared” is specific to the intended publication and does not mean that an item becomes project-owned or covered by CC BY-SA 4.0. Third-party material must retain its own rights notice. A public citation may remain publishable even when downloading or redistributing the cited asset is not.

Anything committed here should be treated as publicly and durably disclosed through the current tree, Git history, clones, caches, and release copies.

The project is responsible for obtaining and observing the rights needed for its own acquisition, storage, modification, publication, submission, and other authorized uses. It must identify third-party material and its controlling terms accurately, preserve required notices, and avoid purporting to grant rights it does not hold. Once an item and its limits are sufficiently distinguished for a reasonable recipient to make an informed decision, an independent downstream party’s unauthorized extraction, relicensing, or other misuse is that party’s responsibility rather than a project rights-clearance obligation. This boundary does not excuse a restriction on the project’s own distribution, a representation made in a submission agreement, or a rights notice known to be materially misleading.

## Zone 2: private evidence archive

The private archive holds material that may be inspected for research but is not approved for public redistribution or disclosure, including:

- source-quality non-free originals, rights-unknown copies, and other files retained for research but not selected for public use;
- restricted stock and other account-licensed assets;
- private correspondence, permission evidence, purchase or subscription records, and account-linked licence documents;
- unpublished field material;
- precise locations, contact details, personally identifying information, and other sensitive data; and
- private catalogues that map stable evidence identifiers to storage paths.

Keep this archive outside the public repository and its Git history, with access, retention, backup, and deletion controls appropriate to the material. A Git ignore rule is an accident-prevention aid, not a confidentiality boundary, so an external private store is preferable to an ignored folder inside the public checkout.

No private file, private catalogue, or sensitive metadata should ever be committed to the public repository, whether as an ordinary Git object or a Git LFS object. A separately access-controlled private repository may use Git or Git LFS if useful, but those mechanisms do not supply the underlying rights, privacy, retention, or access decision.

## Zone 3: public evidence records for privately held material

When a public claim relies on a private asset, publish a safe evidence record wherever possible. Assign the original an opaque, stable, candidate-scoped identifier that does not encode a person’s name, a private location, or a rights conclusion. The public record refers to that identifier and says that the asset is privately held; a private catalogue maps it to the storage path. Do not publish the private path or an unnecessarily revealing source filename.

Record, at a proportionate level:

- a safe description of the item, the claim it supports, and whether support is observed, sourced, or inferential;
- creator or source, provenance and chain of custody, source reference, and relevant event, capture, acquisition, and access dates;
- country, locality, venue, and context at the most precise level safe to disclose;
- separate rights, privacy, and publication statuses, including the basis for any restriction;
- the exact licence or permission summary, required attribution, provider and stable asset ID, or non-free-reference status as applicable;
- identifiers for any public derivatives and their relationship to the private original; and
- file format, byte size, and a named checksum such as SHA-256 where they materially improve integrity checking and are safe to disclose.

Withhold or generalize a field when publication would expose confidential terms or create a material privacy, safety, contractual, or legal risk disproportionate to its research value. State the nature of the omission when that can be done safely, and qualify any public claim that cannot be audited beyond the resulting record.

## Originals and derivatives

Preserve an acquired or captured original unchanged and identify it independently of its filename. Do not require a separate identifier or process log for every mechanical working crop or resize. Give a public or decision-bearing derivative its own identifier when it changes the evidential meaning, rights or privacy analysis, redaction, attribution, or citation target; otherwise record the transformation at the scoped group or publication-package level. Link every published derivative to its original and describe the material transformation and purpose.

The publication decision must cover the derivative as used. It may do so through an existing scoped decision when the transformation and context are materially alike. A derivative does not acquire public status merely because it is smaller, transformed, or project-created. Conversely, a permitted public derivative may be stored in Zone 1 while its source original remains in Zone 2. Do not overwrite an original to make a correction or redaction.

## Licence, permission, and stock documentation

For Creative Commons and other licensed material, record the rights holder or credited creator, exact licence and version, source URL, acquisition or capture date, required attribution and notices, whether adaptation is permitted, share-alike or compatibility duties, and evidence of the terms available at acquisition.

For permission-cleared material, identify the covered evidence IDs and retain the primary permission record privately. The public summary should state the grantor, permitted uses and publication channels, adaptation and attribution conditions, duration or withdrawal terms if stated, and any unresolved limit without exposing private correspondence.

For stock and other account-licensed material, record the provider, stable asset ID, governing licence or agreement, acquisition date, permitted use, required attribution, restrictions, and intended use context. Keep account-linked, payment, order, purchase, subscription, and full licence evidence private. Access, purchase, subscription, or download does not establish permission to redistribute the supplied asset or place a restricted original in public Git or Git LFS. A single documented decision may cover a defined research work, its permitted derivatives, and its in-context distribution across named or licence-defined channels. Reassess a new use when its context, function, audience, transformation, access model, or governing terms change materially.

Record model- and property-release information when supplied or material to the intended use. Do not treat the lack of a release as a universal prohibition when the applicable licence or legal basis permits editorial or documentary use. Apply the same contextual approach to depicted signs, logos, trademarks, artwork, and recognizable property.

For source availability, acquisition planning, or provider-specific issues, additionally apply [Content sources and licensing](<Content sources and licensing.md>) and the relevant item-level evidence record.

A limited reproduction of non-free material for identification, criticism, commentary, research, or another legally recognized purpose may be approved under a destination- and jurisdiction-appropriate analysis. Use fit-for-purpose rather than automatically low resolution: retain enough quality and context to make the evidence auditable, while avoiding unnecessary extent or a reusable substitute for the source work. Attribution, cropping, or critical purpose is relevant but not automatic permission. Keep any source-quality copy private unless its distribution is independently permitted. For an obvious low-risk use, the ordinary provenance and publication fields are enough; record a fuller purpose, amount, market-effect, and uncertainty rationale only when the basis is materially ambiguous or consequential.

## Correction, withdrawal, and changed rights

Retain dated evidence of the licence or permission relied on. If a source changes its terms, a permission is disputed or withdrawn, a credible concern is raised, privacy risk emerges, or metadata proves wrong:

1. place future publication under review and update the public record’s status;
2. preserve the original and prior record revision privately where retention remains permitted;
3. publish a correction, replacement, or safe tombstone rather than silently changing the evidential history; and
4. reassess affected derivatives, websites, release packages, and proposal snapshots individually.

Do not assume that a later source-page change either cancels or preserves earlier rights; the recorded terms and circumstances require review. Do not silently revise a submitted snapshot. If its continued public distribution remains approved, retain it as the exact historical record and issue a correction or withdrawal as a new dated record. If continued distribution is no longer approved, document the removal and retain an exact private archival copy only where permitted.

If private or sensitive material enters public Git history accidentally, treat it as a disclosure incident: stop further publication, remove it from the current tree, assess whether history rewriting and downstream notification are required, and document the response without repeating the sensitive content. Rewriting cannot recall existing clones or caches and is not a substitute for keeping private material out of public history.

## Proposal submission freeze

At each submission, freeze the exact public package: editable source where intended for release, rendered submitted document, incorporated public derivatives, attribution and rights notices, cited public evidence-record revisions, submission date and version or assigned document number, and integrity checksums for the package. Do not silently update that snapshot after submission.

At the same time, freeze a private support manifest, where retention is permitted, containing the stable identifiers and checksums of privately held originals relied on, the relevant permission and licence evidence, stock acquisition records, and any non-free-use review decision. The manifest proves what was reviewed at submission time; it does not move the restricted files into the public package.

## Role of Git LFS

Git LFS is only a storage and transfer mechanism:

- in Zone 1, it may store large public, distributable binaries when repository size, hosting, cost, and retrieval needs justify it;
- in Zone 2, it may be used only within a separately secured private system after access and rights decisions have already been made; and
- in Zone 3, the normally small public records belong in ordinary Git, although a rights-cleared public derivative may independently qualify for Zone 1 LFS storage.

An LFS pointer in a public repository still leads to content intended for public retrieval. LFS must never be treated as a rights, confidentiality, privacy, or publication boundary. Configure tracking only when actual public files and operational needs justify a rule; do not choose file-type rules in anticipation of an empty archive.

## Incremental adoption

Keep organization and review proportional to the collection. Create a candidate evidence record, private catalogue, or asset directory only when material needs it; this policy does not require an empty directory tree, a universal table schema, or a legal essay for an ordinary use. Inventory and classify already held material before moving, publishing, or batch-importing it. Use scoped batch decisions for materially similar items, and review only ambiguous or consequential cases with the project owner.
