import litert_lm as llm


def create_conversation_model(engine: llm.Engine, messages: llm.Message.system):
    conversation = engine.create_conversation(messages=messages)
    return conversation