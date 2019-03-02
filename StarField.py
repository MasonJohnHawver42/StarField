from Star import Star
import numpy as np
import cv2


def pntInSize(pnt, size):
    if np.any(pnt < 0) or np.any(pnt >= size):
        return False
    else:
        return True


def starField(size, star_num, speed=.01):
    stars = Star.getRndStar(star_num, size)

    while True:
        img = np.zeros((size[0], size[1], 3))
        for star in stars:
            star.update(speed)
            pnt = star.getPoint(size)
            if pntInSize(pnt, size):
                star.draw(pnt, img)

            else:
                stars.remove(star)
                stars.append(Star.getRndStar(1, size)[0])

        cv2.imshow("", img)
        cv2.waitKey(1)

starField(np.array([1000, 1000]), 100)