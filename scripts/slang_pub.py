#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
import sys 

rospy.init_node('input')                                
pub = rospy.Publisher('slang', String, queue_size=1)  
while not rospy.is_shutdown():
    n = String()
    n.data = raw_input('input message: ')
    pub.publish(n)
