# Set up your imports here!
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1>Hello to puppy world!</h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] == 'y':
        latin_name = name[:-1]+'iful'
    else:
        latin_name = name+'y'
    return f'Hi {name}! Your puppylatin name is {latin_name}.'

if __name__ == '__main__':
    # Fill me in!
    app.run()
