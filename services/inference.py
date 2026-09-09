import asyncio
import litert_lm as llm


async def inferance(conversation, prompt, img_byte=None):
    stream = None
    out = ""
    if img_byte is not None:
        multimodal_prompt = llm.Contents.of(
            llm.Content.ImageBytes(img_byte),
            prompt
        )
        stream = conversation.send_message_async(multimodal_prompt)
    else:
        stream = conversation.send_message_async(prompt)

    for chunk in stream:
        for item in chunk.get("content", []):
            if item["type"] == "text":
                out += item["text"]
                yield out
                await asyncio.sleep(.01)