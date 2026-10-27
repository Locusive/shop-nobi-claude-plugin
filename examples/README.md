# Use Shop Nobi in your own agent

Shop Nobi is a product search engine for the best products online, exposed as a public, read-only MCP server at `https://api.nobi.ai/v1/shop/mcp`. No sign-in or API key is needed. Point any MCP-capable agent framework at that URL and its product-search tools appear automatically, so these recipes stay short and keep working as new tools are added.

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
