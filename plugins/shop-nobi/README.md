# Shop Nobi

Shop Nobi is a product search engine. It searches the live catalogs of about 900 vetted independent online stores. Store catalogs are kept constantly refreshed, so prices and stock are up to date. Shop Nobi sells nothing itself. You buy on the website of the store.

## What this plugin adds

- The Shop Nobi connector, at https://api.nobi.ai/v1/shop/mcp. It gives Claude two tools: search_products finds products, and find_shop_nobi_page finds a Shop Nobi page for a broad topic. No sign-in is needed.
- The shop-nobi skill. It guides Claude through product search, a gift finder (5 picks with one-line reasons) and a side-by-side compare table.

## Try it

- "Find me a waterproof jacket under $200."
- "Gift ideas for my dad. He likes fishing. Budget $75."
- "Compare these two: <product 1> and <product 2>."

## What is sent, and where

- Your search text and the number of results asked for are sent to api.nobi.ai, which Locusive runs. Like any web request, each call also carries your IP address and the name and version of your Claude app. Shop Nobi records these to count usage and to tie clicks to searches.
- The plugin runs no local code and reads no files.
- Product links point to the store's own website. Some links carry tracking tags, and some show a label such as "We may earn a commission". The skill shows that label next to the link.

Privacy policy: https://nobi.ai/privacy
