def show_user_inventory(user_id):
    user = User.query.get(user_id)
    inventory = Inventory.query.filter_by(user_id=user.user_id).all()

    for i in inventory:
        print i.beer.name

show_user_inventory(3)


