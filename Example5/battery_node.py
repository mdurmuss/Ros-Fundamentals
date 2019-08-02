#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Mustafa Durmuş

import rospy
from my_robot_msgs.srv import SetLed

NODE_NAME = "battery"
SERVICE_NAME = "/set_led"


def set_led(battery_state):
    """

    """
      rospy.wait_for_service(
          SERVICE_NAME)  # wait until the service is available
       try:
            # take the service with its name
            service = rospy.ServiceProxy(SERVICE_NAME, SetLed)
            state = 0  # state will be 0 by default
            if battery_state == 'empty':  # if battery is empty then state will be 1
                state = 1
            # send request as (3 and state) and take response
            resp = service(3, state)
            # response will be true or false
            rospy.loginfo("Set led success flag : " + str(resp))
        except rospy.ServiceException as e:
            rospy.logerr(e)


if __name__ == '__main__':

    rospy.init_node(NODE_NAME)  # initialize the client_node
    battery_state = "full"  # battery state will be full by default

    while not rospy.is_shutdown():  # until node is still alive
        rospy.sleep(7)
        battery_state = "empty"  # after 7 seconds battery will be low
        rospy.loginfo("The battery is empty !")
        set_led(battery_state)  # call the set_led function with battery_state
        rospy.sleep(3)
        battery_state = "full"
        rospy.loginfo("The battery is now full")
        set_led(battery_state)
