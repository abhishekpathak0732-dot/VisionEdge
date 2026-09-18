# Project Statement

## Project Title
**VisionEdge: Smart Image Quality & Feature Analyzer**

## Student
**Abhishek Pathak**

## Registration Number
**24BAI10897**

## Course
**Computer Vision**

## Problem Statement
Image quality strongly affects downstream computer-vision tasks such as recognition, detection, and visual inspection. A user may have an image that is too dark, low-contrast, blurry, or lacking useful edges, but identifying the issue manually is subjective.

VisionEdge provides a lightweight command-line solution that accepts an image, applies standard computer-vision preprocessing and analysis operations, calculates objective quality indicators, detects prominent edges, and creates an enhanced preview.

## Scope
The project focuses on:
- Image validation and loading
- Grayscale conversion and preprocessing
- Brightness and contrast measurement
- Sharpness estimation using the variance of the Laplacian
- Canny edge detection
- Edge-density calculation
- CLAHE-based enhancement
- JSON reporting

It does not attempt to replace specialized professional image-quality benchmarks or deep-learning vision models.

## Target Users
- Computer Vision students
- Developers learning OpenCV
- Researchers performing quick image diagnostics
- Users who need a terminal-based image quality check

## High-Level Features
1. Command-line image input
2. Automatic preprocessing
3. Brightness and contrast analysis
4. Blur/sharpness analysis
5. Edge detection
6. Image enhancement
7. JSON report generation
8. Automated tests
