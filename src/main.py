import logging
import dotenv

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import WebBaseLoader

from chain import get_chain

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def load_document(url):
    loader = WebBaseLoader(url)
    return loader.load()

def make_script(llm, document):
    chain = get_chain(llm)
    resp = chain.invoke(
        input={
            "document": document
        }
    )
    return resp

def main():
    url = input("Enter the URL: ")
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.9)
    document = load_document(url)
    script = make_script(llm, document)
    with open("output.txt", "w") as f:
        f.write(script)

if __name__ == "__main__":
    main()
