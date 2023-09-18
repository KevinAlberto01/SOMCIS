#!/usr/bin/env python

######################################### Setup environment and import libraries 

import rospy
from std_msgs.msg import String

##########################################

########################################## Define Callback
def callback(msg):
    rospy.loginfo("I heard %s", msg.data)
##########################################

########################################## Create variables and initialise
if __name__=='__main__':
    rospy. init_node('listener')
    rospy.Subscriber("chatter", String, callback)
##########################################   
    rospy.spin()
##########################################
