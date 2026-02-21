from flask import Flask, render_template, jsonify


app = Flask(__name__)

@app.route('/')
def index() -> None:
    return render_template('landing.html')

@app.route('/login')
def login() -> None:
    return render_template('login.html')

@app.route('/register')
def register() -> None:
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)