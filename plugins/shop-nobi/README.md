# Shop Nobi

Shop Nobi is an online search engine. Its public MCP tools currently search product listings from curated online stores, not services or other offerings. Shop Nobi sells nothing itself. Check final price, stock and delivery on the selling store's website.

## What this plugin adds

- The Shop Nobi connector, at https://api.nobi.ai/v1/shop/mcp. It gives Claude six tools: `search_products`, `find_shop_nobi_page`, `get_product_details`, `compare_products`, `check_price_and_availability` and `find_alternatives`. They cover product search, exact-topic shopping pages, catalog details, comparison, price and stock checks, and similar listings. No Nobi sign-in is needed.
- The shop-nobi skill. It guides Claude through product search, a gift finder (5 picks with one-line reasons) and a side-by-side compare table.

## Try it

- "Find me a waterproof jacket under $200."
- "Gift ideas for my dad. He likes fishing. Budget $75."
- "Compare these two: <product 1> and <product 2>."

## What is sent, and where

- Your search text, selected product identifiers, result limits and any price ceiling are sent to api.nobi.ai, which Locusive runs. Like any web request, each call also carries your IP address and the name and version of your Claude app. Shop Nobi records these to count usage and to tie clicks to searches.
- The plugin runs no local code and reads no files.
- A returned product URL may be a Nobi click link that forwards to the selling store. Some links show a label such as "We may earn a commission". The skill shows that label next to the link.

Privacy policy: https://nobi.ai/privacy

Setup and examples: https://nobi.ai/shop/mcp
Agent-readable tool and response guide: https://nobi.ai/shop-nobi-mcp.md
