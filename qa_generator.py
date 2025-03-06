import json
import os
from typing import List, Dict, Optional
import requests
from openai import OpenAI
from tqdm import tqdm
import config

class QAGenerator:
    def __init__(self, use_ollama: bool = False):
        self.use_ollama = use_ollama
        if not use_ollama:
            self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        
    def generate_qa_pairs(self, text: str, max_questions: int) -> List[Dict[str, str]]:
        """Generate question-answer pairs from the given text."""
        if self.use_ollama:
            return self._generate_with_ollama(text, max_questions)
        else:
            return self._generate_with_openai(text, max_questions)
    
    def _generate_with_openai(self, text: str, max_questions: int) -> List[Dict[str, str]]:
        """Generate QA pairs using OpenAI API."""
        prompt = f"""Given the following text, generate {max_questions} question-answer pairs.
        Format each pair as a JSON object with 'question' and 'answer' fields.
        Make questions diverse and challenging.
        
        Text:
        {text}
        
        Generate the QA pairs in the following format:
        [
            {{"question": "Q1", "answer": "A1"}},
            {{"question": "Q2", "answer": "A2"}},
            ...
        ]
        """
        
        response = self.client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_TOKENS
        )
        
        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            print("Error: Failed to parse OpenAI response as JSON")
            return []
    
    def _generate_with_ollama(self, text: str, max_questions: int) -> List[Dict[str, str]]:
        """Generate QA pairs using Ollama API."""
        prompt = f"""Given the following text, generate {max_questions} question-answer pairs.
        Format each pair as a JSON object with 'question' and 'answer' fields.
        Make questions diverse and challenging.
        
        Text:
        {text}
        
        Generate the QA pairs in the following format:
        [
            {{"question": "Q1", "answer": "A1"}},
            {{"question": "Q2", "answer": "A2"}},
            ...
        ]
        """
        
        response = requests.post(
            f"{config.OLLAMA_API_URL}/api/generate",
            json={
                "model": config.OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        
        try:
            return json.loads(response.json()["response"])
        except (json.JSONDecodeError, KeyError):
            print("Error: Failed to parse Ollama response as JSON")
            return []

def process_text_file(input_file: str, output_file: str, max_questions: int, use_ollama: bool = False):
    """Process a text file and generate QA pairs."""
    # Create output directory if it doesn't exist
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    
    # Read input text
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Generate QA pairs
    generator = QAGenerator(use_ollama=use_ollama)
    qa_pairs = generator.generate_qa_pairs(text, max_questions)
    
    # Save results
    output_path = os.path.join(config.OUTPUT_DIR, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(qa_pairs, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {len(qa_pairs)} QA pairs and saved to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate QA pairs from text')
    parser.add_argument('input_file', help='Input text file')
    parser.add_argument('output_file', help='Output JSON file name')
    parser.add_argument('max_questions', help='Maximum number of questions to generate')

    parser.add_argument('--use-ollama', action='store_true', help='Use Ollama instead of OpenAI')
    
    args = parser.parse_args()
    process_text_file(args.input_file, args.output_file, args.max_questions, args.use_ollama) 