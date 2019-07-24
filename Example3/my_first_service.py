#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts

NODE_NAME = "add_two_integer"
SERVICE_NAME = "/add_two_ints"


def handle_add_two_ints(req):  # req is the returning variable from server
    result = req.a + req.b
    rospy.loginfo("Sum of ( " + str(req.a) + " and " + str(req.b) +")
    is "+str(result))
    return result  # result will send to client

if __name__ == "__main__":
    rospy.init_node(NODE_NAME)  # create server node
    rospy.loginfo("Add two integer server node has created!")

    service=rospy.Service(SERVICE_NAME, AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Service server has been started!")

    rospy.spin()  # that make program runs until any interrupt
    