import rclpy
from rclpy.node import Node
from datetime import datetime
import cv2

BLACK_BOX_PATH = '~/usb/'


class Camera_Node(Node):
    def __init__(self):
        super().__init__('Camera_Node')
        self.cap = cv2.VideoCapture(-1, cv2.CAP_V4L)

        fourcc = cv2.VideoWriter_fourcc(*'X264')
        self.out = cv2.VideoWriter(BLACK_BOX_PATH + datetime.now().strftime(
            "flight_com_%m_%d_%H_%M_%S.mkv"), fourcc, 20, (1280, 720))
        timer_period = 1.0/60.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        ret, frame = self.cap.read()
        self.out.write(frame)

    def destroy_node(self):
        self.cap.release()
        self.out.release()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    camera_node = Camera_Node()
    rclpy.spin(camera_node)

    camera_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
