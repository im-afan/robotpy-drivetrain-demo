import wpilib # gives a lot of useful stuff for robotics
from phoenix5 import TalonSRX, FollowerType, ControlMode

class Hardware:
    def __init__(self):
        self.left_leader = TalonSRX(1) # 3 motors on the left side
        self.left_follower1 = TalonSRX(2)
        self.left_follower2 = TalonSRX(3)

        self.right_leader = TalonSRX(4) # 3 motors on the right side
        self.right_follower1 = TalonSRX(5) # the number passed in TalonSRX is the port number
        self.right_follower2 = TalonSRX(6) # which is defined when you build the robot

        self.left_follower1.follow(self.left_leader, FollowerType.PercentOutput) # makes the follower motors follow
        self.left_follower2.follow(self.left_leader, FollowerType.PercentOutput) # makes the follower motors follow


        self.right_follower1.follow(self.right_leader, FollowerType.PercentOutput) # makes the follower motors follow
        self.right_follower2.follow(self.right_leader, FollowerType.PercentOutput) # makes the follower motors follow


        #initialize joysticks
        self.left_stick = wpilib.Joystick(0) # once again the number denotes the port number
        self.right_stick = wpilib.Joystick(1) # this time it depends on which USB port the joystick is connected to


