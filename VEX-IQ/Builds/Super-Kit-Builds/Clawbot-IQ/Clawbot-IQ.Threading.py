from drivetrain import Drivetrain
from vexiq import \
    Bumper, \
    ColorSensor, \
    DistanceSensor, \
    Gyro, \
    Joystick, \
    Motor, \
    TouchLed, \
    UNIT_CM

from sys import run_in_thread


# drive base configs
LEFT_MOTOR = \
    Motor(
        1,   # port
        False   # switch_polarity
    )
RIGHT_MOTOR = \
    Motor(
        6,   # port
        True   # switch_polarity
    )
DRIVETRAIN = \
    Drivetrain(
        LEFT_MOTOR,   # left_motor
        RIGHT_MOTOR,   # right_motor
        200,   # wheel_travel_mm
        176   # track_mm
    )

# sensor configs
TOUCH_LED = TouchLed(2)
COLOR_SENSOR = \
    ColorSensor(
        3,   # index
        False,   # is_grayscale
        700   # proximity
    )
GYRO_SENSOR = \
    Gyro(
        4,   # index
        True   # calibrate
    )
DISTANCE_SENSOR = \
    DistanceSensor(
        7,   # port
        UNIT_CM   # unit
    )
BUMPER_SWITCH = Bumper(8)

# actuator configs
ARM_MOTOR = \
    Motor(
        10,   # index
        False   # reverse
    )
ARM_MOTOR_VELOCITY = 30   # %

CLAW_MOTOR = \
    Motor(
        11,   # index
        False   # reverse
    )
CLAW_MOTOR_VELOCITY = 60   # %

# controller configs
CONTROLLER = Joystick()
CONTROLLER.set_deadband(3)


def drive_once_by_controller():
    LEFT_MOTOR.run(
        CONTROLLER.axisA(),   # power
        None,   # distance
        False   # hold
    )
    RIGHT_MOTOR.run(
        CONTROLLER.axisD(),   # power
        None,   # distance
        False   # hold
    )


def keep_driving_by_controller():
    while True:
        drive_once_by_controller()


def lower_or_raise_arm_once_by_controller():
    if CONTROLLER.bLdown():
        ARM_MOTOR.run(
            -ARM_MOTOR_VELOCITY,   # power
            None,   # distance
            False   # hold
        )

    elif CONTROLLER.bLup():
        ARM_MOTOR.run(
            ARM_MOTOR_VELOCITY,   # power
            None,   # distance
            False   # hold
        )

    else:
        ARM_MOTOR.hold()


def keep_lowering_or_raising_arm_by_controller():
    while True:
        lower_or_raise_arm_once_by_controller()


def grab_or_release_object_by_controller():
    if CONTROLLER.bRdown():
        CLAW_MOTOR.run(
            -CLAW_MOTOR_VELOCITY,   # power
            None,   # distance
            False   # hold
        )

    elif CONTROLLER.bRup():
        CLAW_MOTOR.run(
            CLAW_MOTOR_VELOCITY,   # power
            None,   # distance
            False   # hold
        )

    else:
        CLAW_MOTOR.hold()


def keep_grabbing_or_releasing_objects_by_controller(self):
    while True:
        grab_or_release_object_by_controller()


run_in_thread(keep_lowering_or_raising_arm_by_controller)
run_in_thread(keep_grabbing_or_releasing_objects_by_controller)
keep_driving_by_controller()
