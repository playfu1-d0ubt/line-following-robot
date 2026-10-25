from controller import choose_turn
from line import Line
from robot import Robot
from sensor import Sensor

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

sensor = Sensor(0.3)
print(sensor.position(Robot(1, 2, 0, 2)))
print(sensor.position(Robot(1, 2, 90, 2)))

print(sensor.reads_line(Robot(1, 0, 0, 2), line))
print(sensor.reads_line(Robot(1, 0.5, 0, 2), line))
print(sensor.reads_line(Robot(1, -0.3, 90, 2), line))

left = Sensor(0.3, 0.15)
right = Sensor(0.3, -0.15)
for y in (0, 0.1, -0.1):
    robot = Robot(1, y, 0, 2)
    print(y, left.reads_line(robot, line), right.reads_line(robot, line))

print(choose_turn(False, False))
print(choose_turn(True, False))
print(choose_turn(False, True))
print(choose_turn(True, True))
