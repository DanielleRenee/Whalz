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


b = requests.get("http://api.brewerydb.com/v2/beers?key=9726819debab5cfdba5b6744dbbf1616&order=createDate&sort=DESC&withBreweries=Y&withIngredients=Y")

brew_style = b.json()

brewery_styles = {}

for i in range(0, 100):
    
    brewery = brew_style['data'][i].get('breweries')

    if brewery != None:

        brewery_name = brewery[0]['name']

        # styles = []
       
        brewery_styles[brewery_name] = brew_style['data'][i].get('styleId')



    # print new_list