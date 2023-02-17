from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signUp.html')


if __name__ == '__main__':
	app.run(debug=True)