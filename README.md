# 🧬 Tumor Detection & Segmentation

This repository presents a deep learning pipeline for detecting and segmenting tumors in grayscale medical images. It features both object detection and semantic segmentation tasks, evaluated under various training approaches.



## 📁 Repository Structure

```
📂 Tumor-Detection-Segmentation/
├── README.md                     # Project overview
├── Tumor Detection & Segmentation Report.pdf  # Detailed technical report
├── comparison.ipynb             # Notebook comparing models and results
├── inference.ipynb              # Inference pipeline on test/validation data
├── gitignore.txt                # Git ignore rules
```



## 🧠 Project Overview

* **Detection Stage**: Object detection model identifies tumor locations (bounding boxes).
* **Segmentation Stage**: U-Net-based model segments tumor areas in full images and detection crops.
* **Evaluation**: Performance compared under multiple training schemes with visual outputs and metrics.



## 📊 Highlights

* 📌 U-Net implemented from scratch
* 🔍 Comparison of detection vs full-image segmentation
* 📈 Includes training metrics and results analysis
* 📷 Visual inference outputs from validation set



## 📄 Report

For a complete explanation of the methods, results, and future work, refer to the included [Tumor Detection & Segmentation Report.pdf](./Tumor%20Detection%20%26%20Segmentation%20Report.pdf).



## 🚀 Quick Start

```bash
# Run inference
Open inference.ipynb in your environment (e.g., Google Colab or Jupyter)

# Compare different models
Use comparison.ipynb to visualize and evaluate results
```



## 📌 Notes

* Designed for educational and research purposes
* Datasets and models not included due to size constraints — please update paths as needed


