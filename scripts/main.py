import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Frequnecy channels (MHz)
frequencies = [2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480]

# Number of hops (and time steps)
num_hops = 50

# Generate a pseudo-random hopping sequence
hopping_sequence = random.choices(frequencies, k=num_hops)

# Simulate drone movement in 3D space (X, Y, Z)
x_positions = np.linspace(0, 10, num_hops)  
y_positions = np.sin(np.linspace(0, 10, num_hops)) * 5  
z_positions = hopping_sequence  

# Defining a jamming frequency from frequencies arr
jamming_frequency = random.choice(frequencies)

# Jamming signal: let's say the jammer is stationary at one point in space, at a fixed frequency
jammer_x = 5  # Stationary at X=5
jammer_y = 0  # Stationary at Y=0
jammer_z = [jamming_frequency] * num_hops  # Constant frequency for the jammer

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot limits
ax.set_xlim([0, 10])
ax.set_ylim([-5, 5])
ax.set_zlim([min(frequencies), max(frequencies)])

# Labels and titles
ax.set_xlabel("X Position (Drone Movement)")
ax.set_ylabel("Y Position (Drone Movement)")
ax.set_zlabel("Frequency (MHz)")
ax.set_title(f"Simulated 3D Frequency Hopping for Drone Communication\nwith Jamming Signal at {jamming_frequency} MHz")

# Plotting jamming signal (represented as a red sphere at constant position)
ax.scatter(jammer_x, jammer_y, jamming_frequency, color='r', s=100, label="Jamming Signal", marker='o')

# Plotting the drone's initial position
drone_marker, = ax.plot([], [], [], 'bo', label="Drone (Frequency Hopping)")

# Creating an empty line object for the path of the drone
drone_path, = ax.plot([], [], [], color='b', linestyle='-', marker='o')

# Update function for the animation
def update(frame):
    # Updating drone's position as sequences (even for one frame, pass it as list)
    drone_marker.set_data([x_positions[frame]], [y_positions[frame]])
    drone_marker.set_3d_properties([z_positions[frame]])

    # Updating drone's path
    drone_path.set_data(x_positions[:frame+1], y_positions[:frame+1])
    drone_path.set_3d_properties(z_positions[:frame+1])

    return drone_marker, drone_path


# Creating animation
ani = FuncAnimation(fig, update, frames=num_hops, interval=100, blit=True)

plt.legend()
plt.show()
