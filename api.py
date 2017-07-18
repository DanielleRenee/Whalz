import requests
import os
import sys
import json

#need to refractor to use recursion instead!


f = open("allbeerdata.json", "w")


beer_list = []

for i in range(1, 1270):
    if i % 10 == 0:

        APIKEY = '9726819debab5cfdba5b6744dbbf1616'
        # APIKEY =os.environ['API_KEY']
        # payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
        payload = {'p': i}

        response = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)

        http://api.brewerydb.com/v2/beers?key=9726819debab5cfdba5b6744dbbf1616&order=createDate&sort=DESC


        print(response.url)
        #print it just for myself to make sure it is the correct url!


        beer_raw = response.json()

# i want to make my own dictionary. set name, beer_id, description... as the keys
# in the dict and value as the unique beer values. 

        for i in range(0, 50):


            my_dict={}

            my_dict['name']= beer_raw['data'][i].get('name')
            my_dict['beer_id'] = beer_raw['data'][i].get('id')
            my_dict['description'] = beer_raw['data'][i].get('description')
            my_dict['name_display'] = beer_raw['data'][i].get('nameDisplay')
            my_dict['labels'] = beer_raw['data'][i].get('labels')
            my_dict['website'] = beer_raw['data'][i].get('website')
            my_dict['year'] = beer_raw['data'][i].get('year')
            my_dict['beer_variation'] = beer_raw['data'][i].get('beerVariation')
            my_dict['beer_variation_id'] = beer_raw['data'][i].get('beerVariationId')
            my_dict['style_id'] = beer_raw['data'][i].get('styleId')
            my_dict['abv'] = beer_raw['data'][i].get('abv')
            my_dict['ibu'] = beer_raw['data'][i].get('ibu')



            beer_list.append(my_dict)

json.dump(beer_list, f)

# f.write('%s\n' % (,))
# write each response as a new line in beers.txt  
# http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

f.close()


# converting allbeerdata to python dictionary
beerz = json.load(open('allbeerdata.json'))