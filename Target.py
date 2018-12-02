class Target(object):
    """Holds attributes of target contour"""
    def __init__(self, img, contours):
        #img
        self.img = img
        #set min values to width and height of image
        self.ymin, self.xmin = img.shape[:2]
        #set max values to 0
        self.xmax, self.ymax = (0, 0)
        #find min and max values
        for cont in contours:
            for i in range(len(cont)):
                x = cont[i][0][0]
                y = cont[i][0][1]
                if x < self.xmin:
                    self.xmin = x
                if x > self.xmax:
                    self.xmax = x
                if y < self.ymin:
                    self.ymin = y
                if y > self.ymax:
                    self.ymax = y
    #return width
    def width(self):
        return self.xmax - self.xmin
    #return height
    def height(self):
        return self.ymax - self.ymin
    #return center of target (x, y)
    def center(self):
        return ((self.xmin + self.xmax)/2, (self.ymin + self.ymax)/2)
    #return center of image (x, y)
    def img_center(self):
        return (self.img.shape[1]/2, self.img.shape[0]/2)