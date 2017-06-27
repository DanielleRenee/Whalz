import requests
import os
import sys


f = open("beers.txt", "w")

for i in range(1, 1264):
    if i % 10 == 0:

        APIKEY = '9726819debab5cfdba5b6744dbbf1616'
        # APIKEY =os.environ['API_KEY']
        # payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
        payload = {'p': i}

        response = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)


        print(response.url)
        #print it just for myself to make sure it is the correct url!


        beer_raw = response.json()


         
        f.write('> %s\n' % (beer_raw,))
        # write each response as a new line in beers.txt  
        # http://www.afterhoursprogramming.com/tutorial/Python/Writing-to-Files/
        # http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python


f.close()

------------------------------------------------------------

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

------------------------------------------------------------

def process_beers():
    """Read beers file and return dictionary of {restaurant-name: score}."""

    beers_txt = open('beers.txt')

    beers = {}

    for line in beers_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores
 

# do a file write, add new line character add the end. 