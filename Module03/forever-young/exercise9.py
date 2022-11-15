from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

x = 1

for i in range(0, 4):
    for i in range(0, x):
        x += 1
        robotArm.grab()
        for i in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,5):
            robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()