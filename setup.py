from setuptools import setup

package_name = 'Spearhead_Payloads'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='akc369@msstate.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'bmp388_pub = Spearhead_Payloads.bmp388_pub:main',
            'bno055_pub = Spearhead_Payloads.bno055_pub:main',
        	'gps_pub_example = Spearhead_Payloads.gps_pub_example:main',
            'antenna_node = Spearhead_Payloads.antenna_node:main',
            'black_box_node = Spearhead_Payloads.black_box_node:main',
            'camera_node = Spearhead_Payloads.camera_node:main',
            'thermistor_node = Spearhead_Payloads.thermistor:main',
        ],
    },
)
