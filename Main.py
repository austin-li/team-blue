import cv2
from TargetDetector import TargetDetector
from Target import Target
from TargetProcessor import TargetProcessor

import network

cam = cv2.VideoCapture(1)

global network1
network1 = network.Network()
network1.userServer()

while(True):
    ret, frame = cam.read()
    if not ret:
        continue

    detect = TargetDetector(frame)
    detect.threshold()
    detect.contours()
    detect.filterContours()
    target = Target(frame, detect.getContour())
    processor = TargetProcessor(frame, target.xmin, target.xmax, target.ymin, target.ymax)
    processor.calculate()
    if processor.getAzimuth() != 0.0:
        #print("Distance", processor.getDistance())
        #print("Azimuth", processor.getAzimuth())
        #print("Altitude", processor.getAltitude())
        #print()
        network1.setDistance(str(processor.getDistance()))
        network1.setAzimuth(str(processor.getAzimuth()))
        network1.setAltitude(str(processor.getAltitude()))

    cv2.imshow("image", detect.img)
    cv2.imshow("thresh", detect.thresh)

    if cv2.waitKey(10) == 27:
        cv2.destroyAllWindows()
        break