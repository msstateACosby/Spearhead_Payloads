# Spearhead Payloads

This is the github repo for all of the (onboard) payload software going on Spearhead. ROS 2 is being used to assist development by providing a communication scheme for payload code files to interact with each other. 

## Dependencies
* ROS 2
* CircuitPython
* {NEED TO ADD THE REST}

## Installing the package
Navigate to ~/ros2_ws/src and clone this repository.

## Building the Package
On a raspberry pi that has ROS 2 and this package installed run the following commands in ~/ros2_ws

```
colcon build
. install/setup.bash
```
 
Yes, that is period in that second line.

## Running the GPS example
Anywhere after building on the pi:

```
ros2 run Spearhead_Payloads gps_pub_example
```

Nothing will happen and the terminal will lock up! This is intentional, this means the program is running.
In another terminal, run the follwowing command:

```
ros2 topic echo /gps_data
```

This will print out the gps data.

## To add/edit python files
All python files will exist in ~/ros2_ws/src/Spearhead_Payloads/spearhead_code/spearhead_code/.
[Here](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html) shows how to write two basic nodes for publishers and subscribers.

Following that guide, one can ignore package creation as we already have a package, and is primarily useful for the actual code in the file.
After writing your file, you will also have to add the following line to the 'console_scripts' list in setup.py in the root directory of this repo.
Add the following line, (with modifications relevant to your code marked by {}):

```
'{file_name} = spearhead_code.{file_name}:main'
```

After editing your file and/or setup.py build the package again.
Run your file with

```
ros2 run spearhead_code {file_name}
```






