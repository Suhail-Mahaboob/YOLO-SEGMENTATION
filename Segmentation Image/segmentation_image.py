from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-seg.pt")

image_path = "test.jpg"
results = model(image_path)

for r in results:
    annotated_frame = r.plot()
    cv2.imshow("Segmentation Result", annotated_frame)
    cv2.imwrite("result_test_segmentation.jpg", annotated_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
