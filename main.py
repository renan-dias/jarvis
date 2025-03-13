from ui import JarvisUI
from modules.voice import VoiceAssistant
from modules.ai import GeminiAI
from modules.webscraper import WebScraper

class Jarvis:
    def __init__(self):
        """Inicializa os módulos do Jarvis"""
        self.voice = VoiceAssistant()
        self.ai = GeminiAI(api_key="SUA_CHAVE_AQUI")
        self.scraper = WebScraper()
        self.interface = JarvisUI(self)

    def process_command(self, command):
        """Processa os comandos do usuário"""
        command = command.lower()

        if "pesquisar" in command:
            query = command.replace("pesquisar", "").strip()
            return self.scraper.fetch_data(f"https://www.google.com/search?q={query}")

        elif "quem é você" in command:
            return "Eu sou o Jarvis, seu assistente pessoal com inteligência artificial!"

        elif "sair" in command or "fechar" in command:
            self.voice.speak("Até logo!")
            exit()

        else:
            return self.ai.chat(command)

    def run(self):
        """Inicia a interface gráfica"""
        self.interface.run()

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
