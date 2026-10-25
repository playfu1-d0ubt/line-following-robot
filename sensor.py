"""A sensor that checks if the floor under it is the line."""

import math


class Sensor:
    """A sensor fixed ahead of the robot centre."""

    def __init__(self, ahead):
        """Set how far ahead of the robot centre the sensor sits."""
        self.ahead = ahead

    def position(self, robot):
        heading_rad = math.radians(robot.heading_deg)
        sensor_x = robot.x + self.ahead * math.cos(heading_rad)
        sensor_y = robot.y + self.ahead * math.sin(heading_rad)
        return sensor_x, sensor_y
