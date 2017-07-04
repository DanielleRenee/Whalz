"""Get latest feature from BDB."""

import requests
import json

r = requests.get("http://api.brewerydb.com/v2/featured?key=9726819debab5cfdba5b6744dbbf1616")

latest_feature = r.json()


beer_name = latest_feature['data']['beer'].get('name')
beer_id = latest_feature['data']['beer'].get('id')
description = latest_feature['data']['beer'].get('description')
abv = latest_feature['data']['beer'].get('abv')

style_id = latest_feature['data']['beer']['style'].get('id')
style_name = latest_feature['data']['beer']['style'].get('name')
style_description = latest_feature['data']['beer']['style'].get('description')


print beer_id, beer_name, 
print style_id, style_name

           