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

  pub.publish(message)

  state['delta'] = delta
  state['x'] += dx

  return state

