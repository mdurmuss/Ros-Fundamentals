#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş 

import rospy
from rospy_tutorials.srv import AddTwoInts

NODE_NAME = "add_two_integer"
SERVICE_NAME = "/add_two_ints"


def handle_add_two_ints(req):  # req is the returning variable from server
    """
    runs when service is called from a client.
    req : contains two number. (req.a, req.b)
    returns a sum of these numbers.
    """
    result = req.a + req.b
    rospy.loginfo("Sum of ( " + str(req.a) + " and " + str(req.b) + "is "+str(result))
    return result


def service():
    """
    creates a ros node, a ros server.
    """
    rospy.init_node(NODE_NAME)  # create server node
    rospy.loginfo("Add two integer server node has created!")

    # AddTwoInts : Takes 2 number and response sum of them.
    service = rospy.Service(SERVICE_NAME, AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Service server has been started!")

    rospy.spin()  # that make program runs until any interrupt


if __name__ == "__main__":
    service()
