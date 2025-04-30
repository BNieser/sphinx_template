#!/usr/bin/env python3
import subprocess
import http.server
import socketserver
import os

DOCS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'docs'))
BUILD_DIR = os.path.join(DOCS_DIR, '_build', 'html')

def build_docs():
    subprocess.run(['sphinx-build', '-b', 'html', DOCS_DIR, BUILD_DIR], check=True)

def serve_docs(port=8000):
    os.chdir(BUILD_DIR)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving Sphinx docs at http://localhost:{port}")
        httpd.serve_forever()

if __name__ == "__main__":
    build_docs()
    serve_docs()