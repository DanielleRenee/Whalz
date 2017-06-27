"""Models and database functions for Ratings project."""
from flask_sqlalchemy import SQLAlchemy
import correlation
from collections import defaultdict

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
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id, self.email)



class Beer(db.Model):
    """Kind of beer in database."""

    __tablename__ = "beers"

    beer_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(200), nullable=True)
    style_id = db.Column(db.Integer, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    abv = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(1000), nullable=True)
    beer_variation = db.Column(db.String(100), nullable=True)
    beer_variation_id = db.Column(db.String(100), nullable=True)
    ibu = db.Column(db.Integer, nullable=True)
    labels = db.Column(db.String(1000), nullable=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Beer beer_code=%s name=%s>" % (self.beer_code, self.name)




class Inventory(db.Model):
    """Inventory of a beer by a user."""

    __tablename__ = "inventories"


    inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    beer_code = db.Column(db.String(10), db.ForeignKey('beers.beer_code'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    quantity = db.Column(db.Integer)


    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("inventories", order_by=inventory_id))

    # Define relationship to beer
    beer = db.relationship("Beer",
                            backref=db.backref("inventories", order_by=inventory_id))



    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Rating inventory_id=%s beer_code=%s user_id=%s inventory=%s>" % (
            self.inventory_id, self.beer_code, self.user_id, self.inventory)


##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
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
