from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt_template = """You are a helpful professional economic news analyst. \
Please analyze the contents of <document> and summarize them in the form of <format>. \
<format> must be written in Korean. \

<document>
{document}
</document>

<format>
관련 분야: 
긍정적인 내용: 
부정적인 내용: 
주요 내용: 
</format>
"""

class EconomicWriterChain():
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