# what styles of beer are companies making

# http://www.brewerydb.com/developers/docs-endpoint/style_index

# get a list of styles that each brewery makes

# name of brewery

# get a list of all the styles and their style_id


s = requests.get("http://api.brewerydb.com/v2/styles?key=9726819debab5cfdba5b6744dbbf1616")

style = s.json()


for i in range(len(style['data'])):

    style_name = style['data'][i].get('name')
    style_id = style['data'][i].get('id')

    print style_name, style_id


# key is the brewery
# values is a list are all the style id's that a brewery has 

-----------------------------------------------------------------------

import requests
import json


brews = []

for i in range(0, 1):
    # if i % 10 == 0:

        APIKEY = '9726819debab5cfdba5b6744dbbf1616'
        # APIKEY =os.environ['API_KEY']
        payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
        # payload = {'p': i}

        b = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)


        print(b.url)

        #print it just for myself to make sure it is the correct url!

        brew_list = b.json()

        brews.append(brew_list)



from collections import defaultdict





>>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
>>> d = defaultdict(list)
>>> for k, v in s:
...     d[k].append(v)
...
>>> d.items()
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


#create a list of tuples with brewey name and 

style_tuples = []

# for url in range(len(brews)):
x = range(len(brews))

for i in x:

    for y in range(0, 49):

        # brewery = brews['data'][x].get('breweries')

        brewery = brews[i]['data'][y].get('breweries')

        if brewery != None:

            brewery_name = brewery[0]['name']

            # example: brewery_name = brewery[0]['name']
            #          u'Harpoon Brewery'

            sty_num = brews[i]['data'][y].get('styleId')
           
            # example: sty_num = brews['data'][1].get('styleId')
            #          61

            style_tuples.append((brewery_name, sty_num))

            

    # print new_list