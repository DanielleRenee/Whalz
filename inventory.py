def show_user_inventory(user_id):
    """ 
    Query PSQL database and make and print a list of all a user's inventory.

    >>> psql whalz
    >>> SELECT * FROM inventories WHERE user_id = 44;


    """
    user = User.query.get(user_id)
    inventory = Inventory.query.filter_by(user_id=user.user_id).all()

    for i in inventory:
        print i.beer.name

show_user_inventory(3)



def show_user_iso(user_id):
    """
    Query PSQL database and make and print a list of all a user's isos.

    >>> psql whalz
    >>> SELECT * FROM iso WHERE user_id = 64;

    """
    user = User.query.get(user_id)
    iso = ISO.query.filter_by(user_id=user.user_id).all()

    for i in iso:
        print i.beer.name


show_user_inventory(3)


