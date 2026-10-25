"""A simple robot that moves on a flat floor."""

import math


class Robot:
    """A robot with a position, a heading and a speed."""

    def __init__(self, x, y, heading_deg, speed):
        """Set where the robot start.

        heading_deg is degrees. 0 face right, 90 face up.
        """
        self.x = x
        self.y = y
        self.heading_deg = heading_deg
        self.speed = speed

    def step(self, dt):
        """Move forward for dt seconds."""
        heading_rad = math.radians(self.heading_deg)
        self.x += self.speed * math.cos(heading_rad) * dt
        self.y += self.speed * math.sin(heading_rad) * dt

    def turn(self, degrees):
        """Turn the robot by degrees. Positive turn left."""
        self.heading_deg += degrees
