import math
import rospy
from geometry_msgs.msg import Twist

def prepare(pub):
  # Size of the field the robot is in divided by two.
  r = 5

  # Moves the turtle forward, drawing one half of the x axis.
  move(pub, r, 2)
  # Moves the turtle backwards twice the length, putting it to the left edge.
  move(pub, 2 * r, -2)

def move(pub, distance, speed):
  message = Twist()
  message.linear.x = speed

  while not rospy.is_shutdown():
    traveled = 0
    t0 = rospy.Time.now().to_sec()

    while (math.fabs(traveled) < distance):
      pub.publish(message)

      t1 = rospy.Time.now().to_sec()
      traveled = speed * (t1 - t0)

    message.linear.x = 0
    pub.publish(message)

    break
