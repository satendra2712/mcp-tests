# client_ai.py
import asyncio
from mcp.client import Client
from mcp.server import StdioServerTransport
from mcp.types import SamplingRequest, SamplingResponse, TextContent


class AIClient(Client):
    async def on_sampling(self, request: SamplingRequest) -> SamplingResponse:
        """
        This is where the client acts like an AI model.
        The server will ask us for text completion here.
        """

        # Get user prompt text (messages list contains text parts)
        prompt = ""
        for msg in request.messages:
            if msg.content:
                for c in msg.content:
                    if isinstance(c, TextContent):
                        prompt += c.text

        print(f"[Client] Server requested LLM completion. Prompt = {prompt!r}")

        # Fake AI model completion
        generated_text = f"(Fake AI Completion) → {prompt}"

        return SamplingResponse(
            samples=[
                {
                    "id": "sample-1",
                    "content": [TextContent(type="text", text=generated_text)],
                    "finish_reason": "stop",
                }
            ]
        )


async def main():
    transport = StdioServerTransport()   # server communicates over stdio
    client = AIClient(transport)

    print("[Client] Ready. Waiting for server to request sampling...")
    await client.run()


if __name__ == "__main__":
    asyncio.run(main())
