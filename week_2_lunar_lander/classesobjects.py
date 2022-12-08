import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as widgets
import matplotlib.patheffects as pe
from random import randint

# TODO add slider for fuelw

DT = np.arange(1, 10001, 0.01)
GRAVITY = 5
TIMER = range(3, 0, -1)
DIFFICULTY = {"easy": 100, "medium": 50, "hard": 25}
GROUND_HEIGHT = 140

user_difficulty_selection = input("""Please type in your difficulty from the options below\n
Easy \nMedium \nHard\n\n""").lower()
threshold_velocity = DIFFICULTY[user_difficulty_selection]


def close_callback(event):
    plt.close('all')


def game_timer():
    # Gives player time to adjust thruster value
    for i in TIMER:
        t = ax.text(
            0.28, 0.5, f"Game starting in {i}s", c="lime", weight="bold", size=20)
        t.set_path_effects(
            [pe.withStroke(linewidth=3, foreground="green")])
        plt.pause(1)
        ax.cla()


def velocity_colour():
    if abs(my_rocket.velocity) > threshold_velocity:
        colour = "red"
    else:
        colour = "green"
    vc = text_axes.text(
        0.1, 0.3, f"V = {abs(round(my_rocket.velocity, 2))} m/s", c=colour, size=15)
    vc.set_path_effects([pe.withStroke(linewidth=0.5, foreground="w")])
    print(my_rocket.velocity)


def stars():
    for _ in range(75):
        ax.plot(randint(-500, 500) / 100, randint(1000, 10000),
                "*", c="w", markersize=0.5)


def ground():
    ax.axhline(100, 0, lw=5, c="blanchedalmond")


class Rocket:
    velocity = 0
    fuel = 100  # TODO: show the fuel on the UI for the user

    def __init__(self, height, mass, velocity=None, fuel=None):
        self.height = height
        self.mass = mass

        if velocity is not None:
            self.velocity = velocity

        if fuel is not None:
            self.fuel = fuel

    def get_acceleration(self):
        engine_thrust = slider_handle.val
        # engine_thrust is multiplied by 0.25 because fuel consumption and engine thrust need scale factor
        self.fuel = max(self.fuel - engine_thrust * 0.25, 0)
        if self.fuel <= 0:
            engine_thrust = 0
        return engine_thrust - GRAVITY

    def update_velocity(self, dt):
        self.velocity += self.get_acceleration() * dt

    def update_height(self, dt):
        self.height = max(self.height + self.velocity * dt, 50)


my_rocket = Rocket(10000, 1000)

# Set up matplotlib figures and axes
figure = plt.figure(figsize=(10, 8))
figure.set_facecolor("dimgrey")
ax = plt.axes([0.1, 0.1, 0.7, 0.7])
ax.set_facecolor("black")
ax.axes.get_xaxis().set_visible(False)

slider_axes = plt.axes([0.85, 0.1, 0.075, 0.65])
slider_handle = widgets.Slider(
    slider_axes, 'Thrusters', 0, 7, valinit=0, valstep=0.01, orientation="vertical")

button_axes = plt.axes([0.85, 0.85, 0.1, 0.075])
button_handle = widgets.Button(
    button_axes, 'Close', color="white")
button_handle.label.set_font("monospace")
button_handle.on_clicked(close_callback)

text_axes = plt.axes((0.1, 0.85, 0.2, 0.05))
text_axes.set_facecolor("black")
text_axes.axes.get_xaxis().set_visible(False)
text_axes.axes.get_yaxis().set_visible(False)

result_text = plt.axes((0.6, 0.85, 0.2, 0.075))
result_text.set_facecolor("black")
result_text.get_xaxis().set_visible(False)
result_text.axes.get_yaxis().set_visible(False)

game_timer()

for time_step in DT:

    # Prevents axis from rescaling, makes UI work properly.
    text_axes.cla()
    ax.cla()
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 10020)

    # Plots stars and ground, updates rocket variables and text colour
    stars()
    ground()
    my_rocket.update_velocity(time_step)
    my_rocket.update_height(time_step)
    velocity_colour()

    axes_handle, = ax.plot(0, my_rocket.height + GROUND_HEIGHT, 'bo')
    plt.pause(0.01)
    print(my_rocket.height)

    # Checking if player has landed or crashed and exiting loop
    if my_rocket.height <= GROUND_HEIGHT and abs(my_rocket.velocity) > threshold_velocity:
        crashed = result_text.text(
            0.18, 0.3, f"Crashed!", c="r", size=20)
        crashed.set_path_effects(
            [pe.withStroke(linewidth=3, foreground="maroon")])
        break
    elif my_rocket.height <= GROUND_HEIGHT and abs(my_rocket.velocity) < threshold_velocity:
        landed = result_text.text(
            0.18, 0.3, f"Landed!", c="green", size=20)
        landed.set_path_effects(
            [pe.withStroke(linewidth=3, foreground="greenyellow")])
        break

plt.show()
