from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-seg.pt")
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("result_out_Segmentation_webcam.mp4", fourcc, 30, (width,height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("Segmentation Result", annotated_frame)
        out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if cv2.getWindowProperty("Segmentation Result", cv2.WND_PROP_VISIBLE)<1:
            break

out.release()
cap.release()
cv2.destroyAllWindows()
