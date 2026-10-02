from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return 'Welcome! <a href="/about">About<a/> | <a href="/contact">Contact</a>'

@app.route('/about')
def about():
	return 'This app is built with <a href="https://flask.palletsprojects.com">Flask</a> and a <a href="https://www.python.org">Python</a>.'

@app.route('/contact')
def contact():
	return 'Contact me at: igorteklak05@gmail.com'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)




