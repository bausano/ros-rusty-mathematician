import math
import rospy
from geometry_msgs.msg import Twist

dx = math.pi / 4
f = math.sin

_dxsq = dx * dx

def loop(pub, state):
  x = state['x']

  dy = f(x + dx) - f(x)

  change = math.sqrt(_dxsq + math.pow(dy, 2))

  delta = math.asin(dy / change)

  message = Twist()
  message.linear.x = change
  message.angular.z = delta - state['delta']

  print(delta, state['delta'], message.angular.z)

  pub.publish(message)

  state['delta'] = delta
  state['x'] += dx

  return state

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
