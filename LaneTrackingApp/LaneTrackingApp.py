# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 11:35:23 2022

@author: erdem
"""

import cv2
import numpy as np


video = cv2.VideoCapture("line.mp4")


"""
işk önce videoyu frame atadık ardından maskeledik canny ile 
kenar ayırdık hougline ile değerleri çektik çizgi koyduk frame geri ekledik
"""
while True:
    ret,frame=video.read()
    #çizgiler sarı olduğu için renk formatını hsv yapıp rengi ayırıcaz
    frame = cv2.resize(frame,(640,480)) #görseli boyutlandırdık
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hsv range for collor name ile hsv aralığı kodu bulunur
    lower_yellow = np.array([18,94,140],np.uint8)
    upper_yellow = np.array([48,255,255],np.uint8)
    
    mask= cv2.inRange(hsv,lower_yellow,upper_yellow) #belirtilen renk koduna özel olan enk arlaığını maksele 
    
    edges =  cv2.Canny(mask,25,150) #oynanıcak görseli ve 75 gürültü altını alma 250 gürültü üstünü alma dedik

    lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap = 50)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),4)
    
    
    cv2.imshow("frame",frame)
    


    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break

video.release()

cv2.destroyAllWindows() 
    