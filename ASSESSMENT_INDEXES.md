# Assessment indexes

Awesome VSM Harness is a curated downstream view. It may route readers to more than one assessment corpus when those corpora answer different questions about the same upstream system.

## General assessment

The canonical general corpus is:

- [`opensiro/vsm-harness-index`](https://github.com/opensiro/vsm-harness-index)

A link into that repository should be labeled **General assessment** when there is any possibility of confusion with a domain-specific assessment.

The general assessment asks which VSM functions are present at the declared boundary and how their decisive organizational closure is owned under the released general Methodology.

It does not claim to answer every purpose-specific question about suitability, evidence sufficiency, capability, or required autonomy in a concrete operating domain.

## Domain-specific indexes

Future domain-specific assessment systems may maintain separate indexes, for example for software engineering, scientific research, government, healthcare, or other operating domains.

A domain-specific index may consume:

- normative VSM semantics from `vsm-harness-profile`;
- the general repository-relative assessment from `vsm-harness-index`;
- reusable public capability evidence;
- additional domain-specific evidence and requirements.

It then owns its own declared:

- operating purpose and system-in-focus;
- admission boundary;
- evidence requirements;
- capability requirements;
- required or permitted ownership arrangements;
- result schema and assessment corpus.

A domain-specific conclusion does not redefine the general assessment and does not redefine Profile-owned VSM semantics.

## Awesome routing rule

Awesome may show both surfaces for the same project:

```text
Project
  ├── General assessment
  └── <Domain> assessment
```

When both exist:

- **General assessment** links to the canonical `vsm-harness-index` artifact;
- **<Domain> assessment** links to the owning domain-specific index;
- Awesome summarizes the distinction but does not copy the canonical evidence or become a second assessment database.

The same upstream system may legitimately receive different conclusions across these indexes when purpose, system boundary, reachable organizational paths, autonomy requirements, capability requirements, or evidence thresholds differ.

## Admission into Awesome

The existence of a domain-specific index does not automatically create a new Awesome section or force a project into this curated list.

Awesome continues to optimize for:

- domain relevance;
- organizational distinctiveness;
- evidence quality;
- current relevance when needed to break ties.

Domain-specific indexes provide additional reviewable evidence and navigation; curation remains an Awesome-owned decision.
