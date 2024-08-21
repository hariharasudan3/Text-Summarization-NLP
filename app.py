from flask import Flask, render_template, request
from summarizer import text_summarize, sentiment_analysis, word_cloud  
from pdf_extractor import extract_text_from_pdf
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    action = request.form['action']
    pdf_file = request.files['pdf_file']
    
    if pdf_file:
        text= ""
        pdf_text = extract_text_from_pdf(pdf_file)
        text += "\n" + pdf_text
        print(text)
    result = None
    if action == 'summarize' and text!="":
        result = text_summarize(text)
        display = 'Summarized Text'
        return render_template('result.html', display=display, result = result)
    elif action == 'sentiment' and text!="":
        result = sentiment_analysis(text)
        display = 'Sentiment Analysis'
        return render_template('result.html', display=display, result = result)
    elif action == 'wordcloud' and text!="":
        filename = "wordcloud.png"
        result = word_cloud(text, filename)
        display = 'Word Cloud'
        return render_template('result1.html', display=display)
    return render_template('result.html', display="No Result", result = "No Result")
    
if __name__ == '__main__':
    app.run(debug=True)
