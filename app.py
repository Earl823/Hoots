from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Frezza Balb',
        'title': 'Power',
        'content': 'Im the most powerful being in the universe',
        'date_posted': 'May 22, 2010'
    },
    {
        'author': 'Goku Gohan',
        'title': 'Legend of Saiyan',
        'content': 'One day the year of the ox', 
        'date_posted': 'December 7, 2016'
    }
]

user = {'email': 'user@gmail.com', 'password': '123'}

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user_pass = request.form['password']

    
        if email == user['email'] and user_pass == user['password']:
            return redirect(url_for('main'))
        else:
            return 'wrong users'

    else:
        return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signUp.html')

@app.route('/main')
def main():
    return render_template('mainPage.html', posts=posts)


if __name__ == '__main__':
	app.run(debug=True)
