# Contributing

Thanks for helping improve Awesome VSM Harness.

This repository is a **curated presentation layer** over the independently maintained [VSM Harness Index](https://github.com/opensiro/vsm-harness-index). It is not the place where harnesses are first discovered or where VSM states are decided.

## Before You Add a Harness

A project should normally satisfy all of the following:

1. It is an agent harness, agent runtime, or closely related system where organizational structure is meaningful.
2. It already has a completed standalone assessment in `opensiro/vsm-harness-index`.
3. There is a clear reason a reader would benefit from seeing it in this curated list.
4. Its proposed shape and domain placement can be explained without inventing new VSM claims in this repository.

If a project has not been assessed yet, propose or queue it in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index) first.

## What Belongs Where

### Base / Constructor

Use this section when the project is primarily a reusable foundation from which downstream developers construct or specialize an agent organization.

Typical signals include first-party surfaces for composing roles, policies, models, coordination, authority, or other organizational decision rights.

### Applied

Use this section when the project ships an opinionated organization for carrying out a concrete class of work, such as software engineering, browser operation, research, science, or another domain.

### Government and Public Sector

Use this domain only when the harness is actually designed for government or public-sector work.

Government ownership alone is not enough. Generic governance, policy, safety, or control-plane functionality also does not make a project a government harness.

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

## Entry Format

Keep entries concise and consistent:

```md
- [Project](https://github.com/org/repo) — One sentence explaining why the project is useful in this section. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/project.md).
```

Descriptions should explain the project's relevant harness shape or domain role, not repeat marketing copy.

## Curation Standard

Awesome VSM Harness is intentionally not exhaustive.

Prefer projects that are useful, representative, distinctive, or important for understanding the harness landscape. Do not add a project merely to increase coverage or because it appears in another Awesome list.

When several near-identical projects exist, prefer the entry that gives the reader the clearest architectural contrast.

## Pull Requests

Keep a pull request focused on one logical change where practical.

For a new entry, include:

- the upstream repository;
- the existing VSM assessment link;
- proposed section and domain;
- one short reason the project improves the curated map.

For a move between sections, explain what changed in the project or in the interpretation of its product shape.

## Related Lists

Broad ecosystem lists are welcome in `Related Awesome Lists` when they provide a genuinely complementary discovery surface. They do not need a VSM assessment because they are references, not harness entries.