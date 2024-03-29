from setuptools import setup

package_name = 'spearhead_code'

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
            	'thermistor_node = spearhead_code.thermistor:main',
                'flight_node = spearhead_code.flight_computer:main',
                'pitot_node = spearhead_code.pitot_node:main',
                'antenna_node = spearhead_code.antenna_node:main',
                'black_box_node = spearhead_code.black_box_node:main',
                'camera_node = spearhead_code.camera_node:main',
        ],
    },
)
