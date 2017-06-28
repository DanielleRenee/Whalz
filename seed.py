# This Python file uses the following encoding: utf-8

"""Utility file to seed Whalz database from Brewery DB and Faker data in seed_data/"""


import datetime
from sqlalchemy import func

from model import User, Beer, Inventory, ISO, Trade, connect_to_db, db
from server import app
import json


def load_beer():
    """Load beer from allbeerdata.json into database."""

    beerz = json.load(open('seed_data/allbeerdata.json'))
    beerz_len = len(beerz)
    # json.load(open(‘file.json’)) loads JSON from a file
    # beerz is a python list
    # there are 6300 beers in beerz

    print "Fill er up! Beers are being loaded."

# can only add 49 beers to db right now, because I haven't split the file on the dictionaries.
# go back and change later!
# really need to be getting the brewey back as well. 

    for i in range(0, 49):

        name = beerz[i]['name_display']
        abv = beerz[i]['abv']
        beer_code = beerz[i]['beer_id']
        # description = beerz[i]['description']
        ibu = beerz[i]['ibu']
        # labels = beerz[i]['labels']
        # website = beerz[i]['website']
        style_id = beerz[i]['style_id']
        beer_variation = beerz[i]['beer_variation']
        beer_variation_id = beerz[i]['beer_variation_id']
        year = beerz[i]['year']


        # add the beer object as a beer in the beer table
        beer = Beer(abv=abv,
                    beer_code=beer_code, 
                    beer_variation=beer_variation, 
                    beer_variation_id=beer_variation_id,
                    # description=description, 
                    ibu=ibu, 
                    # labels=labels, 
                    # website=website, 
                    style_id=style_id, 
                    year=year,
                    name=name,)

        db.session.add(beer)


    # Once we're done, we should commit our work
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_beer()
    # load_movies()
    # load_ratings()
    # set_val_user_id()

