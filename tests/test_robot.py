"""Tests for the Robot class."""

import pytest

from robot import Robot


def test_step_moves_along_heading():
    """A robot facing right should move in x only."""
    robot = Robot(0, 0, 0, 2)
    robot.step(0.5)
    assert robot.x == pytest.approx(1.0)
    assert robot.y == pytest.approx(0.0)


def test_turn_changes_heading():
    robot = Robot(0, 0, 0, 2)
    robot.turn(30)
    assert robot.heading_deg == 30
