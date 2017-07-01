import time

"""Beer Trade Dashboard"""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Beer, Inventory, ISO, Trade, connect_to_db, db


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




@app.route('/users')
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)




# @app.route('/dashboard')
# def fresh_off_the_boat():
#         """Show the freshest ipas hitting right now."""

#         # need to find IPA beer_style_code


#     APIKEY = '9726819debab5cfdba5b6744dbbf1616'
#     # APIKEY =os.environ['API_KEY']
#     # payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
#     payload = {'p': i}

#     response = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)



# def whalz_watch():
#     """Display a featured beer and brewery. Spotlight feature."""


#     http://api.brewerydb.com/v2/featured?key=9726819debab5cfdba5b6744dbbf1616



# def newbies():
#     """Display new unique beers added to the database this week."""

#     http://api.brewerydb.com/v2/changes?key=9726819debab5cfdba5b6744dbbf1616&attributeName=beer&attributeID=name&action=insert&since=1498694400




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
