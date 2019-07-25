#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from std_msgs.msg import Int64

NODE_NAME = "parameter_publisher"
PUB_TOPIC_NAME = "/parameter_number"
PARAM_NAMES = ["/rosversion", "/rosdistro", "/another_param"]


def parameter():
    """
    creates a ros node and publisher.
    gets a parameter and publishes.
    sets a parameter.
    """
    rospy.init_node(NODE_NAME, anonymous=True)

    pub = rospy.Publisher(PUB_TOPIC_NAME, Int64, queue_size=10)

    publish_frequency = rospy.get_param(PARAM_NAMES[0])
    # getting the frequency parameter from ros
    rate = rospy.Rate(2)

    number = rospy.get_param(PARAM_NAMES[1])
    # create another parameter

    rospy.set_param(PARAM_NAMES[2], "HelloROS")
    while not rospy.is_shutdown():

        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep()


if __name__ == "__main__":
    parameter()
