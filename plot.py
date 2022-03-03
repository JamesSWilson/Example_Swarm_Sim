import matplotlib.pyplot as plt


def plot_swarm(width, height, swarm_df, ax):

    # Visualisation section
    ax.clear()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    rob_plot, = ax.plot(swarm_df['x'], swarm_df['y'], 'k.', markersize=30)



    return rob_plot,