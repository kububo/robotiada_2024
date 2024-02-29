#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

sensor_motor = Motor(Port.C)

drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter=9, axle_track=12)

left_sensor = ColorSensor(Port.S1)
middle_left_sensor = ColorSensor(Port.S2)
middle_right_sensor = ColorSensor(Port.S3)
right_sensor = ColorSensor(Port.S4)

speed = 20
smaller_steer = 30
larger_steer = 60


def is_sensor_on_line(sensor):
    return sensor.reflection() < 40


while True:
    if is_sensor_on_line(left_sensor):
        drive_base.drive(speed, -larger_steer)

    elif is_sensor_on_line(right_sensor):
        drive_base.drive(speed, larger_steer)

    elif is_sensor_on_line(middle_left_sensor):
        drive_base.drive(speed, -smaller_steer)

    elif is_sensor_on_line(middle_right_sensor):
        drive_base.drive(speed, smaller_steer)

    else:
        drive_base.straight(speed)

    if abs(sensor_motor.angle()) > 10:
        sensor_motor.run_angle(255, 60, wait=False)
        drive_base.stop()
        break
