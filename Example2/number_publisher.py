#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64


NODE_NAME = "NumberNode"
TOPIC_NAME = "/number"

if __name__ == "__main__":
    rospy.init_node(NODE_NAME, anonymous=True)

    publisher = rospy.Publisher(TOPIC_NAME, Int64, queue_size=10)
    # number is the topic name.
    # Int64 is the type of message of that topic will publish
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        message = Int64()
        message.data = 10
        # that type of message(INT64) has a data variable.
        publisher.publish(message)
        # lets publish it
        rate.sleep()

    rospy.loginfo("Node has stopped!")