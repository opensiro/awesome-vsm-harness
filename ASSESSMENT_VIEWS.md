# General and domain-specific assessment views

Awesome VSM Harness is a curated navigation layer over evidence-backed organizational assessments. It does not define assessment semantics and it does not own canonical assessment findings.

## General assessment

The canonical general assessment corpus is:

```text
opensiro/vsm-harness-index
```

Its assessment artifacts are produced under the canonical general assessment specification owned by:

```text
opensiro/vsm-harness-skills/skills/assess-vsm-harness
```

When this Awesome repository links to an `Assessment` in `opensiro/vsm-harness-index`, that link should be read as the **general OpenSiro VSM Harness assessment**.

Where useful for clarity, future curation may label such links explicitly as `General assessment`.

## Domain-specific indexes

The VSM Harness Profile may also be consumed by domain-specific assessment specifications.

A domain-specific assessment can impose its own:

- operating purpose and system-in-focus;
- admission boundary;
- evidence requirements;
- domain-specific capability requirements;
- required or permitted ownership arrangements;
- publication contract.

Its corpus should live in a distinct domain-specific index or equivalent assessment-owned surface rather than being mixed into the canonical general Index.

A domain-specific index is therefore not a filtered view of `opensiro/vsm-harness-index`.

```text
Profile
  + domain-specific assessment specification
  + domain-specific evidence
  ↓
domain-specific index
```

No domain-specific index is implied to exist merely because Awesome defines this routing model.

## Awesome routing

Awesome may curate multiple assessment views for the same upstream system when those views actually exist and add value.

A future entry may therefore expose links such as:

```text
General assessment · SWE assessment · Science assessment
```

provided that each label resolves to a distinct assessment contract and corpus.

Awesome must not:

- copy the canonical finding into a second source of truth;
- present a domain-specific conclusion as though it were the general assessment;
- infer a domain-specific assessment from general Index metadata alone;
- invent a domain-specific index before one exists.

Its role is navigation and representative curation across assessment ecosystems.

## Relationship to Priority Domain Views

The current `Priority Domain Views` in the root README are curation directions, not domain-specific assessment systems.

A curated domain section may exist without a domain-specific index. Conversely, a future domain-specific index may exist without immediately receiving a curated Awesome section.

This keeps two dimensions separate:

```text
domain-oriented presentation
        ≠
domain-specific assessment contract
```

When a domain-specific index becomes real, Awesome can link it explicitly while continuing to preserve the canonical general Index link.
