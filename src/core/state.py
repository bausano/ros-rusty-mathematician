
class State:

  # @param dx The difference in distance on axis x in each tick
  # @param predicate The function to render
  def __init__(self, dx, predicate):
    self.dx = dx
    self.dxsq = dx * dx
    self.predicate = predicate

    # By default position on x axis is 0.
    self.x = 0
    # The initial state of the robot is perpetual to the x axis.
    self.delta = 0

  # Updates the position on x axis.
  def tick (self):
    self.x += self.dx
