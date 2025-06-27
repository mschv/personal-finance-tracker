from flask import Flask, render_template, request, redirect
import os
from finance import (
    load_transactions,
    summarize_by_category,
    summarize_by_period
)

app = Flask(__name__)
UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    sample_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sample.csv')
    transactions = load_transactions(sample_path)
    summary = summarize_by_category(transactions)
    monthly = summarize_by_period(transactions, period='month')
    yearly = summarize_by_period(transactions, period='year')
    return render_template("index.html", summary=summary, monthly=monthly, yearly=yearly)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'sample.csv'))
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
