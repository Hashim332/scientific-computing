import numpy as np
import matplotlib.pyplot as plt


def initialise_road():
    # function to place cars at t = 0
    for i in car_positions:
        road[i] = car_speeds[car_positions.index(i)]


def print_road():
    # encapsulates print function to make code neater and easier to read
    print(f"The road at t = {t}s", "".join([str(x) for x in road]))


# global variables and initialising varables
TOTAL_TIME = range(1, 751)
MAXIMUM_SPEED = 5
ROAD_LENGTH = 2000
PROBABILITY_THRESHOLD = 0.6
np.random.seed(0xDECAFBAD)
t = 0
# the time after which to start measuring traffic flow
t_start_count = 50

num_of_car_range = range(10, 251)
road_densities = []
flow_rates = []

for num_of_cars in num_of_car_range:
    print(num_of_cars)

    # speed and position arrays of cars at t = 0 for test case scenario
    car_speeds = [0] * num_of_cars
    car_positions = list(range(0, num_of_cars))

    # dummy arrays to store updated variables inside the loop so that the road can be updated simultaneously
    updated_positions = np.zeros([num_of_cars])
    updated_speeds = np.zeros([num_of_cars])

    # placement of cars on road and printing the road
    road = ['.'] * ROAD_LENGTH

    # cars the pass the end of the road
    car_count = 0

    for t in TOTAL_TIME:
        # random values to compare vs threshold to determine if car should decelerate randomly
        random_values = np.random.rand(num_of_cars)

        for i in range(num_of_cars):

            next_cars_pos = car_positions[(i + 1) % num_of_cars]

            # assigning 'current' position and speed values to avoid updating positions and speed arrays prematurely
            current_pos = car_positions[i]
            current_speed = car_speeds[i]

            # these lines sort the cars and assign the leftmost probability to the leftmost car on the road
            pos_order = np.sort(car_positions)
            probability_index = np.where(pos_order == current_pos)
            probability = random_values[probability_index]

            # due to periodic road nature, if the car goes past the last index, it loops back around
            # when measuring relative distances, if checks check the indices of cars relative to eachother
            if next_cars_pos > current_pos:
                delta_positions = next_cars_pos - current_pos

            # the case where a car loops around and ends up behind is encoded here
            elif next_cars_pos < current_pos:
                delta_positions = next_cars_pos - current_pos + ROAD_LENGTH

            empty_cells = delta_positions - 1

            if empty_cells <= current_speed:
                new_speed = empty_cells
            elif current_speed < MAXIMUM_SPEED:
                new_speed = current_speed + 1
            else:
                new_speed = current_speed

            if probability < PROBABILITY_THRESHOLD and new_speed > 0:
                new_speed -= 1

            # new position calculated with the new speed using modulo
            new_position = (current_pos + new_speed) % ROAD_LENGTH

            if current_pos + new_speed > ROAD_LENGTH and t >= t_start_count:
                car_count += 1

            # dummy arrays are updated here
            updated_positions[i] = new_position
            updated_speeds[i] = new_speed

        # road is cleared in preperation for updating with new values
        road = ['.'] * ROAD_LENGTH
        # road and car paraemeters are updated and printed
        for m in range(num_of_cars):
            car_speeds[m] = updated_speeds[m]
            car_positions[m] = updated_positions[m]
            road[int(car_positions[m])] = int(car_speeds[m])

    # calculating road density and flow rate for each iteration of car numbers and saving them
    road_density = num_of_cars / ROAD_LENGTH
    flow_rate = car_count / (len(TOTAL_TIME) - t_start_count)

    road_densities.append(road_density)
    flow_rates.append(flow_rate)

    # print("density", road_density)
    # print("flow rate", flow_rate)

# PLOTTING
fig = plt.figure()
ax = plt.axes()

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }

ax.plot(road_densities, flow_rates, "*")
ax.set_xlabel("Density (cars per site)", fontdict=font)
ax.set_ylabel("Flow rate (cars per timestep)", fontdict=font)
plt.show()
