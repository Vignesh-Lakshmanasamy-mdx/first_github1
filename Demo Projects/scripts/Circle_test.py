#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys


def draw_circle():
    # Initialize the ROS node
    rospy.init_node('draw_circle', anonymous=True)
    
    global pub
    # Create a publisher to the /turtle1/cmd_vel topic
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Set the rate at which to publish messages
    rate = rospy.Rate(10)
    
    # Create a Twist message
    move_cmd = Twist()
    
    # Set linear and angular speeds
    move_cmd.linear.x = 1.0  # Move forward with a speed of 1.0
    move_cmd.angular.z = 1.0  # Rotate with a speed of 1.0
    
    # Publish the message for a certain duration to complete the circle
    for _ in range(100):
        pub.publish(move_cmd)
        rate.sleep()
    
    # Stop the turtle after drawing the circle
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        draw_circle()

    except rospy.ROSInterruptException:
        pass
