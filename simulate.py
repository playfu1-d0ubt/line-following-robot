"""Run the robot one moment at a time."""

from controller import choose_turn


def tick(robot, line, left, right, dt):
    """Run one moment: sense, decide, move."""
    left_on = left.reads_line(robot, line)
    right_on = right.reads_line(robot, line)
    robot.turn(choose_turn(left_on, right_on))
    robot.step(dt)


def run(robot, line, left, right, dt, steps):
    """Run many ticks and return the path as a list of (x, y) points."""
    path = [(robot.x, robot.y)]
    for _ in range(steps):
        tick(robot, line, left, right, dt)
        path.append((robot.x, robot.y))
    return path
