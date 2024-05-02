import logging
import dotenv

from langchain_openai import ChatOpenAI

from loader import load_document
from chain import EconomicWriterChain

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def main():
    url = input("Enter the URL: ")
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.9)
    document = load_document(url)
    script = EconomicWriterChain(llm).invoke(document)

    with open("output.txt", "w") as f:
        f.write(script)

if __name__ == "__main__":
    main()
