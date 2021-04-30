# Random notebook

> It's only a test for now....but think what we can put in it...

# import

import random
import matplotlib.pyplot as plt

# here's one

random.randint(2, 5)

# here's another via print

print(random.randint(2, 5))

def make(x):
    return random.randint(2, x)

make(7)

make(11)

one = [2, 5, 6]
two = [45, 34, 21]

# this line is optional
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_title('I made a scatterplot', size = 24)
plt.scatter(one, two)
plt.show()


