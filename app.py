from flask import Flask, render_template, jsonify, request
from utils.facial_expression import start_facial_expression_thread, stop_camera
from utils.grammar_analysis import grammar_check
from utils.keyword_analysis import evaluate_keywords
from utils.speech_feedback import provide_feedback
from config import DEBUG_MODE, PORT, HOST
import threading
import speech_recognition as sr

app = Flask(__name__)

questions_keywords = [
    {"question": "Tell me about yourself.", "keywords": ["experience", "skills", "background"]},
    {"question": "Why do you want to work here?", "keywords": ["company", "values", "mission"]},
    {"question": "What are your strengths?", "keywords": ["strength", "skill", "expertise"]},
]

results = {
    "facial_expression_score": 0,
    "grammar_score": 0,
    "speech_feedback_score": 0,
    "keyword_score": 0,
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question')
def question_page():
    return render_template('question.html')

@app.route('/get-question/<int:index>')
def get_question(index):
    if index < len(questions_keywords):
        question = questions_keywords[index]["question"]
        return jsonify({"question": question, "index": index})
    else:
        return jsonify({"status": "Interview completed"})

@app.route('/process-answer', methods=['POST'])
def process_answer():
    data = request.get_json()
    index = data.get("index")
    answer = data.get("answer")

    question_data = questions_keywords[index]
    keyword_score = evaluate_keywords(answer, question_data["keywords"])
    grammar_score = grammar_check(answer)
    facial_expression_score = 75  # Placeholder for actual score from facial expression analysis
    speech_feedback_score = provide_feedback(answer)

    # Aggregate the results
    results["facial_expression_score"] += facial_expression_score
    results["grammar_score"] += grammar_score
    results["speech_feedback_score"] += speech_feedback_score
    results["keyword_score"] += keyword_score

    return jsonify({"rating": (keyword_score + grammar_score + facial_expression_score + speech_feedback_score) / 4})

@app.route('/result')
def result_page():
    overall_score = sum(results.values()) / (4 * len(questions_keywords))
    return render_template('result.html', **results, overall_score=overall_score)

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
