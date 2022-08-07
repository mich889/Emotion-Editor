import numpy as np
import cv2


def editPhoto(emotion, photo):
    img = cv2.imread(photo)
    if emotion == "happy":
        contrast = 1.5
        exposure = 35
        cv2.addWeighted(img, contrast, np.zeros(
            img.shape, img.dtype), 0, exposure)
        #smoothening
        cv2.edgePreservingFilter(img, cv2.RECURS_FILTER, 200, 0.6) 
        #saturation
        saturation = 1.2
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype('float32')
        h,s,v = cv2.split(hsv)
        s = s*saturation
        s = np.clip(s, 0, 255)
        hsv = cv2.merge([h,s,v])
        happy_img = cv2.cvtColor(hsv.astype('unit8'), cv2.COLOR_HSV2BGR)
    elif emotion == "sad":
        contrast = 0.5
        exposure = -30
        cv2.addWeighted(img, contrast, np.zeros(
            img.shape, img.dtype), 0, exposure)
        #desaturation
        desaturation = 0.5
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype('float32')
        h,s,v = cv2.split(hsv)
        s = s*desaturation
        s = np.clip(s, 0, 255)
        hsv = cv2.merge([h,s,v])
        sad_img = cv2.cvtColor(hsv.astype('unit8'), cv2.COLOR_HSV2BGR)
    elif emotion == "anger":
        #saturate reds
        lower_red = np.array([160,100,50])
        upper_red = np.array([180,255,255])
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img, img, mask=mask)
        r_saturation = 1.5
        r_hsv = cv2.cvtColor(res, cv2.COLOR_BGR2HSV).astype('float32')
        r_h,r_s,r_v = cv2.split(r_hsv)
        r_s = r_s*r_saturation
        r_s = np.clip(r_s, 0, 255)
        r_hsv = cv2.merge([r_h,r_s,r_v])
        reds = cv2.cvtColor(r_hsv.astype('unit8'), cv2.COLOR_HSV2BGR)
        angry_img = cv2.add(reds,img)
    
    

    





