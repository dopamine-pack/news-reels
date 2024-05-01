from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt_template = """You are a professional short film writer. \
Write a short film script based on the <document>.
<document>
{document}
</document>

Script must be written in Korean.
Script:
"""

prompt = PromptTemplate.from_template(prompt_template)

def get_chain(llm):
    return prompt | llm | StrOutputParser()
