import numpy as np

class TargetProcessor(object):
    """Calculates distance, azimuth, and altitude"""
    def __init__(self, img, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        #calculate target centers
        self.xcenter = (xmin + xmax)/2
        self.ycenter = (ymin + ymax)/2
        #calculate image centers
        self.img_xcenter = img.shape[1]/2
        self.img_ycenter = img.shape[0]/2
        #set focal length and target size in cm
        self.focal = 720
        self.width, self.height = (16.51, 16.51)
    def calculate(self):
        self.distance = (self.focal * self.width)/(self.xmax - self.xmin)
        self.azimuth = np.rad2deg(np.arctan2(self.xcenter - self.img_xcenter, self.focal))
        self.altitude = np.rad2deg(np.arctan2(-(self.ycenter - self.img_ycenter), self.focal))
    #return distance
    def getDistance(self):
        return self.distance
    #return azimuth
    def getAzimuth(self):
        return self.azimuth
    #return altitude
    def getAltitude(self):
        return self.altitude