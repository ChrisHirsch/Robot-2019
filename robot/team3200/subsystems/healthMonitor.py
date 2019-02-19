# -*- coding: utf-8 -*-
import team3200
import wpilib
from wpilib.command.subsystem import Subsystem
import team3200.commands.voltageMonitor
"""
This program checks the battery voltage, and warns the driver
if voltage gets too low.
"""
class HealthMonitor(Subsystem):
    def __init__(self):
        super().__init__("HMS")
        self.warnVoltage = 10
        self.critVoltage = 9
        self.robot = team3200.getRobot()
        self.count = 0
        self.pdp = wpilib.PowerDistributionPanel()
    def setVoltageLimit(self, voltage):
        self.minVoltage = voltage
    
    def rumbleOnLimits(self):
        if ( (self.warnVoltage > 0 or self.criVoltage > 0) and self.count < 1 ):
            self.volts = self.pdp.getVoltage()
            print (self.volts)
            if (self.volts > self.warnVoltage):
                
                self.setRumble(0.0)

            elif (self.volts > self.critVoltage and self.volts < self.warnVoltage):
                print("WARNING: Battery at a low level")
                self.setRumble(0.5)
 
            elif(self.volts < self.critVoltage):
                print("WARNING: Battery Voltage at Critical Level!!!")
                self.setRumble(1.0)
            else:
                pass
                
        self.count += 1
    def setRumble(self, value):
        self.robot.driveController.setRumble(wpilib.Joystick.RumbleType.kLeftRumble, value)
        self.robot.driveController.setRumble(wpilib.Joystick.RumbleType.kRightRumble, value)
        #self.robot.auxController.setRumble(wpilib.Joystick.RumbleType.kLeftRumble, value)
        #self.robot.auxController.setRumble(wpilib.Joystick.RumbleType.kRightRumble, value)
        
    def initDefaultCommand(self):
        self.setDefaultCommand(team3200.commands.voltageMonitor.VoltageMonitor())