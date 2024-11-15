#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

axis_x = 0
axis_y=0
rad_deg=0

def posecallback(pose_message):
    global axis_x,axis_y,rad_deg
    #print(pose_message.x)
    axis_x=pose_message.x
    axis_y=pose_message.y
    rad_deg=pose_message.theta

if __name__=='__main__':
    try:
        rospy.init_node('turtlesim',anonymous=True)
        pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
        rate=rospy.Rate(1)
        print(axis_x,axis_y,rad_deg)
        
        #comment - assign Twist() to var move_val
        move_val= Twist()
        w=0
    
        while not rospy.is_shutdown():
            if w<4 :
                move_val.linear.x=1
                #move_val.angular.z=1
                w+=1
                pub.publish(move_val)
                print(w)
     
            if w==4 :
                w=0
                print(w)
                break
        rate.sleep()
    except rospy.ROSInterruptException:
        pass