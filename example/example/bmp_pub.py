import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BMP_Publisher(Node):
    def __init__(self):
        super().__init__('BMP_Publisher')
        self.publisher = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World'
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    bmp_pub = BMP_Publisher()
    rclpy.spin(bmp_pub)
    

    bmp_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        
