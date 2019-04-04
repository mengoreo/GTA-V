import numpy as np
from PIL import ImageGrab
import cv2
import time
from KeyFunctions import PressKey, ReleaseKey, KEYS


def capture(x=0, y=0, width=13, height=14):
    return np.array(ImageGrab.grab(bbox=(x, y, width, height)))


def show(image):
    cv2.show('Window', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destoryAllWindows()
        return False
    return True


def process(image):
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return processed_image
