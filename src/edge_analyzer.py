import cv2
import numpy as np
from .config import CANNY_LOW, CANNY_HIGH

def detect_edges(gray):
    return cv2.Canny(gray, CANNY_LOW, CANNY_HIGH)

def edge_density(edges):
    return float(np.count_nonzero(edges) / edges.size)

def analyze_edges(gray):
    edges = detect_edges(gray)
    return edges, round(edge_density(edges), 4)
