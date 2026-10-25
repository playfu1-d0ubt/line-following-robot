"""Tests for the steering rule."""

from controller import choose_turn


def test_line_on_left_turns_left():
    """Only the left sensor sees the line, so turn left."""
    assert choose_turn(True, False) == 5


def test_line_on_right_turns_right():
    """Only the right sensor sees the line, so turn right."""
    assert choose_turn(False, True) == -5


def test_neither_sensor_goes_straight():
    """Neither sensor sees the line, so do not turn."""
    assert choose_turn(False, False) == 0


def test_both_sensors_go_straight():
    """Both sensors see the line, so do not turn."""
    assert choose_turn(True, True) == 0
