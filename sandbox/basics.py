# load OpenAI key
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# example one : basic direct use of llm and prompt
from langchain.llms import OpenAI  # import llm

llm = OpenAI(temperature=0.7)  # instance llm
prompt = "what is the population of India"  # prompt as string with no other inputs
# predict = llm(prompt)  # output in variable

# print(type(predict))  # output is string class
# print(predict)  # output is string

# example two : use of prompt template
from langchain.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template(
    "list the top five most {adjective} {items}"
)

prompt_template.format(adjective="livable", items="capital cities")
full_prompt = prompt_template.format(adjective="livable", items="capital cities")

# example three : use of basic LLMchain
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt_template)
inputs = {"adjective": "livable", "items": "capital cities"}
output = chain.run(inputs)
print(output)
