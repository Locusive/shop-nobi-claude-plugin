# Shop Nobi plugin for Claude Code

This plugin adds two things to Claude Code:

- The Shop Nobi connector. It gives Claude two tools, search_products and find_shop_nobi_page, from https://api.nobi.ai/v1/shop/mcp. No sign-in is needed.
- The shop-nobi skill. It guides Claude through product search, a gift finder (5 picks with one-line reasons) and a side-by-side compare table.

Shop Nobi searches the live catalogs of about 900 vetted independent online stores. It sells nothing itself. You buy on the website of the store. Your search text is sent to api.nobi.ai.

## Install

Run these in your terminal. Replace Locusive/shop-nobi-claude-plugin with the GitHub repository that holds this plugin.

```
claude plugin marketplace add Locusive/shop-nobi-claude-plugin
claude plugin install shop-nobi@locusive
```

You can also run the same steps inside Claude Code:

```
/plugin marketplace add Locusive/shop-nobi-claude-plugin
/plugin install shop-nobi@locusive
```

To test from a local copy before the repository is public, pass the folder that holds .claude-plugin/marketplace.json instead of Locusive/shop-nobi-claude-plugin:

```
claude plugin marketplace add /path/to/shop-nobi-plugin
```

## Try it

- "Find me a waterproof jacket under $200."
- "Gift ideas for my dad. He likes fishing. Budget $75."
- "Compare these two: <product 1> and <product 2>."

## What the skill does

- Product requests: searches with your words and shows store, price, stock and link for each product.
- Links: some links show a label such as "We may earn a commission". The skill shows that label next to the link.
- Gift finder: asks who the gift is for, the occasion and the budget if missing, runs 2 to 4 searches, and returns 5 picks.
- Compare: searches each product you name and returns a table with a one-line recommendation.

## Files

- .claude-plugin/marketplace.json: lists the plugin for the marketplace.
- plugins/shop-nobi/.claude-plugin/plugin.json: plugin name, version and author.
- plugins/shop-nobi/.mcp.json: the Shop Nobi connector.
- plugins/shop-nobi/skills/shop-nobi/SKILL.md: the skill.
