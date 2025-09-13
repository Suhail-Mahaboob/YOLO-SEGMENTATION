# YOLOv8 Segmentation on Video

This project demonstrates **YOLOv8 segmentation** on a video file.  
Each frame is processed, segmented, and written into an output video.

---

## Installation
```bash
git clone https://github.com/Suhail-Mahaboob/YOLO-SEGMENTATION.git
cd YOLO-SEGMENTATION/Segmentation Video
pip install -r requirements.txt
```
Usage
```bash
python segmentation_video.py
```
Replace test.mp4 with your own video.

Output
>video is saved as result_out_Segmentation_video.mp4.

Notes
* Make sure the input video exists in the same directory or give the full path.
* Uses YOLOv8 segmentation pretrained weights (yolov8n-seg.pt).
