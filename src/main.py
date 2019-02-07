#!/usr/bin/env python
import rospy
from loop import loop
from prepare import prepare
from geometry_msgs.msg import Twist

if __name__ == '__main__':
  try:
    # Starts a new node with a random hash appended to its name.
    rospy.init_node('trig_functions', anonymous=True)

    # Constructs a new publisher instance that emits messages to the turtle
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=50)

    # Draws x axis and then moves the turtle bot closer to the right edge.
    prepare(pub)

    # Constructs a new rate object on current thread that is used for publishing
    # frequency. There is maximally one message published per tick.
    thread = rospy.Rate(1)

    # State dictionary.
    state = {
      'x': 0,
      'delta': 0,
    }

    # Creates loop that does not exit unless the core was shut down.
    while not rospy.is_shutdown():
      state = loop(pub, state)

      thread.sleep()

  except rospy.ROSInterruptException:
    print('Connection to ROS interrupted.')
