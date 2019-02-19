# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:06:57 2019

@author: Matthew McFarland
"""

from wpilib.command import Command
from wpilib.command import InstantCommand
from networktables import NetworkTables
class LeftTurn(Command):
    def __init__(self, dtSub):
        super().__init__("Left Turn")
        self.dtSub = dtSub
        
    def execute(self):
        self.dtSub.autoTurn(-.5, .5)
        
class RightTurn(Command):
    def __init__(self, dtSub):
        super().__init__("Right Turn")
        self.dtSub = dtSub
        
    def execute(self):
        self.dtSub.autoTurn(.5, -.5)
        
            
class AlignButton(InstantCommand):
    def __init__(self, dtSub):
        super().__init__("Align Button")
        self.table = NetworkTables.getTable("limelight")
        self.dtSub = dtSub
        
    def execute(self):
        '''This aligns the robot up to a target it sees when a button is pressed'''
        print("Alignment Started")
        if(self.table.getEntry('tv').value == 1):
            self.tx = self.table.getNumber('tx', None)
            while(self.tx < -2 or self.tx > 2):
                self.tx = self.table.getNumber('tx', None)
                if(self.tx < 0):
                    '''Active when the target is to the left.'''
                    #print(self.tx)
                    self.dtSub.autoTurn(-.5, .5)
                elif(self.tx > 0):
                    '''Active when the target is to the right.'''
                    #print(self.tx)
                    self.dtSub.autoTurn(.5, -.5)
