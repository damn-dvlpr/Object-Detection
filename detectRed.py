import numpy as np
import cv2 as cv

cam=cv.VideoCapture(0)

# cam.set(3,50)
# cam.set(4,50)
print("width=" + str(cam.get(3)))
print("height=" + str(cam.get(4)))

# while True:
fps=cam.get(cv.CAP_PROP_FPS)
# cv.putText(frame,"FPS from inbuild fn : {0}".format(fps),(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
while True:
    # s=time.time()
    ret,frame=cam.read()
    hsv_frame= cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    low_red=np.array([155,25,0])
    high_red=np.array([179,255,255])
    mask=cv.inRange(hsv_frame,low_red,high_red)
    redf=cv.bitwise_and(frame,frame,mask=mask)
    # e=time.time()
    # rfps=1/(e-s)
    # print("actual fps: {0}".format(rfps))
    cv.imshow("frame",frame)
    cv.imshow("Redframe",mask)
    cv.imshow("onlyred",redf)
    if cv.waitKey(1)==27:
        break
cv.destroyAllWindows()
cam.release()