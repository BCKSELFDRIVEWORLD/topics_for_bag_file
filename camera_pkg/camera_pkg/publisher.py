import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, CameraInfo
from sensor_msgs.msg import PointCloud2  
from nav_msgs.msg import Odometry  
from sensor_msgs.msg import Imu  
from tf2_msgs.msg import TFMessage

class ImagePublisherNode(Node):
    def __init__(self):
        super().__init__('publisher')
        self.infra1_image_publisher = self.create_publisher(Image, '/camera/infra1/image_rect_raw', 10)
        self.infra2_image_publisher = self.create_publisher(Image, '/camera/infra2/image_rect_raw', 10)
        self.infra1_camera_info_publisher = self.create_publisher(CameraInfo, '/camera/infra1/camera_info', 10)
        self.infra2_camera_info_publisher = self.create_publisher(CameraInfo, '/camera/infra2/camera_info', 10)
        self.scan1_publisher = self.create_publisher(PointCloud2, '/scan1', 10) 
        self.scan2_publisher = self.create_publisher(PointCloud2, '/scan2', 10)  
        #self.combined_scan_publisher = self.create_publisher(PointCloud2, '/combined_scan', 10) 
        self.odom_subscription = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)  
        #self.imu_publisher = self.create_publisher(Imu, '/imu', 10)  
        self.camera_imu_publisher = self.create_publisher(Imu, '/camera/imu', 10) 
        self.tf_publisher = self.create_publisher(TFMessage, '/tf', 10)  
        self.tf_static_publisher = self.create_publisher(TFMessage, '/tf_static', 10)  


    def odom_callback(self, msg):
        self.get_logger().info(f'Received Odometry Data: {msg}')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
