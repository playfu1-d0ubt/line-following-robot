"""Line-following robot simulator. Runs one tick as a demo."""

from line import Line
from robot import Robot
from sensor import Sensor
from simulate import tick


def main():
    """Set up the world and run one tick."""
    line = Line()
    left = Sensor(0.3, 0.15)
    right = Sensor(0.3, -0.15)
    robot = Robot(0, 0.2, 0, 2)

    tick(robot, line, left, right, 0.1)
    print(robot.heading_deg, robot.x, robot.y)


if __name__ == "__main__":
    main()
