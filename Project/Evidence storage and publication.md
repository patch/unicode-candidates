---
title: Evidence storage and publication
last_reviewed: 2026-07-28
tags:
  - project
  - governance
  - evidence
  - rights
---

This policy separates evidential value from rights, privacy, publication, and storage decisions. It applies to originals, derivatives, metadata, correspondence, and proposal snapshots. The three zones describe where a particular file or record may be held; a private original and its safe public evidence record can therefore occupy different zones.

Classify material before it enters public Git history. A source being visible online, locally available, purchased, or technically storable does not make it publishable. [LICENCE.md](../LICENCE.md) governs the project’s blanket licence; third-party terms and item-specific permissions remain controlling for their material.

## Zone 1: public repository material

The public repository may contain:

- original project text and assets intended for distribution under the project licence;
- public-domain, Creative Commons, permission-cleared, or otherwise distributable evidence when the exact rights basis and every applicable attribution, adaptation, notice, and share-alike duty are recorded and met;
- metadata, citations, and evidence records that are safe to publish;
- public derivatives whose publication has been separately assessed; and
- exact submitted-proposal snapshots and other intentionally public release artefacts.

“Rights-cleared” is specific to the intended publication and does not mean that an item becomes project-owned or covered by CC BY-SA 4.0. Third-party material must retain its own rights notice. A public citation may remain publishable even when downloading or redistributing the cited asset is not.

Anything committed here should be treated as publicly and durably disclosed through the current tree, Git history, clones, caches, and release copies.

## Zone 2: private evidence archive

The private archive holds material that may be inspected for research but is not approved for public redistribution or disclosure, including:

- non-free originals and rights-unknown copies retained where lawful;
- restricted Shutterstock and other stock assets;
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
- the exact licence or permission summary, required attribution, stock provider and asset ID, or non-free-reference status as applicable;
- identifiers for any public derivatives and their relationship to the private original; and
- file format, byte size, and a named checksum such as SHA-256 where they materially improve integrity checking and are safe to disclose.

Withhold or generalize a field when publication would expose a person, a sensitive location, confidential terms, or another avoidable risk. State the nature of the omission when that can be done safely, and qualify any public claim that cannot be audited beyond the resulting record.

## Originals and derivatives

Preserve an acquired or captured original unchanged and identify it independently of its filename. Give every crop, resize, annotation, redaction, transcription image, and other derivative its own identifier; link it to the original and record who made it, when, by what material transformation, and for what purpose.

Rights and privacy must be assessed for both files. A derivative does not acquire public status merely because it is smaller, transformed, or project-created. Conversely, a permitted public derivative may be stored in Zone 1 while its source original remains in Zone 2. Do not overwrite an original to make a correction or redaction.

## Licence, permission, and stock documentation

For Creative Commons and other licensed material, record the rights holder or credited creator, exact licence and version, source URL, acquisition or capture date, required attribution and notices, whether adaptation is permitted, share-alike or compatibility duties, and evidence of the terms available at acquisition.

For permission-cleared material, identify the covered evidence IDs and retain the primary permission record privately. The public summary should state the grantor, permitted uses and publication channels, adaptation and attribution conditions, duration or withdrawal terms if stated, and any unresolved limit without exposing private correspondence.

For stock material, record the provider and stable asset ID publicly when safe. Keep account, order, download, subscription, and full licence evidence privately where it contains confidential or personal information. Access under a Shutterstock or other stock licence is not permission to place the supplied original in a public Git or LFS store. Assess the exact licensed use, any editorial limitation, the proposal or website destination, and redistribution restrictions before publishing a permitted derivative or incorporation.

### Shutterstock-specific controls

The current [Shutterstock Terms of Service and licence agreements](https://www.shutterstock.com/license), effective 19 January 2026 and accessed 28 July 2026, state that amendments apply to prospective purchases. Shutterstock’s [licence history](https://www.shutterstock.com/license-history), accessed 28 July 2026, says that the terms in force at purchase govern an existing purchase and, for an automatically renewed subscription or pack, the terms in force on the most recent payment date govern downloaded content. “Shutterstock-licensed” is therefore not a sufficient rights record, and the current terms are an operational reference rather than a substitute for the agreement governing a particular acquisition.

For each Shutterstock asset:

- preserve the asset ID, contributor or agency, content class, exact licence and product or plan, licensee, account or seat entitlement, purchase and latest payment or renewal dates, licensing and download dates, order or invoice, and the terms in force for the download;
- distinguish a date observed in an invoice or account record from one inferred from a plan expiry. For an inferred date, record the calculation, confidence, and whether the displayed time zone is known, then replace or confirm it when primary billing evidence becomes available;
- preserve the item page and attached metadata, including an editorial designation, special restrictions, stated model or property releases, required credit, use limits, and any need for additional clearance arising from modification or context;
- map every intended proposal, website, social-media, or other publication to a permitted use. Treat an authorized incorporation into a final work separately from prohibited resale, redistribution, access, sharing, or transfer of the supplied content;
- restrict access to the licensed file and its use to people covered by the account entitlement. Do not infer that a plan is Unlimited merely because it is a subscription: apply Unlimited-plan restrictions only when the governing product and terms identify it as Unlimited. Separately record the licensed context for Editorial content and any actual Unlimited-plan content, because the current terms make each subject to single-use rules and prohibit a new Unlimited-plan use after expiry without a further qualifying download;
- apply the required adjacent contributor and Shutterstock credit to publishing, commentary, and other editorial contexts. Editorial content always requires credit under the current terms and may carry additional context, cover, medium, print-run, or geographic restrictions;
- do not infer that a video licence permits a still image. The current terms restrict stills derived from Video to specified in-context promotion of a derivative work, while watermarked low-resolution Comp Video is for evaluation and cannot enter public or final material; and
- do not use licensed content or a derivative as artificial-intelligence or machine-learning training data. Use an AI-enabled editing tool only where it does not train on the content or derivative and the other licence conditions remain satisfied.

If the licensee receives the notice described in the current terms, or learns that content is subject to a threatened or actual claim covered by that provision, the removal obligation takes precedence over archival retention: remove the content from systems and storage devices and cease future use where possible. Preserve a private incident record containing the asset ID, prior checksum, governing terms, notice or discovery, deletion date, affected uses, and replacement decision, but not the removed content.

A proposed low-resolution use of non-free material for identification, criticism, or commentary remains an item- and destination-specific fair-use or fair-dealing review question. Low resolution, cropping, attribution, or critical purpose is not automatic permission. Keep the original private; document the necessity, extent, context, rights uncertainty, and review outcome before any public reproduction.

## Correction, withdrawal, and changed rights

Retain dated evidence of the licence or permission relied on. If a source changes its terms, a permission is disputed or withdrawn, privacy risk emerges, or metadata proves wrong:

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

Keep organization proportional to the collection. Create a candidate evidence record, private catalogue, or asset directory only when material needs it; this policy does not require an empty directory tree or a universal table schema. Inventory and classify already held material before moving, publishing, or batch-importing it, and review ambiguous cases with the project owner.
