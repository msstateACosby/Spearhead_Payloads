import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import board
import adafruit_bmp3xx
class BMP388_Publisher(Node):
    def __init__(self):
        super().__init__('BMP388_Publisher')
        i2c = board.I2C()
        bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
        timer_period = 0.01
    def timer_callback(self):
        msg = String()
        msg.data = f'Alt (m): {self.bmp.altitude} Pressure: {self.bmp.pressure}'
        self.publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    bmp388_pub = BMP388_Publisher()
    rclpy.spin(bmp388_pub)

    bmp388_pub.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()