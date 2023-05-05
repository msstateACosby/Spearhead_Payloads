port rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Thermistors
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


import math


def voltage_to_temp(voltage, static_r, ref_v):
    resistance = (static_r * ref_v)/ (ref_v-voltage)
    temperature = 1.0/25.0 + 1.0/3380.0*math.log(resistance/10_000.0)
    return temperature

class Thermistor_Node(Node):
    def __init__(self):
        super().__init__('Thermistor_Node')
        i2c = busio.I2C(board.SCL, board.SDA)
        ads_0 = ADS.ADS1115(i2c, address = 0x48)
        ads_1 = ADS.ADS1115(i2c, address = 0x4A)
        
        self.publisher = self.create_publisher(Thermistors, 'thermistors', 20)
        timer_period = .05
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.inputs = [
            AnalogIn(ads_0, ADS.P0),
            AnalogIn(ads_0, ADS.P1),
            AnalogIn(ads_0, ADS.P2),
            AnalogIn(ads_0, ADS.P3),

            AnalogIn(ads_1, ADS.P0),
            AnalogIn(ads_1, ADS.P1),
            AnalogIn(ads_1, ADS.P2),
        ]

        self.internal = AnalogIn(ads_1, ADS.P3)
        

    def timer_callback(self):
        temps = []
        for reading in self.inputs:
            temps.append(voltage_to_temp(reading.voltage,1_000,3.3))
        msg = Thermistors()
        msg.time = time.time()
        msg.surface_temps = temps
        msg.internal_temp = voltage_to_temp(self.internal.voltage,1_000,3.3)
        self.publisher.publish(msg)
    


def main(args=None):
    rclpy.init(args=args)
    therm_node = Thermistor_Node()
    rclpy.spin(therm_node)

    therm_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
