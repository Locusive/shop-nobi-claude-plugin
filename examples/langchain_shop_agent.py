"""Shop Nobi + LangChain / LangGraph.

Connects an agent to the public Shop Nobi MCP server so it can search products.
No Nobi sign-in is needed. Set OPENAI_API_KEY, or swap in any chat model.

    pip install langchain-mcp-adapters langgraph "langchain[openai]"

langchain-mcp-adapters is the MCP bridge; check its current version and home before relying on it.

Results may include a Nobi click link that forwards to the selling store and may earn Nobi a
commission; check final price, stock and delivery on that store's site.
"""

import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

SHOP_NOBI_MCP_URL = "https://api.nobi.ai/v1/shop/mcp?source=framework_example"


async def main() -> None:
    client = MultiServerMCPClient(
        {"shop_nobi": {"url": SHOP_NOBI_MCP_URL, "transport": "streamable_http"}}
    )
    tools = await client.get_tools()  # search_products plus the other Shop Nobi tools
    agent = create_react_agent("openai:gpt-4.1", tools)

    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Find a waterproof jacket under $200."}]}
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
