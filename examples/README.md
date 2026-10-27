# Use Shop Nobi in your own agent

Shop Nobi is a product search engine for the best products online, exposed as a public, read-only MCP server at `https://api.nobi.ai/v1/shop/mcp?source=framework_example`. No sign-in or API key is needed. Point any MCP-capable agent framework at that URL and its product-search tools appear automatically, so these recipes stay short and keep working as new tools are added.

- Canonical tool and response reference: https://nobi.ai/shop-nobi-mcp.md
- Docs: https://docs.nobi.ai/shop-nobi/

Executable recipes and the optional response demo use `?source=framework_example` to identify their configuration in Nobi analytics. It is separate from the client name and stays with copied examples.

Each recipe builds a minimal agent that uses Shop Nobi to search products. Swap in any model; these use an OpenAI model only for brevity.

| Framework | File | Install |
|---|---|---|
| LangChain / LangGraph | `langchain_shop_agent.py` | `pip install langchain-mcp-adapters langgraph "langchain[openai]"` |
| LlamaIndex | `llamaindex_shop_agent.py` | `pip install llama-index-tools-mcp llama-index llama-index-llms-openai` |
| Vercel AI SDK | `vercel_ai_sdk_shop_agent.ts` | `npm i ai @ai-sdk/openai` |
| OpenAI Agents SDK | `openai_agents_sdk_shop_agent.py` | `pip install openai-agents` |

Framework APIs move quickly; check each package's current version before relying on a snippet.

Shop Nobi sells nothing itself. Results may include a Nobi click link that forwards to the selling store and may earn Nobi a commission; final price, stock and delivery should be checked on the store's own site.

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

