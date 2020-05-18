import cv2
import numpy as np
import math
distance1 = 0.0
distance2=  0.0
result=0.0
font = cv2.FONT_HERSHEY_SIMPLEX

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8\\trainer2\\trainingData2.yml")
cascadePath = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.8\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
#font = cv2.Font(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 255, 255)
while True:
    ret, im =cam.read()
    frame = cv2.resize(im, (0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        distancei = (2*3.14 * 180)/(w+h*360)*1000 + 3
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id)
        if(conf>50):
            if(Id==1):
                distance1 = distancei *2.54
                distance1 = math.floor(distancei/2)
                Id="shivam"
            elif(Id==2):
                distance2 = distancei *2.54
                distance2 = math.floor(distancei/2)
                Id="obama"
                if(distance1>distance2):
                    result=distance1-distance2
                elif(distance2>distance1):
                    result=distance2-distance1
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),fontFace,fontScale,fontColor)
        cv2.putText(im,'Distance1 = ' + str(distance1) , (5,100),font,1,(255,255,255),2)
        cv2.putText(im,'Distance2 = ' + str(distance2) + ' Inch', (10,75),font,1,(255,255,255),2)
        cv2.putText(im,'result = ' + str(result) + ' Inch', (50,50),font,1,(255,255,255),2)
    cv2.imshow('im',im) 
    if (cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
