#!/usr/bin/env python3
#license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter',String,queue_size=10)
    rospy.init_node('talker',anonymous=True)
    rate=rospy.Rate(10)
    x =0
    while not rospy.is_shutdown():
    	x+=1
        hello_str='hai NIVI and Charun %s' % x
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        
        rate.sleep()
if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
