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
from collections import defaultdict


brews = []

for i in range(50, 60):
    # if i % 2 == 0:

        APIKEY = '9726819debab5cfdba5b6744dbbf1616'
        # APIKEY =os.environ['API_KEY']
        payload = {'withBreweries': 'Y', 'withIngredients': 'Y', 'p': i}
        # payload = {'p': i}

        b = requests.get('http://api.brewerydb.com/v2/beers?key='+APIKEY, params=payload)


        print(b.url)

        #print it just for myself to make sure it is the correct url!

        brew_list = b.json()

        brews.append(brew_list)


#create a list of tuples with brewey name, beer name, and beer style_id
# style_tuples = []


# beer_dict = {}

d3 = {}
d3['nodes'] = []
d3['links'] = []


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

            beer_name = brews[i]['data'][y].get('name')
           
            # example: sty_num = brews['data'][1].get('styleId')
            #          61


            # check to see if brewery_name is in dictionary. if it is not, add it. 
            # if brewery_name in beer_dict:
            #     beer_dict[brewery_name].append((beer_name, sty_num))

            # else:
            #     beer_dict[brewery_name] = [(beer_name, sty_num)]


            if brewery_name in d3['nodes']:
                d3['links'].append({'source': brewery_name, 'target': sty_num, "beer": beer_name})
             
            else:
                d3['nodes'].append({'name': brewery_name})
                d3['links'].append({'source': brewery_name, 'target': sty_num, "beer": beer_name})




with open("beerstyles.json", 'wt') as out:
    res = json.dump(d3, out, sort_keys=True, indent=4, separators=(',', ': '))


# nodes: 
#     brewery_name: 

# links: 
#     source: 
#         brewery_name
#     target: 
#         beer_name:
#         style_id: 


