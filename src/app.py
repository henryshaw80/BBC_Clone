__author__ = "Timur"

from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.config.from_object('config')

app.secret_key = "Timur"

@app.route('/') # 127.0.0.1:5000/
def home_template():
    return render_template('home.jinja2')


if __name__ == '__main__':
    app.run(port=5000)