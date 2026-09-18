import argparse
from pathlib import Path
from src.pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser(description="VisionEdge - Computer Vision Image Analyzer")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()

    report = run_pipeline(args.input, args.output)

    print("\n=== VisionEdge Analysis ===")
    print(f"Image: {Path(args.input).name}")
    print(f"Resolution: {report['resolution']['width']} x {report['resolution']['height']}")
    print(f"Brightness: {report['metrics']['brightness']}")
    print(f"Contrast: {report['metrics']['contrast']}")
    print(f"Sharpness: {report['metrics']['sharpness']}")
    print(f"Edge Density: {report['metrics']['edge_density']}")
    print(f"Quality Label: {report['quality_label']}")
    print(f"Outputs saved to: {args.output}")

if __name__ == "__main__":
    main()
