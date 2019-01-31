# -*- coding: utf-8 -*-
import team3200
import wpilib
from wpilib import command

class VoltageMonitor(command.Command):
    def __init__(self):
        super().__init__("VoltageMonitorCmd")
        self.robot = team3200.getRobot()
        self.requires(self.robot.healthMonitor)
    
    def execute(self):
        self.robot.healthMonitor.rumbleOnLimits()