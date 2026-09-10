import flet_camera as fc
import litert_lm as llm
from pathlib import Path

class State:
    def __init__(self):
        self.model_path = f"{Path(__file__).parent.parent}/../gemma_4_E2B/model/gemma-4-E2B-it.litertlm"
        self.img_bytes: bytes | None = None
        self.engine = None
        self.conversation = None
        self.inference = False
        self.chats = []
        self.camera = fc.Camera(
            preview_enabled=True
        )
        self.message_system = (
            "Kamu adalah seorang model yang menjelaskan konsep seperti ahli atau senior developer saat berurusan dengan kode yang mampu menjelaskan konteks secara profesional, terperinci, dan mudah untuk dipahami."
            "Setiap akhir percakapan, kamu jawab salah satu (SAYA AKAN LAWAN!!!/BTW, udah imo belum?/BTW, udah punya pacar belum?/'Makanya BELAJAR POKE!!!') dengan markdown teks besar dan tebal"
        )
        self.initial_message = [llm.Message.system(self.message_system)]


state = State()