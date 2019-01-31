

import hal
class RobotMap():
    """
    Robot map gathers all the hard coded values needed to interface with 
    hardware into a single location
    """
    def __init__(self):
        """intilize the robot map"""
        self.motorsMap = CANMap()
        self.pneumaticsMap = PneumaticsMap()
        self.controllerMap = ControllerMap()

        
        
        

class CANMap():
    def __init__(self):
        '''
        holds mappings to all the motors in the robot
        '''
        rampRate = .2
        pid = None
        self.shooterMotors = {}
        self.intakeMotors = {}
        driveMotors = {}
        '''The code below is an example of code for the SparkMax motor controllers'''
        #driveMotors['leftMotor'] = {'channel':0, 'inverted':True, 'type':'SparkMax', 'pid':pid, 'motorType':MotorType.kBrushless}
        '''The code below is for controlling TalonSRX motor controllers as well as their followers'''
        driveMotors['leftMotor'] = {'channel':0, 'inverted':True, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['leftFollower'] = {'channel':3, 'inverted':True, 'type':'CANTalonFollower', 'masterChannel':0, "rampRate":rampRate}
        driveMotors['rightMotor'] = {'channel':1, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['rightFollower'] = {'channel':2, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':1, "rampRate":rampRate}
        
        self.driveMotors = driveMotors
        

class PneumaticsMap():
    def __init__(self):
        pass
    
class ControllerMap():
    def __init__(self):
        '''creates two controllers and assigns
        axis and buttons to joysticks'''
        driverController = {}
        auxController = {}
        
        driverController['controllerId'] = 0
        driverController['leftTread'] = 1
        
        
        if hal.isSimulation():
            driverController['rightTread'] = 3
        else:
            driverController['rightTread'] = 5
        
        driverController['ledToggle'] = 3
        driverController['exampleButton'] = 6
        
        driverController['voltRumble'] = 8.0
        
        self.driverController = driverController
        self.auxController = auxController
        
