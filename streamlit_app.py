import streamlit as st
import http.server
import socketserver


PORT = 8501

Handler = http.server.SimpleHTTPRequestHandler

# Change to the directory where your index.html file is located
web_dir = "."
os.chdir(web_dir)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
