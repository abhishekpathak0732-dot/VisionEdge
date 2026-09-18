import cv2
from .config import CLAHE_CLIP_LIMIT, CLAHE_GRID_SIZE

def enhance(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(
        clipLimit=CLAHE_CLIP_LIMIT,
        tileGridSize=CLAHE_GRID_SIZE
    )
    enhanced_l = clahe.apply(l)
    enhanced_lab = cv2.merge((enhanced_l, a, b))
    return cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
