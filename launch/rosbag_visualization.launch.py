from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    pkg_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    bag_path = '/home/marco/Desktop/cese/frros_ws/r2bdataset2024_v1/r2b_robotarm' #os.path.join(pkg_path, '..', 'r2bdataset2024_v1', 'r2b_robotarm')
    rviz_path = os.path.join(pkg_path, 'rviz', 'r2b_robotarm.rviz')
    rqt_path = os.path.join(pkg_path, 'rqt', 'r2b_robotarm.perspective')

    return LaunchDescription([
        # Reproducir el rosbag
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', bag_path],
            output='screen'
        ),

        # Lanzar RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_path],
            output='screen'
        ),

        # Lanzar RQT
        ExecuteProcess(
            cmd=['rqt', '--perspective-file', rqt_path],
            output='screen'
        )
    ])
