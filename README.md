# Lung Tumor Segmentation – U-Net (PyTorch)

This branch focuses on the **semantic segmentation** stage of the project, where the goal is to accurately segment lung tumor regions in cropped CT scan images using a custom U-Net model.

## ✨ Key Features

- **U-Net from Scratch**: Implemented a lightweight U-Net architecture in PyTorch without using pretrained encoders.
- **Tumor-Aware Augmentation**: Applied size-adaptive augmentations based on original tumor dimensions to preserve small lesion details.
- **Clean Preprocessing Pipeline**:
  - Cropped and resized tumor regions based on detection boxes.
  - Added contextual padding and safeguards for small or edge-case tumors.
- **Flexible Dataset Handling**: Designed a PyTorch Dataset class that reads from a preprocessed DataFrame, with support for optional metadata and augmentation.
- **Inference Support**: Includes an inference pipeline to predict tumor masks on unlabeled test data and visualize results.

## 🧪 Results

Achieved a Dice score of **0.6698**, IoU of **0.5566**, and pixel accuracy of **94.78%** on the validation set.

---

