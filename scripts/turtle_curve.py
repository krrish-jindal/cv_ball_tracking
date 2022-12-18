#! /usr/bin/env python3

import numpy as np
import cv2
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from turtlesim.srv import Spawn
import math
from geometry_msgs.msg import PoseStamped


def pose_callback(pose):

   global my_X, my_Y ,my_theta
   rospy.loginfo("Robot X = %f: Robot Y=%f\n",pose.x,pose.y)
   my_X = round(pose.x,2)
   my_Y = round(pose.y,2)
   my_theta=round(pose.theta,3)

def map_range(x, in_min, in_max, out_min, out_max):
  return ((x - in_min) * (out_max - out_min) /(in_max - in_min)) + out_min

def main():
	global my_X
	rospy.init_node('move_turtle', anonymous=True)
	pose_pub = rospy.Publisher("/turtle/move_pose",PoseStamped,queue_size=10)

	image_pub = rospy.Publisher("/image/ball_animation",Image)

	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
	bridge = CvBridge()


	vel = Twist()

	global x,y
	global a
	global img
	global b
	global image_message
	rospy.Rate(20)

	while not rospy.is_shutdown():

		cv2.waitKey(15)
		m=[]
		n=[]
		mn=[]
		a=np.linspace(100, 400, 150)
		x_1 = a
		y_1=-(((x_1-250)*np.sqrt(150-abs(x_1-250)))/10)+250
		b=np.linspace(400, 100, 150)
		x_2=b	
		y_2=(((x_2-250)*np.sqrt(150-abs(x_2-250)))/10)+250
		
		x_1=x_1.astype(int)
		y_1=y_1.astype(int)
		x_2=x_2.astype(int)
		y_2=y_2.astype(int)
		n=list(zip(x_2,y_2))
		m= list(zip(x_1,y_1))
		mn=m+n

			
		b=0

		for j in mn:
			img = np.zeros((500,500,3),np.uint8)
			img.fill(255)



			cv2.waitKey(5)
			# print("=====",map_range(500,0,500,11.088,0))


			cv2.circle(img,(j[0],j[1]),20,(0,255,0),-10)
			cv2.circle(img,(j[0],j[1]),20,(0,0,0),2)

			cv2.waitKey(10)
			x=map_range(j[0],0,500,11.088,0)
			y=map_range(j[1],0,500,11.088,0)
			pose = PoseStamped()
			pose.pose.position.x=x
			pose.pose.position.y=y

			print(x,"@@@@@@@",y)
			cv2.putText(img, "radians = " + str(mn[b]), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 2)
			cv2.imshow("a",img)
			b=b+1

			# print("------------",mn)
			dis_error=np.sqrt((x-my_X)**2+(y-my_Y)**2)
			dis_x= math.cos(my_theta)*(x-my_X) + math.sin(my_theta)*(y-my_Y)
			dis_y= -math.sin(my_theta)*(x-my_X) + math.cos(my_theta)*(y-my_Y)
			dis_theta=math.atan(y/x)-my_theta
			
			desire_theta=math.atan2(dis_y,dis_x)

			

			vel.linear.x=dis_x
			vel.linear.y=dis_y
			vel.angular.z=(desire_theta-my_theta)*10
			pub.publish(vel)
			image_message = bridge.cv2_to_imgmsg(img, encoding="passthrough")
			pose_pub.publish(pose)
			image_pub.publish(image_message)
			if cv2.waitKey(1) == 27:

				break
			# cv2.destroyAllWindows()


		# if cv2.waitKey(1) == 27:
			# break
	cv2.destroyAllWindows()
main()
