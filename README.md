# Shop Nobi search engine for agents

Shop Nobi is an online search engine. This repository connects Claude Code and Cursor to its public, read-only MCP tools, which currently search product listings from curated online stores. The tools do not search service listings or place orders.

This plugin adds two things to Claude Code:

- The Shop Nobi connector. It gives Claude six Shop Nobi tools from https://api.nobi.ai/v1/shop/mcp: `search_products`, `find_shop_nobi_page`, `get_product_details`, `compare_products`, `check_price_and_availability` and `find_alternatives`. No Nobi sign-in is needed.
- The shop-nobi skill. It guides Claude through product search, a gift finder (5 picks with one-line reasons) and a side-by-side compare table.

Search text, selected product identifiers and any requested price limits are sent to api.nobi.ai. Results may include a Nobi click link that forwards to the selling store. Final price, stock and delivery should be checked on that store's site. Some links may earn Nobi a commission; the skill displays a returned disclosure next to the link.

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

This repository also contains a Cursor plugin manifest, MCP configuration, and the same product-search skill used by Claude Code. Until Cursor approves a marketplace listing, you can [add the MCP server to Cursor](https://cursor.com/install-mcp?name=shop-nobi&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vYXBpLm5vYmkuYWkvdjEvc2hvcC9tY3A%2Fc291cmNlPWN1cnNvcl9wbHVnaW4iLCJoZWFkZXJzIjp7Ingtbm9iaS1tY3AtY2xpZW50Ijoic2hvcC1ub2JpLWN1cnNvciJ9fQ%3D%3D) if Cursor is installed. This link installs the connection only, not the skill or a reviewed marketplace plugin. You can also add the same public endpoint to a project at `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "shop-nobi": {
      "type": "http",
      "url": "https://api.nobi.ai/v1/shop/mcp?source=cursor_plugin",
      "headers": {
        "x-nobi-mcp-client": "shop-nobi-cursor"
      }
    }
  }
}
```

Open Cursor's MCP settings to confirm the connection, then ask its agent to search Shop Nobi for a product. The server currently searches product listings only. It does not search services, place orders, or guarantee current price or availability.

Installed connections include a source label: `claude_plugin` for Claude Code and `cursor_plugin` for Cursor. It identifies the package installation link in Nobi analytics, separately from the client name. A copied configuration keeps its label; it does not prove where someone first found Shop Nobi.

## Product and variant identifiers

Read the live `tools/list` schema before calling a tool. The returned `id` is an opaque Nobi variant identifier, not a Shopify ID or SKU. Nobi `productId` and `variantId`, when exposed, identify our own parent product and selected variant.

When using a Shopify product or variant ID, always include the selling merchant's domain as `storeDomain`, for example `example.com`. Use `sourceProductId` for a Shopify parent product and `sourceVariantId` for a Shopify variant, only when the live `get_product_details` schema advertises those arguments:

```json
{"sourceProductId":"123456789","storeDomain":"example.com"}
```

```json
{"sourceVariantId":"987654321","storeDomain":"example.com"}
```

These IDs and domain are illustrative; use the actual catalog ID and merchant hostname. A known Nobi `merchantId` is an alternative merchant context where supported. SKUs also require merchant context. Never resolve source IDs or SKUs globally, guess a merchant, or put a Shopify ID into Nobi `id`, `productId` or `variantId` fields.

If the available schema accepts only `id`, use the Nobi variant ID returned by `search_products` rather than sending unsupported source-ID arguments. Comparison, price/availability and alternatives tools use returned Nobi variant IDs. A parent lookup returns variant choices; select a variant before reporting its price or stock.

[Full identifier and response guide](https://docs.nobi.ai/shop-nobi-mcp-response/).

## Try it

- "Find me a waterproof jacket under $200."
- "Gift ideas for my dad. He likes fishing. Budget $75."
- "Compare these two: <product 1> and <product 2>."

To inspect a real MCP product response before installing the plugin, clone this repository and run `node examples/try-search.mjs "linen dress for a summer wedding under $150"` from its root with Node 18 or newer. This optional example uses no package dependencies or account, and is not run by the plugin. Its query is sent to Shop Nobi; our own runs of it are operator tests, not outside adoption.

For other MCP clients, see the [setup page](https://nobi.ai/shop/mcp), [Shop Nobi documentation](https://docs.nobi.ai/shop-nobi-connector/), and [plain Markdown tool and response guide](https://nobi.ai/shop-nobi-mcp.md). To build an agent that searches products through Shop Nobi, see the recipes in [`examples/`](examples/).

## What the skill does

- Product requests: searches with your words and shows the returned catalog fields. Store, price, image and link may be absent.
- Product details: reads descriptions, specifications, images and variant choices for a result.
- Price and stock: checks one or more results against the latest catalog data.
- Alternatives: finds similar catalog listings, with an optional price ceiling.
- Links: some links show a label such as "We may earn a commission". The skill shows that label next to the link.
- Gift finder: asks who the gift is for, the occasion and the budget if missing, runs 2 to 4 searches, and returns 5 picks.
- Compare: resolves each named product through search, uses the comparison tool and returns a table with a one-line recommendation based on the returned facts.

## Files

- .cursor-plugin/plugin.json and mcp.json: the Cursor plugin, shared product-search skill, and remote MCP connection.
- .claude-plugin/marketplace.json: lists the plugin for the marketplace.
- plugins/shop-nobi/.claude-plugin/plugin.json: plugin name, version and author.
- plugins/shop-nobi/.mcp.json: the Shop Nobi connector.
- plugins/shop-nobi/skills/shop-nobi/SKILL.md: the skill.
- plugins/shop-nobi/README.md: the directory listing text.
- examples/try-search.mjs: optional no-account live response example.
- examples/README.md and the *_shop_agent files: recipes for LangChain, LlamaIndex, the Vercel AI SDK and the OpenAI Agents SDK.
- LICENSE: MIT.
