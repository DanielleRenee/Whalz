# This Python file uses the following encoding: utf-8

"""Utility file to seed Whalz database from Brewery DB and Faker data in seed_data/"""

from sqlalchemy import func
import random

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


def load_users():
    """Load users from easy fake data generated into database."""

    print "All of your great fake users are being loaded"

    for i, row in enumerate(open("seed_data/fake_data.csv")):
        row = row.rstrip()
        name, email, password = row.split(",")

        user = User(name=name,
                    email=email,
                    password=password)

        # Skipping the address import for now, may want to add it later. 
        # We need to add to the session or it won't ever be stored
        db.session.add(user)


    # Once we're done, we should commit our work
    db.session.commit()



def load_inventories():
    from mixer.backend.flask import mixer
    mixer.init_app(app)

    """Load small sample of inventories into database."""

    print "Inventories are filling up. Waiting in 1PP lines really pays off."

    for i in range(0, 20):
    #create 20 random inventory items
        beer_code_list = ["4Vmwih", "oQR5YM", "Qg6dpg", "9wNKio", "0DVz81", "YP4dCI", "Eyr9Kg", "jT5vQ0", "4Vmwih", "kQ42vv"]
        user_id = random.randint(1, 100)
        beer_code = random.choice(beer_code_list)

        # inventories = mixer.cycle(100).blend(Inventory, user=user, beer=beer)
        inventories = Inventory(beer_code=beer_code, user_id=user_id)
        # inventories = mixer.blend(Inventory, user=user, beer=beer)

        db.session.add(inventories)
        db.session.commit()



def load_isos():

    """Load small sample of isos into database."""

    print "Fear of missing out is real. ISOs are being generated."

    for i in range(0, 20):
    #create 20 random inventory items
        beer_code_list = ["4Vmwih", "oQR5YM", "Qg6dpg", "9wNKio", "0DVz81", "YP4dCI", "Eyr9Kg", "jT5vQ0", "4Vmwih", "kQ42vv"]
        user_id = random.randint(1, 100)
        beer_code = random.choice(beer_code_list)

        iso = ISO(beer_code=beer_code, user_id=user_id)
        # inventories = mixer.cycle(100).blend(Inventory, user=user, beer=beer)
        # inventories = mixer.blend(Inventory, user=user, beer=beer)

        db.session.add(iso)
        db.session.commit()



def search_for_trades():

    """Search database for matches in ISO and Inventory tables."""

    print "Think of all time your saving!"


    # first search for a trade at all. 

    # this find all inventories that match up with an iso:
CREATE VIEW as possible_trades AS
SELECT beer_code, inventory_id, iso_id
FROM inventories
JOIN iso
USING (beer_code);

trade_possibilites = db.session.query(
                                      Inventory.inventory_id, 
                                      Inventory.beer_code, 
                                      ISO.iso_id, 
                                      ISO.beer_code).join(ISO).using(beer_code)

    # from this i can facilitate a trade one way.

    take the dictionary 


    # then search for a trader either within a close proximty, with the most matches, with the highest rating...

    # update iso to active to be false 
    # update the inventory_id.qty to be minus the trade qty


    # db.session.add(trade)
    # db.session.commit()

for row in query:
    HAVE TO FIND MATCHES BOTH WAYS 
    if inventory_id different than iso_id:
        that means we have a match one way 
        inventory_id_one = inventory_id
        iso_id_one = iso_id
        so now we check the other way


        k = inventory_id
        v = iso_id
        21, 23
        17, 20
        5, 16
        15, 6
        1, 3
        18, 7
        19, 5
        22, 9
        16, 22
        11, 18
        7, 17
        24, 13
        9, 11
        24, 8
        4, 1



    trade = ISO(iso_id=iso_id, inventory_id=inventory_id, quantity=1)
    db.session.add(trade)
    db.commit()

    # first search for a trade at all. 

    # this find all inventories that match up with an iso:
    # SELECT beer_code, inventory_id, iso_id
    # FROM inventories
    # JOIN iso
    # USING (beer_code);

    # from this i can facilitate a trade 


    # then search for a trader either within a close proximty, with the most matches, with the highest rating...

    # update iso to active to be false 
    # update the inventory_id.qty to be minus the trade qty 

    # db.session.add(trade)
    # db.session.commit()







if __name__ == "__main__":
    connect_to_db(app)
    # db.create_all()
    # load_beer()
    # load_users()
    # load_inventories()
    # load_isos()
    # load_ratings()
    # set_val_user_id()

