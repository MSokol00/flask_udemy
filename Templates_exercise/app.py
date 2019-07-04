from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    fails_list = []
    result = True
    if not any([c.isupper() for c in username]):
        fails_list.append('You did not use uppercase letter')
    if not any([c.islower() for c in username]):
        fails_list.append(('You did not use lowercase letter'))
    if not username[-1].isdigit():
        fails_list.append('You did not end your username with a number.')
    if len(fails_list) > 0:
        result = False
    return render_template('report.html', result=result, fails_list=fails_list)


if __name__ == '__main__':
    app.run()
