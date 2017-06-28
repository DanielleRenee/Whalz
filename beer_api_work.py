import json

# json.load(open(‘file.json’)) loads JSON from a file

# JSON

# A data format
# string that looks like a JS object and like a Python dictionary


beerz = json.load(open('src/whalz/seed_data/allbeerdata.json'))


 {u'abv': u'4',
  u'beer_id': u'73tmow',
  u'beer_variation': None,
  u'beer_variation_id': None,
  u'description': None,
  u'ibu': None,
  u'labels': {u'icon': u'https://s3.amazonaws.com/brewerydbapi/beer/73tmow/upload_osa2xo-icon.png',
   u'large': u'https://s3.amazonaws.com/brewerydbapi/beer/73tmow/upload_osa2xo-large.png',
   u'medium': u'https://s3.amazonaws.com/brewerydbapi/beer/73tmow/upload_osa2xo-medium.png'},
  u'name': u'Brahma Malzbier',
  u'name_display': u'Brahma Malzbier',
  u'style_id': 14,
  u'website': None,
  u'year': None},


# beerz is a python list
# for each item in the list 
# there are 6300 beers in beerz
# could just do the list index?


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


        print name, year, beer_code, website 


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

