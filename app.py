from flask import Flask, render_template, request, flash, redirect, url_for
from qa_generator import QAGenerator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qa():
    try:
        text = request.form.get('text', '').strip()
        num_questions = int(request.form.get('num_questions', 5))
        model = request.form.get('model', 'openai')

        if not text:
            flash('Please provide some text to generate questions from.', 'warning')
            return redirect(url_for('index'))

        if num_questions < 1 or num_questions > 20:
            flash('Number of questions must be between 1 and 20.', 'warning')
            return redirect(url_for('index'))

        # Initialize generator with selected model
        generator = QAGenerator(use_ollama=(model == 'ollama'))
        
        # Generate QA pairs
        qa_pairs = generator.generate_qa_pairs(text, num_questions)
        
        if not qa_pairs:
            flash('Failed to generate QA pairs. Please try again.', 'danger')
            return redirect(url_for('index'))

        return render_template('index.html', qa_pairs=qa_pairs)

    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 