import os
import logging
import dotenv

from langchain_openai import ChatOpenAI

from loader import load_document
from chain import EconomicWriterChain
from feed import NewsFeedParser

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def main():
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.9)
    economic_writer_chain = EconomicWriterChain(llm)
    news_feed_parser = NewsFeedParser()

    feeds = news_feed_parser.fetch_news()[:10]

    mkdir("outputs")
    for feed in feeds:
        logger.info(f"Processing feed: {feed['title'], {feed['link']}}")
        document = load_document(feed['link'])
        summary = economic_writer_chain.invoke(document)
        with open(f"outputs/{feed['title']}.txt", "w") as f:
            f.write(summary)

if __name__ == "__main__":
    main()
