import os
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Make sure the 'data' folder exists
DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_FOLDER, exist_ok=True)
CSV_PATH = os.path.join(DATA_FOLDER, 'contacts.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to contacts.csv inside the 'data' folder
        with open(CSV_PATH, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        return render_template('contact.html', success=True)

    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
