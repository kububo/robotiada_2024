#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter=9, axle_track=12)

left_sensor = ColorSensor(Port.S1)
middle_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S4)

# Settings
base_speed = 15
large_speed = 30
min_speed = 5
speed_descend_coefficient = 0.99

base_steer = 5
large_steer = 40
steer_growth_rate = 1
max_steer = 100

wait_time = 5


def is_sensor_on_line(sensor):
    return sensor.reflection() < 40


while True:
    if is_sensor_on_line(left_sensor):
        current_speed = base_speed
        current_steer = base_steer

        while not is_sensor_on_line(middle_sensor) and not is_sensor_on_line(right_sensor):
            current_speed *= speed_descend_coefficient if current_speed > min_speed else 1

            if current_steer < 15:
                current_steer += steer_growth_rate if current_steer < max_steer else 0
            else:
                current_steer += steer_growth_rate * 5 if current_steer < max_steer else 0

            drive_base.drive(current_speed, -current_steer)
            wait(wait_time)

            print("LEFT", current_speed, current_steer)

    elif is_sensor_on_line(right_sensor):
        current_speed = base_speed
        current_steer = base_steer

        while not is_sensor_on_line(middle_sensor) and not is_sensor_on_line(left_sensor):
            current_speed *= speed_descend_coefficient if current_speed > min_speed else 1

            if current_steer < 15:
                current_steer += steer_growth_rate if current_steer < max_steer else 0
            else:
                current_steer += steer_growth_rate * 5 if current_steer < max_steer else 0

            drive_base.drive(current_speed, current_steer)
            wait(wait_time)

            print("RIGHT", current_speed, current_steer)

    else:
        drive_base.drive(large_speed, 0)
