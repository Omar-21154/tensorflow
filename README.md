# 🎯 YOLOv8 Vision - Real-time Object Detection

A modern, responsive Streamlit web application for real-time object detection using YOLOv8. Detect and classify 80 different object types with live camera feed, image upload, or photo capture.

## ✨ Features

- **🎥 Live Video Stream** - Real-time object detection using your webcam (WebRTC powered)
- **📷 Photo Capture** - Take photos directly from your device and analyze them
- **📁 File Upload** - Upload images (JPG, PNG) for analysis
- **⚙️ Model Selection** - Choose between Nano, Small, or Medium YOLOv8 models
- **🎚️ Confidence Tuning** - Adjust detection confidence threshold (10%-90%)
- **📊 Detailed Results** - View detected objects with confidence scores and visual progress bars
- **🌙 Dark Mode UI** - Modern, dark-themed interface with gradient text

## 🚀 Quick Start

### Local Installation

1. **Clone or download this repository**

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download YOLO models** (first run will download automatically, or manually):
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt'); YOLO('yolov8s.pt'); YOLO('yolov8m.pt')"
```

5. **Run the application**
```bash
streamlit run yolo_tanima.py
```

6. **Open in browser** - Navigate to `http://localhost:8501`

## 📋 Requirements

- Python 3.8+
- See [requirements.txt](requirements.txt) for dependencies

### System Dependencies
For Linux/Docker deployments, ensure `packages.txt` dependencies are installed.

## 🎯 Usage Modes

### 1. Live Video (🎥 Canlı video)
- Click START to begin webcam streaming
- Browser will request camera permissions
- Detection runs in real-time on each frame

### 2. Photo Capture (📷 Foto çək)
- Click to open camera and capture a photo
- App analyzes and displays detected objects

### 3. File Upload (📁 Fayl yüklə)
- Upload JPG or PNG images
- Get instant detection results

## ⚙️ Configuration

### Model Selection
- **Nano (⚡)** - Fastest, ~6M parameters, good for real-time
- **Small (⚖️)** - Balanced, ~11M parameters, recommended
- **Medium (🎯)** - Most accurate, ~25M parameters, slower

### Confidence Threshold
- **Low (0.1)** - More detections, possible false positives
- **High (0.9)** - Fewer detections, only high-confidence results

## 🌐 Deployment

### Streamlit Cloud (Free)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select your repository and `yolo_tanima.py`
4. Deploy!

**Note:** For faster response times, the Nano model is recommended for cloud deployment.

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y $(cat packages.txt)
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "yolo_tanima.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Environment Variables
```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_RUNONSAVE=false
```

## 🛠️ Troubleshooting

### WebRTC Not Working
- Enable microphone/camera permissions in browser settings
- Use HTTPS (required for camera access on hosted deployments)
- Check browser console for errors

### Model Download Issues
- Manually download from [YOLOv8 Releases](https://github.com/ultralytics/assets/releases)
- Place in same directory as script

### Slow Performance
- Switch to Nano model
- Lower video resolution in browser
- Reduce confidence threshold

## 📝 Supported Object Classes

YOLOv8 detects 80 COCO dataset classes including:
- Vehicles (car, truck, bus, motorcycle, bicycle)
- Animals (dog, cat, bird, horse, cow, sheep, bear, zebra, giraffe)
- People (person)
- Sports equipment
- Kitchen items
- Electronics
- And 65+ more!

## 📄 License

This application uses [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) which is licensed under AGPL-3.0.

## 🤝 Contributing

Contributions welcome! Feel free to open issues or submit pull requests.

## 📧 Support

For issues with YOLOv8, see [Ultralytics Documentation](https://docs.ultralytics.com)

---

**Made with ❤️ using Streamlit and YOLOv8**
