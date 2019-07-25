#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

NODE_NAME = "led_panel"
SERVICE_NAME = "/set_led"
import rospy
from my_robot_msgs.srv import SetLed

led_states = [0,0,0]

def callback_set_led(req): # it takes the request, request include a led_number and state
	led_number = req.led_number
	state = req.state
	global led_states

	#led number could be 1,2,3 and state could be 0 or 1
	if (led_number > len(led_states)) or (led_number <= 0):
		return False
	# unacceptable points
	if not (state == 0 or state == 1):
		return False
	# in acceptable point led_state will change according to request
	led_states[led_number - 1] = state

	return True

if __name__ == '__main__':
	rospy.init_node(NODE_NAME) # initialize the server node


	server = rospy.Service(SERVICE_NAME, SetLed, callback_set_led) # create the server
	# if server gets any request then callback_set_led function will be called

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		rospy.loginfo(led_states) # server will always print led_states
		rate.sleep()

