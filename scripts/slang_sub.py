#!/usr/bin/env python2
import rospy
from std_msgs.msg import UInt16

def cb(message):
    rospy.loginfo(message.data)
    if message.data == 143 or message.data == 831:
        print '>> '+'I love you\n'
    elif message.data == 182:
        print '>> '+'I hate you\n'
    elif message.data == 511:
        print '>> '+'Too much information\n'
    elif message.data == 637:
        print '>> '+'Always and forever\n'
    elif message.data == 823:
        print '>> '+'Thinkng of you\n'
    else :
        print '[UNDEFINED]\n'

if __name__ == '__main__':
    rospy.init_node('translate')
    sub = rospy.Subscriber('slang', UInt16, cb)
    rospy.spin()           
