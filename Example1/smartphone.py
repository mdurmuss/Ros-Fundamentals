#!/usr/bin/env python

import rospy
from std_msgs.msg import String

NODE_NAME = "smartphone"
SUB_TOPIC_NAME = "/robot_news_radioooo"


def callback_receive_radio_data(msg):
    """
    runs when subscriber node takes a mesage from publisher and prints it.
    msg : published message
    """
    rospy.loginfo("Message received : "+str(msg))


if __name__ == '__main__':

    rospy.init_node(NODE_NAME)
    sub = rospy.Subscriber(SUB_TOPIC_NAME, String, callback_receive_radio_data)
    rospy.spin()
