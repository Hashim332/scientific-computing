import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


def A_prime(z, a, j):
    return -(a/z + j)


def epsilon_prime(E, psi):
    return -E * psi

# # Task 1: 2nd order ODE - Bessel function


# N = 0
# DZ = 0.1

# # Initialising arrays
# z = [0]
# j = [1]
# a = [0]

# # Initialise figure window
# plt.figure(1, figsize=(6, 5))
# fig1 = plt.axes()

# for i in range(100):

#     if z == 0:
#         a_half = 0
#     else:
#         a_half = a[i] + DZ/2 * A_prime(z[i] + DZ, a[i], j[i])

#     j_half = j[i] + DZ/2 * a[i]

#     j_next = j[i] + DZ * j_half
#     j.append(j_next)

#     a_next = a[i] + DZ * A_prime(z[i]+DZ/2, a_half, j_half)
#     a.append(a_next)

#     z_new = z[i] + DZ
#     z.append(z_new)

# fig1.plot(z, j)
# plt.show()


# Task 3: 1D Schrodingers Equation
'''We have been given a boundary conditiont that for x >= 0, V is infitinite, therefore
the wavefunction must be 0. This means the derivative of the wavefunction at x = 0 is also
0'''

# Initialise arrays with boundary conditions and global constants, epsilon is psi prime

# DX = 0.01
# # A = range(0, 1.01, 0.01)

# e_guess = -5

# x = [0]
# psi = [0]
# epsilon = [0]

# # Figure windows
# plt.figure(2, figsize=(6, 5))
# fig2 = plt.axes()
# # fig2.set_ylim(0, 4)

# for i in range(101):
#     psi_half = psi[i] + DX/2 * epsilon[i]
#     epsilon_half = epsilon[i] + DX/2 * epsilon_prime(e_guess, psi[i])

#     psi_next = psi[i] + DX * psi_half
#     psi.append(psi_next)

#     epsilon_next = epsilon[i] + DX * epsilon_prime(e_guess, psi_half)
#     epsilon.append(epsilon_next)

#     x_new = x[i] + DX
#     x.append(x_new)

# fig2.plot(x, psi)
# plt.show()

# Task 3


def gamma_prime(energy, wavefunction_value, V_0):
    return -(V_0*wavefunction_value + energy*wavefunction_value)


DX = 0.02

# e_guess wasn't able to be determined via a loop condition due to the way
# python handles floats and large decimal points

e_guess = -8.3

# initial arrays for region 1 (inside potential well)
x1 = [0.05]
psi1 = [-0.1]
gamma1 = [0]

# loop for region 1
for i in range(1000):
    if x1[-1] <= 1:
        psi1_half = psi1[i] + DX/2 * gamma1[i]
        gamma1_half = gamma1[i] + DX/2 * gamma_prime(e_guess, psi1[i], 10)

        psi1_next = psi1[i] + DX * gamma1_half
        psi1.append(psi1_next)

        gamma1_next = gamma1[i] + DX * gamma_prime(e_guess, psi1_half, 10)
        gamma1.append(gamma1_next)

        x1_next = x1[i] + DX
        x1.append(x1_next)

# arrays for loop 2 where values are taken from previous arrays due to continuity

x2 = [x1[-1]]
psi2 = [psi1[-1]]
gamma2 = [gamma1[-1]]

# loop 2 for region 2 (V = 0)
for i in range(100):
    psi2_half = psi2[i] + DX/2 * gamma2[i]
    gamma2_half = gamma2[i] + DX/2 * gamma_prime(e_guess, psi2[i], 0)

    psi2_next = psi2[i] + DX * gamma2_half
    psi2.append(psi2_next)

    gamma2_next = gamma2[i] + DX * gamma_prime(e_guess, psi2_half, 0)
    gamma2.append(gamma2_next)

    x2_next = x2[i] + DX
    x2.append(x2_next)

# figures
plt.figure(1, figsize=(6, 5))
fig1 = plt.axes()
fig1.set_title("Wavefunction $\psi (x)$ via Runge Kutta 2nd order")
fig1.set_ylabel("$\psi (x)$")
fig1.set_xlabel("x")
fig1.plot(x1, psi1, "r*", label="$\psi_1 (x)$")
fig1.plot(x2, psi2, "b*", label="$\psi_2 (x)$")
fig1.legend()

plt.show()
