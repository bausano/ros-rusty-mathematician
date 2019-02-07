#!/usr/bin/env python

import math
import rospy
from core.prepare import prepare
from geometry_msgs.msg import Twist
from core.subscriber import Subscriber

# ROS Boot.
if __name__ == '__main__':
  # Starts a new node with a random hash appended to its name.
  rospy.init_node('trig_functions', anonymous=True)

  # Constructs a new publisher instance that emits messages to the turtle
  pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=50)

  # Draws x axis and then moves the turtle bot closer to the right edge.
  prepare(pub)

  # Constructs a new rate object on current thread that is used for publishing
  # frequency. There is maximally one message published per tick.
  thread = rospy.Rate(1)

  # Subscriber instance.
  subscriber = Subscriber(pub)

  # Creates loop that does not exit unless the core was shut down.
  while not rospy.is_shutdown():
    subscriber.tick(
      math.pi / 12,
      math.sin
      # lambda x: x*x
    )

    # Mimics frequency functionality.
    thread.sleep()
