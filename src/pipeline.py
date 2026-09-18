from pathlib import Path
import cv2
from .image_loader import load_image
from .preprocessing import to_grayscale, denoise
from .quality_analyzer import analyze
from .edge_analyzer import analyze_edges
from .enhancement import enhance
from .reporter import save_report

def run_pipeline(input_path, output_dir="outputs"):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    image = load_image(input_path)
    gray = to_grayscale(image)
    filtered = denoise(gray)

    quality = analyze(filtered)
    edges, density = analyze_edges(filtered)
    enhanced = enhance(image)

    cv2.imwrite(str(output / "enhanced.jpg"), enhanced)
    cv2.imwrite(str(output / "edges.jpg"), edges)

    h, w = image.shape[:2]
    report = {
        "project": "VisionEdge",
        "student": "Abhishek Pathak",
        "registration_number": "24BAI10897",
        "resolution": {"width": w, "height": h},
        "metrics": {
            "brightness": quality["brightness"],
            "contrast": quality["contrast"],
            "sharpness": quality["sharpness"],
            "edge_density": density,
        },
        "quality_label": quality["quality_label"],
        "outputs": ["enhanced.jpg", "edges.jpg", "analysis_report.json"],
    }
    save_report(report, output)
    return report
