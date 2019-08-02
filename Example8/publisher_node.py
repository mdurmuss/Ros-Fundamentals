#!/usr/bin/env python

import rospy
from my_robot_msgs.msg import HardwareTest
# related libs imported

if __name__ == "__main__":
    rospy.init_node("TEST")
    # node created

    pub = rospy.Publisher("/status", HardwareTest, queue_size=10)
    # publisher created
    rate = rospy.Rate(5)
    # frequency
    msg = HardwareTest()

    while not rospy.is_shutdown():

        # message created from HardwareTest class
        msg.name = "MD101"
        msg.isVisible = True
        msg.location = [41.6, 12.2, 105.3]
        pub.publish(msg)
        # message publishing

        rate.sleep()
