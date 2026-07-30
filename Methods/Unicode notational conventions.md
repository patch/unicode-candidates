---
title: Unicode notational conventions
method_status: maintained project reference
last_reviewed: 2026-07-30
tags:
  - method
  - unicode
  - notation
  - style
---

This profile uses the relevant parts of Unicode 17.0 [Appendix A, “Notational Conventions”](https://www.unicode.org/versions/Unicode17.0.0/core-spec/appendix-a/) as a baseline style guide for uniformity with the primary Unicode standard. It is not a claim of conformance: Appendix A describes conventions used within the Unicode Standard, while this project and any resulting proposal are separate works.

The project narrows that baseline by selecting one display option where Appendix A permits several, omitting sections that have no planned application here, and adding conventions for recurring editorial cases that Appendix A does not settle.

## Scope and maintenance

The current profile covers:

- code points and code-point ranges;
- formal character names and character name aliases;
- character block names;
- character and emoji sequences; and
- character property names and values.

It does not adopt Appendix A’s miscellaneous linguistic notation, operators, extended BNF, character-class syntax, or rendering-rule notation. Add one of those subjects only when actual project material requires it; absence from this profile creates no project rule for it.

Use this profile for routine writing and review. Check the current official source when:

- a material case is absent here;
- an exact Unicode rule or classification is at issue;
- local usage appears to conflict with an applicable specification; or
- a Unicode release or scheduled review gives reason to revalidate the convention.

Keep technical identity separate from presentation. Small capitals, literal display and table layout aid readers, but do not change whether something is an encoded character, a character sequence, a glyph, or a provisional proposal-stage name.

## Code points, ranges and properties

Write a Unicode code point as U+ followed by four to six uppercase hexadecimal digits. Retain leading zeroes when needed to provide at least four digits:

- U+0061
- U+00E4
- U+200D
- U+1F34B

Always retain U+, including in tables. Write an inclusive range with U+ at both endpoints and an en dash:

- U+0061–U+007A

Do not use the alternative two-dot range notation in editorial prose or tables.

Characters, code points, code-point ranges and character names are not code and do not receive Markdown backticks in editorial prose or tables. Backticks remain appropriate when the material is genuinely code or machine-oriented syntax, including commands, regular expressions, data excerpts, filenames and property expressions.

Write formal character property names and values in backticks, preserving their official capitalization and underscores, for example `General_Category`, `Uppercase_Letter` and `Emoji_Presentation=Yes`. Use short property or value aliases only when their brevity is useful and the meaning is clear.

## Character names and aliases

Display a formal Unicode character name in all small capitals:

- <span style="font-variant:all-small-caps">LATIN SMALL LETTER A</span>
- <span style="font-variant:all-small-caps">ZERO WIDTH JOINER</span>
- <span style="font-variant:all-small-caps">LEMON</span>

Use the same treatment for a formal `Name_Alias` value when it functions as the identifying label. The versioned UCD [`NameAliases.txt`](https://www.unicode.org/Public/17.0.0/ucd/NameAliases.txt) file controls the formal aliases and their types. After a full prose introduction, use an alias of type `abbreviation` when one exists and is contextually appropriate:

- <span style="font-variant:all-small-caps">ZWJ</span>
- <span style="font-variant:all-small-caps">NBSP</span>

When an abbreviation is incorporated into ordinary prose rather than used as a name label, it does not require small capitals: “ZWJ sequence” and “NBSP character”. If a code point has more than one formal abbreviation alias, select the one appropriate to the stated function rather than assuming a general precedence among them.

Use italics for an informative character alias or an unencoded text element when the distinction is material, following Appendix A. Do not treat a CLDR short name as a formal Unicode character name.

Working candidate names remain in title case. A provisional proposal-style character name may use all small capitals in clearly labelled proposed repertoire or property data, but its typography does not imply that Unicode has assigned the name.

The inline style is intended to survive into compatible rendered documents and generated PDFs. GitHub may remove the style and display the underlying uppercase text; that graceful fallback is acceptable. Do not substitute lookalike small-cap Unicode characters for the letters in a name.

## Literal display and prose forms

Include a literal character when it has a meaningful standalone graphic display. Do not include a standalone literal for a non-graphic character, including a code point in the `Separator` (`gc=Z`) or `Other` (`gc=C`) General Category group. A complete character sequence or quoted string may retain such a character as part of its literal form even though the component is not displayed separately.

If a printable combining mark later needs to be shown by itself, U+25CC ◌ <span style="font-variant:all-small-caps">DOTTED CIRCLE</span> may supply the base required to display the visible mark. Do not use dotted-circle display for a non-printing combining character, and do not add a more detailed combining-mark convention until project material requires one.

In ordinary prose, a graphic character may instead be mentioned casually by its literal when its visible or orthographic form is the point, the identity is unambiguous and exact technical identification is not material. Enclose the literal in typographic double quotation marks; do not leave it bare or put it in backticks. Match its case to the layer being described:

- the “o” in “Ducoff”
- the “O” position in the all-capital “DUCOFF” wordmark
- a lowercase “d”
- ordinary “O”, “.”, or “d”

Use the casual form for an orthographic position, a source’s displayed or quoted form, or a visually discussed substitution whose exact encoded identity is not at issue. It does not replace a full technical introduction when the code point, case distinction or character identity becomes material. After that introduction, use the abbreviated name form when technical identity remains material, and ordinary referential wording when no character is being identified. In a coordinated list, use either quoted literals or name labels consistently.

For punctuation, write the quoted literal “.” when it is parallel to “O” and “d”, or use <span style="font-variant:all-small-caps">FULL STOP</span> when naming the character. Do not use an unstyled ‘full stop’ or ‘full-stop’ as a substitute for the character’s literal or formal name.

On the first material prose reference in a file for which technical identity is material, use the full form unless a preceding identity table on the page supplies the same information:

- U+0061 a <span style="font-variant:all-small-caps">LATIN SMALL LETTER A</span>
- U+00E4 ä <span style="font-variant:all-small-caps">LATIN SMALL LETTER A WITH DIAERESIS</span>
- U+200D <span style="font-variant:all-small-caps">ZERO WIDTH JOINER</span>
- U+1F34B 🍋 <span style="font-variant:all-small-caps">LEMON</span>

For a sequence, put the complete literal first, then give an angle-bracketed, comma-delimited list of its components in order. Within the list, give each component in the applicable full form:

- 🍋‍🟩 \<U+1F34B 🍋 <span style="font-variant:all-small-caps">LEMON</span>, U+200D <span style="font-variant:all-small-caps">ZERO WIDTH JOINER</span>, U+1F7E9 🟩 <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span>\>

After introduction, use the abbreviated name form when the literal and code point are not needed:

- <span style="font-variant:all-small-caps">LATIN SMALL LETTER A</span>
- <span style="font-variant:all-small-caps">LATIN SMALL LETTER A WITH DIAERESIS</span>
- <span style="font-variant:all-small-caps">ZWJ</span>
- <span style="font-variant:all-small-caps">LEMON</span>
- \<<span style="font-variant:all-small-caps">LEMON</span>, <span style="font-variant:all-small-caps">ZWJ</span>, <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span>\>

These forms are available when technical identity matters; they do not require replacing an ordinary, unambiguous referent such as “the lime emoji sequence” with repeated formal labels.

## Sequences and emoji terminology

Angle brackets containing an ordered, comma-delimited list identify a sequence, not a set. Use U+ for every code point:

- \<U+1F34B, U+200D, U+1F7E9\>

In prose, use **emoji sequence** by default. Qualify the exact class from [Unicode Emoji](https://www.unicode.org/reports/tr51/#Definitions), such as **RGI emoji ZWJ sequence**, only when its construction, qualification or recommended-interchange status is material. Once that status has been established, return to the shorter term when the distinction is no longer needed.

Use **abstract character sequence** when the abstract-versus-coded distinction is itself material, and **coded character sequence** for the ordered code-point representation. A sequence may behave as one user-perceived emoji or text element without thereby becoming one emoji character or one separately encoded character.

## Identity tables

Place the literal, code-point notation and name labels in the first three columns, followed by any analytical columns. Use the headings appropriate to the table’s contents:

- characters only: **Character**, **Code point**, **Name**;
- characters and sequences: **Character or sequence**, **Code point(s)**, **Name(s)**; and
- sequences only: **Sequence**, **Code points**, **Names**.

Display one extended grapheme cluster per row in the first column. In a sequence row:

- the code-point cell contains an angle-bracketed, comma-delimited sequence;
- the names cell contains the corresponding ordered, angle-bracketed component labels;
- a formal abbreviation alias such as <span style="font-variant:all-small-caps">ZWJ</span> may be used even when the table is the file’s first technical presentation of the sequence; and
- the component labels are not presented as an official name for the sequence itself.

| Character or sequence | Code point(s) | Name(s) |
| --- | --- | --- |
| 🍋 | U+1F34B | <span style="font-variant:all-small-caps">LEMON</span> |
| 🍋‍🟩 | \<U+1F34B, U+200D, U+1F7E9\> | \<<span style="font-variant:all-small-caps">LEMON</span>, <span style="font-variant:all-small-caps">ZWJ</span>, <span style="font-variant:all-small-caps">LARGE GREEN SQUARE</span>\> |

## Character blocks

Refer to a normative character block by its exact title-cased name followed by “block”:

- the Latin Extended-B block

When a range is useful, apply the project’s range notation:

- the Basic Latin block (U+0000–U+007F)

Do not assume that an informal chapter heading, chart label or subrange is a normative block name. Verify a material block reference against the applicable version of [`Blocks.txt`](https://www.unicode.org/Public/17.0.0/ucd/Blocks.txt).

## Exceptions

Preserve quoted third-party wording and syntax faithfully. Do not restyle:

- a quotation merely to match project notation;
- a URL, filename, identifier, command, regular expression or machine-readable data field;
- code-point notation within a source whose notation is itself under discussion; or
- an official document title or label whose capitalization has evidential value.

Explain a material conflict outside the quotation or data excerpt rather than silently altering the source.

## Revision history

- **2026-07-30:** Established the profile and applied it across the 73 Markdown files in the working tree based on commit `7ac48e7b9bd0a2e0b7c0e6fa854dd134290f1a33`. Thirteen files contained concrete code-point notation. The audit converted project-authored prose and identity tables, preserved machine-oriented and source-specific exceptions, and validated edited code-point/name pairs against Unicode 17.0 `UnicodeData.txt` and `NameAliases.txt`. Clarified the distinction between full technical references and casual quoted-literal references after review.
