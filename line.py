"""A straight line on the floor for the robot to follow."""


class Line:
    """A strip of tape along the x axis."""

    def __init__(self, y=0.0, width=0.2):
        """Set the middle of the line and how wide it is."""
        self.y = y
        self.width = width

    def contains(self, x, y):
        """Say if the point is on the line."""
        distance = abs(y - self.y)
        return distance <= self.width / 2
