#!/usr/bin/env python

def handle_add_two_ints(req): # req is the returning variable from server
    result = req.a + req.b 
    rospy.loginfo("Sum of ( " + str(req.a)+ " and "+ str(req.b)+" ) is "+str(result))
    return result # result will send to client

import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == "__main__":
    rospy.init_node("add_two_integer") # create server node
    rospy.loginfo("Add two integer server node has created!")

    service = rospy.Service("/add_two_ints",AddTwoInts,handle_add_two_ints) # create service
    rospy.loginfo("Service server has been started!")

    rospy.spin() # that make program runs until any interrupt