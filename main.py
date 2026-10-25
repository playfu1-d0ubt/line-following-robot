"""Line-following robot simulator. Runs one tick as a demo."""

from line import Line
from robot import Robot
from sensor import Sensor
from simulate import run


def main():
    """Set up the world and run one tick."""
    line = Line()
    left = Sensor(0.3, 0.15)
    right = Sensor(0.3, -0.15)
    robot = Robot(0, 0.2, 0, 2)

    path = run(robot, line, left, right, 0.1, 100)
    print(len(path))
    print(path[-1])
    for point in path[::10]:
        print(point)


if __name__ == "__main__":
    main()
