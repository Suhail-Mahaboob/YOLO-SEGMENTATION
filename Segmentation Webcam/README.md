# YOLOv8 Segmentation on Webcam

This project runs **YOLOv8 segmentation** live on your webcam feed.  
You can view results in real time, and the processed video is also saved.

---

## Installation
```bash
git clone https://github.com/Suhail-Mahaboob/YOLO-SEGMENTATION.git
cd YOLO-SEGMENTATION/Segmentation Webcam
pip install -r requirements.txt
```
Usage
```bash
python segmentation_webcam.py
```
Press Q to quit.

Output 
> video is saved as result_out_Segmentation_webcam.mp4.

Notes
* Works with default webcam (cv2.VideoCapture(0)).
* You can change the index to use an external camera.

Uses YOLOv8 segmentation pretrained weights (yolov8n-seg.pt).
