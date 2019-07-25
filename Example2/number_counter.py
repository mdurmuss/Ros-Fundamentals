#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş [mustafa@hummingdrone.co]
# Company: Hummingdrone Inc. [hummingdrone.co]

import rospy
from std_msgs.msg import Int64

NODE_NAME = "numberCounter"
SUB_TOPIC_NAME = "/number"
PUB_TOPIC_NAME = "/number_count"

counter = 0


def my_function(message):
    """
    gets the message topic sent and will publish its new message.
    message
    message : Message that taken from the subscribed topic.
    """
    rospy.loginfo("Message has just received!")
    rospy.loginfo(message)
    global counter
    counter += message.data

    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)


if __name__ == "__main__":
    rospy.init_node(NODE_NAME)
    # that node is a subscriber to "/number" topic
    # and a publisher of "/number_count" topic.
    subscriber = rospy.Subscriber(SUB_TOPIC_NAME, Int64, my_function)
    # create a subscriber
    pub = rospy.Publisher(PUB_TOPIC_NAME, Int64, queue_size=10)
    # create a publisher
    rate = rospy.Rate(2)
    rospy.spin()
