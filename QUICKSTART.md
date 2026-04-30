# Quick Start Guide 🚀

Get up and running in **5 minutes**.

## Option 1: Online (Easiest) ☁️

### Use Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Create new app → Select this repo → `yolo_tanima.py`
4. 🎉 Done! Your app is live

**Free tier includes 3 deployed apps**

---

## Option 2: Local Installation ⚡

### Prerequisites
- Python 3.8+ ([Download](https://www.python.org/downloads/))
- Git ([Download](https://git-scm.com/))

### Installation (2 minutes)

#### Windows
```cmd
# Clone repository
git clone https://github.com/your-repo/yolo-vision.git
cd yolo-vision

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run yolo_tanima.py
```

#### macOS/Linux
```bash
# Clone repository
git clone https://github.com/your-repo/yolo-vision.git
cd yolo-vision

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run yolo_tanima.py
```

### Your app is now running at: **http://localhost:8501**

---

## Option 3: Docker (Isolated) 🐳

### Prerequisites
- Docker ([Download](https://www.docker.com/products/docker-desktop))

### Run (1 command)
```bash
docker run -p 8501:8501 ghcr.io/your-repo/yolo-vision:latest
```

Or build locally:
```bash
docker build -t yolo-vision .
docker run -p 8501:8501 yolo-vision
```

Visit: **http://localhost:8501**

---

## First Steps

### 1️⃣ Try It Out
- Select a model (start with "Small" ⚖️)
- Choose a mode:
  - **🎥 Live Video** - Use your webcam
  - **📷 Photo** - Take a picture
  - **📁 Upload** - Choose an image file

### 2️⃣ Adjust Settings
- **Confidence Slider** - Controls detection sensitivity
  - Low (0.1) = More detections
  - High (0.9) = Only confident detections
- **Model Selection** - Trade speed vs accuracy
  - Nano = Fastest
  - Medium = Most accurate

### 3️⃣ Interpret Results
- **Detected Objects** - List with confidence scores
- **Progress Bars** - Visual confidence representation
- **Count** - Total objects found

---

## 📖 Helpful Links

| Topic | Link |
|-------|------|
| Full Documentation | [README.md](README.md) |
| Deployment Options | [DEPLOYMENT.md](DEPLOYMENT.md) |
| Contributing | [CONTRIBUTING.md](CONTRIBUTING.md) |
| YOLOv8 Docs | [docs.ultralytics.com](https://docs.ultralytics.com) |
| Streamlit Docs | [docs.streamlit.io](https://docs.streamlit.io) |

---

## ❓ Troubleshooting

### Port Already in Use
```bash
streamlit run yolo_tanima.py --server.port=8502
```

### Out of Memory
- Switch to Nano model
- Use lower resolution images

### WebRTC Camera Issues
- Check browser permissions
- Use HTTPS for camera access (required on deployed apps)
- Try a different browser

### Models Not Downloading
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

---

## 📊 What Can It Detect?

YOLOv8 recognizes **80 COCO classes** including:
- 🚗 Vehicles (car, truck, bus, motorcycle, bicycle)
- 🦁 Animals (dog, cat, bird, horse, cow, bear, zebra, giraffe)
- 👤 People
- 🍎 Food items
- 💻 Electronics
- 🪑 Furniture
- And 60+ more!

---

## 🎯 Next Steps

1. **Read** [README.md](README.md) for full features
2. **Deploy** using [DEPLOYMENT.md](DEPLOYMENT.md)
3. **Customize** the interface
4. **Contribute** improvements

---

## 🆘 Need Help?

- 📧 Open an issue on GitHub
- 💬 Check existing issues
- 📚 Read the documentation
- 🔍 Search online forums

---

**Happy detecting! 🎉**
