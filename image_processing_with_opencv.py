'''
pip install opencv-contrib-python
pip install imutils
'''
#Reading images
import cv2
import imutils
#read the image
image = cv2.imread("Bean.webp")
#print(image) #outcome is a 3-D array -->h,w,d
#print(image.shape) #height,width,depth
#to show the image -->imshow
#cv2.imshow("Bean",image)
#use waitKey to make image to be displayed
#cv2.waitKey(1000) #milliseconds
#generally we keep waitKey(0) default
#cv2.waitKey(0) #Press Esc to close default
'''
img = cv2.imread("Bean.webp",0) #0-->grayscale(B/W)
cv2.imshow("Bean",img)
cv2.waitKey()

#cv2.cvtColor(src, code)

img = cv2.imread("Bean.webp")
img1=cv2.cvtColor(img,cv2.COLOR_RGB2YCrCb )
cv2.imshow("Newbean",img1)
cv2.waitKey()
'''
#Rotation -->imutils

img = cv2.imread("Bean.webp")
'''img1 = imutils.rotate(img,-45) #+ve anticlockwise
#-ve -->clockwise
cv2.imshow("RotatedBean",img1)
cv2.waitKey()
'''

#Multiple rotations
for angle in range(0, 360, 90):
    # rotate the image and display it
    rotated = imutils.rotate(img, angle=angle)
    cv2.imshow("Angle=%d" % (angle), rotated)
cv2.waitKey()










