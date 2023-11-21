from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
 
app = Flask(__name__)

# NLTK setup (download if necessary)
nltk.download('punkt')
nltk.download('stopwords')

# Mock database for storing correct answers (Replace this with your data storage)
correct_answers = {
    'q1': 'b',
    'q2': 'b',
    'q3': 'b',
    'q4': 'b',
    'q5': 'b'
}

# Simple text preprocessing using NLTK
def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    return filtered_tokens

# Endpoint to receive and process user answers
@app.route('/submit-answers', methods=['POST'])
def submit_answers():
    user_answers = request.json  # Assuming frontend sends answers as JSON
    
    # NLTK-based text processing example (preprocessing user responses)
    processed_answers = {}
    for q_num, user_answer in user_answers.items():
        tokens = preprocess_text(user_answer)
        processed_answers[q_num] = tokens
    
    # Example response with processed answers
    return jsonify(processed_answers)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
