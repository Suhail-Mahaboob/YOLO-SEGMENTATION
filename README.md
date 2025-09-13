# YOLOv8 Segmentation Projects

This repository contains mini-projects using YOLOv8 segmentation on different input sources:

🖼 Image Segmentation → run YOLOv8 segmentation on a single image.

🎥 Video Segmentation → process videos frame by frame and save the segmented output.

📷 Webcam Segmentation → apply segmentation live using your webcam.

Each task is placed in its own folder with code, README, and requirements.
```
📂 Repository Structure
yolo-segmentation/
│
├── image_segmentation/
│   ├── segmentation_image.py
│   ├── requirements.txt
│   └── README.md
│
├── video_segmentation/
│   ├── segmentation_video.py
│   ├── requirements.txt
│   └── README.md
│
├── webcam_segmentation/
│   ├── segmentation_webcam.py
│   ├── requirements.txt
│   └── README.md
│
└── README.md   <-- (this file)
```
🚀 Installation

Clone the repository:
```
git clone https://github.com/Suhail-Mahaboob/YOLO-SEGMENTATION.git
cd YOLO-SEGMENTATION
```

Each subfolder has its own requirements.txt.
For example, to install dependencies for image segmentation:
```
cd Segmentation Image
pip install -r requirements.txt
```
▶️ Usage

For image segmentation:
```
cd Segmentation Image
python segmentation_image.py
```

For video segmentation:
```
cd Segmentation Video
python segmentation_video.py
```

For webcam segmentation:
```
cd Segmentation Webcam
python segmentation_webcam.py
```

📌 Notes

> All projects use YOLOv8 segmentation weights (yolov8n-seg.pt).
> You can replace with other YOLOv8 models (yolov8s-seg.pt, yolov8m-seg.pt) for higher accuracy.

Output files will be saved automatically:
* Image → inside runs/segment/
* Video → result_out_Segmentation_video.mp4
* Webcam → result_out_Segmentation_webcam.mp4
