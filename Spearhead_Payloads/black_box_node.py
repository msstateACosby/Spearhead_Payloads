import rclpy
from rclpy.node import Node
#from spearhead_msgs.msg import Temperatures,Flight_Com_Data
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
        self.flight_com_subscription = self.create_subscription(
            Flight_Com_Data,
            'kalman_values',
            self.flight_com_data_callback,
            20
        )
        #
        timer_period = 10
        self.save_timer = self.create_timer(timer_period, self.save_data)

        self.start_time = time.time()
        self.temp_file = open(datetime.now().strftime("temp_%m_%d_%H_%M_%S.csv"), 'w')
        self.temp_writer = csv.writer(self.temp_file)
        self.flight_com_file = open(datetime.now().strftime("flight_com_%m_%d_%H_%M_%S.csv"), 'w')
        self.flight_com_writer = csv.writer(self.flight_com_file)
        self.temperatures = Temperatures()
        self.flight_com_data = Flight_Com_Data()
        
    def temp_callback(self, msg):
        self.temperatures = msg
        #add code to write data to csv

    def flight_com_data_callback(self, msg):
        self.flight_com_data = msg
        #add code to write data to csv
    
    def save_data(self):
        self.tempfile.flush()
        self.flight_com_file.flush()
    
    def destroy_node(self):
        self.temp_file.close()
        self.flight_com_file.close()
        super().destroy_node()




    
def main(args=None):
    rclpy.init(args=args)
    black_box_node = Black_Box_Node()
    rclpy.spin(black_box_node)

    black_box_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




