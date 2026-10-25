from line import Line
from robot import Robot

robot = Robot(0, 0, 0, 2)
robot.step(0.5)
print(robot.x, robot.y)
robot.turn(30)
robot.step(0.5)
print(robot.x, robot.y)

line = Line()
print(line.contains(3, 0.05))
print(line.contains(3, -0.08))
print(line.contains(3, 0.5))
