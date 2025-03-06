# Question-Answer Generator for Llama Fine-tuning

A web application that generates question-answer pairs from text input using either OpenAI's GPT or Ollama's Llama model. The generated pairs are formatted in a way that's suitable for fine-tuning Llama models.

## Features

- Web-based interface for easy interaction
- Generate question-answer pairs from text input
- Support for both OpenAI GPT and Ollama APIs
- Configurable number of questions
- JSON output format suitable for fine-tuning
- Download generated QA pairs as JSON
- Modern, responsive UI with loading indicators

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
OLLAMA_API_URL=http://localhost:11434  # Optional, defaults to this value
```

3. If using Ollama, make sure you have Ollama installed and running locally with the Llama model pulled.

4. Set up the Flask secret key in `app.py` (change the default value for production).

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Enter your text, select the number of questions, and choose the model (ChatGPT or Ollama)

4. Click "Generate QA Pairs" to process the text

5. View the generated QA pairs and download them as JSON if needed

## Output Format

The generated QA pairs are available in JSON format:
```json
[
  {
    "question": "What is...",
    "answer": "The answer is..."
  },
  ...
]
```

## Configuration

You can modify the following settings in `config.py`:
- `MAX_TOKENS`: Maximum tokens for generation
- `TEMPERATURE`: Controls randomness in generation
- `OUTPUT_DIR`: Directory for saving generated QA pairs

## Requirements

- Python 3.7+
- OpenAI API key (if using OpenAI)
- Ollama installation (if using Ollama)
- Required Python packages (see requirements.txt) 