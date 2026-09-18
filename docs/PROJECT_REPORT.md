# VisionEdge — Project Report

**Course:** Computer Vision  
**Student:** Abhishek Pathak  
**Registration No.:** 24BAI10897

## 1. Cover Page
### VisionEdge: Smart Image Quality & Feature Analyzer
A command-line Computer Vision project using OpenCV.

**Submitted by:** Abhishek Pathak  
**Registration No.:** 24BAI10897

## 2. Introduction
Computer vision systems depend heavily on the quality of visual input. Poor illumination, low contrast, blur, and weak structural information can reduce the usefulness of an image for later processing. VisionEdge is a compact diagnostic pipeline that uses classical computer-vision techniques to quantify these properties.

The system takes an image from the command line, performs preprocessing, calculates objective image-quality metrics, detects edges, enhances the image using CLAHE, and produces a machine-readable JSON report.

## 3. Problem Statement
Manual inspection of image quality is subjective and difficult to standardize. A lightweight automated tool is therefore useful for identifying common image-quality problems before an image is used in another vision task.

## 4. Objectives
- Build a fully command-line computer-vision application.
- Apply image preprocessing using grayscale conversion and Gaussian filtering.
- Measure brightness and contrast.
- Estimate sharpness using variance of the Laplacian.
- Detect structural edges with Canny edge detection.
- Improve local contrast with CLAHE.
- Produce reproducible output files and a JSON report.
- Demonstrate modular software design and automated testing.

## 5. Functional Requirements
### FR1 — Image Input
The system shall accept a supported image path from the command line.

### FR2 — Preprocessing
The system shall convert the image to grayscale and apply Gaussian filtering.

### FR3 — Quality Analysis
The system shall calculate brightness, contrast, and sharpness.

### FR4 — Edge Analysis
The system shall generate an edge map and calculate edge density.

### FR5 — Enhancement
The system shall generate an enhanced preview using CLAHE.

### FR6 — Reporting
The system shall save results as a JSON report and output images.

## 6. Non-Functional Requirements
- Performance: lightweight classical algorithms suitable for CPU execution.
- Usability: simple CLI with clear arguments and terminal output.
- Reliability: validation of input paths, extensions, and decoded image data.
- Maintainability: separate modules for loading, preprocessing, analysis, enhancement, reporting, and orchestration.
- Resource Efficiency: no GPU or large pretrained model required.
- Error Handling: clear errors for missing, unsupported, or unreadable images.

## 7. System Architecture
```text
Command Line -> Image Loader -> Preprocessing
                                  |       |
                                  v       v
                           Quality      Edge
                           Analyzer     Analyzer
                                  \       /
                                   Enhancement
                                       |
                                    Reporter
                                  /          \
                             JSON Report    Images
```

## 8. Process Workflow
```text
Start -> Read CLI arguments -> Validate image -> Load image
-> Grayscale -> Gaussian filtering
-> Quality metrics + Canny edges
-> CLAHE enhancement -> Save outputs -> Save JSON -> End
```

## 9. Use Case Diagram
```text
User -> Analyze Image
User -> View Metrics
User -> Generate Edge Map
User -> Generate Enhanced Image
User -> Read JSON Report
```

## 10. Sequence Diagram
```text
User -> CLI: provide image path
CLI -> Pipeline: run_pipeline()
Pipeline -> Loader: load_image()
Loader --> Pipeline: image
Pipeline -> Preprocessor: grayscale + filter
Preprocessor --> Pipeline: processed image
Pipeline -> Quality Analyzer: calculate metrics
Quality Analyzer --> Pipeline: metrics
Pipeline -> Edge Analyzer: detect edges
Edge Analyzer --> Pipeline: edge map + density
Pipeline -> Enhancement: enhance()
Enhancement --> Pipeline: enhanced image
Pipeline -> Reporter: save JSON
Reporter --> Pipeline: report path
Pipeline --> CLI: final report
CLI --> User: display results
```

## 11. Component Design
The implementation uses functional modules rather than large classes.

| Component | Responsibility |
|---|---|
| image_loader.py | Input validation and OpenCV loading |
| preprocessing.py | Grayscale conversion and Gaussian filtering |
| quality_analyzer.py | Brightness, contrast, sharpness, quality label |
| edge_analyzer.py | Canny edge detection and edge density |
| enhancement.py | CLAHE-based enhancement |
| reporter.py | JSON report generation |
| pipeline.py | End-to-end orchestration |
| run.py | Command-line interface |

## 12. Dataset / Input Description
VisionEdge is an image-processing application and does not require a training dataset. The input is supplied by the user as a JPG, JPEG, PNG, BMP, or TIFF image.

## 13. Algorithm Selection Rationale
No machine-learning training model is required. Classical algorithms were selected because the project objective is image-quality and feature analysis.

- Gaussian blur reduces small-scale noise.
- Laplacian variance provides a sharpness indicator.
- Canny detects strong intensity transitions.
- CLAHE improves local contrast.

## 14. Evaluation Methodology
1. Input validation tests.
2. Unit tests for quality metrics.
3. Edge-density range validation.
4. Manual inspection of generated enhanced and edge images.
5. Verification that the JSON report contains expected fields.

## 15. Implementation Details
The pipeline is written in Python using OpenCV and NumPy. `run.py` exposes a simple CLI. Processing stages are separated into modules.

Metrics:
- Brightness = mean grayscale intensity.
- Contrast = standard deviation of grayscale intensity.
- Sharpness = variance of the Laplacian.
- Edge density = non-zero edge pixels divided by total pixels.

## 16. Results
Running:
```bash
python run.py --input data/sample_images/sample.jpg
```
generates enhanced and edge images plus a JSON report.

## 17. Testing Approach
Automated tests are provided in `tests/test_pipeline.py`.

```bash
pytest -q
```

## 18. Challenges Faced
- Selecting lightweight algorithms that work without GPU resources.
- Designing a meaningful quality label from numerical metrics.
- Handling unsupported and unreadable input files.
- Keeping the implementation modular.

## 19. Learnings & Key Takeaways
- Image statistics can quantify visual properties.
- Practiced grayscale conversion and filtering.
- Applied Laplacian and Canny operators.
- Understood CLAHE-based local contrast enhancement.
- Practiced modular Python organization and automated testing.

## 20. Future Enhancements
- Histogram visualizations
- Noise-level estimation
- SSIM when a reference image is available
- Batch-folder processing
- Optional object-detection integration
- HTML reporting
- Optional web interface

## 21. References
1. OpenCV documentation — image processing, filtering, Canny edge detection, and CLAHE.
2. NumPy documentation — numerical and statistical operations.
3. Python documentation — command-line interfaces and file handling.
4. VITyarthi Build Your Own Project — supplied course project requirements.
