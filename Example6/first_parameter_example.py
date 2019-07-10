#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

if __name__ == "__main__":
    rospy.init_node("parameter_publisher",anonymous=True)

    pub = rospy.Publisher("/parameter_number",Int64,queue_size=10)

    publish_frequency = rospy.get_param("/number_publisher_frequency")
    # getting the frequency parameter from ros
    rate = rospy.Rate(publish_frequency)

    number = rospy.get_param("/number_to_publish")
    # create another parameter

    rospy.set_param("/another_param","HelloROS")
    while not rospy.is_shutdown():

        msg = Int64()
        msg.data = number
        pub.publish(msg)
        rate.sleep()