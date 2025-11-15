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
TOTAL_TIME = range(1, 11)
MAXIMUM_SPEED = 5
ROAD_LENGTH = 10
PROBABILITY_THRESHOLD = 0.6
np.random.seed(0xDECAFBAD)
t = 0

# speed and position arrays of cars at t = 0
car_speeds = [5, 0]
car_positions = [2, 6]
num_of_cars = len(car_speeds)

# dummy arrays to store updated variables inside the loop so that the road can be updated simultaneously
updated_positions = np.zeros([2])
updated_speeds = np.zeros([2])

# placement of cars on road and printing the road at t = 0
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

    # saving a snapshot of this road so that this can be plotted
    np_road = np.array([road])
    road_states = np.append(road_states, np_road, 0)
    plt.pause(0.05)


# PLOTTING
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 14,
        }
fig = plt.figure(figsize=(5, 5))
ax = plt.axes((0.15, 0.1, 0.75, 0.75))
axes_height = np.linspace(0.9, 0.1, len(range(11)))

plt.xticks([])
ax.set_xlabel("Space (road)", fontdict=font, labelpad=10)
ax.xaxis.set_label_position('top')

plt.yticks([])
ax.set_ylabel("Time", fontdict=font)

ax.spines[['bottom', 'right']].set_visible(False)

print(axes_height)

for p in range(11):
    text2 = ax.text(
        0.1, axes_height[p], "      ".join([str(x) for x in road_states[p]]), bbox=dict(facecolor='grey', alpha=0.4))


plt.show()
