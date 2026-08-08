from flask import Flask, send_from_directory, render_template, abort
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pdf_folder = os.path.join(BASE_DIR, 'books')
os.makedirs(pdf_folder, exist_ok=True)


@app.route("/books", methods=['GET'])
def list_pdfs():
    books = sorted(f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf'))
    return render_template('index.html', books=books)


@app.route("/books/<path:filename>", methods=['GET'])
def download_pdf(filename):
    # secure_filename strips path separators/traversal, so this can only
    # ever resolve to a plain file directly inside pdf_folder.
    safe_name = secure_filename(filename)
    if not safe_name.lower().endswith('.pdf') or safe_name != filename:
        abort(400, description="Invalid request")

    if not os.path.isfile(os.path.join(pdf_folder, safe_name)):
        abort(404)

    return send_from_directory(pdf_folder, safe_name, as_attachment=True)


if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_RUN_HOST", "127.0.0.1"),
             port=int(os.environ.get("FLASK_RUN_PORT", 5000)))