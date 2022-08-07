import numpy as np
import cv2


def editPhoto(emotion, photo):
    img = cv2.imread(photo)
    if emotion == "happy":
        contrast = 1.5
        exposure = 35
        cv2.addWeighted(img, contrast, np.zeros(
            img.shape, img.dtype), 0, exposure)
