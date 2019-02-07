import math
import rospy
from geometry_msgs.msg import Twist

# Main program loop that calculates the changes in between the ticks.
#
# @param pub Publisher instance to send message with
# @param state State of the program
def loop(pub, state):
  x = state.x
  f = state.predicate

  # Calculates the change on axis y.
  dy = f(x + state.dx) - f(x)

  # Calculates the hypotenuse of the dx dy right triangle.
  change = math.sqrt(state.dxsq + math.pow(dy, 2))

  # The between dx and hypotenuse.
  delta = math.asin(dy / change)

  message = Twist()
  message.linear.x = change
  # The difference between new delta and old delta is the
  # angle the robot to turns by.
  message.angular.z = delta - state.delta

  pub.publish(message)

  # Update the state.
  state.tick()
  state.delta = delta
