from robot import Robot
from plot import plot_swarm

import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.animation import FuncAnimation

experiment_length = 100
width = 500
height = 500

swarm_size = 10

# instantiate robot class
swarm = [Robot(x=250, y=250, max_speed=20, width=width, height=height, id=x) for x in range(swarm_size)]


def robot_behaviour(i):

    rob_x = []
    rob_y = []

    # robot behaviour
    for robot in swarm:

        if (i + robot.id) % 10 == 0:
            robot.random_walk()

        robot.wall_bounce()
        robot.update()

        # record new robot positions
        rob_x.append(robot.position[0])
        rob_y.append(robot.position[1])

    # draw robots
    swarm_df = {'x': rob_x,
                'y': rob_y}

    rob_plot, = plot_swarm(width, height, swarm_df, ax)

    return rob_plot


fig, ax = plt.subplots(figsize=(10, 10))

frame_list = []

simulation = FuncAnimation(fig=fig,
                           func=robot_behaviour,
                           frames=np.arange(0, experiment_length, 1),
                           fargs=(),
                           interval=0.025,
                           save_count=experiment_length)

#simulation.save("animation.gif")

plt.show()
