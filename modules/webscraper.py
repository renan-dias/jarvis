import requests
from bs4 import BeautifulSoup

class WebScraper:
    def fetch_data(self, url):
        """Coleta informações de um site"""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                return soup.get_text()
            return "Erro ao acessar o site."
        except Exception as e:
            return f"Erro: {e}"

# Teste
if __name__ == "__main__":
    scraper = WebScraper()
    print(scraper.fetch_data("https://www.python.org"))
