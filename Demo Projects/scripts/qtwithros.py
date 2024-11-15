#!/usr/bin/env python3
import sys
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets

deg=0
axis_x=0
axis_y=0

def posecallback(pose_message):
    global deg,axis_x,axis_y
    deg=pose_message.theta
    axis_x=pose_message.x
    axis_y=pose_message.y

def move_turtle():
    twist = Twist()
    global deg,axis_x,axis_y
    while not False:
        twist.linear.x = 2.0
        twist.angular.z = 0.5
        cmd_vel_pub.publish(twist)
        if axis_y<5:
            break
 

def main():
    rospy.init_node('turtlesim_control_gui', anonymous=True)

    global cmd_vel_pub
    cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)

    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    rospy.spin()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(400, 10, 81, 621))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 60, 80, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Move Turtle")
  
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton.clicked.connect(move_turtle)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Turtlesim Control GUI"))

if __name__ == "__main__":
    main()
