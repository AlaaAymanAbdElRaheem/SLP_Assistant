#!/usr/bin/python3

""" This module starts a Flask web application
spl_assistant route"""

from flask import Flask, render_template
from models import storage
from models.age_range import AgeRange
from models.category import Category

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(error):
    """ close storage """
    storage.close()


@app.route('/slp_assistant', strict_slashes=False)
def result_route():
    """ display AgeRange objects """
    age_ranges = storage.all(AgeRange).values()
    categories = storage.all(Category).values()
    return render_template('index.html', age_ranges=age_ranges, categories=categories)

@app.route('/about', strict_slashes=False)
def about():
    """about page"""
    return render_template('about.html')

@app.route('/contact', strict_slashes=False)
def contact():
    """contact page"""""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
