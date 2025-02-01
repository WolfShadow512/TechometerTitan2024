from hub import light_matrix, motion_sensor, port
import runloop
import motor_pair
#from app import display
import motor
import color_matrix

# declare constants
ROTATION_TO_CM = 28 #17.2787595947
ROTATION_TO_INCH = 11 #7
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
# convert distance from inch to rotation degrees on motor
#####################################################################
def convertInchToDegree(inch):
    return int ( ( 360 / ROTATION_TO_INCH ) * inch)
#####################################################################
# convert actual degree to motor specification
#####################################################################
def turnDegree(angle):
    return int(( TURNFACTOR ) * angle )



#####################################################################
# Main code
#####################################################################
async def main():
    # Set Motor pair1
    motor_pair.pair(motor_pair.PAIR_1, WHEELRIGHTPORT, WHEELLEFTPORT)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(30), 300, 300)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-50,50)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-15), 50, -50)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-50,50)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(15), 100, 100)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-20,50)
    await motor_pair.move_tank_for_degrees(0, turnDegree(15), 200, -200)
    await motor.run_for_degrees(FRONTATTACMENTPORT,100,100)
"""
    await motor.run_for_degrees(FRONTATTACMENTPORT,-20,100)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-15), 200, -200)
    motor_pair.move_tank_for_degrees(0,convertcmToDegree(12), 300, 300)
    motor.run_for_degrees(FRONTATTACMENTPORT,-20,100)"""

    
'''
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(40), 300, 300)
    await motor_pair.move_tank_for_degrees(0, turnDegree(-90), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(35), 300, 300)
    await motor.run_for_degrees(FRONTATTACMENTPORT,20,500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(80), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(8), 100, 100)
    await motor.run_for_degrees(FRONTATTACMENTPORT,-500,500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(85), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(-55), 500, 500)
    await motor_pair.move_tank_for_degrees(0, turnDegree(110), 200, -200)
    await motor_pair.move_tank_for_degrees(0,convertcmToDegree(75), 500, 500)
    '''
runloop.run(main())
