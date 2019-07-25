#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş [mustafa@hummingdrone.co]
# Company: Hummingdrone Inc. [hummingdrone.co]

import rospy
from rospy_tutorials.srv import AddTwoInts

NODE_NAME = "add_two_ints_client"
SERVICE_NAME = "/add_two_ints"


def client():
    """
    this function tries to connect a service and
    sends a message and takes a response.
    """
    rospy.init_node(NODE_NAME)
    rospy.wait_for_service(SERVICE_NAME)  # wait until the service is available

    # after service is available, lets do our job
    # first write a try/except block for any fault about service
    for i in range(10):
        try:
            add_two_ints = rospy.ServiceProxy(SERVICE_NAME, AddTwoInts)
            # client created
            response = add_two_ints(i, i+3)
            # response from service
            rospy.loginfo("Sum is : "+str(response))
        except rospy.ServiceException as e:
            rospy.logwarn("Service failed because of : "+str(e))


if __name__ == "__main__":
    try:
        client()
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed because of : "+str(e))
