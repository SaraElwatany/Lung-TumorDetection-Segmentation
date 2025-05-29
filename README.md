# Tumor Segmentation From Whole Input Image

This branch focuses on segmenting tumors in medical images using deep learning without any prior detection.

---

## 📚 Table of Contents

- [Tumor Segmentation](#tumor-segmentation)
  - [Model: U-Net](#model-u-net-implemented-from-scratch)
  - [Data Details](#data-details)
  - [Preprocessing Steps](#preprocessing-steps)
- [Approaches](#approaches)
  - [First Approach: Split Training/Validation Sets](#1️⃣-first-approach-split-trainingvalidation-sets)
  - [Second Approach: Full Training Data](#2️⃣-second-approach-full-training-data)
- [Results](#results)
- [Recommendations](#recommendations)
- [Screenshots](#📸-screenshots)
- [Project Structure](#📁-project-structure)

---

## 🧠 Tumor Segmentation

Binary segmentation was performed on grayscale medical images to localize tumor regions.

### 🏗️ Model: U-Net (Implemented from Scratch)

- **Encoder (Contracting Path)**: Multiple double convolution blocks with downsampling.
- **Decoder (Expanding Path)**: Upsampling with skip connections and double conv layers.

### 📑 Data Details

- Each image is paired with a **binary ground truth mask**:
  - White pixels (255) = Tumor region
  - Black pixels (0) = Background

### 🔄 Preprocessing Steps

- Converted to grayscale
- Resized to **256×256**
- Normalized and converted to tensors

---

## ⚙️ Approaches

### 1️⃣ First Approach: Split Training/Validation Sets

- Used `train_test_split` with fixed `random_state`
- Saved best models using checkpoints
- Reserved test set for final evaluation

### 2️⃣ Second Approach: Full Training Data

- Trained on all available training data
- Used provided validation set for evaluation
- Same preprocessing and checkpointing strategy

---

## 📊 Results

| Approach        | Training Loss | Validation Loss | Test Loss |
|----------------|----------------|------------------|------------|
| **First**       | 0.0010         | 0.0152           | 0.0024     |
| **Second**      | 0.0044         | 0.0048           | N/A        |

> 🔎 These results indicate **possible underfitting** in the second approach, likely due to model complexity or data limitations.

---


### Recommendations

- ✅ **Train longer**: More epochs may improve learning.
- ✅ **Data Augmentation**:
  - Flipping
  - Rotation
  - Elastic deformation
- ✅ **Add more data**: Collect or annotate more tumor samples.
- ✅ **Try Advanced Models**:
  - `Mask R-CNN`
  - `DeepLabv3+`
  - Hybrid 2-stage pipelines

---

## 📸 Screenshots

- Training & Validation Loss:
![Screenshot 2025-05-24 130514](https://github.com/user-attachments/assets/707d37e6-bcfe-4a4d-b8b1-48a4b82f23fb)

![Screenshot 2025-05-24 130521](https://github.com/user-attachments/assets/02b3072b-e83b-4bfb-a68d-a49bdd23b35d)

- Inference:
![Screenshot 2025-05-24 130647](https://github.com/user-attachments/assets/a8561fdb-0e18-40ad-9482-463e30d70351)


---

## 📁 Project Structure

<pre> <code> ``` 
Lung-TumorDetection-Segmentation/
│
├── Train, Val, Test/
│ └── First Checkpoint/
│ ├── Second Checkpoint/
│ ├── Third Checkpoint/
│
├── Train, Val/
│ └── Second Checkpoint/
│ ├── Fifth Checkpoint/
│
└── README.md
``` </code> </pre>
