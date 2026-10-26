"""Shop Nobi + OpenAI Agents SDK.

Uses a hosted MCP tool: the Responses API lists and runs the Shop Nobi tools for you, which
works because the server is publicly reachable. No Nobi sign-in is needed. Set OPENAI_API_KEY.

    pip install openai-agents

Results may include a Nobi click link that forwards to the selling store and may earn Nobi a
commission; verify final price, stock and delivery on that store's site.
"""

import asyncio

from agents import Agent, HostedMCPTool, Runner

SHOP_NOBI_MCP_URL = "https://api.nobi.ai/v1/shop/mcp"

agent = Agent(
    name="Product search agent",
    instructions="Use the Shop Nobi tools to find and compare products for the user.",
    tools=[
        HostedMCPTool(
            tool_config={
                "type": "mcp",
                "server_label": "shop_nobi",
                "server_url": SHOP_NOBI_MCP_URL,
                "require_approval": "never",  # Shop Nobi is public and read-only
            }
        )
    ],
)


async def main() -> None:
    result = await Runner.run(agent, "Find waterproof hiking boots under $200 and show the top 3.")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
