import customtkinter as ctk
from modules.voice import VoiceAssistant
from modules.ai import GeminiAI

class JarvisUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Renan AI")
        self.window.geometry("800x600")

        self.voice = VoiceAssistant()
        self.ai = GeminiAI(api_key="SUA_CHAVE_AQUI")

        self.chat_label = ctk.CTkLabel(self.window, text="Digite ou Fale:")
        self.chat_label.pack(pady=10)

        self.entry = ctk.CTkEntry(self.window, width=400)
        self.entry.pack()

        self.send_button = ctk.CTkButton(self.window, text="Enviar", command=self.send_message)
        self.send_button.pack(pady=5)

        self.voice_button = ctk.CTkButton(self.window, text="Falar", command=self.speak_message)
        self.voice_button.pack(pady=5)

        self.output_label = ctk.CTkLabel(self.window, text="")
        self.output_label.pack(pady=10)

        self.window.mainloop()

    def send_message(self):
        text = self.entry.get()
        response = self.ai.chat(text)
        self.output_label.configure(text=response)
        self.voice.speak(response)

    def speak_message(self):
        text = self.voice.listen()
        self.entry.delete(0, ctk.END)
        self.entry.insert(0, text)
        self.send_message()

if __name__ == "__main__":
    JarvisUI()
