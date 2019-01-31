'''
    This is a demo program showing how to use Mecanum control with the
    RobotDrive class.
'''

import team3200
import wpilib
from networktables import NetworkTables
from wpilib.buttons.joystickbutton import JoystickButton
import commandbased
from team3200.commands.lights import Lights
from team3200.commands.lights import ExampleButton
import team3200.subsystems.driveTrain
import team3200.subsystems.healthMonitor

class MyRobot(commandbased.CommandBasedRobot):
    
    def robotInit(self):
        '''This is where the robot code starts.'''
        team3200.getRobot = lambda x=0:self
        self.map = team3200.robotMap.RobotMap()
        self.networkTableInit()
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()
        self.driveController = wpilib.XboxController(0)
        self.createButtons()
        self.healthMonitor = team3200.subsystems.healthMonitor.HealthMonitor()
    
    def networkTableInit(self):
        '''This sets up the network tables and adds a variable called sensitivity'''
        NetworkTables.initialize(server = 'roborio-3200-frc.local')
        
        self.liveWindowTable = NetworkTables.getTable('LiveWindow')
        self.liveWindowTable.putNumber('Sensitivity', -1)
        

    def controllerInit(self):
        self.driveController = wpilib.XboxController(0)
        self.lightButton = JoystickButton(self.driveController, 3)

        self.lightButton.whenPressed(Lights())
        self.exampleButton = JoystickButton(self.driveController, self.map.controllerMap.driverController['exampleButton'])
        self.exampleButton.whenPressed(ExampleButton())

    def driveInit(self):
        self.dtSub = team3200.subsystems.driveTrain.DriveTrainSub()

if __name__ == '__main__':
    try:
        #patch no exit error if not running on robot
        try:
            print(wpilib._impl.main.exit)
        except:
            wpilib._impl.main.exit = exit
            
        #fixes simulation rerun errors.
        #todo verify this causes no issues on robot
        wpilib.DriverStation._reset()

        #patch simulation
        #we update the simluation files to ours. If we update WPIlib these may break
        import sim.ui
        import sim.pygame_joysticks
        import pyfrc.sim
        import pyfrc.sim.pygame_joysticks
        pyfrc.sim.SimUI = sim.ui.SimUI
        pyfrc.sim.pygame_joysticks.UsbJoysticks = sim.pygame_joysticks.UsbJoysticks
    except Exception as err:
            print("Failed to patch runtime. Error", err)
    
    wpilib.run(MyRobot,physics_enabled=True)

def exit(retval):
    pass