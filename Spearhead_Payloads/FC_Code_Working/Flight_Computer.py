### SC Flight computer code
# Draft version, written by Alexander Ketzle
import storage
import time

### INIT SECTION: BRING IN ROS2 INPUTS HERE
# BEFORE THESE CLASSES, ALL SENSORS ARE INITIALIZED AND READY TO SEND DATA
class BNO055:
    gravity = (0,0,0) #TODO: GET ROS2 INPUT
    acceleration = (0,0,0) #TODO: GET ROS2 INPUT
    linear_acceleration = (0,0,0) #TODO: GET ROS2 INPUT
class BMP388:
    altitude = 0 #TODO: GET ROS2 INPUT
# class GPS: #TODO: FLESH OUT DATA GRABBED

arm_state = 0
storage.remount("/",False)
log_file = open(f"/{time.time()}_flight_data.csv","x")
log_file.write("timestamp,altitude,linear acceleration,gravity,acceleration\n")
print(f"{log_file.name} created. Standby for launch")
arm_state = 1
zeroTime = time.monotonic()
timestamp = 0
while arm_state == 1:
    if mag(BNO055.linear_acceleration) >= 10 and BMP388.altitude >= 5:
        zeroTime = time.monotonic()
        timestamp = time.monotonic - zeroTime
        log_file.write(f"{timestamp},{BMP388.altitude:.2f},{BNO055.linear_acceleration:.2f},{BNO055.gravity:.2f},{BNO055.acceleration:.2f}\n")
        arm_state = 2
while arm_state == 2:
    if time.monotonic-zeroTime-timestamp >= 10:
        timestamp = time.monotonic-zeroTime
        log_file.write(f"{timestamp},{BMP388.altitude:.2f},{BNO055.linear_acceleration:.2f},{BNO055.gravity:.2f},{BNO055.acceleration:.2f}\n")
    if timestamp >= 1800000: # 30 minutes of flight time. Use this as a failsafe in addition to landing detection methods
        arm_state = 3
while arm_state == 3:
    print(f"Closing {log_file.name}")
    log_file.close()
    print("File closed")
    arm_state = 4