#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from std_msgs.msg import Int64

NODE_NAME = "PublisherNode"
TOPIC_NAME = "/NumberPublisher"


def publisher():
    """
    creates a message type of Int64 and publishes.
    """
    # publisher created
    rospy.loginfo("Message is publishing")
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg.data = 7
        pub.publish(msg)
        # publisher sending the message
        rate.sleep()

    rospy.loginfo("Publisher node has stopped!")


if __name__ == "__main__":
    rospy.init_node(NODE_NAME)  # node created
    pub = rospy.Publisher(TOPIC_NAME, Int64, queue_size=10)
    msg = Int64()
    publisher()
