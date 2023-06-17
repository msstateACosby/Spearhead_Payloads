import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import FlightComputer
import time
import board
import busio
import adafruit_bno055 as BNO
import adafruit_bmp3xx as BMP
import adafruit_gps as GPS
import serial

import math


class Flight_Node(Node):
    def __init__(self):
        super().__init__('Flight_Node')
        i2c = busio.I2C(board.SCL, board.SDA)
        self.bno = BNO.BNO055_I2C(i2c, address=0x29)
        self.bmp = BMP.BMP3XX_I2C(i2c)
        uart = serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)
        # uart = serial.Serial("/dev/tty1",baudrate=115200,timeout=10) #might have to use this line for UART instead of the above line
        self.gps = GPS.GPS(uart, debug=False)
        self.gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
        self.gps.send_command(b"PMTK220,100")

        self.publisher = self.create_publisher(
            FlightComputer, 'FlightComputer', 20)
        timer_period = .05
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        self.gps.update()
        msg = FlightComputer()
        msg.time = time.time()
        msg.gravity = list(self.bno.gravity)
        msg.acceleration = list(self.bno.acceleration)
        msg.linear_acceleration = list(self.bno.linear_acceleration)
        msg.quaternion_orientation = list(self.bno.quaternion)
        msg.angular_velocity = list(self.bno.gyro)
        msg.bmp_altitude = self.bmp.altitude
        msg.internal_pressure = self.bmp.pressure
        if (self.gps.has_fix):
            msg.gps_altitude = self.gps.altitude_m
        else:
            msg.gps_altitude = -1.0
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    flight_node = Flight_Node()
    rclpy.spin(flight_node)

    flight_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
