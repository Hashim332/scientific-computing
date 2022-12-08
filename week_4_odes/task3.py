import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

'''In this task, gamma was denoted to be first derivative of psi, the wavefunction and therefore 
gamma_prime to be the second derivative of psi'''


def gamma_prime(energy, wavefunction_value, V_0):
    # a function to calculate the double differential
    return -(V_0*wavefunction_value + energy*wavefunction_value)


DX = 0.02

# e_guess wasn't able to be determined via a loop condition due to the way
# python handles floats and large decimal points
e_guess = -8.5052111

# initial arrays for region 1 (inside potential well) using boundary conditions
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
for i in range(150):
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

print(x1[-1])
print(psi1[-1])

plt.show()
