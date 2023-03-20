import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Temperatures, Kalman_Values
import time
import board
import busio




class Antenna_Node(Node):
    def __init__(self):
        super().__init__('Antenna_Node')

        self.temp_subscription = self.create_subscription(
            Temperatures,
            'temperatures',
            self.temp_callback,
            20
        )
        self.kalman_callback = self.create_subscription(
            Kalman_Values,
            'kalman_values',
            self.temp_callback,
            20
        )
        self.start_time = time.time()
    
    def temp_callback(self, msg):

        pass

    def kalman_callback(self, msg):

        pass

    def record_data(self):
        curr_time = time.time()-self.start_time()
        


def main(args=None):
    rclpy.init(args=args)
    antenna_node = Antenna_Node()
    rclpy.spin(antenna_node)

    antenna_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()