"""Get latest feature from BDB."""

import requests
import json

r = requests.get("http://api.brewerydb.com/v2/beers?key=9726819debab5cfdba5b6744dbbf1616&order=createDate&sort=DESC&withBreweries=Y&withIngredients=Y")

# 'withBreweries': 'Y', 'withIngredients': 'Y'

# &withBreweries=Y&withIngredients=Y

# &abv=+10

new_brews = r.json()

for i in range(0, 50):

    name = new_brews['data'][i].get('name')
    beer_id = new_brews['data'][i].get('id')
    description = new_brews['data'][i].get('description')
    name_display = new_brews['data'][i].get('nameDisplay')
    labels = new_brews['data'][i].get('labels')
    website = new_brews['data'][i].get('website')
    year = new_brews['data'][i].get('year')
    beer_variation = new_brews['data'][i].get('beerVariation')
    beer_variation_id = new_brews['data'][i].get('beerVariationId')
    style_id = new_brews['data'][i].get('styleId')
    abv = new_brews['data'][i].get('abv')
    ibu = new_brews['data'][i].get('ibu')

    if description != None:

        print name 
        print description

           