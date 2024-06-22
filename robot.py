import wpilib # gives a lot of useful stuff for robotics
from hardware import Hardware
from drive_forward import DriveForward
from phoenix5 import ControlMode

class Robot(wpilib.TimedRobot):
    def robotInit(self): #initializes motors, controllers, etc
        self.hardware = Hardware()

    def autonomousInit(self):
        self.drive_forward_routine = DriveForward(2, self.hardware)
        self.drive_forward_routine.start()
        pass

    def autonomousPeriodic(self):
        if self.drive_forward_routine.check_done():
            return
        self.drive_forward_routine.update()
        pass



    def teleopPeriodic(self): #calls this every few milliseconds - lets us control the robot
        self.hardware.left_leader.set(ControlMode.PercentOutput, self.hardware.left_stick.getY() + self.hardware.left_stick.getX()) # set motors to 20% output
        self.hardware.right_leader.set(ControlMode.PercentOutput, -self.hardware.left_stick.getY() + self.hardware.left_stick.getX()) # set motors to 20% output



