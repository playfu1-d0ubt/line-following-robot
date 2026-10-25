"""A simple rule that decides how the robot should turn."""

TURN_DEG = 5


def choose_turn(left_on, right_on):
    """Return degrees to turn, given what each sensor sees."""
    if left_on and not right_on:
        return TURN_DEG
    elif right_on and not left_on:
        return -TURN_DEG
    else:
        return 0
