# GTM Master Tool Registry

This registry defines the platform-neutral tool layer for GTM Master. Skills
request capability slots; Codex, Claude Code, or another MCP-aware client maps
those slots to available MCP servers, CLI tools, APIs, browser tools, or manual
uploads.

Connector implementations are optional. A missing connector must create a data
gap or manual-upload path, not block the whole report.

## platform_targets

```yaml
platform_targets:
  codex:
    skill_installation: ".agents/skills or the Codex skills directory"
    mcp_usage: "Use configured MCP servers or built-in browser/web tools when available."
    cli_usage: "Run local CLI tools only when credentials and user approval/scope are clear."
    private_data_default: "Prefer upload parsing or local-only calculators for sensitive fields."

  claude_code:
    skill_installation: ".agents/skills with .claude/skills compatibility where needed"
    mcp_usage: "Use configured MCP servers from Claude Code settings."
    cli_usage: "Use zero-dependency CLIs or provider CLIs when installed and authenticated."
    private_data_default: "Do not paste raw private commercial data unless explicitly approved."
```

## capability_slots

```yaml
capability_slots:
  primary_search:
    capabilities: [web_search, serp_search, competitor_discovery]
    integrations: [search-and-serp.md]
    best_for: [local source discovery, competitor discovery, query expansion]

  primary_web_extractor:
    capabilities: [web_scraping, structured_extraction]
    integrations: [web-extraction.md]
    best_for: [public page extraction, product tables, price snippets]

  browser_automation:
    capabilities: [browser_automation]
    integrations: [browser-automation.md]
    best_for: [JavaScript pages, filters, pagination, screenshots]

  marketplace_reviews:
    capabilities: [marketplace_review_mining, structured_extraction]
    integrations: [review-comment-mining.md]
    best_for: [reviews, ratings, verified-buyer signals]

  social_listening:
    capabilities: [social_listening, video_comment_mining]
    integrations: [review-comment-mining.md]
    best_for: [local discussion themes, video comments, creator mentions]

  site_specific_comment_collection:
    capabilities: [site_specific_comment_collection, web_scraping, browser_automation]
    integrations: [review-comment-mining.md]
    best_for: [local forums, specialist media comments, deal communities, Q&A pages]

  price_intelligence:
    capabilities: [price_monitoring, competitor_discovery]
    integrations: [price-intelligence.md]
    best_for: [local_price_corridor, promo floor, discount norms, price anchors]

  translation_and_local_language_processing:
    capabilities: [translation, local_language_query_generation, theme_clustering]
    integrations: [translation-local-language.md]
    best_for: [local-language queries, original phrasing, translated summaries]

  private_file_upload:
    capabilities: [manual_upload, spreadsheet_parse, pdf_parse, private_data_extraction]
    integrations: [private-file-upload.md]
    best_for: [spec sheets, internal sales, NSS/NPS, channel plans, private benchmarks]
```

## Required Runtime Behavior

```text
1. Active skill names evidence needs.
2. S00 maps evidence needs to capability slots.
3. Runtime picks an available MCP, CLI, API, browser tool, or manual upload.
4. Output is normalized into evidence records and collection logs.
5. Missing tools become data gaps with fallback suggestions.
```

## User-Side Setup Summary

Read `tools/integrations/platform-setup.md` when installing GTM Master into
Codex or Claude Code. Read the slot-specific guide only when that capability is
needed by the active skill.
