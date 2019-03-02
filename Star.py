import numpy as np
import cv2

class Star:

    def __init__(self, x, y, z):
        self.x_cord = x
        self.y_cord = y
        self.z_cord = z

    def update(self, rate):
        if self.z_cord > .5:
            self.z_cord -= rate


    def getPoint(self, size):  # size(h, w)
        center = size / 2
        new_x = (size[1] * ((self.x_cord - center[1]) / ((self.z_cord * size[1]) - center[1]))) + center[1]
        new_y = (size[0] * ((self.y_cord - center[0]) / ((self.z_cord * size[0]) - center[0]))) + center[0]
        return np.array([new_y, new_x])

    def getSize(self, minSize, maxSize):
        return maxSize + (minSize - (minSize + (maxSize - minSize) * (self.z_cord - .5)))

    def draw(self, pnt, img):
        cv2.circle(img, (int(pnt[1]), int(pnt[0])), int(self.getSize(0, 4)), (255, 255, 255), -1)

    @staticmethod
    def getRndStar(num, size):
        x_cords = np.random.randint(0, size[1], num)
        y_cords = np.random.randint(0, size[0], num)
        z_cords = np.random.uniform(1.49, 1.5, num)

        return [Star(x_cords[i], y_cords[i], z_cords[i]) for i in range(num)]