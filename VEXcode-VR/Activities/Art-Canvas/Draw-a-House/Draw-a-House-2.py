def when_started():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    drivetrain.drive_for(FORWARD, 300, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    pen.move(DOWN)
    for repeat_count in range(4):
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 600, MM)
        wait(5, MSEC)
    drivetrain.turn_for(LEFT, 150, DEGREES)
    drivetrain.drive_for(FORWARD, 346.4, MM)
    drivetrain.turn_for(LEFT, 60, DEGREES)
    drivetrain.drive_for(FORWARD, 346.4, MM)
    pen.set_pen_color(BLUE)
    drivetrain.turn_for(LEFT, 60, DEGREES)
    drivetrain.drive_for(FORWARD, 200, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.drive_for(REVERSE, 50, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    for repeat_count2 in range(2):
        drivetrain.drive_for(FORWARD, 350, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 300, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        wait(5, MSEC)

vr_thread(when_started())
