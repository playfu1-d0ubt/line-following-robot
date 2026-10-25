"""Test that the whole robot follows the line."""

from line import Line
from robot import Robot
from sensor import Sensor
from simulate import run


def test_robot_ends_on_the_line():
    """A robot starting above the line should settle on it."""
    line = Line()
    left = Sensor(0.3, 0.15)
    right = Sensor(0.3, -0.15)
    robot = Robot(0, 0.2, 0, 2)

    path = run(robot, line, left, right, 0.1, 100)

    final_y = path[-1][1]
    assert abs(final_y) <= 0.1
