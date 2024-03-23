from flask import Flask, render_template
import requests
import string
import random

app = Flask(__name__)

# Define the URL of the Flask application to collect strings
flask_app_url = 'http://localhost:8569/'  # Replace 'localhost' with the actual host if needed

# Function to collect strings from the Flask application and add one random character to each string
def collect_and_add_1_char():
    try:
        response = requests.get(flask_app_url)
        if response.status_code == 200:
            random_strings = response.json().get('random_strings', [])
            modified_strings = []
            for random_string in random_strings:
                if len(random_string) == 15:  # Check if the length is 15 before adding a character
                    random_character = random.choice(string.ascii_letters + string.digits)
                    modified_strings.append(random_string + random_character)
                else:
                    modified_strings.append(random_string)
            return modified_strings
        else:
            print(f"Failed to collect random strings. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

# Route to display the modified strings
@app.route('/')
def display_modified_strings():
    modified_strings = collect_and_add_1_char()
    return render_template('modified_strings.html', modified_strings=modified_strings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6985)
