import rclpy, sys
from rclpy.node import Node
from geometry_msgs.msg import Twist

#a = 0.2
#flag = 0
class CirclePublisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher = self.create_publisher(Twist, '/robot/cmd_vel', 5) 
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        twist = Twist()
        
        self.publisher.publish(twist)
        
        
        
def main(args=None):
    rclpy.init(args=args)

    circling = CirclePublisher()

    rclpy.spin(circling)

    #circling.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
