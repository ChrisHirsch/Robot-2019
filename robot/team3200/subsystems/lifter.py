# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:00:27 2019

@author: Micro
"""
from enum import IntEnum

class Level(IntEnum):
	kFloor = 0
	kLowPanel = 1
	kLowBall = 2
	kBallCargo = 3
	kMidPanel = 4
	kMidBall = 5
	kHighPanel = 6
	kHighBall = 7

from wpilib.command.subsystem import Subsystem
import team3200
import wpilib

class LifterSub(Subsystem):
	def __init__(self):
		super().__init__("LifterSub")
		self.robot = team3200.getRobot()
		self.map = self.robot.map
		self.level = 0
		self.intakeSpd = 1
		self.lifterMotors = {}
		for key, motorDesc in self.map.motorsMap.lifterMotors.items():
			self.lifterMotors[key] = team3200.motorHelper.createMotor(motorDesc)
			print(key, motorDesc, self.lifterMotors[key])
			
	
	def StopLifter(self):
		print(self.level)
	
	def RaiseLevel(self):
		if self.level < Level.kHighBall:
			self.lifterMotors['liftMotor'].set(.5)
			wpilib.Timer.delay(1)
			self.lifterMotors['liftMotor'].set(0)
			self.level = self.level + 1

	def LowerLevel(self):
		if self.level > Level.kFloor:
			self.lifterMotors['liftMotor'].set(-.5)
			wpilib.Timer.delay(1)
			self.lifterMotors['liftMotor'].set(0)
			self.level = self.level - 1
			
			
	def ToggleRoller(self):
		self.intakeSpd = -self.intakeSpd
		
	def RunRoller(self, speed):
		if(self.lifterMotors['roller'].get() == 0):
			self.lifterMotors['roller'].set(speed * self.intakeSpd)
		else:
			self.lifterMotors['roller'].set(0)
			
from wpilib import DoubleSolenoid
class PlatePiston(Subsystem):
	def __init__(self):
		super().__init__("Plate Piston")
		self.robot = team3200.getRobot()
		self.map = self.robot.map.pneumaticsMap
		self.platePiston = DoubleSolenoid(self.map.pcmCan, self.map.forwardChannel, self.map.reverseChannel)
		
	def Activate(self):
		self.platePiston.set(DoubleSolenoid.Value.kForward)
		print("Piston Forwards")
		wpilib.Timer.delay(1)
		self.platePiston.set(DoubleSolenoid.Value.kReverse)
		print("Piston Backwards")
		wpilib.Timer.delay(1)