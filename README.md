# VisionEdge: Smart Image Quality & Feature Analyzer

**Course:** Computer Vision  
**Student:** Abhishek Pathak  
**Registration No.:** 24BAI10897

## Project Overview
VisionEdge is a command-line computer vision project that analyzes an input image and produces a compact visual-quality report. It combines classical computer-vision operations to estimate image brightness and contrast, detect edges, calculate a blur/sharpness score, and generate an enhanced preview.

## Major Functional Modules
1. Image Validation & Loading
2. Image Quality Analysis
3. Edge & Feature Analysis
4. Image Enhancement & Reporting

## Technologies
- Python 3.10+
- OpenCV
- NumPy
- Pillow
- pytest

## Project Structure
```text
VisionEdge/
├── README.md
├── statement.md
├── requirements.txt
├── run.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── image_loader.py
│   ├── preprocessing.py
│   ├── quality_analyzer.py
│   ├── edge_analyzer.py
│   ├── enhancement.py
│   ├── reporter.py
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── data/sample_images/
├── outputs/
└── docs/
    └── PROJECT_REPORT.md
```

## Setup
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python run.py --input data/sample_images/sample.jpg
```

The program generates `enhanced.jpg`, `edges.jpg`, and `analysis_report.json`.

## Testing
```bash
pytest -q
```

## Computer Vision Concepts
- Image acquisition
- Color-space conversion
- Gaussian filtering
- Histogram statistics
- Laplacian operator
- Canny edge detection
- CLAHE contrast enhancement
- Quantitative image-quality metrics

## Academic Note
This project follows the supplied VITyarthi Computer Vision project requirements, including modular implementation, documentation, testing, architecture/workflow artefacts, and a detailed project report.
