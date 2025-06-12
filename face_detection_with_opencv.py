import cv2
'''#pretrained haarcascade detector
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('Bean.webp',1)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img,1.5, 7)
#print(faces)
for (x,y,w,h) in faces:
    #print(x,y,w,h)
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),5)
    cv2.putText(img, "Bean", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    #starting pixel co-ordinate,which is topleft,ending pixel coordinate,
    #color BGR tuple,thickness(negative will make solid)
resized = cv2.resize(img, (500,500))     
#cv2.imshow('img',img)
#cv2.imshow('img', resized)
cv2.imshow("Text", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Testing your camera
'''
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()


#Face Detection

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.2,
                                         minNeighbors=5,
                                         minSize=(20, 20))
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff #0xFF is a bit mask which sets the left 24 bits to zero, because ord() returns a value betwen 0 and 255,
                                #since your keyboard only has a limited character set
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
'''




