# Trig Functions ${name}er

Tutorial package for `turtlebot_sim`. This subscriber attempts to render given function of `x`.

## Installation
1. Install `ros` following the documentation ()[here].

2. Clone this package into your workspace. See tutorial on work spaces ()[here].

3. Build the package and make sure your `devel/setup.bash` is in your path variable.

## Usage
You have to boot ROS with `$ roscore` before you start working with ROS. Then run `$ rosrun turtlesim turtlesim_node` to boot the UI.
To run the package, use `$ rosrun ${name} main.py`.

### The Subscriber API
The method `tick` publishes a message to the node.
The first parameter is the change `dx` that should be done each tick.
In second parameter you specify what predicate should it use as a function of `x`.

## Screenshots
