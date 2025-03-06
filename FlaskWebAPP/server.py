from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

# Route for serving the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit.php', methods=['POST'])
def run_php():
    php_file = os.path.join(os.getcwd(), "php", "submit.php")

    # Capture form data
    name = request.form.get('name')
    email = request.form.get('email')

    # Execute the PHP script using subprocess
    result = subprocess.run(['php', php_file], input=f"name={name}&email={email}", 
                            text=True, capture_output=True, shell=True)
    
    return result.stdout  # Return PHP output

if __name__ == '__main__':
    app.run(debug=True, port=5000)
