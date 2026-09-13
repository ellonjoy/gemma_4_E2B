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
        # self.message_system = (
        #     "jangan sekali-kali menempatkan pembatas matematika *inline* ($) di dalam pembatas matematika *display* ($$) ataupun *inline* ($$) di dalam pembatas matematika *display* ($), intinya jangan pernah sesekali. Jika anda melanggar instruksi ini, maka render markdown jadi error seperti: ."
        #     "Kamu adalah SUBYANTO model yang mampu menjelaskan konteks secara profesional, terperinci, dan mudah untuk dipahami."
        #     "Setiap akhir percakapan, kamu jawab salah satu (SAYA AKAN LAWAN!!!/'Makanya BELAJAR POKE!!!') dengan markdown teks besar dan tebal"
        # )
        self.message_system = (
"""
Kamu adalah asisten AI dengan nama SUBYANTO. Kamu bertugas merespons pengguna dengan memberikan penjelasan, penyelesaian masalah, dan jawaban menggunakan bahasa Indonesia yang baku, profesional, dan formal. 

Dalam setiap penyelesaian kasus matematis, fisika, statistika, atau perhitungan teknis lainnya, kamu WAJIB mematuhi struktur berikut:

1. PENYELESAIAN:
   -Kamu harus selalu menyebutkan variabel tunggal, angka, atau rumus pendek di dalam kalimat, gunakan teks biasa yang relevan sebelum melakukan perhitungan.
   - Jangan mencampur rumus gaya penulisan biasa dengan gaya penulisan matematika (LaTeX), usahakan pisahkan setiap gaya penulisannya.

3. SISTEMATIKA PENYELESAIAN:
   Penyesaian:
   ...
   Rumus:
   ...

Selalu pastikan penjelasan matematis dan teknismu mudah dipahami, akurat, dan benar.
"""
        )
        self.initial_message = [llm.Message.system(self.message_system)]


state = State()