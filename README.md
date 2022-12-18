# opencv_curve_tracer

## Installation

### ROS and Catkin_ws 
- ROS noetic : Refer to the [official documentation](http://wiki.ros.org/noetic/Installation/Ubuntu) for installation of ROS noetic.
               
- Catkin workspace : A catkin workspace is a folder where you modify, build, and. install catkin packages. Take a look at the [official documentation](http://wiki.ros.org/catkin/Tutorials/create_a_workspace) for instructions regarding creation of a catkin workspace

### Installation of Virtualenvwrapper, OpenCV, and CV_bridge
Your can refer to [A.T.O.M's_wiki](https://atom-robotics-lab.github.io/wiki/setup/virtualenv.html) for installation of the above mentioned packages and libraries.

### Turtlesim
Your can refer to [Turtlesim_official_wiki](http://wiki.ros.org/turtlesim) for installation of the above mentioned packages and libraries.

## Clone the OpenCV_curve_Trace
Now go ahead and clone this repository inside the "src" folder of the catkin workspace you just created by executing the command given below in your terminal.
```bash
git@github.com:krrish-jindal/opencv_curve_tracer.git
```
__Make the package__
We'll need to "make" everything in our catkin workspace so that the ROS environment knows about our new package.  (This will also compile any necessary code in the package). Execute the given commands in your terminal.

```bash
cd ~/catkin_ws
catkin_make
```

## Launch Files
```bash
roscore
```
```bash
rosrun turtlesim turtlesim_node
```
```bash
rosrun turtle turtle_curve.py 
```
<img src = "https://github.com/krrish-jindal/opencv_curve_tracer/blob/origin/Assets/curve_tracer.gif" >
