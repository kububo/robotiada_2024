import rpyc
import time

robot = rpyc.classic.connect("192.168.137.178")

ev3dev2_motor = robot.modules['ev3dev2.motor']
ev3dev2_sensor = robot.modules['ev3dev2.sensor']
ev3dev2_sensor_lego = robot.modules['ev3dev2.sensor.lego']

y_axis_left = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_D)
y_axis_right = ev3dev2_motor.LargeMotor(ev3dev2_motor.OUTPUT_C)
x_axis = ev3dev2_motor.MediumMotor(ev3dev2_motor.OUTPUT_B)
z_axis = ev3dev2_motor.MediumMotor(ev3dev2_motor.OUTPUT_A)

y_axis_button_left = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_2)
y_axis_button_right = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_3)
x_axis_button = ev3dev2_sensor_lego.TouchSensor(ev3dev2_sensor.INPUT_1)

# Speed options
y_max_speed = 40
x_max_speed = 40
z_max_speed = 60

# Resetting values
y_axis_left.position = 0
y_axis_right.position = 0
x_axis.position = 0
z_axis.position = 0

# Y axis calibration
y_start_time = time.time()

y_axis_left.on(y_max_speed)
y_axis_right.on(y_max_speed)

while True:
  if y_axis_button_left.is_pressed(): y_axis_left.off()
  if y_axis_button_right.is_pressed(): y_axis_right.off()

  if y_axis_button_left.is_pressed() and y_axis_button_right.is_pressed():
    y_axis_left.off()
    y_axis_right.off()
    break

y_axis_move_time = time.time() - y_start_time
y_axis_max_value = y_axis_right.position

# X axis calibration
x_start_time = time.time()

x_axis.on(x_max_speed)

while True:
  if x_axis_button.is_pressed:
    x_axis.off()
    break

x_axis_move_time = time.time() - x_start_time
x_axis_max_value = x_axis.position

# Z axis calibration
z_axis_max_value = 30
z_axis.on_to_abs_pos(z_max_speed, z_axis_max_value)

# Functions

def move_z(direction):
  if direction == "UP":
    z_axis.on_to_abs_pos(z_max_speed, z_axis_max_value)
  elif direction == "DOWN":
    z_axis.on_to_abs_pos(z_max_speed, 0)

def move_x_y(x, y):
  x_distance = abs(x_axis.position - x)
  y_distance = abs(y_axis_left.position - y)

  x_time = x_axis_move_time * x_distance
  y_time = y_axis_move_time * y_distance

  if x_time > y_time:
    speed_coefficient = y_time / x_time

    y_axis_left.on_to_abs_pos(y_max_speed, y, block=False)
    y_axis_right.on_to_abs_pos(y_max_speed, y, block=False)

    x_axis.on_to_abs_pos(x_max_speed * speed_coefficient, x, block=False)
  else:
    speed_coefficient = x_time / y_time

    x_axis.on_to_abs_pos(x_max_speed, x, block=False)

    y_axis_left.on_to_abs_pos(y_max_speed * speed_coefficient, y, block=False)
    y_axis_right.on_to_abs_pos(y_max_speed * speed_coefficient, y, block=False)

  x_axis.wait_while("running") # TODO: Maybe add this for only one motor?
  y_axis_left.wait_while("running")
  y_axis_right.wait_while("running")