#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

NODE_NAME = "Subscriber_and_Publisher"
SUB_TOPIC_NAME = "/NumberPublisher"
PUB_TOPIC_NAME = "/CountPublisher"
SERVICE_NAME = "/reset_number_count"
counter = 0


def callback_function(msg):
    """
    runs when subscriber takes a message.
    counts of all messages and publishes.
    """
    rospy.loginfo("Message has arrived! -->"+str(msg))
    global counter
    counter += msg.data

    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)


def handler_set_bool(req):
    """
    runs when service is called by a client.
    takes a request and returns a response.
    req : request of the client.
    returns True or False according to the request data
    """
    global counter
    if req.data is True:
        counter = 0
        return [True, "Counter is arranged to 0!"]
    return [False, "Counter still counting!"]


if __name__ == "__main__":

    rospy.init_node(NODE_NAME)
    pub = rospy.Publisher(PUB_TOPIC_NAME, Int64, queue_size=10)
    # publisher created
    sub = rospy.Subscriber(SUB_TOPIC_NAME, Int64, callback_function)
    # subscriber created, take message to callback_function
    srv = rospy.Service(SERVICE_NAME, SetBool, handler_set_bool)
    # service created
    rospy.loginfo("Count Service server has been started!")

    rate = rospy.Rate(2)
    rospy.spin()
