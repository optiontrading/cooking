from flask import render_template
from flask import jsonify
from flask import request

from app import app
import requests
from curl_python import search_ingredients

# html page for searching ingredients
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# return search ingredients to html page using elasticsearch and mongodb
@app.route('/search', methods=['POST'])
def search():

    title = 'Home'

    # return ingredients search from html page
    searched_ingredients = request.form['search']
    # print(searched_ingredients)

    user = {'username': '%s'%(searched_ingredients)}

    # find ingredients on elasticsearch index
    results_found = search_ingredients(searched_ingredients)

    # filter data - return recipe name and ingredients
    filtered_data = results_found['hits']['hits']

    filtered_data = [_['_source'] for _ in filtered_data]

    # return jsonify(results_found)
    # return jsonify(filtered_data)
    return render_template('search.html', title='Home', user=user, posts=filtered_data)

    # print()

    # search ingredients using elasticsearch

    # title = 'Home'
    # user = {'username': 'Miguel'}
    # posts = [
    # {
    # 'author': {'recipe_name': 'PIÑA COLADA SMOOTHIE', 'ingredients' : 'pineapple chunks, coconut milk, banana, ice cubes, dates seedless, vanilla bean powder'},
    # 'body': 'PIÑA COLADA SMOOTHIE INGREDIENTS SERVES 1, MAKES 500 ML 1 cup pineapple chunks 1 cup coconut milk 1⁄2 medium banana 1⁄4 cup ice cubes 2 dates, seedless 1⁄8 teaspoon vanilla bean powder (optional)'
    # },
    # {
    # 'author': {'recipe_name': 'BANANA DATE SHAKE', 'ingredients' : 'coconut milk, bananas, dates, ice cubes, cinnamon powder'},
    # 'body': 'BANANA DATE SHAKE INGREDIENTS SERVES 1, SERVES 2, MAKES 700 ML 11⁄2 cups coconut milk 3 bananas 6 dates, seedless 4 ice cubes 1⁄2 teaspoon cinnamon powder'
    # }
    # ]
    # return render_template('search.html', title='Home', user=user, posts=posts)

# todo: creating a search page for searching ingredients

    # search = request.form['search']
    # # search = request.args.get("search")
    # resp = search_ingredients(search)
    # # print(resp)
    # return jsonify(resp)
    # # products = Product.query.filter(Product.name.like(search)).all()
    # # return render_template('index.html', title='Home', user=user)

# todo: creating an html page containing table with recipe and ingredients
@app.route('/dummy1')
def dummy1():

    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'ingredients': 'PIÑA COLADA SMOOTHIE INGREDIENTS SERVES 1, MAKES 500 ML 1 cup pineapple chunks 1 cup coconut milk 1⁄2 medium banana 1⁄4 cup ice cubes 2 dates, seedless 1⁄8 teaspoon vanilla bean powder (optional)'
        },
        {
            'author': {'username': 'Susan'},
            'ingredients': 'BANANA DATE SHAKE INGREDIENTS SERVES 1, SERVES 2, MAKES 700 ML 11⁄2 cups coconut milk 3 bananas 6 dates, seedless 4 ice cubes 1⁄2 teaspoon cinnamon powder'
        }
    ]

    return render_template('search.html', title='Home', user=user, posts=posts)
    # return render_template('dummy1.html', title='Home', user=user, data=posts)

# ------------------------------------------ Extras -----------------------------------------------------
@app.route('/dummy2')
def dummy2():
    user = 'Miguel'
    return render_template('dummy2.html', title='Home', user=user)

