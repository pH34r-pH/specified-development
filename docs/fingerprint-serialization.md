# Fingerprint serialization

## Existing authority pins: `sorted-json-authority-v1`

The version 1 authority pin is SHA-256 of the following byte sequence. This
serialization is preserved for historical pins; the name identifies the byte
contract, not a new field added to existing bundles.

1. Start with the reviewed authority object after the bundle's shape checks.
   Its keys and string values are not normalized, case-folded, trimmed or
   reordered. Arrays retain their original order and repetitions.
2. Recursively sort object keys by the lexicographic sequence of Unicode code
   points, as Python sorts strings. Sorting uses the original unescaped keys.
3. Serialize JSON with no whitespace between members or elements: comma and
   colon are the only separators. Escape double quotes and backslashes; use
   `\b`, `\f`, `\n`, `\r`, and `\t` for those controls and lowercase
   `\u00xx` for other U+0000–U+001F controls. Do not escape `/`.
4. Retain printable ASCII U+0020–U+007E except the escapes above. Escape U+007F
   (DEL) and non-ASCII characters with lowercase hexadecimal `\uXXXX` sequences.
   A character above U+FFFF uses the corresponding high/low UTF-16 surrogate
   pair. JSON delimiters and all remaining characters are ASCII.
5. Encode as UTF-8 without a byte-order mark or trailing newline, then compute
   the lowercase hexadecimal SHA-256 digest.

The implementation is Python's standard `json.dumps` with `sort_keys=True`,
`separators=(",", ":")`, `ensure_ascii=True` and `allow_nan=False`, followed by
UTF-8 encoding. The supported authority projection contains objects with string
keys, strings and arrays of strings; other values are rejected by its shape
contract. A direct call to this low-level serializer does not establish that an
arbitrary object is an accepted authority declaration.

Version 2's reviewed projection additionally includes schema/version data,
commands and source records. It reuses the same serialization algorithm, with
nonnegative integer schema fields written as ordinary base-10 JSON integers.
The projection definition and the serialization algorithm are separate
contracts. Changing either changes the reviewed pin; version 1's projection and
fixture remain unchanged. Floating-point values, arbitrary object keys and
unpaired surrogate strings are not a supported way to extend the declared
bundle schema.

## Fixed conformance vectors

[`authority-serialization-v1.json`](../tests/fixtures/tooling/authority-serialization-v1.json)
contains independent expected serialized text and SHA-256 values. The tests
hash those literal bytes and compare the implementation's result. Non-ASCII
examples exercise escaping and code-point key ordering; they are serialization
vectors, not complete policy-valid authorities.

| Vector | Expected SHA-256 |
| --- | --- |
| Qualified version 1 fixture authority | `5d10341e61568ce6795fe194ffc4d0188863b7e32f46864c00dfb118e8f034ec` |
| Unicode and escaped characters | `0413eeeb245a777fdbc0647d9fb720c47e4be69e989ab587adedddc7099e6909` |
| Code-point key ordering | `d9f4dde0bdd9101de452870925af73c623dc9e1ea9cd3f2708e2acac19a344c2` |
| Array order and nested objects | `ef9d2d8e844de4353361251fe0d04fb71bdcf4d1e7127781431a1f5df953f8d1` |
| ASCII DEL escaping | `2a4be89ced8ad4d4ff64d890bb443669cd846aaf7b706c45ba3218cee13a30ad` |

In particular, U+E000 sorts before U+10000 under this contract. This is a useful
counterexample to accidentally switching to UTF-16 code-unit ordering.

## Why this is not RFC 8785

[RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) specifies JSON
Canonicalization Scheme, including UTF-16 property-name ordering and an
ECMAScript-compatible number representation. The existing Python format is not
JCS. The maintained [rfc8785 package](https://pypi.org/project/rfc8785/) provides
that algorithm without transitive dependencies, but substituting it here would
change established non-ASCII pins and introduce a mandatory runtime dependency.

The current decision is to retain and specify the existing byte contract and
test it with fixed vectors. If another consumer requires JCS, use that existing
implementation through an explicit reviewed profile migration; do not write a
new canonical JSON implementation or silently relabel old pins as RFC 8785.

## Review-detail bytes have a separate purpose

`bundle_review.canonical()` uses sorted compact JSON with `ensure_ascii=False`,
UTF-8 encoding and one trailing LF. That format hashes lossless detail and
regeneration records, rather than reviewed authority alone. Its UTF-8 and
newline differences are intentional and tested. Regeneration still binds the
generator and environment identity; a successful pin comparison does not prove
arbitrary command behavior or target acceptance.

The relevant standard-library behavior is documented in
[Python's JSON module](https://docs.python.org/3.12/library/json.html).
