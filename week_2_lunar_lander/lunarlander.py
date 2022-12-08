import matplotlib.pyplot as plt
import numpy as np
import matplotlib.widgets as widgets

GRAVITY = 5
DT = np.arange(1, 10001, 0.01)


def get_new_position(v, dt):
    return current_position + (v * dt)


def get_new_velocity(a, dt):
    return current_velocity + (a * dt)


def close_callback(event):
    plt.close('all')


figure = plt.figure(figsize=(10, 8))
ax = plt.axes([0.1, 0.1, 0.7, 0.7])

slider_axes = plt.axes([0.15, 0.01, 0.6, 0.05])
slider_handle = widgets.Slider(
    slider_axes,
    'Thrusters',
    0,
    8,
    valinit=0,
    valstep=0.01)

button_axes = plt.axes([0.85, 0.75, 0.1, 0.1])
button_handle = widgets.Button(button_axes, 'Close')
button_handle.on_clicked(close_callback)

text = plt.axes((0.1, 0.85, 0.7, 0.1))
text.axes.get_xaxis().set_visible(False)
text.axes.get_yaxis().set_visible(False)
text.axis("off")

current_position = 10000
current_velocity = 0

for i in DT:
    text.cla()
    ax.cla()
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 10020)

    engine_thrust = slider_handle.val
    acceleration = engine_thrust - GRAVITY

    new_v = get_new_velocity(acceleration, i)
    current_velocity = new_v
    new_x = get_new_position(new_v, i)
    current_position = new_x

    axes_handle, = ax.plot(0, new_x, 'bo')
    text.text(0.1, 0.8, "Try to land at V less than 25 m/s!", c="navy")

    if abs(new_v) > 25:
        colour = "red"
    else:
        colour = "green"

    text.text(0.1, 0.5, f"V = {abs(round(new_v, 2))} m/s", c=colour, size=15)

    if new_x <= 0 and abs(new_v) > 25:
        text.text(0.5, 0.5, f"You Crashed!", c="red", size=25)
        break
    elif new_x <= 0 and abs(new_v) < 25:
        text.text(0.5, 0.5, f"You Landed!", c="green", size=25)
        break

    plt.pause(0.1)

plt.show()
