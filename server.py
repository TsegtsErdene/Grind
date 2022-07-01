from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/about')
def about():
    return 'The about'

@app.route('/blog/<int:blog_id>')
def blogpost(blog_id):
    return 

if __name__ == '__main__':
    app.run()