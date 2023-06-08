from smbus import SMBus
import time
import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Pitot, FlightComputer

PMAX = 58.02
PMIN = 0
OMAX = .9 * pow(2, 24)
OMIN = .1 * pow(2, 24)
PITOT_ADDRESS = 0x28


class Pitot_Node(Node):
    def __init__(self):
        super().__init('Pitot_Node')
        self.bus = SMBus(1)
        self.publisher = self.create_publisher(Pitot, 'Pitot', 20)
        timer_period = 20
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.flight_com_subscription = self.create_subscription(
            FlightComputer,
            'FlightComputer',
            self.flight_com_data_callback,
            20
        )
        self.current_static_pressure = -1

    def timer_callback(self):
        self.bus.write_i2c_block_data(PITOT_ADDRESS, 0xAA, [0x00, 0x00])
        time.sleep(.005)
        data = self.bus.read_i2c_block_data(PITOT_ADDRESS, 0x00, 4)
        press_value = data[3] + data[2] * 256 + data[1] * 65536
        message = Pitot()
        message.time = time.time()
        message.static_pressure = self.current_static_pressure
        message.dynamic_pressure = (press_value - OMIN) * \
            (PMAX - PMIN) / (OMAX - OMIN) + PMIN
        self.publisher.publish(message)

    def flight_com_data_callback(self, msg):
        self.current_static_pressure = msg.internal_pressure


def main(args=None):
    rclpy.init(args=args)
    pitot_node = Pitot_Node()
    rclpy.spin(pitot_node)
    pitot_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
