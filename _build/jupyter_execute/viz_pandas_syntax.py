# Basic charts in pandas

### documentation

> https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html

> https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html

> Source (pubs): https://www.ons.gov.uk/businessindustryandtrade/business/activitysizeandlocation/datasets/publichousesandbarsbylocalauthority

> Source (population): https://statswales.gov.wales/Catalogue/Population-and-Migration/Population/Estimates/Local-Authority/populationestimates-by-localauthority-year

> plots available in pandas


        ‘line’ : line plot (default)
        ‘bar’ : vertical bar plot
        ‘barh’ : horizontal bar plot
        ‘hist’ : histogram
        ‘box’ : boxplot
        ‘kde’ : Kernel Density Estimation plot
        ‘density’ : same as ‘kde’
        ‘area’ : area plot
        ‘pie’ : pie plot
        ‘scatter’ : scatter plot
        ‘hexbin’ : hexbin plot



import pandas as pd

import matplotlib.pyplot as plt

# import population data in Wales for 2001, 2018

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/'
file = 'wales_population.csv'

pop = pd.read_csv(path + file)


pop[:3]

# check data types 

pop.info()

# fix integers

# remove the ,
pop = pop.replace(',','', regex = True)

# cast population columns to integers
pop.pop_one = pop.pop_one.astype(int)
pop.pop_eighteen = pop.pop_eighteen.astype(int)

# check datatypes again

print(pop.info())
pop[:3]

## Bar chart

# use area names column as index (instead of row numbers) - this will label the x axis

pop.set_index('area', inplace=True)

pop.head()

# bar chart

pop.pop_eighteen.plot(kind = 'bar')

# this works a placeholder 'do nothing' but here stops the <AxesSubplot:title ETC. A semicolon also works
pass

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 5))

pop.boxplot(vert=False, color = 'black')

plt.xlabel('\nxlabel', fontsize = 14)
# plt.legend(topleft)

plt.title('Some title\n', fontsize = 16)

plt.show()


<br><br><br>

# # horizontal bar chart, with adjusted opacity, title and figure size

pop.pop_eighteen.plot(kind = 'barh', alpha = 0.5, figsize=(15,9));

# stacked barchart with title, grid and labels

pop[['pop_one','pop_eighteen']].plot(kind = 'barh', 
                                     figsize=(15,9),
                                     title = 'Population estimates mid-2001 & mid-2018 in Wales (by local authority)',
                                     grid = True,
                                     stacked = False,
                                     xlabel = 'Area', 
                                     ylabel = 'Population');

<br><br>
## Linechart

> using numbers of pubs in Wales by local authority 2001-18

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/'
file = 'wales_pubs_area_2001_18.csv'

# give the df a variable name 'years'
years = pd.read_csv(path + file)

years[:2]

# delete the 'code' column

del years['code']

# set the area name as the index

years = years.set_index('area')

years[:2]

# transpose to set the years as the y axis and rename the vertical axis as 'year'

years = years.transpose().rename_axis('year', axis=1)

years[:2]

# plot a single column by time

years.Conwy.plot(title = 'Number of pubs in Conwy, 2001-18');

# plot a selection of columns

years[['Cardiff', 'Newport', 'Swansea']].plot(figsize = (15, 9), title = 'Number of pubs in Cardiff, Newport & Swansea, 2001-18');


# plot a period and several areas

years['2008':'2016'][['Ceredigion', 'Pembrokeshire', 'Carmarthenshire']].plot(figsize = (15, 9), 
                                                                             title = 'Number of pubs in Ceredigion, Carmarthenshire & Pembrokeshire & Swansea, 2008-16');


<br><br>

## Scatterplot

> Wales pubs and population in 2018: gives a (dependent) variable to set against population: the number of pubs in local authorities

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/'
file = 'wales_all.csv'

pp = pd.read_csv(path + file)

pp[:3]

# scatterplot with dotsize (s) and dotcolour (c)

pp.plot(kind = 'scatter', 
        x = 'pop', 
        y = 'pubs', 
        figsize=(15,9),
        alpha = 0.9,
        title = ('Population (mid-2018 estimate) and number of pubs in Wales (by local authority)'),
        grid = True,
        s = 165, 
        c = 'r',
        xlabel = 'POPULATION',
        ylabel = 'PUBS')

# save to current directory
plt.savefig('wales_pop_pub.png')

<br><br>

## Histogram

# histogram on a single column

pop.pop_eighteen.hist();

# histogram on both cols

pop[['pop_one','pop_eighteen']].plot(kind = 'hist', 
                                     alpha = 0.5, 
                                     figsize=(15,9),
                                     title = 'Population estimates mid-2001 & mid-2018 in Wales (by local authority)',
                                     grid = True,
                                     stacked = False,
                                     bins = 12,
                                     xlabel = 'Area', 
                                     ylabel = 'Population');


<br><br>

## Piechart

# piechart

pop['pop_one'].plot.pie(figsize=(20,12), title = 'Breakdown of Welsh population in 2001 by local authority');


<br><br>

## Boxplot

# box plots by single column...

pop.boxplot('pop_one'); 

pop.boxplot('pop_eighteen');

# ... and by df (with default vertical turned off) and colour selected

pop.boxplot(vert = False, grid = False, color = 'red');





