import numpy as np

# initial parameters
TOTAL_TIME = range(11)
V_MAX = 5

# intialising the road and cars
v_car1 = 5

road = ['.', '.', '.', '.', '.', '.', '.',
        '.', '.', '.']  # empty cells are occupied by '.'
road[1] = v_car1  # places the car at the desired index

for i in TOTAL_TIME:

    # print(f"The road at {i}: {road}")
    print(f"The road at {i}", "".join([str(x) for x in road]))

    #
    old_pos = road.index(v_car1)
    new_pos = (old_pos + v_car1) % len(road)

    road[old_pos], road[new_pos] = road[new_pos], road[old_pos]
