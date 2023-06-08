import rclpy
from rclpy.node import Node
from datetime import datetime
import cv2

BLACK_BOX_PATH = '/media/usb'


class Camera_Node(Node):
    def __init__(self):
        super().__init__('Camera_Node')
        self.cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        fourcc = cv2.VideoWriter_fourcc(*'H264')
        self.out = cv2.VideoWriter(BLACK_BOX_PATH + datetime.now().strftime(
            "flight_com_%m_%d_%H_%M_%S.h264"), fourcc, 20, (1280, 720))
        timer_period = 1.0/60.0
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        ret, frame = self.cap.read()
        self.out.write(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))

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
