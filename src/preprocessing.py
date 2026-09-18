import cv2
from .config import GAUSSIAN_KERNEL

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise(gray):
    return cv2.GaussianBlur(gray, GAUSSIAN_KERNEL, 0)
