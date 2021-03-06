"""Utility file to seed Whalz database from Brewery DB and Faker data in seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Beer, Inventory, ISO, Trade, connect_to_db, db
from server import app
import json

# json.load(open(‘file.json’)) loads JSON from a file

beerz = json.load(open('seed_data/allbeerdata.json'))

# beerz is a python list
# there are 6300 beers in beerz

def load_beer():
    """Load beer from allbeerdata.json into database."""

    print "Fill er up! Beers are being loaded."

    for i in range(0, 6300):

        name = beerz[i]['name_display']
        abv = beerz[i]['abv']
        beer_code = beerz[i]['beer_id']
        description = beerz[i]['description']
        ibu = beerz[i]['ibu']
        labels = beerz[i]['labels']
        website = beerz[i]['website']
        style_id = beerz[i]['style_id']
        beer_variation = beerz[i]['beer_variation']
        beer_variation_id = beerz[i]['beer_variation_id']
        year = beerz[i]['year']


        # add the beer object as a beer in the beer table
        beer = Beer(abv=abv,
                    beer_code=beer_code, 
                    beer_variation=beer_variation, 
                    beer_variation_id=beer_variation_id,
                    description=description, 
                    ibu=ibu, 
                    labels=labels, 
                    website=website, 
                    style_id=style_id, 
                    year=year,
                    name=name,)

        db.session.add(beer)


    # Once we're done, we should commit our work
    db.session.commit()

