# PDF Book Server Project

## Table of Contents
- [Introduction](#introduction)
- [Motivation](#motivation)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
- [Installation](#installation)
  - [Local Installation](#local-installation)
  - [Docker Installation](#docker-installation)
- [Adding Books](#adding-books)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

PDF Book Server is a lightweight Flask app that lists and serves PDF files from a local `books/` folder. It's designed to be dropped onto a small server or run in Docker to give you a simple, private web page for browsing and downloading your own PDFs.

## Motivation

I had an old iPad that still worked fine, but it was old enough that neither new apps nor even old/legacy apps could be installed on it anymore. On top of that, I had forgotten the Apple ID it was signed into, so I couldn't connect it to iTunes/Finder on my PC or Mac to sync files the normal way either.

I just wanted to get some books (PDFs) from my PC onto the iPad to read, and none of the usual routes worked. So I built this small Flask app instead: I ran it on my PC, opened `localhost` in the iPad's Safari browser (both on the same network), and used it to browse and download the PDFs directly onto the iPad. It's a small project, but it solved a real problem when every "normal" way of transferring files was blocked.

## Features
- Lists every PDF found in the `books/` folder.
- Serves individual PDFs as downloads via a clean, safe route.
- Filename validation to prevent path traversal outside the `books/` folder.
- Runs behind Gunicorn in Docker for production use (no dev-server debugger exposed).
- Simple, dependency-light codebase — easy to extend.

## Technologies Used
- **Backend:** Python, Flask
- **WSGI Server:** Gunicorn
- **Deployment:** Docker or locally

## Configuration

Local development settings are read from `.env` / `.flaskenv` (not committed). Key settings include:
- **FLASK_APP:** Entry point for the Flask CLI (`app.py`).
- **FLASK_RUN_HOST:** Host the dev server binds to (e.g. `0.0.0.0`).
- **FLASK_RUN_PORT:** Port the dev server binds to (e.g. `5000`).
- **FLASK_DEBUG:** Enables the interactive debugger and auto-reload. **Local development only — never enable in production**, as it allows arbitrary code execution if exposed.

## Installation

### Local Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/consultomer/PDF.git
   cd PDF
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   flask run
   ```

### Docker Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/consultomer/PDF.git
   cd PDF
   ```
2. **Build the Docker image:**
   ```bash
   docker build -t pdf-server:0.0.1 .
   ```
3. **Run the container**, mounting your books folder so PDFs persist outside the container:
   ```bash
   docker run -dit --name pdf-server --restart unless-stopped \
     -p 5000:5000 \
     -v $(pwd)/books:/app/books \
     pdf-server:0.0.1
   ```

## Adding Books
Drop your PDF files into the `books/` folder in the project root (created automatically on first run if it doesn't exist). Each file must have a `.pdf` extension to appear in the list.

## Routes
Once the app is running, the following routes are available:

- **`GET /books`**: Lists all PDFs currently in the `books/` folder, with download links.
- **`GET /books/<filename>`**: Downloads the specified PDF file.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and passes all tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact:

- **Omer Abdulrehman**
- **Email:** [consultomer@gmail.com](mailto:consultomer@gmail.com)
- **LinkedIn:** [Omer Abdulrehman](https://www.linkedin.com/in/omerarehman/)
