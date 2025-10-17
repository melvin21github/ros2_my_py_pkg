from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_py_pkg',
            executable='talker',
            name='my_publisher',
            output='screen'
        ),
        Node(
            package='my_py_pkg',
            executable='listener',
            name='my_subscriber',
            output='screen'
        )
    ])

