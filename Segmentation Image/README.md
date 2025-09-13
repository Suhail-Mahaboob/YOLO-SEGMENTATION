# YOLOv8 Segmentation on Image

This project applies **YOLOv8 segmentation** on a single image to detect and segment objects.  
The output image is displayed and also saved locally.

---

## Installation
```bash
git clone https://github.com/Suhail-Mahaboob/YOLO-SEGMENTATION.git
cd YOLO-SEGMENTATION/Segmentation Image
pip install -r requirements.txt
```
Usage
```bash
python segmentation_image.py
```
Replace test.jpg with your own image.

Segmented results will be saved automatically in the runs/segment/ folder.

Notes
*Uses the pretrained YOLOv8 segmentation model (yolov8n-seg.pt).
*You can switch to other YOLOv8 segmentation models (e.g., yolov8s-seg.pt, yolov8m-seg.pt) for better accuracy.
