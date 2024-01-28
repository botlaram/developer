# app.py
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    gender = request.form.get('gender')
    phone = request.form.get('phone')

    # Create a txt file in the local folder
    file_content = f"Name: {name}\nGender: {gender}\nPhone: {phone}"
    file_path = f"{name}_details.txt"

    with open(file_path, 'w') as file:
        file.write(file_content)

    return render_template('success.html', file_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
