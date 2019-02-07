import math
import rospy
from geometry_msgs.msg import Twist

# TODO: Move this out to a class.
dx = math.pi / 4
f = math.sin

_dxsq = dx * dx

# Main program loop that calculates the changes in between the ticks.
#
# @param pub Publisher instance to send message with
# @param state State of the program
def loop(pub, state):
  x = state['x']

  # Calculates the change on axis y.
  dy = f(x + dx) - f(x)

  # Calculates the hypotenuse of the dx dy right triangle.
  change = math.sqrt(_dxsq + math.pow(dy, 2))

  # The between dx and hypotenuse.
  delta = math.asin(dy / change)

  message = Twist()
  message.linear.x = change
  # The difference between new delta and old delta is the
  # angle the robot to turns by.
  message.angular.z = delta - state['delta']

  pub.publish(message)

  # Save new state.
  state['delta'] = delta
  state['x'] += dx

  return state

