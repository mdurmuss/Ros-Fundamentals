#!/usr/bin/env python
NODE_NAME = "PublisherNode"
TOPIC_NAME ="/NumberPublisher"
import rospy
from std_msgs.msg import Int64

if __name__ == "__main__":

    rospy.init_node(NODE_NAME) # node created
    pub = rospy.Publisher(TOPIC_NAME,Int64,queue_size=10) #publisher created
    rospy.loginfo("Message is publishing")
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = Int64()
        msg.data = 7
        pub.publish(msg)
        # publisher sending the message
        rate.sleep()

    rospy.loginfo("Publisher node has stopped!")
