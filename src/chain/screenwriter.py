from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt_template = """You are a professional short film writer. \
Write a short film script based on the <document>.
Make the content as stimulating as possible.

<document>
{document}
</document>

Script must be written in Korean.
Script:
"""

class ScreenWriterChain():
    def __init__(self, llm):
        prompt = PromptTemplate.from_template(prompt_template)

        self.llm = llm
        self.chain = prompt | llm | StrOutputParser()

    def invoke(self, document):
        return self.chain.invoke(
            input={
                "document": document
            }
        )