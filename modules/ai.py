import google.generativeai as genai

class GeminiAI:
    def __init__(self, api_key="SUA_CHAVE_AQUI"):
        genai.configure(api_key=api_key)

    def chat(self, prompt):
        """Interage com a IA Gemini"""
        try:
            response = genai.chat(prompt)
            return response['candidates'][0]['content']
        except Exception as e:
            return f"Erro: {e}"

# Teste
if __name__ == "__main__":
    ai = GeminiAI()
    print(ai.chat("Quem é você?"))
