import rclpy
from rclpy.node import Node
#from spearhead_msgs.msg import Temperatures, Flight_Com_Data
import time
import board
import busio
import digitalio

import adafruit_rfm9x



class Antenna_Node(Node):
    def __init__(self):
        
        super().__init__('Antenna_Node')
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO = board.MISO)
        cs = digitalio.DigitalInOut(board.D17)
        reset = digitalio.DigitalInOut(board.D22)
        self.rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
        

        '''
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
        '''
        #
        timer_period = .05
        self.send_data = self.create_timer(timer_period, self.send_data)

        self.start_time = time.time()
        self.packet_num = 0
        
        
        #self.temperatures = Temperatures()
        #self.flight_com_data = Flight_Com_Data()
        self.start_time = time.time()
        
    def temp_callback(self, msg):
        self.temperatures = msg
        #add code to write data to csv

    def flight_com_data_callback(self, msg):
        self.flight_com_data = msg
        #add code to write data to csv
        
    def send_data(self):
        #each packet starts with a packet num between 0 and 9 (one byte string) and the time since program start
        #because of floats the time could be anywhere from 4 characters (x.xx) to around 9 characters realisticly
        # we have about 240 numbers left to send
        curr_time = time.time() - self.time()
        data_string = f'{self.packet_num} {curr_time:.2f}'
        self.packet_num = (self.packet_num + 1) % 10
        #add code to convert messages into string
        self.rfm9x.send(data_string.encode('utf-8'))
        
def main(args=None):
    rclpy.init(args=args)
    antenna_node = Antenna_Node()
    rclpy.spin(antenna_node)

    antenna_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
