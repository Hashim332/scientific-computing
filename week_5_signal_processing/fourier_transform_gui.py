import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

'''This weeks task is to generate a GUI that will perform signal processing via numpy's inbuilt fft to plot power
spectra, inverse fft whose parameters should be controllable by a user'''


def signal_figure_properties():
    fig.set_facecolor('slategrey')
    signal_ax.set_facecolor('k')
    signal_ax.grid(True, color='darkgreen', linewidth=0.35)
    signal_ax.set_ylabel("Amplitude")
    signal_ax.set_xlabel("t (s)")
    signal_ax.set_title("Signal")


def powerspec_figure_properties():
    power_spectrum_ax.set_facecolor('k')
    power_spectrum_ax.grid(True, color='darkgreen', linewidth=0.35)
    power_spectrum_ax.set_ylabel("Amplitude")
    power_spectrum_ax.set_xlabel("Frequency (Hz)")
    power_spectrum_ax.set_title("Power spectrum")


def close_callback(event):
    plt.close('all')


def frequency_slider_callback(value):
    signal_plot.set_ydata(sine(value))

    fourier_transform = np.fft.fft(sine(value))

    power_spectrum = (np.conj(fourier_transform) *
                      fourier_transform)/sampling_points[-1]

    # q is the index to select values from the power spectra that are positive
    q = (len(sampling_points)-1)/2
    positive_frequencies = power_spectrum[0:int(q)]

    power_spectrum_plot.set_ydata(positive_frequencies)
    plt.draw()


def sp_slider_callback(value):
    global sampling_points
    sampling_points = range(value+1)
    sine(frequency)
    plt.draw()


def sine(frequency):
    function_values.clear()
    for i in sampling_points:
        function_values.append(
            np.sin(frequency * (2 * np.pi * i * time_step)))
    return function_values


# 100 sampling points
# sampling_points = range(101)
sampling_points = range(101)
time_step = 0.01
frequency = 10

# total time is a function of sampling points and time step and values of function are stored in empty list
total_time = np.arange(
    0, (sampling_points[-1] * time_step) + time_step, time_step)
function_values = []

sampling_rate = 1/time_step

# Fourier transform of signal
fourier_transform = np.fft.fft(sine(frequency))

power_spectrum = (np.conj(fourier_transform) *
                  fourier_transform)/sampling_points[-1]

# q is the index to select values from the power spectra that are positive
q = (len(sampling_points)-1)/2
positive_frequencies = power_spectrum[0:int(q)]


# figures and buttons
fig = plt.figure(figsize=(13.5, 7))

# signal plot
signal_ax = plt.axes([0.05, 0.6, 0.25, 0.3])

signal_plot, = signal_ax.plot(
    total_time, sine(frequency), '.-', color='firebrick')
signal_figure_properties()

# power spectrum plot
power_spectrum_ax = plt.axes([0.4, 0.6, 0.25, 0.3])

power_spectrum_plot, = power_spectrum_ax.plot(
    positive_frequencies, '.-', color='firebrick')
powerspec_figure_properties()

# close button
button_ax = plt.axes([0.45, 0.01, 0.05, 0.05])
button_handle = widgets.Button(
    button_ax, 'CLOSE', color='grey', hovercolor='dimgrey')
button_handle.on_clicked(close_callback)

# frequency slider
frequency_slider_ax = plt.axes([0.05, 0.1, 0.015, 0.35])
frequency_slider_handle = widgets.Slider(
    frequency_slider_ax, label="Frequency (Hz)", valmin=1, valmax=50, valinit=frequency, orientation='vertical')
frequency_slider_handle.on_changed(frequency_slider_callback)

# phase slider
# phase_slider_ax = plt.axes([0.15, 0.1, 0.015, 0.35])
# phase_slider_handle = widgets.Slider(
#     phase_slider_ax, label="Phase ($phi)", valmin=0, valmax=50, valinit=0, orientation='vertical')
# frequency_slider_handle.on_changed(frequency_slider_callback)

# sample points slider (using sp to shorten sample points)
sample_points_slider_ax = plt.axes([0.25, 0.1, 0.015, 0.35])
sp_slider_handle = widgets.Slider(
    sample_points_slider_ax, label="Sampling points",
    valmin=5,
    valmax=250,
    valinit=sampling_points[-1],
    valstep=1,
    orientation='vertical')
sp_slider_handle.on_changed(sp_slider_callback)

plt.show()
