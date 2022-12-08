import random

# Define the parameters of the model
road_length = 100  # Length of the road
v_max = 5  # Maximum velocity of the vehicles
p = 0.3  # Probability of random deceleration

# Initialize the road
road = [0] * road_length  # 0 indicates an empty cell
road[10] = 1  # 1 indicates a vehicle
road[20] = 2  # 2 indicates a vehicle with velocity 2

# Perform the simulation
for time_step in range(100):
    # Perform the four steps of the simulation in parallel
    for i in range(road_length):
        # Step 1: Acceleration
        if road[i] > 0 and road[i] < v_max:
            road[i] += 1

        # Step 2: Following
        j = 1  # Number of empty cells between vehicles
        while road[(i + j) % road_length] == 0:
            j += 1
        if road[i] > j - 1:
            road[i] = j - 1

        # Step 3: Randomization
        if road[i] > 0 and random.random() < p:
            road[i] -= 1

        # Step 4: Car motion
        road[(i + road[i]) % road_length] = road[i]
        road[i] = 0

    # Print the current state of the road
    for i in range(road_length):
        if road[i] == 0:
            print('_', end='')
        else:
            print(road[i], end='')
    print()
