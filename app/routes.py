from flask import render_template
from flask import jsonify
from flask import request

from app import app
import requests
from curl_python import search_ingredients

# todo: creating an html page containing table with recipe and ingredients
@app.route('/')
@app.route('/dummy1')
def dummy1():
    user = {'username': 'Miguel'}
    posts = [
    {
    'author': {'username': 'John'},
    'body': 'Beautiful day in Portland!'
    },
    {
    'author': {'username': 'Susan'},
    'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('dummy1.html', title='Home', user=user, posts=posts)

# ------------------------------------------ Extras -----------------------------------------------------
@app.route('/dummy2')
def dummy2():
    user = 'Miguel'
    return render_template('dummy2.html', title='Home', user=user)

@app.route('/search', methods=['POST'])
def search():
    search = request.form['search']
    # search = request.args.get("search")
    resp = search_ingredients(search)
    # print(resp)
    return jsonify(resp)
    # products = Product.query.filter(Product.name.like(search)).all()
    # return render_template('index.html', title='Home', user=user)
