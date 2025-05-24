# 🧠 Lung Tumor Detection




### using YOLOv8

This project utilizes a pretrained **YOLOv8** model to detect lung tumors in medical images. It includes the full pipeline from data preprocessing and training to inference.

---

### 📁 Project Structure

```
prtrained_model/
├── inference/
│   ├── images/                # Images for inference
│   └── inference.py           # Script to run inference
├── runs/                      # YOLO training outputs and weights
├── model-training.ipynb       # Notebook used to train YOLOv8 model
```

---

### ⚙️ Setup

#### 🔧 Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```
---

### 🛠️ Preprocessing

Before training the model, follow these steps to prepare your dataset:

1. **Convert Task Directories to Images and Labels:**
   - Read the original annotation file(s).
   - Parse bounding box coordinates.
   - Convert boxes to YOLO format:
     ```
     class_id center_x center_y width height
     ```

2. **Normalize Bounding Boxes:**
   - Normalize `center_x`, `center_y`, `width`, and `height` using the image width and height.

3. **Handle Images Without Tumors:**
   - If an image has no tumor, create an empty `.txt` file with the same name as the image to maintain YOLO format consistency.

4. **Create the `data.yaml` File:**

Example:
```yaml
train: path/to/train/images
val: path/to/val/images

nc: 1
names: ['tumor']
```

---

## 🧪 Training

We use the **Ultralytics YOLOv8** model for training the lung tumor detector.

### 🔹 First Training Attempt

- Image size: `640`
- Number of epochs: `50`

### 🔸 Second Training Attempt (Tuned Hyperparameters)

- Epochs: `50`
- Image size: `1024`
- Patience: `10` (early stopping)
- Initial learning rate: `1e-4`
- Close mosaic augmentation after epoch `10`
- Box loss gain: `0.05`
- Class loss gain: `0.5`

> ✅ Training results, including the best weights, are saved under:

```
prtrained_model/runs/detect/train/weights/best.pt
```

You can also view training logs and performance metrics in the `runs/detect/train` directory.

---

## 🔍 Inference

Once training is complete, you can use the trained model to make predictions on new images.

### ▶️ Run Inference

To detect tumors in an image:

```bash
python prtrained_model/inference/inference.py
```

> Default image used:
```
prtrained_model/inference/images/289.png
```
 ---
## 🖼 Output Example

Below is an example of tumor detection with bounding boxes:

![Tumor Detection Output](prtrained_model\inference\images\tumor_detection.png)
 
---

## ✅ Notes

- Change `img_path` inside `inference.py` to test with different images.
- Make sure every image has a corresponding `.txt` label file, even if it's empty.

---

## 🧠 Model Reference

Built using the [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) detection framework.

---

## 👨‍🔬 Author

This repository was developed for a lung tumor detection project using deep learning and computer vision.
