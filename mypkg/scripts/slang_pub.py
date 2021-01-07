#!/usr/bin/env python2                                                                              # -*- coding: utf-8 -*-            
import rospy
from std_msgs.msg import UInt16
import sys 

rospy.init_node('input')                                
pub = rospy.Publisher('slang', UInt16, queue_size=1)  
rate = rospy.Rate(10)                                  
n = 0 
while not rospy.is_shutdown():
    n = input('input slang: ')
    pub.publish(n)
    rate.sleep()

