"""Models and database functions for Whalz beer trading app."""
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_utils import IntRangeType
from random import randint
from datetime import datetime

# import correlation
# from collections import defaultdict

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of Whalz website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)



class Beer(db.Model):
    """Kind of beer in database."""

    __tablename__ = "beers"

    beer_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # website = db.Column(db.String(200), nullable=True)
    style_id = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    abv = db.Column(db.Float, nullable=True)
    # description = db.Column(db.Text, nullable=True)
    beer_variation = db.Column(db.String(100), nullable=True)
    beer_variation_id = db.Column(db.String(100), nullable=True)
    ibu = db.Column(db.Float, nullable=True)
    # labels = db.Column(db.String(1000), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Beer beer_code=%s name=%s>" % (self.beer_code, self.name)




class Inventory(db.Model):
    """Inventory of a beer by a user."""

    __tablename__ = "inventories"

    inventory_number = randint(1, 12)


    inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    beer_code = db.Column(db.String(10), db.ForeignKey('beers.beer_code'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    # quantity = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=inventory_number)
   

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("inventories", order_by=inventory_id))

    # Define relationship to beer
    beer = db.relationship("Beer",
                            backref=db.backref("inventories", order_by=inventory_id))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Inventory inventory_id=%s beer_code=%s user_id=%s inventory=%s>" % (
            self.inventory_id, self.beer_code, self.user_id, self.inventory)



class ISO(db.Model):
    """Wish list of individual beers by a user. The In Search Of aka ISO table."""

    __tablename__ = "iso"


    iso_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    beer_code = db.Column(db.String(10), db.ForeignKey('beers.beer_code'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    quantity = db.Column(db.Integer, default=1)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    # set default to true and change to false after a trade has been completed.
    # https://pythonhosted.org/Flask-User/data_models.html
    # unique pairing between a user and a beer
    # unqiue key constraint that works on two columns
    # combo of the beer_code and user should be unique 


    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("iso", order_by=iso_id))

    # Define relationship to beer
    beer = db.relationship("Beer",
                            backref=db.backref("iso", order_by=iso_id))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<ISO iso_id=%s beer_code=%s user_id=%s quantity=%s>" % (
            self.iso_id, self.beer_code, self.user_id, self.quantity)




class Trade(db.Model):
    """Trade list of individual beer trade by two users."""

    __tablename__ = "trades"


    trade_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    traded_at = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.inventory_id'), index=True)
    iso_id = db.Column(db.Integer, db.ForeignKey('iso.iso_id'), index=True)
    # REMEMBER to set the iso to false after a trade has been made
    # If if remove the iso after a trade is complete


    # Define relationship to inventory
    inventory = db.relationship("Inventory",
                           backref=db.backref("trade", order_by=trade_id))

    # Define relationship to iso
    iso = db.relationship("ISO",
                            backref=db.backref("trade", order_by=trade_id))




    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Trade trade_id=%s inventory_id=%s iso_id=%s quantity=%s>" % (
            self.trade_id, self.inventory_id, self.iso_id, self.quantity)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///whalz'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app

    connect_to_db(app)
    print "Connected to DB."
