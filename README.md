# Question-Answer Generator for Llama Fine-tuning

This application generates question-answer pairs from text input using either OpenAI's GPT or Ollama's Llama model. The generated pairs are formatted in a way that's suitable for fine-tuning Llama models.

## Features

- Generate question-answer pairs from text input
- Support for both OpenAI GPT and Ollama APIs
- Configurable generation parameters
- JSON output format suitable for fine-tuning
- Command-line interface

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

## Usage

### Basic Usage

Generate QA pairs using OpenAI (default):
```bash
python qa_generator.py input.txt output.json
```

Generate QA pairs using Ollama:
```bash
python qa_generator.py input.txt output.json --use-ollama
```

### Output Format

The generated QA pairs will be saved in JSON format in the `qa_pairs` directory:
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
- `MAX_QUESTIONS_PER_TEXT`: Number of QA pairs to generate per text
- `TEMPERATURE`: Controls randomness in generation
- `MAX_TOKENS`: Maximum tokens for generation
- `OUTPUT_DIR`: Directory for saving generated QA pairs

## Requirements

- Python 3.7+
- OpenAI API key (if using OpenAI)
- Ollama installation (if using Ollama)
- Required Python packages (see requirements.txt) 