#!/usr/bin/env pybricks-micropython
from src.program import Program
from src.get_distance_traveled import get_distance_traveled
from src._input import wheel_spacing
from math import pi

from pybricks.tools import DataLog
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction

max_speed = 200

logger = DataLog()
program = Program()

left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)

left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)

while True:
    distance_traveled = get_distance_traveled(
        left_motor.angle(), right_motor.angle())
    instruction = program.get_current_instruction()

    if instruction["type"] == "LINE":
        print(left_sensor.reflection(), right_sensor.reflection())

        if left_sensor.reflection() < 50:
            left_motor.run(max_speed * 0.9)
            right_motor.run(max_speed)

        elif right_sensor.reflection() < 50:
            left_motor.run(max_speed)
            right_motor.run(max_speed * 0.9)

        else:
            left_motor.run(max_speed)
            right_motor.run(max_speed)
    elif instruction["type"] == "ARC":
        inner_wheel = 2 * pi * (instruction["radius"] - (wheel_spacing / 2))
        outer_wheel = 2 * pi * (instruction["radius"] + (wheel_spacing / 2))

        inner_speed_coefficient = inner_wheel / outer_wheel

        if left_sensor.reflection() < 40:
            if (instruction["direction"] == "LEFT"):
                left_motor.run(max_speed * inner_speed_coefficient * 0.95)
                right_motor.run(max_speed)

                while left_sensor.reflection() >= 30 or right_sensor.reflection() < 50:
                    pass

                left_motor.run(max_speed)
                right_motor.run(max_speed * 0.9)
            else:
                left_motor.run(max_speed * 0.9)
                right_motor.run(max_speed)

        elif right_sensor.reflection() < 40:
            if (instruction["direction"] == "RIGHT"):
                left_motor.run(max_speed)
                right_motor.run(max_speed * inner_speed_coefficient * 0.95)

                while right_sensor.reflection() >= 30 or left_sensor.reflection() < 50:
                    pass

                left_motor.run(max_speed * 0.9)
                right_motor.run(max_speed)
            else:
                left_motor.run(max_speed)
                right_motor.run(max_speed * 0.9)

        else:
            left_motor.run(max_speed)
            right_motor.run(max_speed)
    else:
        left_motor.stop()
        right_motor.stop()

    if (distance_traveled >= program.previous_distance + instruction["length"]):
        program.move_to_next_instruction()
        print("--- Moving To Next Instruction ---")
