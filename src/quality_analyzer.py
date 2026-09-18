import cv2
import numpy as np

def brightness(gray):
    return float(np.mean(gray))

def contrast(gray):
    return float(np.std(gray))

def sharpness(gray):
    return float(cv2.Laplacian(gray, cv2.CV_64F).var())

def quality_label(bright, cont, sharp):
    if sharp < 40:
        return "BLURRY"
    if bright < 45 or bright > 215:
        return "EXPOSURE ISSUE"
    if cont < 25:
        return "LOW CONTRAST"
    return "GOOD"

def analyze(gray):
    b = brightness(gray)
    c = contrast(gray)
    s = sharpness(gray)
    return {
        "brightness": round(b, 2),
        "contrast": round(c, 2),
        "sharpness": round(s, 2),
        "quality_label": quality_label(b, c, s),
    }
