#!/usr/bin/env python

import rospy
from my_robot_msgs.srv import SetLed

def set_led(battery_state):
	rospy.wait_for_service("/set_led") # wait until the service is available
	try:
		service = rospy.ServiceProxy("/set_led", SetLed) # take the service with its name
		state = 0 # state will be 0 by default
		if battery_state == 'empty': # if battery is empty then state will be 1
			state = 1
		resp = service(3, state) # send request as (3 and state) and take response
		rospy.loginfo("Set led success flag : " + str(resp)) # response will be true or false
	except rospy.ServiceException as e:
		rospy.logerr(e)


if __name__ == '__main__':
	rospy.init_node('battery') #initialize the client_node

	battery_state = "full" # battery state will be full by default

	while not rospy.is_shutdown(): # until node is still alive
		rospy.sleep(7)
		battery_state = "empty" # after 7 seconds battery will be low
		rospy.loginfo("The battery is empty !")
		set_led(battery_state) # call the set_led function with battery_state
		rospy.sleep(3)
		battery_state = "full"
		rospy.loginfo("The battery is now full")
		set_led(battery_state)
