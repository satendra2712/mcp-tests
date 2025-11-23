import mcp
import mcp.client
import mcp.server
import mcp.server.stdio
import mcp.types

print("mcp.client:", dir(mcp.client))
print("mcp.server:", dir(mcp.server))
print("mcp.server.stdio:", dir(mcp.server.stdio))
try:
    import mcp.client.stdio
    print("mcp.client.stdio:", dir(mcp.client.stdio))
except ImportError:
    print("mcp.client.stdio not found")
