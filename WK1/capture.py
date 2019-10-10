#!/usr/bin/env python
import cv2
import numpy as np



if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('rpi_image.jpg', frame)
    print("hello")
    cap.release()