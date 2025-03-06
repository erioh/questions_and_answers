import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434')

# Model Configuration
OPENAI_MODEL = "gpt-4o-mini"
OLLAMA_MODEL = "llama3.1:8b"

# Generation Settings
MAX_TOKENS = 1000
TEMPERATURE = 0.7
MAX_QUESTIONS_PER_TEXT = 5

# Output Format
OUTPUT_DIR = "qa_pairs" 