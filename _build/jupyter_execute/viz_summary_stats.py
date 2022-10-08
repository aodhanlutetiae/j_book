# Summary statistics

Overview of three examples of how summary statistics can hide differences that are exposed through visualisation

The three sources are:

> https://www.sjsu.edu/faculty/gerstman/StatPrimer/anscombe1973.pdf

> http://www.thefunctionalart.com/2016/08/download-datasaurus-never-trust-summary.html

> https://www.autodesk.com/research/publications/same-stats-different-graphs

See also (not considered here): https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128

import pandas as pd

from IPython.display import display_html
from itertools import chain,cycle

import numpy as np
import matplotlib.pyplot as plt


## Anscombe (1973)

# define file locations

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/anscombe_csvs/'

file1 = 'ans1.csv'
file2 = 'ans2.csv'
file3 = 'ans3.csv'
file4 = 'ans4.csv'

# read in and assign to four different variables

one = pd.read_csv(path + file1)
two = pd.read_csv(path + file2)
three = pd.read_csv(path + file3)
four = pd.read_csv(path + file4)


# VERY HELPFUL FUNCTION TAKEN FROM THIS STACK OVERFLOW USER TO DISPLAY DATAFRAMES SIDE BY SIDE
# https://stackoverflow.com/questions/38783027/jupyter-notebook-display-two-pandas-tables-side-by-side

def display_side_by_side(*args, titles=cycle([''])):
    html_str=''
    
    for df,title in zip(args, chain(titles,cycle(['</br>'])) ):
        html_str+='<th style="text-align:center"><td style="vertical-align:top">'
        html_str+=f'<h2>{title}</h2>'
        html_str+=df.to_html().replace('table','table style="display:inline"')
        html_str+='</td></th>'
        
    display_html(html_str,raw=True)

# run function: show data in the four dfs

display_side_by_side(one, two, three, four, titles=['one','two', 'three', 'four']) 

# show summary statistics (function will run with added methods chained on)

display_side_by_side(one.describe().round(2), 
                     two.describe().round(2), 
                     three.describe().round(2), 
                     four.describe().round(2), 
                     titles=['one','two', 'three', 'four'])


# what about correlation between x and y in the four datasets? The same up to three decimal points

print(np.corrcoef(one.x1, one.y1)[1][0].round(5))
print(np.corrcoef(two.x2, two.y2)[1][0].round(5))
print(np.corrcoef(three.x3, three.y3)[1][0].round(5))
print(np.corrcoef(four.x4, four.y4)[1][0].round(5))


# plot the four datasets

one.plot(kind = 'scatter', x = 'x1', y = 'y1', title = 'ONE');
two.plot(kind = 'scatter', x = 'x2', y = 'y2', title = 'TWO');
three.plot(kind = 'scatter', x = 'x3', y = 'y3', title = 'THREE');
four.plot(kind = 'scatter', x = 'x4', y = 'y4', title = 'FOUR');

## Lines

> The relationships between x values and y values are similar when seen in lines, but of course are not the same, as the data is not the same (just the measures of central tendancy)

# define the two sets of data

x = np.array(one.x1)
y = np.array(one.y1)
plt.plot(x, y, 'o')

# establish the slope (m) and the intercept (c)

m, c = np.polyfit (x, y, 1)

# plot the linear regression

plt.plot (x, m * x + c)

# print the value of the slope and where it's situated (in terms of the y-axis)

print('slope:', m.round(5), 'y-int:', c.round(5))


x = np.array(two.x2)
y = np.array(two.y2)
plt.plot(x, y, 'o')

m, c = np.polyfit (x, y, 1)

plt.plot (x, m * x + c)

print('slope:', m.round(5), 'y-int:', c.round(5))


x = np.array(three.x3)
y = np.array(three.y3)
plt.plot(x, y, 'o')

m, c = np.polyfit (x, y, 1)

plt.plot (x, m * x + c)

print('slope:', m.round(5), 'y-int:', c.round(5))


x = np.array(four.x4)
y = np.array(four.y4)
plt.plot(x, y, 'o')

m, c = np.polyfit (x, y, 1)

plt.plot (x, m * x + c)

print('slope:', m.round(5), 'y-int:', c.round(5))

## Datasaurus (2016)

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/'
file = 'datasaurus_data.csv'

cols = ['town_A', 'town_B']
din = pd.read_csv(path + file, names = cols)

# say the data refers to two towns...

din

# scatter plot to show any trends in the relationship betwen the data in town A, and the data in town B

din.plot.scatter(x = 'town_A', y = 'town_B');


## Datasaurus dozen (2017)

path = '/Users/aidanair/Documents/DATA/ALL_DATASETS/'
file1 = 'DatasaurusDozen.tsv'

d = pd.read_csv(path + file1, sep = "\t")


print(d.shape)
d[:3]

> "These 13 datasets (the Datasaurus, plus 12 others) each have the same summary statistics (**x/y mean**, **x/y standard deviation**, and **Pearson's correlation**) to two decimal places, while being drastically different in appearance."


## Consider two of the dozen

display_side_by_side(d[d.dataset == 'away'].head(), 
                     d[d.dataset == 'bullseye'].head(), 
                     titles=['away','bullseye'])

# Show the correlation measure, and the mean and std for x values and y values in each of the two datasets

print('(Pearson) Correlation between x and y values for "Away" and "Bullseye" datasets')
print('Away:', np.corrcoef(d[d.dataset == 'away'].x, d[d.dataset == 'away'].y)[1][0].round(3))
print('Bullseye:', np.corrcoef(d[d.dataset == 'bullseye'].x, d[d.dataset == 'bullseye'].y)[1][0].round(3))

display_side_by_side(d[d.dataset == 'away'].describe().round(2), 
                     d[d.dataset == 'bullseye'].describe().round(2), 
                     titles=['away','bullseye'])

# plot both datasets, with their (almost) identical mean, std and correlation

df = d[d.dataset == 'away']
df.plot(kind = 'scatter', x = 'x', y = 'y');

df = d[d.dataset == 'bullseye']
df.plot(kind = 'scatter', x = 'x', y = 'y');


# plot the dinosaur and the dozen others

sets = d.dataset.unique().tolist()

for x in sets:
    df = d[d.dataset == x]
    df.plot(kind = 'scatter', x = 'x', y = 'y', title = x)











