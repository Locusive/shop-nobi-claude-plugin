"""Shop Nobi + LlamaIndex.

Connects a LlamaIndex agent to the public Shop Nobi MCP server over Streamable HTTP.
No Nobi sign-in is needed. Set OPENAI_API_KEY, or swap in any LlamaIndex LLM.

    pip install llama-index-tools-mcp llama-index llama-index-llms-openai

Results may include a Nobi click link that forwards to the selling store and may earn Nobi a
commission; verify final price, stock and delivery on that store's site.
"""

import asyncio

from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.tools.mcp import get_tools_from_mcp_url

SHOP_NOBI_MCP_URL = "https://api.nobi.ai/v1/shop/mcp?source=framework_example"


async def main() -> None:
    tools = await get_tools_from_mcp_url(SHOP_NOBI_MCP_URL)  # Shop Nobi tools
    agent = FunctionAgent(tools=tools, llm=OpenAI(model="gpt-4.1"))

    response = await agent.run("Gift ideas for my dad who likes fishing, budget $75.")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
