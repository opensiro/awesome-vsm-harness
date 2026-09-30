# Contributing

Thanks for helping improve Awesome VSM Harness.

This repository is a **curated presentation layer** over independently maintained assessment indexes. The canonical general corpus is [VSM Harness Index](https://github.com/opensiro/vsm-harness-index); future domain-specific assessment systems may expose separate indexes under their own contracts. See [`ASSESSMENT_INDEXES.md`](ASSESSMENT_INDEXES.md).

Awesome is not the place where harnesses are first discovered or where VSM states are decided.

## Before You Add a Harness

A project should normally satisfy all of the following:

1. It is an agent harness, agent runtime, or closely related system where organizational structure is meaningful.
2. It already has a completed **general assessment** in `opensiro/vsm-harness-index`.
3. It adds a useful organizational contrast rather than duplicating a VSM form already represented clearly.
4. Its description can be grounded in the general Index assessment without inventing new VSM claims in this repository.

If a project has not been assessed yet, propose or queue it in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index) first.

A qualifying domain-specific assessment may be linked in addition to the general assessment. It does not replace the general assessment requirement for the current Awesome list unless the curation contract is explicitly changed later.

## What This List Optimizes For

Awesome VSM Harness is intentionally not exhaustive. The Index may grow to hundreds or thousands of systems; this list should remain browsable.

Selection optimizes for:

1. **Domain relevance** — the project genuinely performs work in the stated domain when it is being considered for a domain view.
2. **Organizational distinctiveness** — it demonstrates a VSM-relevant control structure not already represented clearly.
3. **Evidence quality** — the general Index assessment and any linked domain-specific assessment support the organizational summary.
4. **Current relevance** — activity, adoption, or contemporary architectural importance may break ties between otherwise similar projects.

GitHub stars and VSM autonomy rank are not admission scores.

When two projects instantiate essentially the same organization, prefer the clearest representative. A new entry should improve the map, not merely increase the count.

## What Belongs Where

### Organizational Building Blocks

Use this section for reusable foundations from which downstream developers construct or specialize an agent organization.

Typical signals include first-party surfaces for composing roles, policies, models, coordination, authority, or other organizational decision rights.

This section should remain compact. Broad framework coverage belongs in the general Index and in other Awesome lists.

### Priority Domain Views

The README currently keeps domain coverage at the **view level** rather than maintaining populated domain sections for common categories such as coding, browser use, or generic research.

Priority domains are curation directions, not quotas. A domain should become a populated section only when the available assessment evidence is sufficient to show a meaningful organizational contrast through VSM.

That evidence may eventually include both:

- the canonical general VSM assessment;
- a separate domain-specific assessment index with additional purpose/evidence/capability requirements.

A domain label is not justified merely because:

- the maintainer belongs to that industry;
- the harness exposes generic governance, safety, workflow, or policy features;
- a downstream user could configure the harness for the domain;
- one README example mentions the domain.

Until a domain reaches the threshold for a useful curated comparison, its candidate systems should remain discoverable and assessed in the appropriate owning index rather than being duplicated here.

## VSM Evidence and Classification

Do not introduce or change `A / C / P / — / ?` states in this repository.

If the **general assessment** is wrong or incomplete:

1. open the corresponding assessment in `opensiro/vsm-harness-index`;
2. provide primary repository evidence for the correction;
3. update the general Index through its assessment workflow;
4. only then update this Awesome list if the curated description or placement is affected.

If a **domain-specific assessment** is wrong or incomplete, update its owning domain-specific index instead. Awesome must not reconcile conflicting assessment contracts by inventing a new local conclusion.

The dependency direction is:

```text
upstream project
      ↓
assessment specifications
      ↓
├── general Index
└── domain-specific Index(es)
      ↓
awesome-vsm-harness
```

Never use Awesome VSM Harness as evidence for an assessment index.

Do not copy canonical VSM state vectors, TL;DR/signature text, rank numbers, or ranking vectors into Awesome. Those values remain in their owning indexes. Awesome should link to them.

## Entry Format

Keep entries concise and organizationally specific. Use the stable general Index `harness_id` for TL;DR and Ranking anchors.

When only the general assessment exists:

```md
- [Project](https://github.com/org/repo) — Mission and organizational signature: what performs the operational work, and what is distinctive about coordination, regulation, audit, adaptation, policy, or authority. [General assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/project.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#project) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#project).
```

When a separate domain-specific assessment also exists:

```md
- [Project](https://github.com/org/repo) — ... [General assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/project.md) · [<Domain> assessment](https://github.com/owner/domain-index/...) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#project).
```

A good entry can usually be derived from three questions:

```text
Mission: what real-world work does the organization perform?
Operations: what acts as S1?
Control and authority: what is distinctive about the metasystem or parent authority?
```

Avoid generic feature inventories such as `memory · tools · MCP · planning` unless one of those features is directly relevant to the organizational distinction.

## Machine-checkable Index consistency

`index-consistency` complements `awesome-lint`. Formatting remains the job of `awesome-lint`; the consistency job checks deterministic relationships to a read-only checkout of the current canonical **general Index**.

For each curated README entry that links a general Index assessment, it verifies that:

- the referenced assessment exists;
- the assessment filename and canonical `harness_id` agree;
- the entry's upstream repository matches the assessment `repository` field;
- the linked TL;DR and Ranking anchors use that `harness_id` and exist in the canonical generated files;
- the entry does not copy a six-state vector, per-system state assignment, or numeric rank that belongs in the Index.

The validator deliberately does **not** decide whether a harness is representative, organizationally distinctive, well evidenced, relevant to a domain, or currently important. Those remain curation judgments.

Future domain-specific links need their own owning-index validation rather than being silently treated as general Index links.

To run the deterministic general-Index check locally with the repositories checked out side by side:

```bash
python scripts/validate_index_consistency.py --index-dir ../vsm-harness-index
python -m unittest discover -s tests -v
```

## Domain and VSM Are Orthogonal

Domain placement must not be inferred from the autonomy vector, and autonomy rank must not be used as a proxy for domain importance.

Two systems in the same domain may have different VSM forms. Two systems in different domains may share the same form. Both observations are useful.

The purpose of this repository is to expose those contrasts without changing either the general assessment methodology or a domain-specific assessment contract.

## Pull Requests

Keep a pull request focused on one logical change where practical.

For a new building-block entry, include:

- the upstream repository;
- the existing **General assessment** link;
- the stable TL;DR and Ranking anchor links when available;
- any additional domain-specific assessment link when relevant;
- a short explanation of the organizational form it adds;
- why an existing entry does not already represent the same contrast.

For a proposed domain section, include enough assessed systems to demonstrate that the section adds a real organizational comparison rather than another generic application category.

## Related Lists

Broad ecosystem lists are welcome in `Related Awesome Lists` when they provide a genuinely complementary discovery surface. They do not need a VSM assessment because they are references, not harness entries.

Domain-oriented agent lists are also relevant references, but Awesome VSM Harness should remain differentiated by requiring reviewable harnesses and using VSM evidence to describe organizational control structure.
