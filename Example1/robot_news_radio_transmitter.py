#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from std_msgs.msg import String

NODE_NAME = "robot_news_radio_transmitter"
PUB_TOPIC_NAME = "/robot_news_radio"


if __name__ == '__main__':

	rospy.init_node(NODE_NAME, anonymous=True)

	pub = rospy.Publisher(PUB_TOPIC_NAME, String, queue_size=10)
	# create a publisher
	# topic name : /robot_news_radio
	# topic message type : String
	rate = rospy.Rate(2)

	while not rospy.is_shutdown():
		msg = String()
		msg.data = "Hi, this is Mustafa from your Robot Radio !"
		pub.publish(msg)
		# publish the message
		rate.sleep()

	rospy.loginfo("Node has stopped")