import rclpy, sys
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan, Image
from cv_bridge import CvBridge
import cv2
import numpy as np


#a = 0.2
#flag = 0

is_obstacle=0

class CirclePublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 5) 
        self.subscription = self.create_subscription(Image, "/depth/image", self.listener_callback, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        twist = Twist()
        if is_obstacle:
            twist.linear.x = 0.
        else:
            twist.linear.x = 0.8
        self.publisher.publish(twist)
    
    
    

    def listener_callback(self, msg):     
        cv_bridge = CvBridge()
        depth_image = cv_bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        depth_array = np.array(depth_image, dtype=np.float32)
        h, w = depth_array.shape

        global is_obstacle
        is_obstacle = 1 if depth_array[120][w//2] < 4 else 0
        	

        
        
def main(args=None):
    rclpy.init(args=args)

    circling = CirclePublisher()

    rclpy.spin(circling)

    #circling.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
