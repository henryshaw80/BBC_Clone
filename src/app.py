__author__ = "Timur"

from flask import Flask, render_template, request, session, make_response
from random import randint

app = Flask(__name__)
app.config.from_object('config')

app.secret_key = "Timur"

@app.route('/') # 127.0.0.1:5000/
def home_template():
    return render_template('home.jinja2')

@app.route('/bootstrap') # 127.0.0.1:5000/bootstrap
def bootstrap_template():
    # we need to render jinja2 language into something
    # that a web browser understand

    population = list(range(1, 11))
    sample = []
    count = 0
    while (count < 10):
        index = randint(0, 9)
        if population[index] is not 0: # if we found an unmarked value
            sample.append(population[index])
            population[index] = 0 #mark selected
            count = count + 1

    #imgloc = "static/img/" + "clockimage.png"
    return render_template('bootstrap.jinja2', sample=sample)


if __name__ == '__main__':
    app.run(port=5000)