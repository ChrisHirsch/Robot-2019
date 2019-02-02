# -*- coding: utf-8 -*-

from wpilib.command import Command
class JoystickDrive(Command):
    """
    This command will read the joystick values that are used
    to control the robot drive train and then set the drivetrain subsystem
    """
    
    def __init__(self, robot):
        super().__init__("Joystick Drive")
        self.robot = robot
        self.requires(self.robot.dtSub)
        self.sensitivity = -1
        
    def setSensitivity(self, newSensitivity):
        self.sensitivity = newSensitivity
        
    def getSensitivity(self):
        return self.sensitivity
    
    def execute(self):
        '''This sets up the axes on the controller to send into tankDrive'''
        dc = self.robot.driveController
        leftSide = dc.getRawAxis(self.robot.map.controllerMap.driverController['leftTread']) * self.sensitivity
        rightSide = dc.getRawAxis(self.robot.map.controllerMap.driverController['rightTread']) * self.sensitivity
        
        self.robot.dtSub.setTankDrive(leftSide,rightSide)
