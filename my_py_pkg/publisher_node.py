import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Standard message type

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')  # Node name
        # Create publisher on topic 'chatter', queue size 10
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.publish_message)  # Publish every 1 sec
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f"Hello ROS2: {self.count}"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = SimplePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

#Key Concepts:
#create_publisher() – sets the topic and message type.
#create_timer() – calls a function periodically.
#get_logger().info() – prints info to terminal.
#String() – message object.