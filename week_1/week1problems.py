from importlib.metadata import distribution
from matplotlib.backend_bases import key_press_handler
import numpy as np
import matplotlib.pyplot as plt

# Question 1
# array_of_10 = np.arange(1, 11, 1)
# print(len(array_of_10), array_of_10)

# # further parts
# array_sum = np.sum(array_of_10)
# array_mean = np.mean(array_of_10)
# array_median = np.median(array_of_10)

# print(f"""The array python has printed is {array_of_10}, the sum of all its values is {array_sum}, the mean and median 
# of all the values in the array are {array_mean} and {array_median} respectively.""")


# # Question 2
# uniform_integers = np.random.randint(1, 13, 1200)
# print(uniform_integers)

# unique, recurrences = np.unique(uniform_integers, return_counts=True)
# #print(unique, recurrences)
# print(f"A dictionary containing the number of recurring values for each number: {dict(zip(unique, recurrences))}")

# plt.figure(1, figsize=(8,6))
# fig1 = plt.axes()
# fig1.hist(uniform_integers, bins=12)
# plt.show()


# Question 3
# arr_1 = [] #The intermediate values of the sum are stored in this array to be used later on
# arr_2 = []
# n = np.arange(0, 21)

# for i in n:
#     leibniz_sum = ((-1)**i)/(2*i + 1)
#     arr_1.append(leibniz_sum)
#     var_1 = np.sum(arr_1)
#     arr_2.append(var_1)


# pi = 4 * np.array(arr_2)
# print(f"The final Leibniz sum is {pi[-1]}")

# plt.figure(2, figsize=(8, 6))
# fig2 = plt.axes()
# fig2.plot(n, pi, "-*")
# fig2.set_xlabel("n")
# fig2.set_ylabel("Leibniz sum")
# plt.show()

#part (b)
n = 0
arr_1 = [] 
arr_2 = []
delta_vals = 0

while True:
    leibniz_sum = ((-1)**n)/(2*n + 1)
    arr_1.append(leibniz_sum)
    var_1 = np.sum(arr_1)
    arr_2.append(var_1)
    n += 1
    if len(arr_2) >= 2:
        pi = 4 * np.array(arr_2)
        delta_vals = pi[-1] - pi[-2]
        if abs(delta_vals) <= 0.02:
            break



print(n, delta_vals)
print(pi[-1])



# Question 4

# integer_n = 7
# vector_n = np.arange(1, integer_n+1)
# k_square_vector = []
# k_square_value = None
# k_square_sum = None

# for i in vector_n:
#     k_square_value = (i * (i +1) * (2*i + 1)) / 6
#     k_square_vector.append(k_square_value)
#     k_square_sum = np.sum(k_square_vector)

# print(f"""The vector containing the k squared values is {k_square_vector}, where the value {k_square_vector[-1]}
# is the value for {integer_n} and the sum of the values in this vector is {k_square_sum}""")

# # Question 5
# # part (a)
# height_vals = np.array([2.2, 2.1, 1.8, 2.1, 2.0, 1.9])
# h_mean = np.mean(height_vals)
# print(f"The mean of the values of height {height_vals} is {h_mean:.2f}. ")

# # part (b)
# L = len(height_vals) #Used as index for iterating through height_vals
# h_sum_vector = []

# for i in range(L):
#     h_minus_hbar_term = (height_vals[i] - h_mean) ** 2
#     h_sum_vector.append(h_minus_hbar_term)

# h_sum = np.sum(h_sum_vector)

# width = np.sqrt(1/L * h_sum)
# print(f"The width is {width:.2f}")

# # part (c)
# h_plus_w = h_mean + width 
# h_minus_w = h_mean - width

# for i in range(L):
#     if height_vals[i] > h_plus_w:
#         print(f"{height_vals[i]} was determined to be greater than {h_plus_w:.2f}")
#     elif height_vals[i] < h_minus_w:
#         print(f"{height_vals[i]} was determined to be less than {h_minus_w:.2f}")

# # Question 6
# # part(a)

# k_boltzmann = 1.38e-23
# temperatures = [1e7,2e7, 3e7]
# energies = np.linspace(0, 1.5e-15, 100)
# total_distribution_vals = []

# for i in temperatures:
#     for j in energies:
#         maxwell_boltzmann = 2/np.sqrt(np.pi)*((1/(2*k_boltzmann * i))**1.5) * j**0.5 * np.exp(-j/(k_boltzmann*i))
#         total_distribution_vals.append(maxwell_boltzmann)

# distribution_t1 = total_distribution_vals[0:100]
# distribution_t2 = total_distribution_vals[100:200]
# distribution_t3 = total_distribution_vals[200::]

# plt.figure(3, figsize=(8, 6))
# fig3 = plt.axes()
# fig3.plot(energies, distribution_t1, 'r')
# fig3.plot(energies, distribution_t2, 'b')
# fig3.plot(energies, distribution_t3, 'g')
# fig3.set_xlabel("")
# fig3.set_xlabel("")
# plt.show()