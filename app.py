from flask import Flask
from flask import jsonify, send_file, send_from_directory, render_template
import os


app = Flask(__name__)


pdf_folder = 'books'
@app.route("/books", methods=['GET'])
def list_pdfs():
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    # Create a list of links with href attributes
    pdf_links = [{'filename': file, 'link': f'/books/{file}'} for file in pdf_files]

    return render_template('index.html', pdf_links=pdf_links)


@app.route("/books/<filename>", methods=['GET'])
def download_pdf(filename):
    # Ensure the requested file is within the 'books' folder and has a .pdf extension
    if not filename.endswith('.pdf') or '..' in filename:
        return "Invalid request", 400

    return send_from_directory(pdf_folder, filename, as_attachment=True)