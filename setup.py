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
        	'bmp_pub_example = Spearhead_Payloads.bmp_pub_example:main',
        	'gps_pub_example = Spearhead_Payloads.gps_pub_example:main',
        ],
    },
)