import math
import rospy
from geometry_msgs.msg import Twist

dx = 0.1
f = math.sin

_dxsq = dx * dx

def loop(pub, state):
  x = state['x']

  change = math.sqrt(
    _dxsq + math.pow(f(x + dx) + f(x), 2)
  )

  delta = math.acos(dx / change) - state['delta']

  print(delta)

  message = Twist()
  message.linear.x = change
  message.angular.z = delta

  pub.publish(message)

  state['delta'] = change
  state['x'] += dx

  print(state)

  return state

def move(message):
  vel_msg = Twist()

  #Receiveing the user's input
  print("Let's move your robot")
  speed = 2
  distance = 3
  isForward = True

  #Checking if the movement is forward or backwards
  if(isForward):
    vel_msg.linear.x = abs(speed)
  else:
    vel_msg.linear.x = -abs(speed)
  #Since we are moving just in x-axis
  vel_msg.linear.y = 0
  vel_msg.linear.z = 0
  vel_msg.angular.x = 0
  vel_msg.angular.y = 0
  vel_msg.angular.z = 0

  while not rospy.is_shutdown():
    #Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    #Loop to move the turtle in an specified distance
    while(current_distance < distance):
        #Publish the velocity
        #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        #Calculates distancePoseStamped
        current_distance= speed*(t1-t0)
    #After the loop, stops the robot
    vel_msg.linear.x = 0
    #Force the robot to stop
