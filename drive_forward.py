import wpilib 
from datetime import datetime
from phoenix5 import ControlMode

class DriveForward:
    def __init__(self, wanted_time, hardware):
        self.wanted_time = wanted_time
        self.hardware = hardware

    def start(self): #when the routine starts, we basically set a timer
        self.start_time = datetime.now().second

    def update(self):
        self.hardware.left_leader.set(ControlMode.PercentOutput, 0.2) # set motors to 20% output
        self.hardware.right_leader.set(ControlMode.PercentOutput, -0.2) # set motors to 20% output


    def check_done(self): 
        if(datetime.now().second - self.start_time > self.wanted_time):
            return True
        return False

