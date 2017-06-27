import requests
import os
import sys


# beer_results = []
# per notes from henry, make each request a seperate line in the output file. 
f = open("beers.txt", "w")

for i in range(5, 9):

    APIKEY = ''
    # APIKEY =os.environ['API_KEY']
    # payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
    payload = {'withIngredients': 'Y', 'p': i}

    response = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)

    print(response.url)
    #print it just for myself to make sure it is the correct url!

    # write each response as a new line in beers.txt    
    f.write('> %s\n' % (response,))
    # http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/
    # http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    # put beer_raw in to file and add a new line character

f.close()


beer_raw = response.json()
    #I think I need it to be a string in order to write it. so I will not make a json until I have all of the lines


    # beer_results.append(beer_raw)


# need to replace indexes with the current number
for i in range(0, 49):

    name = beer_raw['data'][i].get('name')
    beer_id = beer_raw['data'][i].get('id')
    description = beer_raw['data'][i].get('description')
    name_display = beer_raw['data'][i].get('nameDisplay')
    labels = beer_raw['data'][i].get('labels')
    # website = beer_raw['data'][i].get('website')
    year = beer_raw['data'][i].get('year')
    beer_variation = beer_raw['data'][i].get('beerVariation')
    beer_variation_id = beer_raw['data'][i].get('beerVariationId')
    style_id = beer_raw['data'][i].get('styleId')
    abv = beer_raw['data'][i].get('abv')
    ibu = beer_raw['data'][i].get('ibu')

    print name, abv




1294 
 

# do a file write, add new line character add the end. 