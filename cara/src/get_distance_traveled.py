from src._input import wheel_radius
from math import pi

wheel_circumference = 2 * pi * wheel_radius

def get_distance_traveled(left_motor_angle, right_motor_angle):
  left_motor_distance = left_motor_angle / 360 * wheel_circumference
  right_motor_distance = right_motor_angle / 360 * wheel_circumference

  return (left_motor_distance + right_motor_distance) / 2 