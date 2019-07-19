#!/usr/bin/env python

NODE_NAME = "parameter_publisher"
PUB_TOPIC_NAME ="/parameter_number"
PARAM_NAME = ["/rosversion","/rosdistro","/another_param"]
import rospy
from std_msgs.msg import Int64

if __name__ == "__main__":
    rospy.init_node(NODE_NAME,anonymous=True)

    pub = rospy.Publisher(PUB_TOPIC_NAME,Int64,queue_size=10)

    publish_frequency = rospy.get_param(PARAM_NAME[0])
    # getting the frequency parameter from ros
    rate = rospy.Rate(2)

    number = rospy.get_param(PARAM_NAME[1])
    # create another parameter

    rospy.set_param(PARAM_NAME[2],"HelloROS")
    while not rospy.is_shutdown():

        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep()