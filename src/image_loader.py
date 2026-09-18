from pathlib import Path
import cv2

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff"}

def load_image(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Input image not found: {path}")
    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported image format: {file_path.suffix}")
    image = cv2.imread(str(file_path))
    if image is None:
        raise ValueError("OpenCV could not decode the image.")
    return image
