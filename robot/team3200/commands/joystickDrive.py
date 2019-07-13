# -*- coding: utf-8 -*-

from wpilib.command import Command
from wpilib.command import InstantCommand
import team3200
class JoystickDrive(Command):
    """
    This command will read the joystick values that are used
    to control the robot drive train and then set the drivetrain subsystem
    """
    
    def __init__(self, ntSensitivity = None):
        super().__init__("Joystick Drive")
        self.robot = team3200.getRobot()
        self.requires(self.robot.dtSub)
        self.tank = True
        self.sensitivity = -.8
        if ntSensitivity != None:    
            self.sensitivity = ntSensitivity.getNumber(-1)
            ntSensitivity.addListener(self.networkTableSensListener, 0b010100) #trying to properly deal with bitmasks or whatever. should use flags from https://robotpy.readthedocs.io/projects/pynetworktables/en/latest/api.html#networktables.NetworkTablesInstance.NotifyFlags

    def setSensitivity(newSens, self):
        self.sensitvity = newSens
        
    def networkTableSensListener(self, entry, key, value, param):
        self.setSensitivity(value)
        
    def getSensitivity(self):
        return self.sensitivity
    
    def execute(self):
        '''This sets up the axes on the controller to send into tankDrive'''
        dc = self.robot.driveController
        padAngle = dc.getPOV(0)
        if padAngle == -1:
            leftSide = dc.getRawAxis(self.robot.map.controllerMap.driverController['leftTread']) * self.sensitivity
            rightSide = dc.getRawAxis(self.robot.map.controllerMap.driverController['rightTread']) * self.sensitivity
            leftRot = dc.getRawAxis(self.robot.map.controllerMap.driverController['leftRot']) * self.sensitivity
            if self.tank:
                self.robot.dtSub.setTankDrive(leftSide,rightSide)
            elif not self.tank:
                self.robot.dtSub.setArcadeDrive(leftSide, leftRot)
        
        else:
            if padAngle == 0:
                self.robot.dtSub.autoTurn(-1 * self.sensitivity, -1 * self.sensitivity)
            elif padAngle == 90:
                self.robot.dtSub.autoTurn(-1 * self.sensitivity, 1 * self.sensitivity)
            elif padAngle == 180:
                self.robot.dtSub.autoTurn(1 * self.sensitivity, 1 * self.sensitivity)
            elif padAngle == 270:
                self.robot.dtSub.autoTurn(1 * self.sensitivity, -1 * self.sensitivity)
                
class GearUp(InstantCommand):
    def __init__(self, robot):
        super().__init__("GearUp")
        self.robot = robot
        
    def execute(self):
        if(self.robot.jDrive.getSensitivity() > -1):
            self.robot.jDrive.setSensitivity(self.robot.jDrive.getSensitivity() - .1)
            
class GearDown(InstantCommand):
    def __init__(self, robot):
        super().__init__("GearUp")
        self.robot = robot
        
    def execute(self):
        if(self.robot.jDrive.getSensitivity() < 0):
            self.robot.jDrive.setSensitivity(self.robot.jDrive.getSensitivity() + .1)
        