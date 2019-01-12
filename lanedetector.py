import numpy as np 
import matplotlib.pyplot as plt 
import cv2

class lanefinder:
	def __init__(self):
		pass
	
	def showpredict(self,img,lines):
		for line in lines:
			x1,y1,x2,y2=line
			cv2.line(img,(x1,y1),(x2,y2),[255,0,0],10)
		cv2.imshow("dashboard",img)

	def create_filter_img(self,img):
		imgflt=np.zeros_like(img)
		triangle_filter=np.array([(250,700),(590,310),(1100,700)])
		cv2.fillPoly(imgflt,[triangle_filter],[255,255,255])
		img=cv2.bitwise_and(img,imgflt)
		return img
	
	def linenormalizer(self,lines):
		leftlane=[]
		rightlane=[]
		for line in lines:
			x1,y1,x2,y2=line[0]
			slope,intercept=np.polyfit((x1,x2),(y1,y2),1)
			if slope<0:
				leftlane.append(np.array([slope,intercept]))
			else:
				rightlane.append(np.array([slope,intercept]))
		lines=self.getaverage([leftlane,rightlane])
		return lines
	
	def getaverage(self,lines):
		ln=[]
		for line in lines:
			if(line!=[]):
				x,y=np.average(line,axis=0)
				ln.append([int((400-y)/x),400,int((700-y)/x),700])
		return ln

	def findlane(self,image):
		imgorg=np.copy(image)
		img=cv2.cvtColor(imgorg,cv2.COLOR_RGB2GRAY)
		img=cv2.Canny(img,50,150)
		img=self.create_filter_img(img)
		lines=cv2.HoughLinesP(img,2,np.pi/180,100,np.array([]),minLineLength=20,maxLineGap=5032)
		lines=self.linenormalizer(lines)
		self.showpredict(imgorg,lines)


lanedetector=lanefinder()
cap=cv2.VideoCapture("road.mp4")
while(cap.isOpened()):
	_,frame=cap.read()
	lanedetector.findlane(frame)
	key=cv2.waitKey(1)
	if key==27:
		break