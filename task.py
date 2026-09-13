import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance_node')
        
        # Publisher to send movement commands to the robot's wheels
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscriber to listen to the front distance sensor
        self.subscription = self.create_subscription(
            Float32,
            '/distance',
            self.sensor_callback,
            10
        )
        
        self.current_distance = 5.0  # Start with a safe default value
        self.safe_distance = 1.0     # Obstacle threshold in meters
        
        # Timer to run the control loop at 10 times per second (10 Hz)
        self.timer = self.create_timer(0.1, self.control_loop)

    def sensor_callback(self, msg):
        # Step 1: SENSE - Update the current distance whenever a new message arrives
        self.current_distance = msg.data

    def control_loop(self):
        msg = Twist()
        
        # Step 2: DECIDE
        if self.current_distance > self.safe_distance:
            # Step 3: ACT (Path is clear -> Move Forward)
            msg.linear.x = 0.5  # Move forward speed
            msg.angular.z = 0.0 # No turning
        else:
            # Step 3: ACT (Obstacle detected -> Stop and Turn)
            msg.linear.x = 0.0  # Stop moving forward
            msg.angular.z = 1.0 # Turn around to avoid obstacle
            
        # Send the command to the robot
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()