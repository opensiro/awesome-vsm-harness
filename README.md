<!--lint disable awesome-github-->
# Awesome VSM Harness [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated map of **distinct organizational forms in agent harnesses across real-world domains**, backed by evidence-based [Viable System Model (VSM)](https://github.com/opensiro/vsm-harness-profile) assessments.

This repository is intentionally **not** an exhaustive harness directory. Discovery and assessment live in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index). Awesome VSM Harness selects representative systems from that evidence base to answer a different question:

> What kind of organization does this harness instantiate, and where do operations, coordination, regulation, audit, adaptation, policy, and ultimate authority reside?

Most harness lists are organized around engineering components such as orchestration, context, memory, tools, sandboxing, evaluation, or observability. Domain-oriented agent lists also exist, but usually group applications without comparing their organizational control structure. This list focuses on the intersection: **harnesses × real operating domains × organizational architecture**.

## Contents

- [Scope](#scope)
- [Selection Principle](#selection-principle)
- [How to Read an Entry](#how-to-read-an-entry)
- [Organizational Building Blocks](#organizational-building-blocks)
- [Priority Domain Views](#priority-domain-views)
- [Related Awesome Lists](#related-awesome-lists)

## Scope

The VSM view asks where the following organizational functions live inside a harness.

**S1 — Operations:** units that perform useful work.

**S2 — Coordination:** mechanisms that damp conflicts and synchronize operations.

**S3 — Current-system regulation:** control of the present operational whole.

**S3\* — Independent audit:** channels that inspect operational reality independently of normal management reporting.

**S4 — Adaptation:** mechanisms that model the environment and prepare the organization for change.

**S5 — Policy and identity:** ultimate policy, identity, and authority.

The underlying assessments also record who owns those functions using the OpenSiro `A / C / P / — / ?` notation. Canonical state vectors, evidence, TL;DRs, and rankings remain in the Index rather than being copied here.

A project belongs in this Awesome list because it is a useful **organizational example**, not merely because it is popular, technically capable, or present in another directory.

## Selection Principle

The Index may eventually contain thousands of harnesses. This repository should stay small enough to browse.

Selection optimizes for **domain relevance**: the system is genuinely designed to perform work in the stated domain.

It also optimizes for **organizational distinctiveness**: the system exposes a VSM-relevant organizational form that is not already represented clearly by another entry.

**Evidence quality** matters because the corresponding Index assessment must be complete enough to support the description.

Finally, **current relevance** such as activity, adoption, or contemporary architectural importance may break ties between otherwise similar systems.

Popularity and VSM autonomy rank are not admission scores. A lower-ranked constructor may be more important to include than a higher-ranked autonomous system when it represents a different organizational pattern.

When several projects in the same domain instantiate essentially the same organization, prefer the clearest representative rather than listing every implementation.

## How to Read an Entry

Descriptions here emphasize organizational structure rather than feature inventory.

A useful summary answers three questions:

```text
Mission: what real-world work does the organization perform?
Operations: what acts as S1?
Control and authority: what is distinctive about coordination, regulation,
audit, adaptation, policy, or parent authority?
```

The detailed evidence remains one click away in the Index through `Assessment`, `TL;DR`, and `Ranking` links.

Domain and organizational shape are separate dimensions. Two harnesses in the same domain may implement very different control structures; two harnesses in different domains may share a similar VSM form.

## Organizational Building Blocks

Reusable foundations from which downstream developers construct or specialize an agent organization. These are kept deliberately compact because broad framework coverage belongs in the Index and in other Awesome lists.

- [Agno](https://github.com/agno-agi/agno) - Reusable agent and team runtime in which downstream builders define the operational roles, team topology, and substantial control structure. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/agno.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#agno) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#agno).
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-oriented constructor for creating operational crews and manager-mediated organizations whose final policy and domain closure remain application-defined. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/crewai.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#crewai) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#crewai).
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful graph runtime that lets a downstream system encode coordination and control paths while leaving the organizational meaning of those paths to the application. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/langgraph.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#langgraph) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#langgraph).
- [Microsoft AutoGen AgentChat](https://github.com/microsoft/autogen) - Multi-agent constructor with autonomous participants and team coordination patterns; higher-order organizational closure remains largely application-owned. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/autogen-agentchat.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#autogen-agentchat) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#autogen-agentchat).
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Minimal constructor around tool-using agents, handoffs, guardrails, sessions, and tracing; the application retains responsibility for the broader organization. [Assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/openai-agents-sdk.md) · [TL;DR](https://github.com/opensiro/vsm-harness-index/blob/main/TLDR.md#openai-agents-sdk) · [Ranking](https://github.com/opensiro/vsm-harness-index/blob/main/RANKINGS.md#openai-agents-sdk).

## Priority Domain Views

These are **curation directions**, not empty categories and not a completeness checklist. A domain gets its own curated section only after the Index contains enough assessed systems to show a meaningful organizational contrast through VSM.

<dl>
  <dt><strong>Government &amp; Public Administration</strong></dt>
  <dd>Where do statutory authority, case operations, coordination, independent review, and policy remain?</dd>
  <dt><strong>Cybersecurity &amp; Incident Response</strong></dt>
  <dd>How are responders coordinated, who regulates an incident as a whole, and is verification independent from remediation?</dd>
  <dt><strong>Scientific Discovery &amp; Laboratory Automation</strong></dt>
  <dd>How are experimental workers, resource allocation, independent validation, hypothesis search, and research policy separated?</dd>
  <dt><strong>Industrial &amp; Robotic Operations</strong></dt>
  <dd>Which operational units act locally, how are collisions and shared resources coordinated, and where does safety authority sit?</dd>
  <dt><strong>Enterprise Operations</strong></dt>
  <dd>Can business functions form recursive operational units, and which controls remain organization-wide or parent-owned?</dd>
  <dt><strong>Infrastructure &amp; SRE</strong></dt>
  <dd>How are service operations, incident coordination, operational regulation, independent monitoring, and capacity adaptation divided?</dd>
  <dt><strong>Healthcare Operations</strong></dt>
  <dd>Which decisions are agent-operational, which require coordination or independent review, and which authority must remain clinically parent-governed?</dd>
  <dt><strong>Legal &amp; Compliance Operations</strong></dt>
  <dd>How are execution, interpretation, audit, escalation, policy, and final legal authority separated?</dd>
  <dt><strong>Logistics &amp; Supply Chain</strong></dt>
  <dd>How do fleets, warehouses, planning, conflict resolution, optimization, and demand adaptation form a recursive organization?</dd>
  <dt><strong>Autonomous / Decentralized Organizations</strong></dt>
  <dd>Can policy and ultimate authority be internalized or distributed, and what actually performs S5?</dd>
</dl>

Until a domain reaches that threshold, its candidate harnesses remain discoverable and assessed in the Index rather than being duplicated here. This keeps the Awesome list differentiated from broad domain-oriented agent catalogs and prevents early categories such as coding, browser use, or generic research from dominating the presentation merely because they already have many projects.

## Related Awesome Lists

These lists are complementary discovery sources. Some organize the ecosystem by engineering component; others include domain-specific agents. Awesome VSM Harness differs by using VSM evidence to compare **organizational control structures within and across domains**.

- [Agent Harness for Large Language Model Agents](https://github.com/Gloriaameng/Awesome-Agent-Harness) - Research survey and harness completeness taxonomy centered on execution-loop, tools, context, state, lifecycle, and evaluation components.
- [Agent Systems with Harness Engineering](https://github.com/RUCAIBox/awesome-agent-harness) - Research roadmap organized around harness design, model adaptation, engineering mechanisms, and task benchmarks.
- [Awesome Agent Harness](https://github.com/Picrew/awesome-agent-harness) - Broad implementation-first catalog organized mainly by harness engineering layers such as orchestration, context, sandboxing, protocols, evaluation, observability, and governance.
- [Awesome Harness Engineering](https://github.com/ai-boost/awesome-harness-engineering) - Collection of harness-engineering tools, patterns, memory, permissions, evaluation, MCP, observability, and orchestration resources.
- [Awesome LLM Agents](https://github.com/kaushikb11/awesome-llm-agents) - Broad agent ecosystem list that includes a `Domain-Specific Agents` bucket alongside frameworks, runtimes, infrastructure, and research systems.
- [Awesome Agent](https://github.com/uhub/awesome-agent) - General AI-agent catalog with some business, finance, science, and other domain-oriented sections.
- [Best of Agent Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) - Ranked harness catalog with comparisons, machine-readable data, and recommendation surfaces.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

For **currently tracked work across the bounded VSM Harness OSS group**, start with the shared [`OpenSiro VSM OSS TODO`](https://github.com/opensiro/vsm-oss-organization/blob/main/TODO.md), then return here when the selected task is Awesome-owned. `TODO.md` owns current selection/order only; Awesome remains authoritative for local curation and presentation acceptance.

New harness discovery, missing evidence, and VSM classification changes should go through the [Index contributor entry point](https://github.com/opensiro/vsm-harness-index/blob/main/CONTRIBUTOR_START.md) first. This repository should stay a curated downstream view rather than becoming a second source of truth.

Questions or proposals about **the organization shared by Profile, Skills, Index, and Awesome** — contributor roles, authority boundaries, cross-repository control/coordination, escalation, current-work ordering, milestone sequencing, or the shared contribution workflow — belong in [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). Keep Awesome-specific curation and presentation work here.
