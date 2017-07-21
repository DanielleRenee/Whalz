def search_for_trades():

    """create a tuple of every inventory_id, iso_id in possible_trades"""

    possible_list = []

    all_possible = db.session.query(ViewPossibleTrade.inventory_id, ViewPossibleTrade.iso_id).all()

    for each in all_possible:
        possible_list.append(each)

    # this returns all possible trades in a list, where each possibility is a tuple,
    # the first index of the tuple is inventory_id and the second is iso_id
return possible_list



def other_way(): 
    """Evaluates the list of possible trade tuples and checks to see if there are any matches the other way"""

    check_the_other_way = [(t[1], t[0]) for t in possible_list]

    # are there any instances of check_the_other_way in all_possible


    other = [i for i, j in zip(all_possible, checked) if i == j]
    # example: [(7, 7), (15, 15)]

    # could possible use the cmp(all_possible, checked) method


    its_a_match = set(all_possible) & set(check_the_other_way)
    # example: set([(2, 14), (7, 7), (13, 6), (6, 13), (14, 2), (15, 15)])



    hard code the results 




   



   -----------------------------------------------------------

    # then search for a trader either within a close proximty, with the most matches, with the highest rating...

    # update iso status from active to be false 
    # update the inventory_id.qty to be minus the trade qty



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
