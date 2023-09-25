from dotenv import load_dotenv
from pathlib import Path
import os
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader, PyPDFLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

loader = WebBaseLoader(
    "https://medium.com/yeagerai/ai-agents-are-taking-us-from-software-to-autonomous-software-c1be5475a15b"
)
loader = WebBaseLoader(
    "https://www.cloudflight.io/en/blog/the-architecture-for-an-entire-vehicle-twin-life/"
)
loader = PyPDFLoader(
    "C:\Storage\python_projects\ashvin\docs\assets\deloitte_digital_twin.pdf"
)
docs = loader.load()
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
chain = load_summarize_chain(llm, chain_type="stuff")
chain1 = load_summarize_chain()

output = chain.run(docs)
print(output)
