# client_ai.py
import asyncio
import sys
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from mcp.types import CreateMessageRequestParams, CreateMessageResult, TextContent

async def sampling_handler(session: ClientSession, request: CreateMessageRequestParams) -> CreateMessageResult:
    """
    This is where the client acts like an AI model.
    The server will ask us for text completion here.
    """
    # Get user prompt text (messages list contains text parts)
    prompt = ""
    for msg in request.messages:
        if msg.content:
            if isinstance(msg.content, TextContent):
                prompt += msg.content.text
            elif isinstance(msg.content, list): # Handle list of contents if necessary, though type hint says TextContent | ImageContent | EmbeddedResource
                 for c in msg.content:
                    if isinstance(c, TextContent):
                        prompt += c.text

    print(f"[Client] Server requested LLM completion. Prompt = {prompt!r}")

    # Fake AI model completion
    generated_text = f"(Fake AI Completion) -> {prompt}"

    return CreateMessageResult(
        role="assistant",
        content=TextContent(type="text", text=generated_text),
        model="demo-model",
        stopReason="stop"
    )

async def main():
    # Connect to the server
    # Note: We are running the server from the same directory
    server_params = None
    # We need to construct StdioServerParameters. 
    # Since we can't import it easily without knowing exact path or if it's exported, 
    # let's rely on stdio_client's ability to take command and args.
    
    # Actually stdio_client takes StdioServerParameters.
    from mcp.client.stdio import StdioServerParameters
    
    server_params = StdioServerParameters(
        command="python3",
        args=["server.py"],
        env=None
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write, sampling_callback=sampling_handler) as session:
            await session.initialize()
            
            print("[Client] Connected to server. Calling trigger_sampling tool...")
            
            # List tools to verify
            tools = await session.list_tools()
            print(f"[Client] Available tools: {[t.name for t in tools.tools]}")
            
            # Call the tool
            result = await session.call_tool("trigger_sampling")
            
            print("[Client] Tool result:")
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
