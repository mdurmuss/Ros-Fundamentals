#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool
counter =0

def callback_function(msg):
    rospy.loginfo("Message has arrived! -->"+str(msg))
    global counter
    counter += msg.data

    new_msg = Int64()
    new_msg.data = counter
    pub.publish(new_msg)

def handler_set_bool(req): # when service takes a request
    # we can 
    # talk with server
    # ask a question
    # get an answer
    # that is the difference between topics and servers
    global counter
    if req.data == True: # if request is True
        counter = 0 # counter will be 0
        return [True,"Counter is arranged to 0!"]
    return [False,"Counter still counting!"]


if __name__ == "__main__":
    rospy.init_node("Subscriber_and_Publisher")
    
    sub = rospy.Subscriber("/NumberPublisher",Int64,callback_function)
    #subscriber created, take message to callback_function
    pub = rospy.Publisher("/CountPublisher",Int64,queue_size=10)
    #publisher created
    srv = rospy.Service("/reset_number_count",SetBool,handler_set_bool)
    #service created
    rospy.loginfo("Count Service server has been started!")

    rate = rospy.Rate(2)
    rospy.spin()