from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/aboutus')
def aboutus():
    return "I am Harsh. <br> Go to   <a href='/'>  Home Page </a>"


if __name__ == '__main__':
    app.run(debug=True)
