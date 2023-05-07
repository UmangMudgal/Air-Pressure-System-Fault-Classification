import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Reading the Mongo DB URL
MONGODB_URL_KEY = os.getenv("MONGODB_URL_KEY")
