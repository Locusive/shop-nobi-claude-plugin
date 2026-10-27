---
name: shop-nobi
description: Find, inspect, compare and choose products from curated online stores using Shop Nobi catalog tools. Use when the user wants to find a product, compare products, pick one to buy, get gift ideas, or asks for something like "best X under $Y", "where can I buy" or "which one should I get".
---

# Shop Nobi

Shop Nobi is an online search engine. Its MCP tools currently search product listings from curated online stores, not services or other offerings. Product prices and availability may lag behind the store. It sells nothing itself; the shopper buys on the selling store's website.

## Tools

- search_products: finds catalog listings from a plain-language request. Use it to resolve a named product or discover options.
- get_product_details: reads one result's description, specifications, images and variant choices. Pass its returned id.
- compare_products: compares 2 to 10 search results using their returned ids.
- check_price_and_availability: checks catalog price and stock for 1 to 20 returned ids. Catalog data may lag behind the selling store.
- find_alternatives: finds similar listings using one returned id. An optional maxPrice uses that result's currency; limit is 1 to 10, default 5.
- find_shop_nobi_page: finds an existing Shop Nobi page for an exact product topic, such as "leather boots". If a page comes back, share its title and link. If none is found, do not invent or substitute a broader page.

The current tool schemas define the supported arguments. A returned id identifies a Nobi catalog variant selection; treat it as opaque. It is not a SKU, a Shopify product ID or a Shopify variant ID. Do not construct or guess IDs. If a lookup says found=false, report that it could not find the listing and search again when useful.

## Searching

- Use the words the shopper uses as the query. Keep the details that matter, such as use, size, color, budget, recipient or occasion. Example: "linen dress for a summer wedding under $150".
- The default is 10 results. Set limit (1 to 20) to ask for more or fewer.
- If no products come back, try one broader query. If still nothing, say no matches were found.
- Use only products from the tool results. Do not add products from memory.

## Showing products

For each product, show:

- Name.
- Store. Write "store not listed" when it is empty.
- Price with currency. Write "price not listed" when it is empty.
- In stock or out of stock, from inStock.
- Link, from url, exactly as returned. Write "no link" when url is empty.
- linkLabel, when it is set. Show it next to that product link, word for word. Example: [Store page] We may earn a commission.

Do not shorten, edit or remove the link or the tags in it.
The returned URL may be a Nobi click link that forwards to the seller. Check final price, stock and delivery on the seller's site.

State only facts from the results. For a question about materials, specifications, descriptions or variant choices, call get_product_details and use the returned catalog fields. Say when a requested detail is absent. The catalog contains no reviews, ratings or price history. Do not infer specifications from a product name.

## Gift finder

Use this when the user asks for gift ideas.

1. Ask for anything missing: who the gift is for, the occasion and the budget. Ask in one short message. Skip anything the user already said.
2. Run 2 to 4 focused searches. Give each search one angle, such as a hobby, a style or a practical need. Put the budget in each query.
3. Return 5 picks. For each pick, show the name, store, price, stock and link (with linkLabel), then one line on why it fits the recipient.
4. If fewer than 5 products fit, return the ones that do and say so.

Keep each reason factual. Say what the product offers the recipient, such as "fits a budget under $50 and suits a fishing hobby". Do not call a pick perfect.

## Compare

Use this when the user asks to compare products or choose between them.

1. Search for each product the user names. Run extra searches only when a product is not found.
2. Pass the selected result ids to compare_products. Use get_product_details if a shopper asks about information beyond the comparison.
3. Show one table with a column per selected product. Include store, price, stock, relevant returned attributes and link. Mark missing values as "not in results".
4. Add a one-line recommendation based on the returned price, stock and attributes. Say why.

## Follow-up requests

- Use check_price_and_availability for a price or stock recheck of selected results. State that the selling store has the final price and availability.
- Use find_alternatives for similar options. Apply maxPrice only in the source result's currency. If no alternatives are returned, say so.
- Preserve returned links and any linkLabel on detail, comparison and alternative results just as on search results.

## Style

- Start with the answer.
- Use plain words and short sentences.
- Keep lists and table cells short.
