import cv2
import numpy as np
from src.quality_analyzer import analyze
from src.edge_analyzer import analyze_edges

def test_quality_analysis_returns_metrics():
    image = np.zeros((100, 100), dtype=np.uint8)
    cv2.rectangle(image, (20, 20), (80, 80), 255, -1)
    result = analyze(image)
    assert "brightness" in result
    assert "contrast" in result
    assert "sharpness" in result

def test_edge_density_is_valid():
    image = np.zeros((100, 100), dtype=np.uint8)
    cv2.line(image, (10, 50), (90, 50), 255, 2)
    edges, density = analyze_edges(image)
    assert edges.shape == image.shape
    assert 0.0 <= density <= 1.0
