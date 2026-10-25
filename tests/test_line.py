"""Tests for the Line class."""

from line import Line


def test_point_on_line():
    """A point near the middle is on the line."""
    line = Line()
    assert line.contains(3, 0.05)


def test_point_far_above_is_off():
    """A point far above the middle is off the line."""
    line = Line()
    assert not line.contains(3, 0.5)


def test_point_far_below_is_off():
    """A point far below the middle is off the line."""
    line = Line()
    assert not line.contains(3, -0.5)
