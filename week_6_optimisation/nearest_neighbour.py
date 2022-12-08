import numpy as np
import time
import errno

# Set up 3D positions

N = 20000
seed = 1234
np.random.seed(seed)
pos = np.random.random((3, N))
start_time = time.time()

'''I've replaced the s array with s_squared since it does not affect the relative value sizes'''

# initilise s_squared array
s_squared = np.zeros((N, N))

# loop over a with vectorised inner sums using numpy broadcasting to calculate and store nearest neighbour
for a in range(N):
    delta_x = np.abs(pos[0, a] - pos[0, :])
    delta_y = np.abs(pos[1, a] - pos[1, :])
    delta_z = np.abs(pos[2, a] - pos[2, :])

    shortest_x = np.minimum(delta_x, 1-delta_x)
    shortest_y = np.minimum(delta_y, 1-delta_y)
    shortest_z = np.minimum(delta_z, 1-delta_z)

    s_squared[a, :] = shortest_x**2 + shortest_y**2 + shortest_z**2

    # since diagonal elements are 0 (a=b), make them extremely large so that np.minimum finds correct min index
    s_squared[a, a] = 1e10

# checks indices along each row
matched_indices = s_squared.argmin(axis=1)

end_time = time.time()

print('Elapsed time = ', repr(end_time - start_time))

# generate filename from N and seed
filename = 'pyneigh' + str(N) + '_' + str(seed)

# if a file with this name already exists read in the nearest neighbour
# list found before and compare this to the current list of neighbours,
# else save the neighbour list to disk for future reference
try:
    fid = open(filename, 'rb')
    matchedIndicesOld = np.loadtxt(fid)
    fid.close()
    if (matchedIndicesOld == matched_indices).all():
        print('Checked match')
    else:
        print('Failed match')
except OSError as e:
    if e.errno == errno.ENOENT:
        print('Saving neighbour list to disk')
        fid = open(filename, 'wb')
        np.savetxt(fid, matched_indices, fmt="%8i")
        fid.close()
    else:
        raise
