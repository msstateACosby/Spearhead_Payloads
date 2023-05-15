import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time
import board
import busio
import adafruit_gps
import serial


class GPS_Publisher(Node):
    def __init__(self):
        #hey i made some changes because i could
        super().__init__('GPS_Publisher')
        uart = serial.Serial("/dev/tty1",baudrate=115200,timeout=10)
        self.publisher = self.create_publisher(String, 'gps_data', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.gps = adafruit_gps.GPS(uart, debug=False)
        self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
        self.gps.send_command(b"PMTK220,500")
        

    def timer_callback(self):
        self.gps.update()
        msg = String()
        msg.data = f'{self.gps.has_fix} {self.gps.altitude_m}'

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    gps_pub = GPS_Publisher()
    rclpy.spin(gps_pub)
    

    gps_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        
