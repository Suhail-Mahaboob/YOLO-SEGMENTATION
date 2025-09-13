from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-seg.pt")
video_path = "testt.mp4"
cap = cv2.VideoCapture(video_path)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("result_test_segmentation.mp4", fourcc, fps, (width,height))

while True:
    ret,frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("Segmentation Result",annotated_frame)
        out.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()
