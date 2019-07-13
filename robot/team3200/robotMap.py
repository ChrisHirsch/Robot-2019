
import wpilib.xboxcontroller
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
        self.networkTableMap = NetworkTableMap()

        
        
        

class CANMap():
    def __init__(self):
        '''
        holds mappings to all the motors in the robot
        '''
        rampRate = .2
        #rotRampRate = .2
        pid = None
        lifterMotors = {}
        driveMotors = {}
        '''The code below is an example of code for the SparkMax motor controllers'''
        #shooterMotors['RotMotor'] = {'channel':4, 'inverted':False, 'type':'SparkMax', 'pid':rotPid, 'motorType':MotorType.kBrushless}
        '''The code below is for controlling TalonSRX motor controllers as well as their followers'''
        driveMotors['leftMotor'] = {'channel':0, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['leftFollower'] = {'channel':3, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':0, "rampRate":rampRate}
        driveMotors['rightMotor'] = {'channel':1, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        driveMotors['rightFollower'] = {'channel':2, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':1, "rampRate":rampRate}
        
        lifterMotors['liftMotor'] = {'channel':4, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        lifterMotors['liftMotor2'] = {'channel':5, 'inverted':False, 'type':'CANTalonFollower', 'masterChannel':4, "rampRate":rampRate}
        lifterMotors['roller'] = {'channel':6, 'inverted':False, 'type':'CANTalon', 'pid':pid, "rampRate":rampRate}
        
        self.driveMotors = driveMotors
        self.lifterMotors = lifterMotors

class PneumaticsMap():
    def __init__(self):
        self.pcmCan = 0
        self.forwardChannel = 0
        self.reverseChannel = 1
    
class ControllerMap():
    def __init__(self):
        '''creates two controllers and assigns
        axis and buttons to joysticks'''
        driverController = {}
        auxController = {}
        
        driverController['controllerId'] = 0
        auxController['controllerId'] = 1
        
        driverController['leftTread'] = 1
        driverController['leftRot'] = 0
        if hal.isSimulation():
            driverController['rightTread'] = 3
        else:
            driverController['rightTread'] = 5
        '''Create buttons for the drive controller'''
        driverController['ledToggle'] = wpilib.XboxController.Button.kX
        driverController['alignButton'] = wpilib.XboxController.Button.kA
        driverController['leftButton'] = wpilib.XboxController.Button.kBumperLeft
        driverController['rightButton'] = wpilib.XboxController.Button.kBumperRight
        driverController['straightButton'] = wpilib.XboxController.Button.kY
        '''Create buttons for the aux controller'''
        auxController['LowerButton'] = wpilib.XboxController.Button.kBumperLeft
        auxController['RaiseButton'] = wpilib.XboxController.Button.kBumperRight
        auxController['StopButton'] = wpilib.XboxController.Button.kY
        auxController['PistonButton'] = wpilib.XboxController.Button.kX
        auxController['RollerIO'] = wpilib.XboxController.Button.kA
        auxController['RollerToggle'] = wpilib.XboxController.Button.kB

        
        driverController['voltRumble'] = 8.0
        
        self.driverController = driverController
        self.auxController = auxController
        
class NetworkTableMap():
    def __init__(self):
        '''
        Create and set default variables for the network tables, defaulted to if we don't create a different file with our saved variables
        '''
        self.networkTableValues = { }
        
        #To create a new network value, create it with the format of "networkTableValues["NameOfValue"] = Value
        self.networkTableValues["ControllerSensitivity"] = -1
        self.networkTableValues["VoltageRumbleBeginsAt"] = 0 #no idea about what value might need to be
    
