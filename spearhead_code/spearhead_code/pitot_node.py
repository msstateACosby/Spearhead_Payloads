from smbus import SMBus
import time
import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Pitot

PMAX = 58.02
PMIN = 0
O_MAX = .9 * pow(2,24)
O_MIN = .1 * pow(2, 24)

class Pitot_Node(Node):
    def __init__(self):
        super().__init('Pitot_Node')
        self.bus = SMBus(1)
        self.publisher = self.create_publisher(Pitot, 'Pitot', 20)
        timer_period = 20
        self.timer = self.create_timer(timer_period, self.timer_callback)
    def timer_callback(self):
        pitotbus.write_i2c_block_data(pitot_address, 0xAA, [0x00, 0x00])
        time.sleep(.005)
        data = pitotbus.read_i2c_block_data(pitot_address, 0x00, 4)
        press_value = data[3] + data[2] * 256 + data[1] * 65536
        message = Pitot()
        message.time = time.time()
        message.pressure =  (press_value - OMIN) * (PMAX - PMIN) / (0MAX - OMIN) + P_MIN)
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    pitot_node = Pitot_Node()
    rclpy.spin(flight_node)
    pitot_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
