#!/usr/bin/env python

import rospy # import python library in ros

if __name__ == '__main__': 
	rospy.init_node('my_first_python_node') # create first node with its name.
	rospy.loginfo("This node has been started") # write a message to log

	rate = rospy.Rate(10) # frequency

	while not rospy.is_shutdown(): # until rospy is still working
		rospy.loginfo("Hello")
		rate.sleep()
