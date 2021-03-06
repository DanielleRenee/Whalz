# This Python file uses the following encoding: utf-8

"""Utility file to seed Whalz database from Brewery DB and Faker data in seed_data/"""

from sqlalchemy import func
import random

from model import User, Beer, Inventory, ISO, Trade, connect_to_db, db
from server import app
import json


def load_beer():
    """
    Load beer from allbeerdata.json into database.

    >>> beerz = json.load(open('seed_data/allbeerdata.json'))
    >>> len(beerz)
    6300

    >>> name = beerz[1]['name_display']
    >>> name
    u'1916 Irish Stout'

    """

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
    """
    Load users from easy fake data generated into database.

    >>> user = <User user_id=None email=walterbarnett@yahoo.com>
    >>> user.name
    'James Bishop'

    >>> user.email
    'walterbarnett@yahoo.com'

    >>> user.password
    'H_$8)sXym1'

    >>> user.inventories
    []

    """

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
    # from mixer.backend.flask import mixer
    # mixer.init_app(app)

    """
    Load small sample of inventories into database.

    >>> import random
    >>> random.choice
    <bound method Random.choice of <random.Random object at 0x1236350>>

    """

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

    """
    Load small sample of isos into database.

    >>> range(0, 20)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    """

    print "Fear of missing out is real. ISOs are being generated."

    for i in range(0, 20):
    #create 19 random inventory items
        beer_code_list = ["4Vmwih", "oQR5YM", "Qg6dpg", "9wNKio", "0DVz81", "YP4dCI", "Eyr9Kg", "jT5vQ0", "4Vmwih", "kQ42vv"]
        user_id = random.randint(1, 100)
        beer_code = random.choice(beer_code_list)

        iso = ISO(beer_code=beer_code, user_id=user_id)
        # inventories = mixer.cycle(100).blend(Inventory, user=user, beer=beer)
        # inventories = mixer.blend(Inventory, user=user, beer=beer)

        db.session.add(iso)
        db.session.commit()



# def load_possible_trades():

#     """Search database for matches in ISO and Inventory tables."""

#     print "Think of all time your saving!"


#     INSERT INTO possible_trades (inventory_id, iso_id)
#     SELECT inventory_id, iso_id
#     FROM inventories
#     JOIN iso
#     USING (beer_code);



def search_for_trades():

    """
    create a tuple of every inventory_id, iso_id in possible_trades

    >>> example_tuple = (2, 14)
    >>> second_tuple = (2, 14)
    >>> lst = []
    >>> lst.append(example_tuple)
    >>> lst.append(second_tuple)
    >>> lst
    [(2, 14), (2, 14)]
    >>> set(lst)
    set([(2, 14)])

    """

    possible_list = []

    # possible = possible_trades.query.all()

    all_possible = db.session.query(ViewPossibleTrade.inventory_id, ViewPossibleTrade.iso_id).all()

    for each in all_possible:
        possible_list.append(each)

    # this returns all possible trades in a list, where each possibility is a tuple,
    # the first index of the tuple is inventory_id and the second is iso_id

    check_the_other_way = [(t[1], t[0]) for t in possible_list]

    # are there any instances of check_the_other_way in all_possible

    other = [i for i, j in zip(all_possible, checked) if i == j]
    # example: [(7, 7), (15, 15)]

    # could possible use the cmp(all_possible, checked) method


    its_a_match = set(all_possible) & set(check_the_other_way)
    # example: set([(2, 14), (7, 7), (13, 6), (6, 13), (14, 2), (15, 15)])



    # hard code the results in load_trades


# def load_trades():

#     """Complete trade."""

#     trade = Trade(initial_trade=4, reciprocal_trade=22, quantity=1)
#     db.session.add(trade)



#     db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)
    # db.create_all()
    # load_beer()
    # load_users()
    # load_inventories()
    # load_isos()
    # load_possible_trades()

