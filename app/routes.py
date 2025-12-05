from app import app
from flask import render_template, redirect, url_for, request, send_from_directory, send_file, Response, flash


@app.route("/")
def index():
    return render_template('index.html')

