import rpyc


def get_robot(ip):
    robot = rpyc.classic.connect(ip)
    motor_module = robot.modules["ev3dev2.motor"]

    left_motor = motor_module.Motor(motor_module.OUTPUT_B)
    right_motor = motor_module.Motor(motor_module.OUTPUT_A)

    return (left_motor, right_motor)
