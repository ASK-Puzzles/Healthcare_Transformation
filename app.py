from flask import Flask, render_template, request, redirect, url_for
import os
from utils.pdf_processor import process_pdf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        summary = process_pdf(file_path)
        return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)