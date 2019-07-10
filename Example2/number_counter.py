#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
# import related libs
counter = 0

def myfunction(message):
    rospy.loginfo("Message has just received!")
    rospy.loginfo(message)
    global counter
    counter += message.data

    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)
    
if __name__ == "__main__":
    rospy.init_node("numberCounter")
    subscriber = rospy.Subscriber("/number",Int64,myfunction) # create a subscriber
    # here there is a function(myfunction)
    # this function will be called when that topic will send a message.
    # after taking that message that function will show it.
    # and will add it to counter and publish it.
    pub = rospy.Publisher("/number_count",Int64,queue_size=10) # create a publisher
    rate = rospy.Rate(2)
    
    rospy.spin()

# that node is a subscriber to "/number" topic and a publisher of "/number_count" topic.