import time
import requests
import json

"""Beer Trade Dashboard"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Beer, Inventory, ISO, Trade, ViewPossibleTrade, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
    """Homepage. A general welcome."""

    return render_template("homepage.html")




@app.route('/testingd3')
def d3():
    """Testing d3."""

    return render_template("index.html")



@app.route('/users')
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)




@app.route('/trade')
def trade_list():
    """Show list of trades."""

    trades = Trade.query.all()

    success_list = []
    for trade in trades:
        success_list.append(trade)


    important_values = []

    for i in range(len(success_list)):

        initial = success_list[i].initial_trade
        reciprocate = success_list[i].reciprocal_trade

        important_values.append([initial, reciprocate])


        # print "Initial: {}, Reciprocate: {}".format(initial, reciprocate)
    
    trade_trade = []

    for i in range(len(important_values)):
        first = important_values[i][0]
        second = important_values[i][1]
        real_first = db.session.query(ViewPossibleTrade).get(first)
        real_second = db.session.query(ViewPossibleTrade).get(second)
        beer_one = real_first.inventory.beer.name
        user_one = real_first.inventory.user.name
        beer_two = real_second.inventory.beer.name
        user_two = real_second.inventory.user.name

        # print "Beer #1: {}, User #1: {}".format(beer_one, user_one)
        # print "Beer #2: {}, User #2: {}".format(beer_two, user_two)
        trade_trade.append([beer_one, user_one, beer_two, user_two])


    print trade_trade


    return render_template("trade_details.html", trade_trade=trade_trade)



@app.route('/dashboard')
def dash():
    """Show dashboard."""

    # call for featured beer and style

    r = requests.get("http://api.brewerydb.com/v2/featured?key=9726819debab5cfdba5b6744dbbf1616")

    latest_feature = r.json()


    beer_name = latest_feature['data']['beer'].get('name')
    beer_id = latest_feature['data']['beer'].get('id')
    description = latest_feature['data']['beer'].get('description')
    abv = latest_feature['data']['beer'].get('abv')

    style_id = latest_feature['data']['beer']['style'].get('id')
    style_name = latest_feature['data']['beer']['style'].get('name')
    style_description = latest_feature['data']['beer']['style'].get('description')

    # call for new brews

    z = requests.get("http://api.brewerydb.com/v2/beers?key=9726819debab5cfdba5b6744dbbf1616&order=createDate&sort=DESC&withBreweries=Y&withIngredients=Y")

    new_brews = z.json()

    new_list = []

    for i in range(0, 40):

        new_name = new_brews['data'][i].get('name')
        beer_id = new_brews['data'][i].get('id')
        new_description = new_brews['data'][i].get('description')
        
        brewery = new_brews['data'][i].get('breweries')

        if brewery != None:
            new_brewery_name = brewery[0]['name']
            name_display = new_brews['data'][i].get('nameDisplay')
            labels = new_brews['data'][i].get('labels')
            website = new_brews['data'][i].get('website')
            year = new_brews['data'][i].get('year')
            beer_variation = new_brews['data'][i].get('beerVariation')
            beer_variation_id = new_brews['data'][i].get('beerVariationId')
            style_id = new_brews['data'][i].get('styleId')
            abv = new_brews['data'][i].get('abv')
            ibu = new_brews['data'][i].get('ibu')

            if new_description != None:
                    new_list.append([new_name, new_description, new_brewery_name, abv])

    # print new_list


    return render_template("dashboard.html", beer_name=beer_name, 
                                             abv=abv, 
                                             description=description, 
                                             style_id=style_id, 
                                             style_name=style_name, 
                                             style_description=style_description, 
                                             new_list=new_list)




# def charts():
#     """Ideas for Charts.js."""
# highest secondary market beer price


# name, and the price





# def whalz_watch():
#     """Display a featured beer and brewery. Spotlight feature."""



# def fresh_off_the_boat():
#      """Show the freshest newest hitting right now."""




# def get_out_there():
#     """List upcoming beer trade oppoprtunitues."""

#        http://api.brewerydb.com/v2/events?key=9726819debab5cfdba5b6744dbbf1616




# def real_whalz():
#     """Display opportunity to trade for one of the rarest beers. Less than 5 qty across the whole database."""

#     #this will come from internal db




# def trades_in_numbers():
#     """Display hot comodities. Beers that are trading at very high rates."""

#     #this will come from internal db




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
