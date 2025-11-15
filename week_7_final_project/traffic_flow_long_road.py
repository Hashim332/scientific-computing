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
TOTAL_TIME = range(1, 151)
MAXIMUM_SPEED = 5
ROAD_LENGTH = 100
PROBABILITY_THRESHOLD = 0.6
np.random.seed(0xDECAFBAD)
t = 0

# speed and position arrays of cars at t = 0
car_speeds = [0] * 10
car_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_of_cars = len(car_speeds)

# dummy arrays to store updated variables inside the loop so that the road can be updated simultaneously
updated_positions = np.zeros([10])
updated_speeds = np.zeros([10])

# placement of cars on road and printing the road
road = ['.'] * ROAD_LENGTH
initialise_road()
road_states = np.array([road])
print_road()

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

    print_road()
    plt.pause(0.05)

    # saving a snapshot of this road so that this can be plotted
    np_road = np.array([road])
    road_states = np.append(road_states, np_road, 0)


# PLOTTING
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }
bbox_dict = dict(facecolor='grey', alpha=0.4)

fig = plt.figure(figsize=(11, 8))
ax = plt.axes((0.075, 0.05, 0.9, 0.9))
axes_height = np.linspace(0.95, 0.05, 30)
p_vals = range(80, 110)

for p in p_vals:
    text2 = ax.text(
        0.03, axes_height[p_vals.index(p)], " ".join([str(x) for x in road_states[p]]), bbox=bbox_dict)

ax.set_xlabel("Space (road) ", fontdict=font, labelpad=10)
ax.xaxis.set_label_position('top')
plt.xticks([])

ax.set_ylabel("Time", fontdict=font)
plt.yticks([0.95])
ax.set_yticklabels(["80s"])

ax.spines[['bottom', 'right']].set_visible(False)
plt.show()
