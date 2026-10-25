"""Run the robot one moment at a time."""

from controller import choose_turn


def tick(robot, line, right, left, dt):
    """Run one moment: sense, decide, move."""
    left_on = left.reads_line(robot, line)
    right_on = right.reads_line(robot, line)
    robot.turn(choose_turn(left_on, right_on))
    robot.step(dt)
