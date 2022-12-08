from email.base64mime import header_length
from random import random
from time import time
from matplotlib import test
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Task 1: Generating distributions

# random_integers = np.random.randint(0, 10000, 10000)/10000
# plt.figure(1, figsize=(6, 5))
# fig1 = plt.axes()
# fig1.hist(random_integers, bins=100)
# fig1.set_ylabel("Frequency")
# fig1.set_xlabel("Number")

# linear_y = np.sqrt(2*random_integers)
# plt.figure(2, figsize=(6, 5))
# fig2 = plt.axes()
# fig2.hist(linear_y, bins=50)
# fig2.set_ylabel("Frequency")
# fig2.set_xlabel("Number")

# Task 2: Monte Carlo Integration

# limit = np.pi/2

# # x needs to be from -limit to +limit
# x = np.arange(-limit, limit+0.01, 0.01)
# base_function = np.exp(-np.abs(x)) * np.cos(x)

# # Initialising figure window
# plt.figure(3, figsize=(6, 5))
# fig3 = plt.axes()
# fig3.plot(x, base_function, "m")
# fig3.set_title("$Monte$ $Carlo$ $Integration$")
# fig3.set_xlabel("x")
# fig3.set_ylabel("f(x)")

# # test func must resemble a square
# test_y_range = list(np.random.randint(0, 120, 2500)/100)
# test_x_range = list(np.random.randint(-(limit*100000),
#                     (limit*100000), 2500)/100000)

# y_length = max(test_y_range) - min(test_y_range)
# x_length = max(test_x_range) - min(test_x_range)


# # count is number of values under curve
# count = 0

# for n in test_x_range:
#     function_value = np.exp(-np.abs(n)) * np.cos(n)
#     index = test_x_range.index(n)

#     y_coordinate = test_y_range[index]
#     plt.pause(0.001)

#     if y_coordinate >= function_value:
#         fig3.plot(n, y_coordinate, 'r*')
#     else:
#         fig3.plot(n, y_coordinate, "g*")
#         count += 1

# area = count/len(test_x_range) * (x_length * y_length)
# print(f"The area via Monte Carlo integration is {area}")


# def base_function2(x): return np.exp(-np.abs(x)) * np.cos(x)


# calculated_area = sp.integrate.quad(base_function2, -limit, limit)
# print(f"The calculated area via an inbuilt function is {calculated_area}")


# Task 3: 3D Monte Carlo Integration of a torus

outer_radius = 10
inner_radius = 5
count = 0

# since radius encodes x and y it is more useful than 2 seperate variables for x, y
radius_range = list(np.random.randint(5000, 10000, 5000)/1000)
random_zs = np.random.randint(0, 5000, 5000)/1000

max_radius = max(radius_range) - min(radius_range)

for i in radius_range:
    z_squared = ((outer_radius - inner_radius)/2)**2 - \
        (np.sqrt(2*(i**2)) - (outer_radius + inner_radius)/2)**2
    index2 = radius_range.index(i)

    z_coordinate = random_zs[index2]
    # plt.pause(0.001)

    if z_coordinate**2 < z_squared:
        count += 1

volume = count/len(radius_range) * ((max_radius**2) * random_zs[4999])

print(f"The volume of the torus via Monte Carlo methods is {volume}")


def function_torus(x): return ((outer_radius - inner_radius)/2)**2 - \
    (np.sqrt(2*(x**2)) - (outer_radius + inner_radius)/2)**2


calc_torus_vol = sp.integrate.quad(function_torus, -5, 5)
print(f"The volume of the torus via integration is {calc_torus_vol}")


# Task 4: 2D Random Walks

# plt.figure(4, figsize=(6, 5))
# fig4 = plt.axes()
# fig4.set_xlim(-20, 20)
# fig4.set_ylim(-20, 20)
# fig4.plot(0, "m*")
# fig4.set_xticks([])
# fig4.set_yticks([])
# fig4.set_title("$2D$ $Random$ $Walks$")
# fig4.set_facecolor("black")

# time_step = range(1000)
# arrow_width = 0.1
# current_x = 0
# current_y = 0

# for i in time_step:

#     plt.pause(0.5)
#     probability = np.random.randint(0, 100, 1)

#     if probability <= 25:
#         fig4.arrow(current_x, current_y, 1, 0, width=arrow_width,
#                    edgecolor="b", facecolor="b")
#         current_x += 1

#     elif 25 < probability <= 50:
#         fig4.arrow(current_x, current_y, 0, 1, width=arrow_width,
#                    edgecolor="r", facecolor="r")
#         current_y += 1

#     elif 50 < probability <= 75:
#         fig4.arrow(current_x, current_y, -1, 0, width=arrow_width,
#                    edgecolor="g", facecolor="g")
#         current_x -= 1

#     elif 75 < probability <= 100:
#         fig4.arrow(current_x, current_y, 0, -1, width=arrow_width,
#                    edgecolor="y", facecolor="y")
#         current_y -= 1

#     print(current_x, current_y)
# plt.show()
