# Contributing

Thanks for helping improve Awesome VSM Harness.

This repository is a **curated presentation layer** over the independently maintained [VSM Harness Index](https://github.com/opensiro/vsm-harness-index). It is not the place where harnesses are first discovered or where VSM states are decided.

## Before You Add a Harness

A project should normally satisfy all of the following:

1. It is an agent harness, agent runtime, or closely related system where organizational structure is meaningful.
2. It already has a completed standalone assessment in `opensiro/vsm-harness-index`.
3. If proposed for a domain section, the reviewed distribution is explicitly designed to perform work in that domain.
4. It adds a useful organizational contrast rather than duplicating a VSM form already represented clearly in the same domain.
5. Its description can be grounded in the Index assessment without inventing new VSM claims in this repository.

If a project has not been assessed yet, propose or queue it in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index) first.

## What This List Optimizes For

Awesome VSM Harness is intentionally not exhaustive. The Index may grow to hundreds or thousands of systems; this list should remain browsable.

Selection optimizes for:

1. **Domain relevance** — the project genuinely performs work in the stated domain.
2. **Organizational distinctiveness** — it demonstrates a VSM-relevant control structure not already represented clearly.
3. **Evidence quality** — the Index assessment supports the organizational summary.
4. **Current relevance** — activity, adoption, or contemporary architectural importance may break ties between otherwise similar projects.

GitHub stars and VSM autonomy rank are not admission scores.

When two projects in the same domain instantiate essentially the same organization, prefer the clearest representative. A new entry should improve the map, not merely increase the count.

## What Belongs Where

### Organizational Building Blocks

Use this section for reusable foundations from which downstream developers construct or specialize an agent organization.

Typical signals include first-party surfaces for composing roles, policies, models, coordination, authority, or other organizational decision rights.

This section should remain compact. Broad framework coverage belongs in the Index and in other Awesome lists.

### Organizations by Domain

Use a domain section when the project ships an opinionated organization for a concrete class of work.

Examples include government operations, cybersecurity incident response, scientific discovery, industrial or robotic operations, enterprise operations, infrastructure/SRE, healthcare operations, legal/compliance work, logistics, or software engineering.

A domain label is not justified merely because:

- the maintainer belongs to that industry;
- the harness exposes generic governance, safety, workflow, or policy features;
- a downstream user could configure the harness for the domain;
- one README example mentions the domain.

### Priority Domain Views

Priority domains in the README are coverage directions, not quotas. Do not add weak entries to make a section look complete.

Create or expand a domain section only when completed assessments provide meaningful organizational contrasts.

## VSM Evidence and Classification

Do not introduce or change `A / C / P / — / ?` states in this repository.

If an assessment is wrong or incomplete:

1. open the corresponding assessment in `opensiro/vsm-harness-index`;
2. provide primary repository evidence for the correction;
3. update the Index through its assessment workflow;
4. only then update this Awesome list if the curated description or placement is affected.

The dependency direction is:

```text
upstream project
      ↓
vsm-harness-index
      ↓
standalone assessment
      ↓
awesome-vsm-harness
```

Never use Awesome VSM Harness as evidence for the Index.

Do not copy canonical VSM state vectors, TL;DR/signature text, rank numbers, or ranking vectors into Awesome. Those values are generated and maintained in the Index. Awesome should link to them.

## Entry Format

Keep entries concise and organizationally specific. Use the stable Index `harness_id` for TL;DR and Ranking anchors:

```md
- [Project](https://github.com/org/repo) — Mission and organizational signature: what performs the operational work, and what is distinctive about coordination, regulation, audit, adaptation, policy, or authority. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/project.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#project) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#project).
```

A good entry can usually be derived from three questions:

```text
Mission: what real-world work does the organization perform?
Operations: what acts as S1?
Control and authority: what is distinctive about the metasystem or parent authority?
```

Avoid generic feature inventories such as `memory · tools · MCP · planning` unless one of those features is directly relevant to the organizational distinction.

## Domain and VSM Are Orthogonal

Domain placement must not be inferred from the autonomy vector, and autonomy rank must not be used as a proxy for domain importance.

Two systems in the same domain may have different VSM forms. Two systems in different domains may share the same form. Both observations are useful.

The purpose of this repository is to expose those contrasts without changing the canonical assessment methodology.

## Pull Requests

Keep a pull request focused on one logical change where practical.

For a new entry, include:

- the upstream repository;
- the existing VSM assessment link;
- the stable TL;DR and Ranking anchor links when available;
- proposed domain or building-block section;
- a short explanation of the organizational form it adds;
- why an existing entry in that section does not already represent the same contrast.

For a move between sections, explain what changed in the project or in the interpretation of its product shape.

## Related Lists

Broad ecosystem lists are welcome in `Related Awesome Lists` when they provide a genuinely complementary discovery surface. They do not need a VSM assessment because they are references, not harness entries.

Domain-oriented agent lists are also relevant references, but Awesome VSM Harness should remain differentiated by requiring reviewable harnesses and using VSM evidence to describe organizational control structure.
