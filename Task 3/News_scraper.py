# news_scraper.py
import requests
from bs4 import BeautifulSoup


URL = 'https://www.bbc.com/news'  # or try https://www.ndtv.com/latest

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all(['h3', 'h2'])

    with open("Task 3/headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                file.write(text + "\n")

    print("✅ Headlines saved to headlines.txt!")
else:
    print(f"❌ Failed to fetch page. Status code: {response.status_code}")
