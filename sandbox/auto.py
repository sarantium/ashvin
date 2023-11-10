from dotenv import load_dotenv
from pathlib import Path
import os


# load API keys
dotenv_path = Path(r"C:\Storage\python_projects\ashvin\.env")
load_dotenv(dotenv_path=dotenv_path)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
