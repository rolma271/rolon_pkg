from setuptools import find_packages, setup

package_name = 'rolon_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/rosbag_visualization.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/r2b_robotarm.rviz']),
        ('share/' + package_name + '/rqt', ['rqt/r2b_robotarm.perspective']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marco',
    maintainer_email='rolma271@gmail.com',
    description='Visualización del rosbag del brazo robótico NVIDIA R2B',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
