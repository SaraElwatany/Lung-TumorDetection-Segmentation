import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO


 
detection_model = YOLO(r'prtrained_model\runs\detect\train\weights\best.pt')


def infer_image(img_path, conf=0.3):
    results = detection_model(img_path, conf=conf)
    boxes = results[0].boxes
    scores = results[0].boxes.conf.cpu().numpy()
    image = cv2.imread(img_path)

    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        label = box.cls[0].item()
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, f"Tumor {conf:.2f}", (x1, y1 - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return image, boxes, scores


def main():
    img_path = r'prtrained_model\inference\images\289.png'
    img, boxes, scores = infer_image(img_path)

    print(f'boxes: {boxes}')
    print(f'scores: {scores}')

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("YOLO Tumor Detection")
    plt.show()


if __name__ == "__main__":
    main()
