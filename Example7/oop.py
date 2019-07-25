#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş [mustafa@hummingdrone.co]
# Company: Hummingdrone Inc. [hummingdrone.co]

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

NODE_NAME = "number_counter"
SUB_TOPIC_NAME = "/number"
PUB_TOPIC_NAME = "/number_count"
SERVICE_NAME = "/reset_counter"


class NumberCounter:
    """
    A class for a subscriber and publisher node.
    """

    def __init__(self):

        self.counter = 0
        self.sub = rospy.Subscriber(
            SUB_TOPIC_NAME, Int64, self.callback_number)
        self.pub = rospy.Publisher(PUB_TOPIC_NAME, Int64, queue_size=10)

        self.reset_service = rospy.Service(
            SERVICE_NAME, Int64, SetBool, self.callback_reset_number)

    def callback_number(self, msg):
        self.counter += msg.data
        new_msg = Int64()
        new_msg.data = self.counter
        self.pub.publish(new_msg)

    def callback_reset_number(self, req):

        if req.data:
            self.counter = 0
            return True
        return False


if __name__ == "__main__":
    rospy.init_node(NODE_NAME)
    NumberCounter()
    rospy.spin()
