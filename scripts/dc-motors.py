#!/usr/bin/env python
import rospy
from std_msgs.msg import String

import Adafruit_BBIO.PWM as PWM

pin = "P9_42"

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)
    # process the data heard and call setDuty with the desired value

def setDuty(value):
    ##duty values are valid 0-100
    if value > 100:
        value = 100
    if value < 0:
        value = 0

    PWM.set_duty_cycle(pin, value)

def dcmotors():
    rospy.init_node('dc-motors', anonymous=True)
    rospy.Subscriber("mpu9150_topic", String, callback)

    # init the PWM
    ##PWM.start(channel, duty, freq=2000)
    PWM.start("P9_14", 50)

    rospy.spin()


if __name__ == '__main__':
    dcmotors()
