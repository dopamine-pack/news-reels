from typing import List

from langchain_community.document_loaders import WebBaseLoader
from langchain.docstore.document import Document

def load_document(url) -> List[Document]:
    """
    Load documents from a given URL.

    Args:
        url (str): The URL of the web page to load.

    Returns:
        List[Document]: The documents loaded from the web page.
    """
    loader = WebBaseLoader(url)
    documents = loader.load()

    for document in documents:
        document.page_content = document.page_content.replace("\n", "")
        document.page_content = document.page_content.replace("\r", "")
        document.page_content = document.page_content.replace("\t", "")
    
    return documents
