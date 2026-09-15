<!--lint disable awesome-github-->
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

The VSM view asks where operations, coordination, current whole-system regulation, independent audit, prospective adaptation, identity, policy, and ultimate authority live inside a harness. It also asks who owns those functions: an agent, a downstream constructor, a parent system, nobody in the reviewed distribution, or an unresolved actor.

The underlying assessments use the OpenSiro `A / C / P / — / ?` autonomy notation. The notation and evidence remain in the Index rather than being duplicated here.

## How to Read This List

**Base / Constructor** describes a reusable platform whose downstream user is expected to define or specialize substantial parts of the agent organization, such as roles, policies, coordination, models, authority, or closure paths.

**Applied** describes an opinionated harness already organized to carry out a concrete class of work.

A harness can also belong to a domain view such as software engineering, research, or government. Domain and shape are separate dimensions. Every listed project links to its standalone assessment; if an assessment changes, this list should point to the updated evidence rather than restating VSM states locally.

## Base / Constructor Harnesses

Reusable foundations for building or specializing agent organizations.

- [Agno](https://github.com/agno-agi/agno) - Agent runtime and framework for composing agents and teams with persistent state and team-level execution patterns. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/agno.md).
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for composing role-based agent crews and event-driven flows into application-specific organizations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/crewai.md).
- [LangGraph](https://github.com/langchain-ai/langgraph) - Stateful graph runtime for durable agent workflows and application-defined control paths. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/langgraph.md).
- [Microsoft AutoGen AgentChat](https://github.com/microsoft/autogen) - Multi-agent application framework with reusable team, orchestration, and group-chat patterns. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/autogen-agentchat.md).
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Reusable agent SDK with tools, handoffs, guardrails, sessions, and tracing for application-defined organizations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/openai-agents-sdk.md).

## Applied Harnesses

Opinionated systems organized around a concrete class of work.

### Software Engineering

- [Cline](https://github.com/cline/cline) - Coding harness for autonomous repository and terminal work with editor integration, tools, feedback, and extensible team surfaces. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/cline.md).
- [OpenHands](https://github.com/OpenHands/OpenHands) - Software-engineering harness for repository work, coding-agent execution, and automation across isolated conversations and backends. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/openhands.md).
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Software-engineering harness centered on an agent-computer interface for issue-to-patch repository work. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/swe-agent.md).

### Browser and Web

- [Browser Use](https://github.com/browser-use/browser-use) - Browser-focused harness that turns goals into iterative browser actions and observations. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/browser-use.md).
- [Stagehand](https://github.com/browserbase/stagehand) - Browser automation harness combining agentic execution with browser primitives and self-healing interaction. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/stagehand.md).

### Research

- [GPT Researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous research harness with specialized research, writing, and fact-checking workflow roles. [VSM assessment](https://github.com/opensiro/vsm-harness-index/blob/main/assessments/gpt-researcher.md).

### Government and Public Sector

This view is intentionally narrow. A project belongs here because its harness is designed for government or public-sector work, not merely because it is maintained by a government organization or implements generic governance controls.

No entries are included until a completed Index assessment and the domain evidence both support inclusion.

## Related Awesome Lists

These lists are complementary discovery sources. They generally optimize for breadth, harness-engineering resources, feature taxonomy, or project recommendation; Awesome VSM Harness focuses on organizational architecture backed by reproducible assessments.

- [Agent Harness for Large Language Model Agents](https://github.com/Gloriaameng/Awesome-Agent-Harness) - Research-oriented survey, taxonomy, papers, and analyzed harness systems.
- [Agent Systems with Harness Engineering](https://github.com/RUCAIBox/awesome-agent-harness) - Academic survey and reading list centered on harness engineering for agent systems.
- [Awesome Agent Harness](https://github.com/Picrew/awesome-agent-harness) - Large implementation-first catalog spanning harness architecture, context, sandboxes, protocols, evaluation, observability, governance, and reference implementations.
- [Awesome Harness Engineering](https://github.com/ai-boost/awesome-harness-engineering) - Broad collection of harness-engineering foundations, design primitives, tools, patterns, evals, memory, security, and orchestration.
- [Best of Agent Harnesses](https://github.com/RyanAlberts/best-of-Agent-Harnesses) - Ranked harness catalog with comparisons, machine-readable data, and recommendation surfaces.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. New harness discovery, missing evidence, or VSM classification changes should go through the [Index contributor entry point](https://github.com/opensiro/vsm-harness-index/blob/main/CONTRIBUTOR_START.md) first.
