from hub import light_matrix, motion_sensor, port
import runloop
import motor_pair
from app import display
import motor
import time

# declare constants
ROTATION_TO_CM = 28 #17.2787595947
#right attachment is port D and Left attachment is port E
WHEELRIGHTPORT= port.F
WHEELLEFTPORT = port.B
FRONTATTACMENTPORT = port.A
REARATTACHMENTPORT = port.E
TURNFACTOR = 1.66

#####################################################################
# Method to convert distance from inch to rotation degrees on motor
#####################################################################
def convertcmToDegree(cm):
    return int(360/( ROTATION_TO_CM ) * cm )


#####################################################################
# convert actual degree to motor specification
#####################################################################
def turnDegree(angle):
    return int(( TURNFACTOR ) * angle )
    # gyro function to turn left
#####################################################################
async def leftGyro(turnDegree,motorPair):
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] < turnDegree:
        motor_pair.move(motorPair,-100)
    motor_pair.stop(motorPair)

#####################################################################
# gyro function to turn right
#####################################################################
async def rightGyro(turnDegree,motorPair):
    motion_sensor.reset_yaw(0)

    while motion_sensor.tilt_angles()[0] > turnDegree:
        motor_pair.move(motorPair,100)
    motor_pair.stop(motorPair)


#####################################################################


async def main():
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)

        # write your code here
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-3),800 , 800)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(88),800 , 800)
    await motor.run_for_degrees(REARATTACHMENTPORT, 1000 , 1000)
    await motor.run_for_degrees(REARATTACHMENTPORT, -100 , 1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-9),800 , 800)
    await motor.run_for_degrees(REARATTACHMENTPORT, -1000 , 1000)
    await motor.run_for_degrees(REARATTACHMENTPORT, 100 , 1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-6),800 , 800)
    await motor.run_for_degrees(REARATTACHMENTPORT, 200 , 400)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-25),1000 , 1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-25),1000 , 1000)
    await leftGyro(1100, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(47),1000 , 1000)
    await leftGyro(1100, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(47),1000 , 1000)
    # await rightGyro(-200, motor_pair.PAIR_1)
    # await motor.run_for_degrees(REARATTACHMENTPORT, -200 , 400)

    # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-5),800 , 800)
    # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(29),800 , 800)
    # await rightGyro(-340, motor_pair.PAIR_1)
    # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(40),800 , 800)
    # await leftGyro(400, motor_pair.PAIR_1)
    # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(24),800 , 800)
    # await motor.run_for_degrees(REARATTACHMENTPORT, 1000 , 1000)
    # await motor.run_for_degrees(REARATTACHMENTPORT, -100 , 1000)
    # await leftGyro(160, motor_pair.PAIR_1)
    # await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-5),800 , 800)
    # await motor.run_for_degrees(REARATTACHMENTPORT, -1000 , 1000)
    # await motor.run_for_degrees(REARATTACHMENTPORT, 100 , 1000)

"""
    await leftGyro(900, motor_pair.PAIR_1)

    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(53),800 , 800)
    await rightGyro(-920, motor_pair.PAIR_1)
    await motor.run_for_degrees(FRONTATTACMENTPORT, 1000 , 1000)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(13),400 , 400)
    await motor.run_for_degrees(FRONTATTACMENTPORT, -500 , 500)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-23),400 , 400)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(10),400 , 400)
    await leftGyro(850, motor_pair.PAIR_1)
    await motor_pair.move_tank_for_degrees(0, convertcmToDegree(-65),800 , 800)
    await motor.run_for_degrees(FRONTATTACMENTPORT, 1000 , 500)"""
runloop.run(main())
