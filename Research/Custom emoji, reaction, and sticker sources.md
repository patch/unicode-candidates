---
title: Custom emoji, reaction, and sticker sources
last_reviewed: 2026-07-29
tags:
  - shared-research
  - sources
  - emoji
  - reactions
  - stickers
  - representation
---

This note records sources that can reveal emoji-like and sticker-like representations of project candidates in messaging and community platforms. It treats custom emoji, built-in reactions, reaction use, and stickers as potentially informative higher-level representations, not as evidence that Unicode should encode a candidate.

In this note, **custom emoji** follows platform terminology and may mean a named raster image or animation rather than an encoded emoji character. A **reaction** is a use position attached to another message through a platform feature; the content placed there may be an encoded emoji or a platform-defined asset. A **sticker** is a separately handled rich-media asset, often animated and transparent. Inline message use, a status, a sticker, an emote, and a reaction are different contexts even when they reuse the same artwork.

Apply [Character identity and encoding analysis](<../Methods/Character identity and encoding analysis.md>) to any candidate conclusion and [Content sources and licensing](<../Project/Content sources and licensing.md>) before acquiring, connecting to, or reproducing material.

## Representation layers

| Layer | Typical representation | Relationship to plain text | Principal research value |
| --- | --- | --- | --- |
| Unicode emoji character or standardized emoji sequence | Encoded character or sequence rendered with emoji presentation | Plain text; emoji presentation does not create a second abstract character | Directly relevant to existing representation, sequence, and route analysis |
| Platform custom emoji | Named image or animation addressed by a local shortcode or provider ID | Not plain text, although entry, inline display, and reaction behaviour may deliberately resemble emoji | Local representation, naming, compact communication, visual variation, and a possible closed-system alternative |
| Sticker, GIF, or emote | Rich-media file selected through search, a picker, an API, or a pack | Farther from plain text; the media object, tags, and platform context carry the representation | Representative forms, expressive or marketing use, creator ecology, and leads to contextual evidence |
| Reaction position | Platform relation attaching a character or asset to another item | Does not decide the encoding status of the attached content | Functional context when an occurrence, count, or event record establishes actual reaction use |

This ordering is analytical rather than a claim that every implementation has the same architecture. Record the actual data model and user context rather than inferring it from the interface label “emoji” or “sticker”.

## What each source type can establish

| Observation | What it can establish | What it does not establish by itself |
| --- | --- | --- |
| Official platform feature documentation | The platform supports specified built-in or custom reaction behaviour at the documented date | Availability or use of a particular candidate representation |
| Public directory or market entry | A labelled emoji-like asset was made publicly available through that service | Installation, inline use, reaction use, semantic accuracy, independent creation, or an encoding need |
| Public sticker-search result | A tagged media asset was discoverable for the query through that service at the search date | A stable symbol identity, general usage level, text-like use, or an encoding need |
| Exact sticker page | The hosted artwork, credited channel, tags, source link, and displayed service metrics where present | Ownership clearance, independent adoption, message use, or an interpretation of an undefined metric |
| Multiple entries or visual variants | More than one hosted asset or label maps to a related search term | Independent users or traditions; entries may be copies, mirrors, edits, or mislabelled graphics |
| Popular, download, copy, or install metric | Service-local activity if the metric, scope, and date are defined | Message or reaction frequency, unique users, cross-platform usage, or public-interchange need |
| Consented workspace inventory or use count | Presence or measured activity in one workspace under the provider’s definition | Public use, independence across communities, or whether activity was inline, reaction, status, or automation unless the data distinguishes them |
| Context-bearing message or reaction occurrence | Actual use in the observed context; a reaction only when the interface or data identifies it as such | A stable abstract-character identity or a need for Unicode encoding |
| Independent, context-bearing occurrences across communities and platforms | A broader convention may exist and warrants identity and interchange analysis | Satisfaction of either the character-proposal criteria or the separate emoji-proposal selection factors |

Directory or sticker-search presence should normally be recorded as **observed availability**. A provider’s description of its corpus, ranking, or metric is a **sourced claim**. Candidate identity, independence, and the interpretation of a visible graphic are **working inferences** until supported. Whether the finding affects a proposal is a **proposal decision**.

## Initial sources

### Slackmojis

[Slackmojis](https://slackmojis.com/) describes itself as an unofficial custom Slack emoji directory. Its public pages provide a shortcode, image, related items, and sometimes placement in popular or recent listings.

The project owner supplied the following exact public item-page leads. Representative pages for every listed candidate were checked on 29 July 2026; separately hosted variants remain distinct records but not presumed independent uses.

| Candidate | Item-page leads |
| --- | --- |
| Durian | [Durian Baby, 14549](https://slackmojis.com/emojis/14549-durian-baby); [Durian, 22569](https://slackmojis.com/emojis/22569-durian); [Durianoci, 50503](https://slackmojis.com/emojis/50503-durianoci); [Durian Fruit Opened, 50507](https://slackmojis.com/emojis/50507-durian_fruit_opened); [Durian Hazard, 61241](https://slackmojis.com/emojis/61241-durian_hazard) |
| Urinal | [23233](https://slackmojis.com/emojis/23233-urinal); [24647](https://slackmojis.com/emojis/24647-urinal); [43751](https://slackmojis.com/emojis/43751-urinal) |
| Inverted Cross | [Invertedcrossq, 72176](https://slackmojis.com/emojis/72176-invertedcrossq) |
| Eye of Providence | [Eye of Providence, 96214](https://slackmojis.com/emojis/96214-eye-of-providence) |
| Ouroboros Symbol | [Ouroboros, 57333](https://slackmojis.com/emojis/57333-ouroboros); [Ouroboros, 97335](https://slackmojis.com/emojis/97335-ouroboros); [Uroboros, 10320](https://slackmojis.com/emojis/10320-uroboros); [Ouroboros, 114866](https://slackmojis.com/emojis/114866-ouroboros) |
| Three Arrows Symbol | [Three Arrows, 10821](https://slackmojis.com/emojis/10821-three-arrows) |

The site described its [main Durian item](https://slackmojis.com/emojis/22569-durian) as suitable for Slack, messages, and reactions, but this is provider wording about intended use, not an observed reaction occurrence. The Ouroboros shortcode appeared in the site’s “Most Popular” listing when checked, but the ranking method and time window were not established; do not convert that placement into a frequency claim.

### EmojiBox

[EmojiBox](https://www.emojibox.app/) describes a searchable library of custom Slack emoji contributed by teams that chose to share theirs, together with packs from public sources. Its [public market](https://www.emojibox.app/market) supports search and popularity, alphabetical, and recent ordering. The landing page advertised more than 98,000 emoji while the public market displayed 79,175 on 29 July 2026, so neither figure should be treated as a stable or fully defined corpus size without clarification.

EmojiBox can also create a private index of a connected workspace and presents use-count features. Those capabilities could support stronger item-level research if the provider defines what is counted and access is explicitly authorized. They do not justify installing the Slack app or extension for this project without a separate privacy, security, rights, and platform-terms review.

The project owner supplied exact public item URLs for the following records:

| Candidate | Item-page leads |
| --- | --- |
| Durian | [Durian Baby, image 48998](https://www.emojibox.app/market/durian-baby?image=48998); [Durian, image 55224](https://www.emojibox.app/market/durian?image=55224); [Durianoci, image 75211](https://www.emojibox.app/market/durianoci?image=75211); [Durian Hazard, image 83656](https://www.emojibox.app/market/durian_hazard?image=83656) |
| Urinal | [Urinal, image 56150](https://www.emojibox.app/market/urinal?image=56150) |
| Inverted Cross | [Invertedcrossq, image 111263](https://www.emojibox.app/market/invertedcrossq?image=111263) |
| Eye of Providence | [Eye of Providence, image 130835](https://www.emojibox.app/market/eye-of-providence?image=130835) |
| Ouroboros Symbol | [Ouroboros, image 81245](https://www.emojibox.app/market/ouroboros?image=81245); [Uroboros, image 43771](https://www.emojibox.app/market/uroboros?image=43771) |
| Three Arrows Symbol | [Three Arrows, image 46198](https://www.emojibox.app/market/three-arrows?image=46198) |

The Durian and Three Arrows pages were visually checked on 29 July 2026. Each displayed a shortcode, one or more visual variants, an added date, a popularity rank and denominator, and a workspace percentage. Preserve those field labels and dated values if used, but do not infer what “popularity” or “workspaces” measures until EmojiBox supplies a definition.

### Emoji.gg

[Emoji.gg](https://emoji.gg/) was added during the initial review as a comparable source. It advertises more than 125,000 user-contributed custom emoji for Discord, Slack, and other platforms, with creator labels, download sorting, packs, and item-level licences. It may broaden searches beyond the Slack-centred sources, but no candidate-specific result has yet been recorded.

### GIPHY stickers

[GIPHY](https://giphy.com/stickers) treats stickers as transparent GIF files and distributes sticker search through its site, API, and integrations. Its [sticker definition](https://support.giphy.com/hc/en-us/articles/360019683332-What-Is-A-GIPHY-Sticker) places stickers in messaging, storytelling, and photo-editing contexts rather than plain text. Its [search documentation](https://support.giphy.com/hc/en-us/articles/360019823451-How-to-Find-the-Content-You-Want) says results are selected using relevance, popularity, cultural significance, and quality, but that provider description does not turn search placement into a general usage-frequency measure.

Initial candidate discovery surfaces retained on 29 July 2026 are:

| Candidate | GIPHY lead |
| --- | --- |
| Durian | [Durian sticker search](https://giphy.com/search/durian-stickers) |
| Urinal | [Urinal sticker search](https://giphy.com/search/urinal-stickers) |
| Inverted Cross | [Inverted Cross sticker search](https://giphy.com/search/inverted-cross-stickers) |
| Eye of Providence | [Eye of Providence sticker search](https://giphy.com/search/eye-of-providence-stickers) |
| Ouroboros Symbol | [Ouroboros search](https://giphy.com/search/ouroboros-stickers) and [Uroboros spelling variant](https://giphy.com/search/uroboros-stickers) |
| Three Arrows Symbol | [Antifa, Antisocial, Antifascist sticker](https://giphy.com/stickers/antifa-antisocial-antifascist-GCfzNHadIb1qn4dchF) |
| Mangosteen Symbol | [Mangosteen sticker search](https://giphy.com/search/mangosteen-stickers) |
| Eye of Ra | [Eye of Ra sticker search](https://giphy.com/search/eye-of-ra-stickers) |
| Squatter Symbol | [Squat Symbol sticker](https://giphy.com/stickers/transparent-0GtbhrhHQEi9uh08Ot) |

The Durian search visibly returned varied depictions from multiple credited creator and brand channels when checked, making it a useful form-survey and provenance-discovery lead after deduplication. The exact Three Arrows page credited Priscila Justina, used the tags “antifa”, “antisocial”, and “antifascist”, and displayed 787,183 views. The exact Squatter Symbol page credited FuzzyQTip, used the tags “symbol”, “squat”, “squatter”, “hausbesetzung”, and “hausbesetzer”, and displayed 2,752,918 views. These are dated, service-local display metrics whose counting method and relationship to actual sharing or message use were not established.

## Platform capability sources

Current official documentation supplies a starting, non-exhaustive platform map:

- [Slack](https://slack.com/help/articles/202931348-Use-emoji-and-reactions) supports emoji in messages and as reactions and routes users to custom-emoji features.
- [Discord](https://support.discord.com/hc/en-us/articles/12102061808663-Reactions-and-Super-Reactions-FAQ) supports emoji reactions; its separate [custom-emoji documentation](https://support.discord.com/hc/en-us/articles/360041139231-How-to-Add-Emojis-on-Discord) describes server-specific custom assets and their wider availability under some account conditions.
- [Mattermost](https://docs.mattermost.com/end-user-guide/collaborate/react-with-emojis-gifs.html) expressly documents uploading custom emoji that workspace members can use to react to messages.
- [Zulip](https://zulip.com/help/emoji-reactions) says that any emoji, including custom emoji, can be used as a reaction; its [custom-emoji documentation](https://zulip.com/help/custom-emoji) also distinguishes organization-level assets.
- [Telegram’s technical documentation](https://core.telegram.org/api/reactions) distinguishes normal emoji reactions from custom-emoji reactions.

These pages establish affordances. Candidate research still needs a public or consented occurrence, a defined provider metric, or another context-bearing record to establish actual use.

Future platform expansion should distinguish:

1. a fixed built-in reaction set, including whether each reaction maps to a Unicode character or sequence or uses a proprietary platform-native identity;
2. custom user or organization emoji that can be used as reactions;
3. Unicode emoji available through an ordinary picker;
4. stickers, emotes, GIFs, badges, and other rich-media systems that the platform does not treat as emoji reactions; and
5. public, private, deleted, access-controlled, and account-personalized evidence surfaces.

## Candidate search and capture procedure

Search the working candidate name, recorded aliases, spelling and separator variants, and visually or semantically adjacent labels. For the present inventory, the initial cross-source search vocabulary includes Durian, All Gender Symbol, Urinal, Inverted Cross, Eye of Providence, Ouroboros Symbol, Three Arrows Symbol, Mangosteen Symbol, Eye of Ra, and Squatter Symbol, together with their candidate-specific aliases.

For each retained result, record:

- provider, platform claimed or observed, stable item URL and provider ID;
- exact displayed name or shortcode and search term that found it;
- access and capture dates, sort order, and corpus or result boundary;
- a neutral visual description and the reason for mapping it to the candidate;
- uploader, creator, originating workspace or pack, and provenance where available;
- whether the evidence is a directory listing, sticker-search result, installation, inline use, rich-media share, reaction use, status use, provider metric, or another context;
- the exact metric label, value, scope, and provider definition, without inferring what an unlabelled number counts;
- independence from other results, including suspected copies, mirrors, edits, aliases, and shared source packs;
- rights holder, exact item licence or permission, attribution, publication status, and any privacy restriction; and
- the favourable, adverse, and unresolved implications for the candidate’s identity and representation analysis.

Preserve a public citation and metadata record even when an image cannot be redistributed. Do not place directory or sticker images or private workspace content in public Git merely because they can be downloaded or viewed. Follow the project’s [evidence-storage policy](<../Project/Evidence storage and publication.md>) for originals, derivatives, private data, and publication decisions.

## Interpretation for candidate research

These ecosystems can support a limited observation that users or contributors have represented a concept with a compact image suitable for platform communication. Context-bearing occurrences may also show a candidate functioning inline or as a reaction. Multiple independent renderings can help test whether the identity survives visual variation. GIPHY search can additionally reveal creator, brand, regional, animated, and stylistic forms that warrant candidate-specific provenance checks.

The same evidence can strengthen an adverse or non-encoding account. Custom emoji are higher-level, platform- or workspace-defined assets designed to carry non-standard pictograms through private identifiers and prior agreement. Stickers are farther removed from plain text and may be expressive illustrations, animations, overlays, or marketing assets rather than stable information units. A successful custom reaction can therefore show that a closed-system representation works, not that public interchange requires a Unicode character. Directory copies, arbitrary shortcodes, search tags, ambiguous metrics, and one-off artwork may show only availability or visual recognizability.

Do not use these sources as substitutes for demonstrated plain-text need, character identity, independent community use, or the prescribed evidence for the separate emoji-proposal route. Their main value is discovery, representative-form and higher-level-representation analysis, and locating stronger contextual evidence.
