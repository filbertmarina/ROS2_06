import rclpy, sys
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

#a = 0.2
#flag = 0

is_obstacle=0

class CirclePublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 5) 
        self.subscription = self.create_subscription(LaserScan, "/robot/scan", self.listener_callback, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        twist = Twist()
        if is_obstacle:
            twist.linear.x = 0.
        else:
            twist.linear.x = 0.8
        self.publisher.publish(twist)
    
    
    

    def listener_callback(self, msg):
        data = msg.ranges
        n = len(data)
        count = 0
        global is_obstacle
        for i in range(10):
        	if data[n//2-5+i]<1:
        		count = 1
        		
        if count == 1:
        	is_obstacle = 1
        else:
        	is_obstacle = 0
        
        	

        
        
def main(args=None):
    rclpy.init(args=args)

    circling = CirclePublisher()

    rclpy.spin(circling)

    #circling.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
