from pathlib import Path

class State:
    def __init__(self):
        self.model_path = f"{Path(__file__).parent.parent}/../gemma_4_E2B/model/gemma-4-E2B-it.litertlm"
        self.conversation = None
        self.inference = False
        self.chats = []


state = State()