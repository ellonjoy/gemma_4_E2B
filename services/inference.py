import litert_lm as llm
import asyncio


async def inferance(conversation, prompt):
    stream = conversation.send_message_async(prompt)
    out = ""

    for chunk in stream:
        for item in chunk.get("content", []):
            if item["type"] == "text":
                out += item["text"]
                yield out
                await asyncio.sleep(.01)