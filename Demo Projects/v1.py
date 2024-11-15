#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Twist
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

def move_turtle():
    twist=Twist()
    twist.linear.x=2.0
    twist.angular.z=0.5
    cmd_vel_pub.publish(twist)

def main():
    rospy.init_node('turtlesim_control_gui', anonymous=True)

    global cmd_vel_pub
    cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)

    app=QApplication(sys.argv)
    window=QWidget()
    window.setWindowTitle('Turtlesim Control')
    window.setGeometry(300,300,400,200)

    button=QPushButton('Move Turtle',window)
    button.setGeometry(QtCore.QRect(130, 110, 89, 41))
    button.clicked.connect(move_turtle)

    window.show()

    rospy.spin()
    sys.exit(app.exec_())

if __name__== '__main__':

    main()
