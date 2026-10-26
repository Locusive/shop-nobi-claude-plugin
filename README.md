# Shop Nobi search engine for agents

Shop Nobi is an online search engine. This repository connects Claude Code and Cursor to its public, read-only MCP tools, which currently search product listings from curated online stores. The tools do not search service listings or place orders.

This plugin adds two things to Claude Code:

- The Shop Nobi connector. It gives Claude two tools, `search_products` and `find_shop_nobi_page`, from https://api.nobi.ai/v1/shop/mcp. No Nobi sign-in is needed.
- The shop-nobi skill. It guides Claude through product search, a gift finder (5 picks with one-line reasons) and a side-by-side compare table.

Search text is sent to api.nobi.ai. Results may include a Nobi click link that forwards to the selling store. Final price, stock and delivery should be checked on that store's site. Some links may earn Nobi a commission; the skill displays a returned disclosure next to the link.

## Install in Claude Code

Run these in your terminal.

```
claude plugin marketplace add Locusive/shop-nobi-claude-plugin
claude plugin install shop-nobi@locusive
```

You can also run the same steps inside Claude Code:

```
/plugin marketplace add Locusive/shop-nobi-claude-plugin
/plugin install shop-nobi@locusive
```

## Install in Cursor

This repository also contains a Cursor plugin manifest and MCP configuration. Until Cursor approves a marketplace listing, you can add the same public MCP endpoint to a project at `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "shop-nobi": {
      "type": "http",
      "url": "https://api.nobi.ai/v1/shop/mcp"
    }
  }
}
```

Open Cursor's MCP settings to confirm the connection, then ask its agent to search Shop Nobi for a product. The server currently searches product listings only. It does not search services, place orders, or guarantee current price or availability.

## Try it

- "Find me a waterproof jacket under $200."
- "Gift ideas for my dad. He likes fishing. Budget $75."
- "Compare these two: <product 1> and <product 2>."

To inspect a real MCP product response before installing the plugin, clone this repository and run `node examples/try-search.mjs "linen dress for a summer wedding under $150"` from its root with Node 18 or newer. This optional example uses no package dependencies or account, and is not run by the plugin. Its query is sent to Shop Nobi; our own runs of it are operator tests, not outside adoption.

For other MCP clients, see the [setup page](https://nobi.ai/shop/mcp), [Shop Nobi documentation](https://docs.nobi.ai/shop-nobi/), and [plain Markdown tool and response guide](https://nobi.ai/shop-nobi-mcp.md).

## What the skill does

- Product requests: searches with your words and shows the fields returned for each product. Store, price, image and link may be absent.
- Links: some links show a label such as "We may earn a commission". The skill shows that label next to the link.
- Gift finder: asks who the gift is for, the occasion and the budget if missing, runs 2 to 4 searches, and returns 5 picks.
- Compare: searches each product you name and returns a table with a one-line recommendation.

## Files

- .cursor-plugin/plugin.json and mcp.json: the Cursor plugin and remote MCP connection.
- .claude-plugin/marketplace.json: lists the plugin for the marketplace.
- plugins/shop-nobi/.claude-plugin/plugin.json: plugin name, version and author.
- plugins/shop-nobi/.mcp.json: the Shop Nobi connector.
- plugins/shop-nobi/skills/shop-nobi/SKILL.md: the skill.
- plugins/shop-nobi/README.md: the directory listing text.
- examples/try-search.mjs: optional no-account live response example.
- LICENSE: MIT.
