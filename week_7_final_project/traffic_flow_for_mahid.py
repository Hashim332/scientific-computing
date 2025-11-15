import numpy as np


'''This code is simulating 2 cars on a circular road similar to the periodic lattice question, if the
 distance between the 2 cars is too little, they must slow down, if not they may accelerate.
 The issue being faced here is that I'm not trying to update the core values in the position and speed
 arrays within the loop, im assigning any 'new' values to dummy arrays. These dummy arrays update the core
 variable arrays at the end of the time step. However, within the inner loop there seems to be an issue
 and the core variable array is getting updated causing one of the cars to think the car ahead of it has 
 already moved therefore it does not slow down accordingly. Please let me know if you see any error that may
 cause the car that loops around to not see the car ahead of it. The % (modulo) operator is used to generate
 the periodic conditions, if you're not familliar with it, just do a quick google search and it will become 
 clear.
 In some places there are print statements that were being used to troubleshoot, please ignore them or feel 
 free to run the code with them uncommented to see what I mean. The main error that is ocurring is simply 
 confined to the value of the variable 'next_cars_pos'. The entire loop relies on this variable being
 calculated correctly but as you can see, it returns the value for the next timestep for some reason.
 
 Please read through slowly and let me know what you see. Thanks! '''

# function to place cars at t = 0 before beginning simulation


def initialise_road():
    for i in car_positions:
        road[i] = car_speeds[car_positions.index(i)]


# intial conditions
TOTAL_TIME = range(1, 11)
MAXIMUM_SPEED = 5
ROAD_LENGTH = 10


# speed and position arrays of cars at t = 0 for test case scenario
car_speeds = [0, 5]
car_positions = [2, 7]
# array length used for to create a range to loop over later
array_length = len(car_speeds)

# dummy arrays to store updated variables inside the loop
updated_positions = np.zeros([2])
updated_speeds = np.zeros([2])

# placement of car on road and printing the road at t = 0
road = ['.'] * ROAD_LENGTH
initialise_road()
print(f"The road at t = 0s", "".join([str(x) for x in road]))

# time step loop
for t in TOTAL_TIME:

    # inner loop for the cars
    for i in range(array_length):

        # next_cars_pos = car_positions[(i + 1) % array_length]

        # trying to use a simpler method to get the next cars position
        if i+1 <= (array_length - 1):
            next_cars_pos = car_positions[i+1]
        else:
            next_cars_pos = car_positions[0]

        # print(" \nposition index of next car = ", next_cars_pos)

        # assigning 'current' position and speed values to avoid updating positions and speed arrays prematurely within the loop
        current_pos = car_positions[i]
        current_speed = car_speeds[i]

        # print("current pos = ", current_pos)

        # due to periodic road nature, if the car goes past the last index, it loops back around
        # to account for this when measuring relative distances, these if checks check the indices of the cars
        # if the inex of next car is greater i.e we are considering the correct order, a simple calculation to find dx can be done
        if next_cars_pos > current_pos:
            delta_positions = next_cars_pos - current_pos

        # the case where a car loops around and ends up behind is encoded here
        elif next_cars_pos < current_pos:
            delta_positions = next_cars_pos - current_pos + ROAD_LENGTH

        # print(f"delta positions = {delta_positions}")
        # print("car_speeds", car_speeds, "car_positions", car_positions)

        # here are the acceleration and decceleration rules the if statement checks if there must be decceleration
        if delta_positions <= current_speed:
            new_speed = delta_positions - 1

        # the elif statement accelerates the cars if they are not already at max speed
        elif current_speed < MAXIMUM_SPEED:
            new_speed = current_speed + 1

        # new position calculated with the new speed
        new_position = (current_pos + new_speed) % ROAD_LENGTH

        # dummy arrays are updated here, one by one
        updated_positions[i] = new_position
        updated_speeds[i] = new_speed

    # road is cleared in preperatio for updating
    road = ['.'] * ROAD_LENGTH

    # dummy arrays and real arrays swapped as both cars have moved and sped up or slowed down
    car_speeds = updated_speeds
    car_positions = updated_positions

    # road is updated
    for i in range(array_length):
        road[int(car_positions[i])] = int(car_speeds[i])

    # road is printed
    print(f"The road at t = {t}s", "".join([str(x) for x in road]))
    print('-' * 50)
