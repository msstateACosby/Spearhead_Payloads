import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import board
import adafruit_bno055

class BNO055_Publisher(Node):

    def __init__(self):
        super().__init__('BNO055_Publisher')
        self.publisher = self.create_publisher(String, 'IMU', 10)
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        i2c = board.I2C()
        bno = adafruit_bno055.BNO055_I2C(i2c)
    def timer_callback(self):
        msg = String()
        msg.data = f'linear accel: {self.bno.linear_acceleration} gyro: {self.bno.gyro}'
        self.publisher_.publish(msg)
        self.get_logger().info('IMU DATA:')
def main(args=None):
    rclpy.init(args=args)
    bno055_pub = BNO055_Publisher()
    rclpy.spin(bno055_pub)
    bno055_pub.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()
