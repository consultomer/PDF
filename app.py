from flask import Flask
from flask import send_from_directory, render_template
import os


app = Flask(__name__)


pdf_folder = '/'
@app.route("/books", methods=['GET'])
def list_pdfs():
    return render_template('index.html')


@app.route("/books/<filename>", methods=['GET'])
def download_pdf(filename):
    # Ensure the requested file is within the 'books' folder and has a .pdf extension
    if not filename.endswith('.pdf') or '..' in filename:
        return "Invalid request", 400

    return send_from_directory(pdf_folder, filename, as_attachment=True)