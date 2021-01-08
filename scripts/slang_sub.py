#!/usr/bin/env python2
import rospy
import time
from std_msgs.msg import String
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(11, RPi.GPIO.OUT)
RPi.GPIO.setup(12, RPi.GPIO.OUT)
RPi.GPIO.setup(13, RPi.GPIO.OUT)
RPi.GPIO.setup(14, RPi.GPIO.OUT)
RPi.GPIO.setup(15, RPi.GPIO.OUT)
RPi.GPIO.setup(16, RPi.GPIO.OUT)
RPi.GPIO.setup(17, RPi.GPIO.OUT)
RPi.GPIO.setup(18, RPi.GPIO.OUT)
RPi.GPIO.output(11, 0)
RPi.GPIO.output(12, 0)
RPi.GPIO.output(13, 0)
RPi.GPIO.output(14, 0)
RPi.GPIO.output(15, 0)
RPi.GPIO.output(16, 0)
RPi.GPIO.output(17, 0)
RPi.GPIO.output(18, 0)

def clgpio():
    for i in range(11, 19):
        RPi.GPIO.output(i, 0)
    time.sleep(0.5)

def cb(message):

    if message.data == 'I love you':
        # 143
        RPi.GPIO.output(11, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 15):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 14):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()

    elif message.data == 'I hate you':
        # 182
        RPi.GPIO.output(11, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 19):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 14):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()

    elif message.data == 'Too much information':
        # 511
        for i in range(11, 16):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()
        RPi.GPIO.output(11, 1)
        time.sleep(0.5)
        clgpio()
        RPi.GPIO.output(11, 1)
        time.sleep(0.5)
        clgpio()

    elif message.data == 'Always and forever':
        # 637
        for i in range(11, 17):
            RPi.GPIO.output(i, 16)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 14):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 18):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()

    elif message.data == 'Thinking of you':
        # 823
        for i in range(11, 19):
            RPi.GPIO.output(i, 16)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 13):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()
        for i in range(11, 14):
            RPi.GPIO.output(i, 1)
        time.sleep(0.5)
        clgpio()

    else:
        for i in range(11, 19):
            RPi.GPIO.output(i, 1)
            time.sleep(0.02)
        for i in range(11, 19):
            RPi.GPIO.output(i, 0)
            time.sleep(0.02)

if __name__ == '__main__':
    rospy.init_node('translate')
    sub = rospy.Subscriber('slang', String, cb)
    rospy.spin()           
