#!usr/bin/env python

import rospy
from my_robot_msgs.msg import HardwareStatus

if __name__ == "__main__":
    rospy.init_node("hardware_status_publisher")

    pub = rospy.Publisher("/my_robot/hardware_status",
                          HardwareStatus, queue_size=10)
    rate = rospy.Rate(5)
    msg = HardwareStatus()

    while not rospy.is_shutdown():

        msg.temperature = 45
        msg.are_motors_up = True
        msg.debug_message = "Everything is doing well"

        pub.publish(msg)

        rate.sleep()
