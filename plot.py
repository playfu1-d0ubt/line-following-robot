"""Draw the robot's path."""

import matplotlib.pyplot as plt


def plot_path(path, line, filename):
    """Draw the path and the line, and save the picture."""
    xs = [point[0] for point in path]
    ys = [point[0] for point in path]

    fig, ax = plt.subplots()
    ax.axhspan(
        line.y - line.width / 2,
        line.y + line.width / 2,
        color="gray",
        alpha=0.5,
        label="line",
    )
    ax.plot(xs, ys, color="orange", label="robot path")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    fig.savefig(filename, dpi=150)
