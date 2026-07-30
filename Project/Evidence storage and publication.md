---
title: Evidence storage and publication
last_reviewed: 2026-07-30
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

The project is responsible for obtaining and observing the rights needed for its own acquisition, storage, modification, publication, submission, and other authorized uses. It must identify third-party material and its controlling terms accurately, preserve required notices, and avoid purporting to grant rights it does not hold. Once an item and its limits are sufficiently distinguished for a reasonable recipient to make an informed decision, an independent downstream party’s unauthorized extraction, relicensing, or other misuse is that party’s responsibility rather than a project rights-clearance obligation. This boundary does not excuse a restriction on the project’s own distribution, a representation made in a submission agreement, or a rights notice known to be materially misleading.

## Zone 2: private evidence archive

The private archive holds material that may be inspected for research but is not approved for public redistribution or disclosure, including:

- non-free originals and rights-unknown copies retained where lawful;
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

Withhold or generalize a field when publication would expose a person, a sensitive location, confidential terms, or another avoidable risk. State the nature of the omission when that can be done safely, and qualify any public claim that cannot be audited beyond the resulting record.

## Originals and derivatives

Preserve an acquired or captured original unchanged and identify it independently of its filename. Give every crop, resize, annotation, redaction, transcription image, and other derivative its own identifier; link it to the original and record who made it, when, by what material transformation, and for what purpose.

Rights and privacy must be assessed for both files. A derivative does not acquire public status merely because it is smaller, transformed, or project-created. Conversely, a permitted public derivative may be stored in Zone 1 while its source original remains in Zone 2. Do not overwrite an original to make a correction or redaction.

## Licence, permission, and stock documentation

For Creative Commons and other licensed material, record the rights holder or credited creator, exact licence and version, source URL, acquisition or capture date, required attribution and notices, whether adaptation is permitted, share-alike or compatibility duties, and evidence of the terms available at acquisition.

For permission-cleared material, identify the covered evidence IDs and retain the primary permission record privately. The public summary should state the grantor, permitted uses and publication channels, adaptation and attribution conditions, duration or withdrawal terms if stated, and any unresolved limit without exposing private correspondence.

For stock and other account-licensed material, record the provider, stable asset ID, governing licence or agreement, acquisition date, permitted use, required attribution, restrictions, and intended publication destination. Keep account-linked, payment, order, purchase, subscription, and full licence evidence private. Access, purchase, subscription, or download does not establish permission to redistribute the supplied asset or place a restricted original in public Git or Git LFS. Assess each derivative, incorporation, and publication destination separately against the governing terms.

For source availability, acquisition planning, or provider-specific issues, additionally apply [Content sources and licensing](<Content sources and licensing.md>) and the relevant item-level evidence record.

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
