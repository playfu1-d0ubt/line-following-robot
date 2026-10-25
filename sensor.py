"""A sensor that checks if the floor under it is the line."""

import math


class Sensor:
    """A sensor fixed ahead of the robot centre."""

    def __init__(self, ahead, side=0.0):
        """Set where the sensor sits on the robot.

        ahead is forward from the centre. side is left (positive) or right (negative).
        """
        self.ahead = ahead
        self.side = side

    def position(self, robot):
        heading = math.radians(robot.heading_deg)
        x = robot.x + self.ahead * math.cos(heading) - self.side * math.sin(heading)
        y = robot.y + self.ahead * math.sin(heading) + self.side * math.cos(heading)
        return x, y

    def reads_line(self, robot, line):
        """Say if the sensor is over the line."""
        x, y = self.position(robot)
        return line.contains(x, y)
