## Open Charge Map API

> documentation: https://openchargemap.org/site/develop/api

> forum: https://community.openchargemap.org/


import requests
import collections


# assign API key to variable

ocm_key = '****'

# test query for GB (Great Britain), 100 results, as single url

call = 'https://api.openchargemap.io/v3/poi/?key=ocm_key&output=json&countrycode=GB&maxresults=100&compact=true&verbose=false'
req = requests.get(call)
req

# all charging points in a 20 mile radius from Jomec

params = {"key": ocm_key,
          "countrycode": "GB", 
          "output": "json", 
          "latitude": 51.476629314550514, 
          "longitude": -3.1808810080300978, 
          "distance":20,
          "distanceunit": 'Miles',
          "compact": True, 
          "verbose": False, 
          "maxresults": 2_000}

endpoint = 'https://api.openchargemap.io/v3/poi/?'

req = requests.get(endpoint, params = params)
print(req)

# how many items were returned?

len(req.json())

# assign to variable and examine first item

data = req.json()
data[0]

# assemble list of postcodes

pc_list = []

for x in data:
    
    pc = x['AddressInfo']['Postcode']
    pc_list.append(pc)

print(len(pc_list))

# 20 mile radius reaches over to Bristol - bit far!

for x in pc_list:
    if x.startswith('BS') == True:
        print(x)

# how many postcodes are CF, Cardiff?
        
len([x for x in pc_list if x.startswith('CF') == True])



### 200 entries from the UK

params = {"key": ocm_key,
          "countrycode": "GB", 
          "output": "json", 
          "compact": True, 
          "verbose": False, 
          "maxresults": 200}

endpoint = 'https://api.openchargemap.io/v3/poi/?'

req = requests.get(endpoint, params = params)
data = req.json()
print(req)

# empty lists to collect cities, and postcodes (and the IDs of problem entries)

city_list = []
pc_list = []
problem_list = []

for x in data:
    
    try:
        town = x['AddressInfo']['Town']
        pc = x['AddressInfo']['Postcode']

        city_list.append(town)
        pc_list.append(pc)
    
    except:
        problem_list.append(x['ID'])
        pass

# build a frequency distribution dictionary for cities, then postcodes
counter = collections.Counter(city_list)
city_freq_dict = dict(counter)

counter = collections.Counter(pc_list)
pc_freq_dict = dict(counter)

# check the number of towns and postcodes gathered, from the 200 entries

print(len(city_list))
print(len(pc_list))

# and the number of problems
print(len(problem_list))

# from a (not at all random) sample of 200 entries, how are UK cities represented?

dict(sorted(city_freq_dict.items(), key=lambda item: item[1], reverse = True))


