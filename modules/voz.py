import pyttsx3
import speech_recognition as sr

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

    def speak(self, text):
        """Converte texto em fala"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Reconhece fala do usuário"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Fale algo...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                return recognizer.recognize_google(audio, language="pt-BR")
            except:
                return "Não entendi."

# Teste
if __name__ == "__main__":
    voice = VoiceAssistant()
    voice.speak("Olá, eu sou o Jarvis!")
    comando = voice.listen()
    print(f"Você disse: {comando}")
