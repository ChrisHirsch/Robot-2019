# -*- coding: utf-8 -*-

from wpilib.command.subsystem import Subsystem
import wpilib.drive.differentialdrive as dd

from team3200.commands.joystickDrive import JoystickDrive 

import team3200
import team3200.motorHelper

class DriveTrainSub(Subsystem):
    '''
    This is the subsystem to control the robots wheels.
    '''
    
    def __init__(self):
        '''Initilizes the subsystem, gets the motors, 
        creates the drivetrain mixer
        '''
        super().__init__("DriveTrainSub")
        self.robot = team3200.getRobot();
        self.map = self.robot.map
        self.driveMotors = {}
        self.canDrive = True
        
        for key, motorDesc in self.map.motorsMap.driveMotors.items():
            self.driveMotors[key] = team3200.motorHelper.createMotor(motorDesc)
            print(key, motorDesc, self.driveMotors[key])

        self.driveTrain = dd.DifferentialDrive(self.driveMotors['leftMotor'], self.driveMotors['rightMotor'])
        
    def setTankDrive(self, leftSide, rightSide):
        if self.canDrive == True:
            self.driveTrain.tankDrive(leftSide, rightSide, False)
        
    def setArcadeDrive(self, speed, rot):
        self.driveTrain.arcadeDrive(speed, rot, False)

    def initDefaultCommand(self):
        if self.defaultCommand == None:
            self.setDefaultCommand(JoystickDrive())
        
    def autoTurn(self, speedL, speedR):
        self.canDrive = False
        self.driveTrain.tankDrive(speedL, speedR)
        self.canDrive = True
