import cv2
import numpy as np

'''
Mouse events

events = [i for i in dir(cv2) if "EVENT" in i]
for i in events:
    print(i)
'''

prevX, prevY = 0,0

def mouse_event(event,x,y, flags,para):
    global prevX,prevY
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(255,255,255),2)
        strXY = f'({x}, {y})'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img,strXY, (x+10,y-10),font,1,(255,255,255))
        if prevX==0 and prevY == 0:
            prevX,prevY = x,y
        else:
            cv2.line(img,(prevX,prevY),(x,y),(0,255,0),5)
            prevX,prevY = x,y
        cv2.imshow('image',img)
    
cv2.namedWindow('image')

# Original image
img = np.zeros((800,800,3), np.uint8)
cv2.setMouseCallback('image',mouse_event)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
