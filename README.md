# Awesome VSM Harness [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated map of agent harnesses by organizational architecture, backed by evidence-based [Viable System Model (VSM)](https://github.com/opensiro/vsm-harness-profile) assessments.

This is **not** another exhaustive catalog of agent tools. Harness discovery and VSM assessment are maintained independently in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index). This list selects useful and representative systems from that evidence base and organizes them for human discovery.

## Contents

- [Scope](#scope)
- [How to Read This List](#how-to-read-this-list)
- [Base / Constructor Harnesses](#base--constructor-harnesses)
- [Applied Harnesses](#applied-harnesses)
  - [Software Engineering](#software-engineering)
  - [Browser and Web](#browser-and-web)
  - [Research](#research)
  - [Government and Public Sector](#government-and-public-sector)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## Scope

The VSM view asks organizational questions that ordinary feature taxonomies usually do not:

- What are the operational units of the harness?
- How are those units coordinated?
- Where does current whole-system regulation live?
- Is there an independent audit or challenge path?
- Where does prospective adaptation happen?
- Where do identity, policy, and ultimate authority close?
- Which of those functions are agent-owned, composable, parent-governed, absent, or still unresolved?

The underlying assessments use the OpenSiro `A / C / P / — / ?` autonomy notation. The notation and evidence live in the [VSM Harness Index](https://github.com/opensiro/vsm-harness-index), not in this repository.

## How to Read This List

**Base / Constructor** and **Applied** describe the shape of a harness, not its quality.

- **Base / Constructor** — a reusable platform whose downstream user is expected to define or specialize substantial parts of the agent organization: roles, policies, coordination, models, authority, or closure paths.
- **Applied** — an opinionated harness already organized to carry out a concrete class of work.

A harness can also belong to a domain view such as software engineering, research, or government. Domain and shape are separate dimensions.

Every listed project links to its standalone assessment in the Index. If the assessment changes, this list should link to the new evidence rather than restating VSM states locally.

## Base / Constructor Harnesses

Reusable foundations for building or specializing agent organizations.

- [Agno](https://github.com/agno-agi/agno) — Agent runtime and framework for composing agents and teams with persistent state and team-level execution patterns. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/agno.md).
- [Microsoft AutoGen AgentChat](https://github.com/microsoft/autogen) — Multi-agent application framework with reusable team, orchestration, and group-chat patterns. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/autogen-agentchat.md).
- [LangGraph](https://github.com/langchain-ai/langgraph) — Stateful graph runtime for durable agent workflows and application-defined control paths. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/langgraph.md).
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) — Reusable agent SDK with tools, handoffs, guardrails, sessions, and tracing for application-defined organizations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/openai-agents-sdk.md).
- [CrewAI](https://github.com/crewAIInc/crewAI) — Framework for composing role-based agent crews and event-driven flows into application-specific organizations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/crewai.md).

## Applied Harnesses

Opinionated systems organized around a concrete class of work.

### Software Engineering

- [OpenHands](https://github.com/OpenHands/OpenHands) — Software-engineering harness for repository work, coding-agent execution, and automation across isolated conversations and backends. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/openhands.md).
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) — Software-engineering harness centered on an agent-computer interface for issue-to-patch repository work. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/swe-agent.md).
- [Cline](https://github.com/cline/cline) — Coding harness for autonomous repository and terminal work with editor integration, tools, feedback, and extensible team surfaces. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/cline.md).

### Browser and Web

- [Browser Use](https://github.com/browser-use/browser-use) — Browser-focused harness that turns goals into iterative browser actions and observations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/browser-use.md).
- [Stagehand](https://github.com/browserbase/stagehand) — Browser automation harness combining agentic execution with browser primitives and self-healing interaction. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/stagehand.md).

### Research

- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) — Autonomous research harness with specialized research, writing, and fact-checking workflow roles. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/gpt-researcher.md).

### Government and Public Sector

This view is intentionally narrow. A project belongs here because its harness is designed for government or public-sector work, not merely because it is maintained by a government organization or implements generic governance controls.

No entries are included until a completed Index assessment and the domain evidence both support inclusion.

## Related Awesome Lists

These lists are complementary discovery sources. They generally optimize for breadth, harness-engineering resources, feature taxonomy, or project recommendation; Awesome VSM Harness focuses on organizational architecture backed by reproducible assessments.

- [Awesome Harness Engineering](https://github.com/ai-boost/awesome-harness-engineering) — Broad collection of harness-engineering foundations, design primitives, tools, patterns, evals, memory, security, and orchestration.
- [Awesome Agent Harness](https://github.com/Picrew/awesome-agent-harness) — Large implementation-first catalog spanning harness architecture, context, sandboxes, protocols, evaluation, observability, governance, and reference implementations.
- [Best of Agent Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) — Ranked harness catalog with comparisons, machine-readable data, and recommendation surfaces.
- [Agent Systems with Harness Engineering](https://github.com/RUCAIBox/awesome-agent-harness) — Academic survey and reading list centered on harness engineering for agent systems.
- [Agent Harness for Large Language Model Agents](https://github.com/Gloriaameng/Awesome-Agent-Harness) — Research-oriented survey, taxonomy, papers, and analyzed harness systems.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

The short version: this repository is a **curated view**, not the indexing pipeline. New harness discovery, missing evidence, or VSM classification changes belong in [opensiro/vsm-harness-index](https://github.com/opensiro/vsm-harness-index) first.

## License

[CC0 1.0 Universal](LICENSE).