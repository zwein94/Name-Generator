# app.py
from flask import Flask, render_template, request
import random
from urllib.parse import quote
app = Flask(__name__)

# Sample data for name generation
male_names = ["John", "Michael", "David", "James", "Robert"]
female_names = ["Mary", "Jennifer", "Linda", "Patricia", "Elizabeth"]
neutral_names = ["Alex", "Taylor", "Jordan", "Casey", "Jamie"]
nationalities = ["American", "British", "French", "German", "Italian"]

# Function to generate random name based on user input
def generate_name(gender, nationality, length):
    if gender == "male":
        names = male_names
    elif gender == "female":
        names = female_names
    else:
        names = neutral_names

    name = random.choice(names)
    nationality = random.choice(nationalities)
    return f"{name} ({nationality})"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    gender = request.form['gender']
    nationality = request.form['nationality']
    length = request.form['length']
    name = generate_name(gender, nationality, length)
    return render_template('result.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
# Example usage:
quoted_url = quote(url)
