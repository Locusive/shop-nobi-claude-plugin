// Shop Nobi + Vercel AI SDK.
//
// Connects the AI SDK to the public Shop Nobi MCP server over Streamable HTTP.
// No Nobi sign-in is needed. Set OPENAI_API_KEY.
//
//   npm i ai @ai-sdk/openai
//
// createMCPClient currently ships from the `ai` package; some newer setups import it from
// `@ai-sdk/mcp`. Check your installed version.
//
// Results may include a Nobi click link that forwards to the selling store and may earn Nobi a
// commission; check final price, stock and delivery on that store's site.

import { experimental_createMCPClient as createMCPClient, generateText } from "ai";
import { openai } from "@ai-sdk/openai";

const SHOP_NOBI_MCP_URL = "https://api.nobi.ai/v1/shop/mcp";

const client = await createMCPClient({
  transport: { type: "http", url: SHOP_NOBI_MCP_URL }, // Streamable HTTP for remote servers
});

try {
  const tools = await client.tools(); // search_products plus the other Shop Nobi tools
  const { text } = await generateText({
    model: openai("gpt-4.1"),
    tools,
    maxSteps: 5,
    prompt: "Compare two good linen shirts under $120 and tell me which to buy.",
  });
  console.log(text);
} finally {
  await client.close();
}
