#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from std_msgs.msg import Int64


NODE_NAME = "NumberNode"
TOPIC_NAME = "/number"

if __name__ == "__main__":
    rospy.init_node(NODE_NAME, anonymous=True)

    publisher = rospy.Publisher(TOPIC_NAME, Int64, queue_size=10)
    # number is the topic name.
    # Int64 is the message type of topic
    rate = rospy.Rate(2)
    message = Int64()
    while not rospy.is_shutdown():
        message.data = 10
        # INT64 message type has a data variable.
        publisher.publish(message)
        # lets publish it
        rate.sleep()
    rospy.loginfo("Node has stopped!")
