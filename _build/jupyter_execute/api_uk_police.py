## UK police API

> source: https://data.police.uk/docs/

import requests

import pandas as pd
# pd.options.display.max_columns = 200

## parameters

    - Availability

    Forces
    Specific force
    Force senior officers
    
    Street level crimes
    Street level outcomes
    Crimes at location
    Crimes with no location
    Crime categories
    Last updated
    Outcomes for a specific crime

    Neighbourhoods
    Specific neighbourhood
    Neighbourhood boundary
    Neighbourhood team
    Neighbourhood events
    Neighbourhood priorities
    Locate neighbourhood

    Stop and searches by area
    - Stop and searches by location
    Stop and searches with no location
    Stop and searches by force


## Availability -- last 3 years (36 months)

# returns list of all available datasets

url = 'https://data.police.uk/api/crimes-street-dates'
req = requests.get(url)
req

# data from earliest month
print(req.json()[35]['date'])

# data from latest month
print(req.json()[0]['date'])

## Stop and search

# send query via variables and f-string

endpoint = 'https://data.police.uk/api'
method = 'stops-street'
lat = "52.629729"
long = "-1.131592"
month = "2021-04"

query = f'{endpoint}/{method}?lat={lat}&lng={long}&date={month}'
print(query)

req = requests.get(query)
req

req.json()

# query via assembled url (bicycle theft, April 2021)

epoint = 'https://data.police.uk/api/crimes-street/bicycle-theft?lat=51.476369992679096&lng=-3.1781098361443667&date=2021-04'

req = requests.get(epoint)
req


response = req.json()

len(response)

response

# first item in the response

response[0]

## using 'params' argument to supply dictionary of arguments



endpoint = 'https://data.police.uk/api/stops-street?'
parameters = {'lat':"52.629729", 'lng':"-1.131592", 'date':"2020-06"}

req = requests.get(endpoint, params = parameters)
req

response = req.json()

response

