import tensorflow as tf
import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

houses = 160
np.random.seed(42)

house_size = np.random.randint(1000, 3500, houses)

np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(20000, 72000, houses)

plt.plot(house_size, house_price, "bx")
plt.xlabel("Size")
plt.ylabel("House")
plt.show()


def normalize(array):
    return (array - array.mean()) / array.std()

