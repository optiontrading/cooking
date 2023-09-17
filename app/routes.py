from flask import render_template
from flask import jsonify
from flask import request

from app import app
import requests
from curl_python import search_ingredients

@app.route('/')
@app.route('/index')
def index():
    user = 'Miguel'
    return render_template('index.html', title='Home', user=user)

@app.route('/search', methods=['POST'])
def search():
    search = request.form['search']
    # search = request.args.get("search")
    resp = search_ingredients(search)
    # print(resp)
    return jsonify(resp)
    # products = Product.query.filter(Product.name.like(search)).all()
    # return render_template('index.html', title='Home', user=user)
