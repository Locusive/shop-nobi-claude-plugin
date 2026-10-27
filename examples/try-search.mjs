#!/usr/bin/env node

// Optional smoke test for the public Shop Nobi MCP server. Node 18+ is required.
const endpoint = "https://api.nobi.ai/v1/shop/mcp?source=framework_example";
const query = process.argv.slice(2).join(" ").trim() || "linen dress for a summer wedding under $150";
const headers = {
  "content-type": "application/json",
  accept: "application/json, text/event-stream",
};

async function request(method, params, id) {
  const response = await fetch(endpoint, {
    method: "POST",
    headers,
    signal: AbortSignal.timeout(15000),
    body: JSON.stringify({ jsonrpc: "2.0", ...(id === undefined ? {} : { id }), method, params }),
  });
  if (!response.ok) throw new Error(`${method} returned HTTP ${response.status}`);
  const sessionId = response.headers.get("mcp-session-id");
  if (sessionId) headers["mcp-session-id"] = sessionId;
  if (id === undefined) return null;

  const message = await response.json();
  if (message.error) throw new Error(`${method}: ${message.error.message}`);
  return message.result;
}

try {
  await request("initialize", {
    protocolVersion: "2025-03-26",
    capabilities: {},
    clientInfo: { name: "shop-nobi-example", version: "1.0.0" },
  }, 1);
  headers["mcp-protocol-version"] = "2025-03-26";
  await request("notifications/initialized", {}, undefined);

  const listed = await request("tools/list", {}, 2);
  if (!listed.tools?.some(tool => tool.name === "search_products")) {
    throw new Error("search_products is not available");
  }

  const result = await request("tools/call", {
    name: "search_products",
    arguments: { query, limit: 3 },
  }, 3);
  if (result.isError) throw new Error(result.content?.[0]?.text || "Search failed");
  const products = result.structuredContent?.products;
  if (!Array.isArray(products)) throw new Error("Search returned no structured products array");

  console.log(`Search: ${query}`);
  if (products.length === 0) console.log("No matching products returned.");
  for (const product of products) {
    const price = product.price == null ? "price not listed" : `${product.currency} ${product.price}`;
    console.log(`\n${product.name} | ${product.store || "store not listed"} | ${price}`);
    if (product.url) console.log(product.url);
    if (product.linkLabel) console.log(product.linkLabel);
  }
  console.log("\nCheck final price, stock, and delivery on the seller's site.");
} catch (error) {
  console.error(`Shop Nobi MCP example failed: ${error.message}`);
  process.exitCode = 1;
}
