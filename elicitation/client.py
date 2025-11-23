import asyncio
import sys
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession
from mcp.types import CreateMessageRequestParams, CreateMessageResult, TextContent

async def sampling_handler(session: ClientSession, request: CreateMessageRequestParams) -> CreateMessageResult:
    """
    Handles sampling requests from the server.
    """
    prompt = ""
    for msg in request.messages:
        if msg.content:
            if isinstance(msg.content, TextContent):
                prompt += msg.content.text
            elif isinstance(msg.content, list):
                 for c in msg.content:
                    if isinstance(c, TextContent):
                        prompt += c.text

    print(f"[Client] Server asked: {prompt}")

    # Simulate user input or just return a static response
    response = "I am doing well, thank you!"
    
    return CreateMessageResult(
        role="assistant",
        content=TextContent(type="text", text=response),
        model="test-model",
        stopReason="stop"
    )

async def main():
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=sampling_handler) as session:
            await session.initialize()
            
            print("[Client] Connected to server.")
            
            # Call the tool
            print("[Client] Calling 'ask_user' tool...")
            result = await session.call_tool("ask_user", arguments={"question": "How are you?"})
            
            print("[Client] Tool result:")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
