import requests
import json

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    CYAN = '\033[96m'

API_KEY = '92fa2d0b0c2a4e6bab573740ce744f1c'
language = 'en'
topic = input("Enter the name of the topic: ")
url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&q={topic}&language={language}&apiKey={API_KEY}'
r = requests.get(url)
news = json.loads(r.text)

if 'articles' in news and news['articles']:
    for article in news['articles']:
        print(f'The Title is "{color.BOLD + color.CYAN + article["title"] + color.END}"')
        print(f'The Article is \n{article["description"]}')
        print("______________________________________________________")
else:
    print("No articles found or there was an error with the request.")
