# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:06:57 2019

@author: Micro
"""
from wpilib.command import InstantCommand
from networktables import NetworkTables
class AlignButton(InstantCommand):
    def __init__(self):
        super().__init__("Align Button")
        self.table = NetworkTables.getTable("limelight")
        
    def execute(self):
        '''This button is an example and prints when you press the button'''
        print("Button Pressed")
        self.tx = self.table.getNumber('tx', None)
        self.ta = self.table.getNumber('tv', None)
        if(self.ta in locals()):
            if(self.tx < 0):
                print(self.tx)
            elif(self.tx > 0):
                print(self.tx)
            elif(self.tx == 0):
                print(self.tx)
        