#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == "__main__":
    rospy.init_node("add_two_ints_client")
    
    rospy.wait_for_service("/add_two_ints") # wait until the service is available

    # after service is available, lets do our job
    # first write a try/except block for any fault about service

    for i in range(10):
        try:
            add_two_ints = rospy.ServiceProxy("/add_two_ints",AddTwoInts) # client created
            response = add_two_ints(i,i+3)  # response from service
            rospy.loginfo("Sum is : "+str(response))
        except rospy.ServiceException as e:
            rospy.logwarn("Service failed because of : "+str(e))







