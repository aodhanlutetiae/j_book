#!/usr/bin/env python
# coding: utf-8

# ## Open Charge Map API
# 
# > documentation: https://openchargemap.org/site/develop/api
# 
# > forum: https://community.openchargemap.org/
# 

# In[1]:


import requests
import collections


# In[2]:


# assign API key to variable

ocm_key = '****'


# In[3]:


# test query for GB (Great Britain), 100 results, as single url

call = 'https://api.openchargemap.io/v3/poi/?key=ocm_key&output=json&countrycode=GB&maxresults=100&compact=true&verbose=false'
req = requests.get(call)
req


# In[4]:


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


# In[5]:


# how many items were returned?

len(req.json())


# In[6]:


# assign to variable and examine first item

data = req.json()
data[0]


# In[7]:


# assemble list of postcodes

pc_list = []

for x in data:
    
    pc = x['AddressInfo']['Postcode']
    pc_list.append(pc)

print(len(pc_list))


# In[8]:


# 20 mile radius reaches over to Bristol - bit far!

for x in pc_list:
    if x.startswith('BS') == True:
        print(x)


# In[9]:


# how many postcodes are CF, Cardiff?
        
len([x for x in pc_list if x.startswith('CF') == True])


# In[ ]:





# In[10]:


# Try 200 queries on the UK

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


# In[11]:


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


# In[12]:


# check the number of towns and postcodes gathered, from the 200 entries

print(len(city_list))
print(len(pc_list))

# and the number of problems
print(len(problem_list))


# In[13]:


# from a (not at all random) sample of 200 entries, how are UK cities represented?

dict(sorted(city_freq_dict.items(), key=lambda item: item[1], reverse = True))


# In[ ]:




