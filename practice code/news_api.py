import requests

# Your NewsAPI key
API_KEY = '92fa2d0b0c2a4e6bab573740ce744f1c'

# Function to fetch news for a given topic
def fetch_news(topic, language='en'):
    url = f'https://newsapi.org/v2/everything?q={topic}&language={language}&apiKey={API_KEY}'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        news_data = response.json()
        return news_data['articles']
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return None

# Fetch news for different topics
topics = ['technology', 'health', 'sports', 'business', 'entertainment']
news_by_topic = {}

for topic in topics:
    news_by_topic[topic] = fetch_news(topic)

# Print out the news titles for each topic
for topic, articles in news_by_topic.items():
    if articles:
        print(f"\nNews about {topic.capitalize()}:")
        for article in articles[:5]:  # Print the first 5 articles
            print(f"- {article['title']}")
    else:
        print(f"No news found for {topic}")
