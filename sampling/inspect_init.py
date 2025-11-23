import inspect
from mcp.client.session import ClientSession

print(inspect.signature(ClientSession.__init__))
