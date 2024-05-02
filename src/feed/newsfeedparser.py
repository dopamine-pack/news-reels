from typing import List
import feedparser

class NewsFeedParser:
    def __init__(self, urls=[]):
        cnn_url = 'http://rss.cnn.com/rss/money_news_economy.rss'
        bloomberg_url = 'https://feeds.bloomberg.com/economics/news.rss'

        self.urls = [cnn_url, bloomberg_url] + urls

    def fetch_news(self) -> List[dict]:
        news_list: List[dict] = []
        for url in self.urls:
            feed = feedparser.parse(url)
            for entry in feed.entries:
                news_item = {
                    'title': entry.title,
                    'link': entry.link,
                }
                news_list.append(news_item)
        return news_list
