import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Temperatures,Kalman_Values
import time
import datetime
import csv

class Black_Box_Node(Node):
    def __init__(self):
        super().__init__('Black_Box_Node')

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
        self.datafile = open(datetime.now().strftime("data_%m_%d_%H_%M_%S.csv"), 'w')
        self.writer = csv.writer(self.datafile)
        
    def temp_callback(self, msg):

        pass

    def kalman_callback(self, msg):

        pass

    def record_data(self):
        curr_time = time.time()-self.start_time()
    
    def destroy_node(self):
        self.datafile.close()
        super().destroy_node()


    
def main(args=None):
    rclpy.init(args=args)
    black_box_node = Black_Box_Node()
    rclpy.spin(black_box_node)

    black_box_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




