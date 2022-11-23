#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import pygame


pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()


def map_range(x, in_min, in_max, out_min, out_max):
   
        map_val= ((x - in_min) * (out_max - out_min) / (in_max - in_min))
        # print ("map: ",map_val+out_min)
        return  map_val+ out_min
        

class JoysticNode(Node):
   

    def __init__(self):
       
        super().__init__("joystick_pub")
        self.get_logger().info("Joystic Initisated!")
        self.publisher_= self.create_publisher(Twist,"cmd_vel",10)
        
        self.create_timer(0.2,self.joystick_data)
    
    
    
    
    def joystick_data(self):
        
        
        # pygame.event.pump()

        direction = map_range(-10*pygame.joystick.Joystick(0).get_axis(0), -10.0, 10.0, -0.25, 0.25)
        throttle = map_range(-10*pygame.joystick.Joystick(0).get_axis(4), -10.0, 10.0, -0.5, 0.5)

        # direction = map_range(8, -10.0, 10.0, -0.2, 0.2)
        # throttle = map_range(8, -10.0, 10.0, -0.2, 0.2)

        # direction=0.0
        # throttle= 0.00
        msg=Twist()
        # msg.linear.x= throttle
        # msg.angular.z=direction
        msg.linear.x = round(throttle, 4) 
        msg.angular.z = round(direction, 4)

        # print("linear : ",msg.linear.x)
        # print("angular : ",msg.angular.z)
        
        self.publisher_.publish(msg)





def main(args=None):
    rclpy.init(args=args)
    node= JoysticNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__" :
    main()

