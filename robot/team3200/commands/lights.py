# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:52:42 2019

@author: Raptor3200
"""

from wpilib.command import InstantCommand

from networktables import NetworkTables

from enum import IntEnum

class LedMode(IntEnum):
    kAUTO = 0
    kOFF = 1
    kBLINK = 2
    kON = 3

class ExampleButton(InstantCommand):
    def __init__(self, dtSub):
        super().__init__("ExampleButton")
        self.dtSub = dtSub
        
    def execute(self):
        '''This button is an example and prints when you press the button'''
        print("Button Pressed")

class Lights(InstantCommand):
    
    def __init__(self):
        super().__init__("Lights")
        self.table = NetworkTables.getTable("limelight")
        
    def execute(self):
        print("Lights Toggled")
        '''This toggles the lights when pressed.'''
        lightNum = self.table.getNumber('ledMode', None)
        if lightNum == LedMode.kOFF:
            self.table.putNumber('ledMode', LedMode.kON)
        else:
            self.table.putNumber('ledMode', LedMode.kOFF)
            

#class SignalLeft(InstantCommand):
#    def __init__(self):
#        self.table = NetworkTables.getTable('limelight')
#        
#    def execute(self):
#        if(self.table.getNumber('ledMode', None) != 4):
#            self.table.putNumber('ledMode', 4)
#        else:
#            self.table.putNumber('ledMode', LedMode.kOFF)

            
