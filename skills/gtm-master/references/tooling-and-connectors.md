# Tooling And Connectors

Use this reference when GTM Master needs web, MCP, CLI, browser, API, or private
file access. The suite must run in Codex and Claude Code without hard-coding one
provider or one client.

## Core Rule

S00 and sub-skills request a capability slot, not a vendor.

```text
evidence need -> capability slot -> available MCP / CLI / API / browser / upload
```

The canonical slot list lives in `tools/REGISTRY.md`. S01 keeps a local
`mcp-connectors.md` view for market research jobs, but that file should mirror
the root registry instead of becoming a separate vendor catalog.

## Platform Model

```yaml
Codex:
  use_for:
    - local repo editing
    - local files and generated artifacts
    - browser verification
    - configured MCP servers
    - CLI tools available in the workspace

Claude Code:
  use_for:
    - skill execution in terminal projects
    - configured MCP servers
    - provider CLIs
    - .agents/skills or .claude/skills compatibility
```

Both platforms should expose the same GTM Master behavior because the skill
contracts depend on slots and output schemas, not on a specific connector.

## User-Facing Flow

```text
1. User enters product features/specs, country, and price range.
2. S00 identifies required evidence needs.
3. Runtime checks which capability slots are connected.
4. User authorizes a connector, uses an installed CLI, or uploads files only when needed.
5. Missing connectors become visible data gaps and fallback instructions.
```

The user should not need to understand MCP. They should see plain source states:

```text
connected
needs authorization
not configured
manual upload available
skipped with data gap
```

## MCP vs CLI

Use MCP when the client has a configured server and the operation benefits from
structured tool calls, OAuth-managed access, or repeated agent interaction.

Use CLI when a provider has a stable local command, the user has already
authenticated it, and the task can be scoped to a dry run, read-only report, or
bounded export.

Use manual upload when data is private, sensitive, unsupported by connectors, or
better handled as a user-owned file.

## Connector Selection

Selection order:

```text
official API or approved internal data
-> search / SERP
-> public web extraction
-> structured extraction
-> browser automation
-> specialized provider
-> manual upload
-> assumption with explicit data gap
```

Never escalate to browser automation or broad crawling if search or page
extraction can answer the question.

## Required Logs

Every connector-backed collection must produce:

```text
collection_job_id
active_skill
capability_slot
tool_or_connector_used
query_or_source
country_or_region
status
records_collected
limitations
created_evidence_refs
```

## Private Data

Private sales, COGS, margin, support, NSS/NPS, channel, or creator-rate data must
be labeled as:

```text
excluded_raw
derived_summary_only
approved_for_internal_artifact
approved_for_public_html
local_calculator_only
```

Default to `derived_summary_only` or `local_calculator_only`.
