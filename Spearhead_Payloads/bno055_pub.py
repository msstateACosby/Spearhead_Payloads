import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import board
import adafruit_bno055

class BNO055_Publisher(Node):
    def __init__(self):
        super().__init__('BNO055_Publisher')
        i2c = board.I2C()
        bno = adafruit_bno055.BNO055_I2C(i2c)
        timer_period = 0.01
    def timer_callback(self):
        msg = String()
        msg.data = f'linear accel: {self.bno.linear_acceleration} gyro: {self.bno.gyro}'
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    bno055_pub = BNO055_Publisher()
    rclpy.spin(bno055_pub)

    bno055_pub.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()