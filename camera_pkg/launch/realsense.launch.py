from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="camera_pkg",
            executable="my_publisher",
            output="screen"
        ),

    ])