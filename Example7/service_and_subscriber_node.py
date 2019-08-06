#!/usr/bin/env python

import rospy
from my_robot_msgs.msg import HardwareTest
from my_robot_msgs.srv import Test
# related libs imported

# OOP will be used in this example


class Drone:

    def __init__(self):
        self.sub = rospy.Subscriber(
            "/status", HardwareTest, self.callback_HardwareTest)
        self.srv = rospy.Service("/takeAction", Test, self.test_handler)
        self.location = []
    # when an object is created, subscriber and server will be created also.
    # subscriber takes message and calls callback_HardwareTest function.
    # when server takes a request, test_handler will be called.

    def callback_HardwareTest(self, msg):
        self.name = msg.name
        self.location = msg.location
        self.isVisible = msg.isVisible
        rospy.loginfo("Drone's name is : "+str(self.name))
        rospy.loginfo("Drone's location" +
                      "    X: "+str(self.location[0]) +
                      "    Y: "+str(self.location[1]) +
                      "    Z: "+str(self.location[2])
                      )
        rospy.loginfo("Enemy visibility: " + str(self.isVisible))

    def test_handler(self, req):
        if self.isVisible and req.distance <= 10.0:
            rospy.loginfo("ENEMY IS BEING SHOOTED")
            return True
        rospy.loginfo("ENEMY NOT FOUND")
        return False


if __name__ == "__main__":
    rospy.init_node("SERVER")
    # node created
    Drone()
    rospy.spin()
