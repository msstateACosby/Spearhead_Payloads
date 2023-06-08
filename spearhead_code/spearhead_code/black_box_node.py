import rclpy
from rclpy.node import Node
from spearhead_msgs.msg import Thermistors, FlightComputer, Pitot
import time
from datetime import datetime
import csv

# get actual path
BLACK_BOX_PATH = '/media/usb/'


class Black_Box_Node(Node):
    def __init__(self):
        super().__init__('Black_Box_Node')

        # callbacks to recieve data from individual payloads
        self.temp_subscription = self.create_subscription(
            Thermistors,
            'Thermistors',
            self.temp_callback,
            20
        )
        self.flight_com_subscription = self.create_subscription(
            FlightComputer,
            'FlightComputer',
            self.flight_com_callback,
            20
        )
        self.pitot_subscription = self.create_subscription(
            Pitot,
            'Pitot',
            self.pitot_callback,
            20
        )
        #
        timer_period = 10
        self.save_timer = self.create_timer(timer_period, self.save_data)

        self.therm_writer = open(BLACK_BOX_PATH + datetime.now().strftime(
            "temp_%m_%d_%H_%M_%S.csv"), 'w')
        self.therm_writer = csv.writer(self.temp_file)
        self.therm_writer.writerow(
            ['Time'] + ['Outside Temp ' + x for x in range(1, 8)] + ['Internal_Temp'])
        self.flight_com_file = open(BLACK_BOX_PATH+datetime.now().strftime(
            "flight_com_%m_%d_%H_%M_%S.csv"), 'w')
        self.flight_com_writer = csv.writer(self.flight_com_file)
        self.flight_com_writer.writerow(['Time', 'BMP Altitude', 'GPS Altitude', 'Internal Pressure', 'Acceleration X', 'Acceleration Y', 'Acceleration Z', 'Linear Accel X', 'Linear Accel Y',
                                        'Linear Accel Z', 'Gravity X', 'Gravity Y', 'Gravity Z', 'Angular Vel X', 'Angular Vel Y', 'Angular Vel Z', 'Quaternion X', 'Quaternion Y', 'Quaternion Z', 'Quaternion i'])

        self.pitot_file = self.therm_writer = open(BLACK_BOX_PATH+datetime.now().strftime(
            "pitot_%m_%d_%H_%M_%S.csv"), 'w')
        self.pitot_writer = csv.writer(self.pitot_file)
        self.pitot_writer.writerow(
            ['Time', 'Static Pressure', 'Dyanmic Pressure'])

    def temp_callback(self, msg):
        self.therm_writer.writerow(
            [msg.time] + msg.surface_temps + [msg.internal_temp])
        # add code to write data to csv

    def flight_com_callback(self, msg):

        self.flight_com_writer.writerow([msg.time, msg.bmp_altitude, msg.gps_altitude, msg.internal_pressure] +
                                        msg.acceleration+msg.linear_acceleration+msg.gravity+msg.angular_velocity+msg.quaternion_orientaion)
        # add code to write data to csv

    def pitot_callback(self, msg):
        self.pitot_writer.writerow(
            [msg.time, msg.static_pressure, msg.dynamic_pressure])

    def save_data(self):
        self.therm_file.flush()
        self.flight_com_file.flush()
        self.pitot_file.flush()

    def destroy_node(self):
        self.temp_file.close()
        self.flight_com_file.close()
        self.pitot_file.close()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    black_box_node = Black_Box_Node()
    rclpy.spin(black_box_node)

    black_box_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
