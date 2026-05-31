# Platform Setup

Use this guide when a user wants to run GTM Master in Codex or Claude Code.
This is user-side setup, not a required step inside every report run.

## Codex

```text
1. Install or sync the GTM Master skills into the Codex skills directory.
2. Configure MCP servers in the Codex app or local MCP config when a connector is needed.
3. Keep provider credentials in environment variables, keychain storage, or the provider's OAuth flow.
4. Use CLI tools only after checking they are installed and authenticated.
5. Route private files through manual upload or local parsing before public HTML rendering.
```

## Claude Code

```text
1. Install skills into .agents/skills or .claude/skills compatibility paths.
2. Configure MCP servers through Claude Code MCP settings.
3. Use provider CLIs when installed, authenticated, and appropriate for the task.
4. Keep OAuth/API credentials outside skill files and report artifacts.
5. Treat private commercial inputs as restricted unless the user approves derived summaries.
```

## MCP And CLI Decision

```text
Use MCP when:
  the client has a configured server and the action needs structured tool calls.

Use CLI when:
  the provider has a stable local command, credentials are already configured,
  and the command can produce a scoped artifact or dry-run output.

Use manual upload when:
  the source is private, sensitive, not reachable by connector, or user-owned.
```

## Safety

Never require a user to understand MCP internals. The user-facing flow should be:

```text
connect source -> authorize or upload -> run report -> review data gaps
```
