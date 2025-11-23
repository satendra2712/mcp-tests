import mcp.server.session
from mcp.server.fastmcp import FastMCP

print("mcp.server.session:", dir(mcp.server.session))
# We can't easily inspect Context return type without running it, but we can guess or check FastMCP.get_context
print("FastMCP.get_context:", FastMCP.get_context)
