#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
from math import radians
from std_srvs.srv import Empty
from turtlesim.srv import Spawn,Kill,TeleportAbsolute


deg =0
axis_x=0
axis_y=0


def turtle1_move1():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg,axis_x,axis_y
    

    time.sleep(1)
    while not rospy.is_shutdown():
        if axis_x!=7.95:
            move_val.linear.x=1
            
            #move_val.angular.z=1
            #w+=1
            pub.publish(move_val)
            #print(w)
     
        if axis_x>8 :
            break
        rate.sleep()


def turtle1_move2():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg,axis_x,axis_y

    time.sleep(1)
    while not rospy.is_shutdown():
        if axis_y!=7.95:
            move_val.linear.x=1
            
            #move_val.angular.z=1
            #w+=1
            pub.publish(move_val)
            #print(w)
     
        if axis_y>8 :
            break
        rate.sleep()

def turtle1_move3():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg,axis_x,axis_y

    time.sleep(1)
    while not rospy.is_shutdown():
        if axis_x!=5.44:
            move_val.linear.x=1
            
            #move_val.angular.z=1
            #w+=1
            pub.publish(move_val)
            #print(w)
     
        if axis_x<5.5 :
            break
        rate.sleep()

def turtle1_move4():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg,axis_x,axis_y

    time.sleep(1)
    while not rospy.is_shutdown():
        if axis_y!=5.54:
            move_val.linear.x=1
            
            #move_val.angular.z=1
            #w+=1
            pub.publish(move_val)
            #print(w)
     
        if axis_y<5.58:
            break
        rate.sleep()


def posecallback(pose_message):
    #print(pose_message.theta)
    #print(pose_message.x)
    #print(pose_message.y)
    global deg,axis_x,axis_y
    deg=pose_message.theta
    axis_x=pose_message.x
    axis_y=pose_message.y
    #print(axis_x,axis_y,deg)
    #print(deg)
    

def turtle1_rotate():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg
    
    #move_val.linear.x=0
    #move_val.angular.z=0.5

    while not rospy.is_shutdown():
        if deg != 1.565 and deg<1.5608:
            move_val.linear.x=0
            move_val.angular.z=0.5236
            pub.publish(move_val)
        #timer1=rospy.Time.now().to_sec()
        #cur_ang=ang_speed*(timer1-time0)
            
        if deg>1.56 :
            break
        rate.sleep()
    print(deg)
    move_val.angular.z=0
    pub.publish(move_val)
    rate.sleep()

def turtle1_rotate1():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg
    n=abs(deg)
    #move_val.linear.x=0
    #move_val.angular.z=0.5

    while not rospy.is_shutdown():
        if deg != 3.125 and deg<3.13:
            move_val.linear.x=0
            move_val.angular.z=0.52133
            pub.publish(move_val)
        #timer1=rospy.Time.now().to_sec()
        #cur_ang=ang_speed*(timer1-time0)
            
        if deg>3.125  :
            break
        rate.sleep()
    print(deg)
    move_val.angular.z=0
    pub.publish(move_val)
    rate.sleep()

def turtle1_rotate2():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg
    w=0
    
    #move_val.linear.x=0
    #move_val.angular.z=0.5

    while not rospy.is_shutdown():
            move_val.linear.x=0
            move_val.angular.z=0.521333
            pub.publish(move_val)
            if abs(deg) <1.57:
                print("a")
                break    
        #timer1=rospy.Time.now().to_sec()
        #cur_ang=ang_speed*(timer1-time0)      
    
    print(deg)
    move_val.angular.z=0
    pub.publish(move_val)
    rate.sleep()

def turtle1_rotate3():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(10)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg
    w=0
    
    #move_val.linear.x=0
    #move_val.angular.z=0.5

    while not rospy.is_shutdown():
            move_val.linear.x=0
            move_val.angular.z=0.521333
            pub.publish(move_val)
            if deg >0:
                print("a")
                break    
        #timer1=rospy.Time.now().to_sec()
        #cur_ang=ang_speed*(timer1-time0)      
    
    print(deg)
    move_val.angular.z=0
    pub.publish(move_val)
    rate.sleep()

def turtle1_circle():
    rospy.init_node('turtlesim',anonymous=True)
    pub =rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)
    rate=rospy.Rate(1)
    
    #comment - assign Twist() to var move_val
    move_val= Twist()
    
    global deg
    w=0
    
    #move_val.linear.x=0
    #move_val.angular.z=0.5

    for s in range(100):
            move_val.linear.x=2
            move_val.angular.z=-1.5708
            pub.publish(move_val)
            w+=1
            print(w)
            
           
               
        #timer1=rospy.Time.now().to_sec()
        #cur_ang=ang_speed*(timer1-time0)      
    
    print(deg)
    move_val.linear.x=0
    move_val.angular.z=0

    pub.publish(move_val)
    rate.sleep()

def draw_circle():
    # Initialize the ROS node
    rospy.init_node('turtlesim', anonymous=True)
    
    # Create a publisher to the /turtle1/cmd_vel topic
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Set the rate at which to publish messages
    rate = rospy.Rate(10)
    
    # Create a Twist message
    move_cmd = Twist()
    
    # Set linear and angular speeds
    move_cmd.linear.x = 1.0  # Move forward with a speed of 1.0
    move_cmd.angular.z = 0.65  # Rotate with a speed of 1.0
    
    # Publish the message for a certain duration to complete the circle
    for _ in range(100):
        pub.publish(move_cmd)
        rate.sleep()
        
    # Stop the turtle after drawing the circle
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

    print(axis_x,axis_y,deg)

    move_cmd.linear.x = 1.0  # Move forward with a speed of 1.0
    move_cmd.angular.z =- 0.65  # Rotate with a speed of 1.0

    # Publish the message for a certain duration to complete the circle
    for _ in range(100):
        pub.publish(move_cmd)
        rate.sleep()

        # Stop the turtle after drawing the circle
    move_cmd.linear.x = 0
    move_cmd.angular.z = 0
    pub.publish(move_cmd)

if __name__=='__main__':
    try:
        
         
        print(axis_x,axis_y,deg)
        turtle1_move1()
        print(axis_x,axis_y,deg)
        turtle1_rotate()
        print(axis_x,axis_y,deg)
        turtle1_move2()
        print(axis_x,axis_y,deg) 
        turtle1_rotate1()
        print(axis_x,axis_y,deg)
        turtle1_move3()
        print(axis_x,axis_y,deg) 
        turtle1_rotate2()
        print(axis_x,axis_y,deg)
        turtle1_move4()
        print(axis_x,axis_y,deg)
        turtle1_rotate3()
        print(axis_x,axis_y,deg) 
             
        
        print('start reset: ')
        rospy.wait_for_service('reset')
        reset_turtle = rospy.ServiceProxy('reset', Empty)
        reset_turtle()
        print('end reset')
        """
        print('start kill: ')
        rospy.wait_for_service('kill')
        kill_turtle = rospy.ServiceProxy('kill', Kill)
        kill_turtle("turtle1")
        print('end kill')
        """   

        print('start spawn: ')
        rospy.wait_for_service('spawn')
        add_turtle = rospy.ServiceProxy('spawn', Spawn)
        add_turtle(5.54,5.54,0,"turtle2")
        print('end spawn')
       
        
        print('start teleport: ')
        rospy.wait_for_service('turtle1/teleport_absolute')
        tele_turtle = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
        tele_turtle(8.0,8.0,-1.57)
        print('end Teleport')
        
        draw_circle()

    except rospy.ROSInterruptException:
        pass