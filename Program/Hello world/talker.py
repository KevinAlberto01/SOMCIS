#!/usr/bin/env python

###############################    Setup environment and import libraries 
import rospy
from std_msgs.msg import String
###############################

########################################################### Create variables and setup node 
if __name__ == '__main__':
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rospy.init_node("talker")
    rate = rospy.Rate(10)
###########################################################

########################################################### Publish message
    while not rospy.is_shutdown():
        hello_str = "helllo world %s" % rospy.get_time()
        pub.publish(hello_str)

############################################################ Wait to run again         
        rate.sleep()
############################################################
