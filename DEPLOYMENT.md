# YOLOv8 Streamlit App - Deployment Guide

## 🚀 Deployment Options

### 1. Streamlit Cloud (Recommended - FREE)

**Pros:** Free, easy, automatic updates, no server management
**Cons:** Limited resources, cold starts

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app" and select this repository
5. Select `yolo_tanima.py` as the main file
6. Deploy!

**Secrets Management:**
- Add `~/.streamlit/secrets.toml` for API keys (if needed)

---

### 2. Docker + Cloud Run (Google Cloud)

**Pros:** Scalable, good performance, supports GPU
**Cons:** Requires Google Cloud account

```bash
# Build Docker image
docker build -t yolo-vision .

# Test locally
docker run -p 8501:8501 yolo-vision

# Deploy to Google Cloud Run
gcloud run deploy yolo-vision --source . --platform managed --region us-central1 --allow-unauthenticated --memory=2Gi --timeout=600
```

---

### 3. Heroku

**Pros:** Simple deployment, free tier available
**Cons:** Slower cold starts, limited resources

```bash
# Install Heroku CLI
brew install heroku

# Login
heroku login

# Create app
heroku create your-yolo-app

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

---

### 4. Docker Compose (Local/VPS)

**Pros:** Full control, works anywhere
**Cons:** Manual management

```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# View logs
docker-compose logs -f
```

---

### 5. Linux VPS / Self-Hosted

**Steps:**
```bash
# SSH into server
ssh user@your-server

# Clone repository
git clone <repo-url>
cd tensorflow

# Install Python 3.9+
sudo apt update && sudo apt install python3.9 python3.9-venv python3-pip

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with systemd
sudo nano /etc/systemd/system/yolo-app.service
```

Add to service file:
```ini
[Unit]
Description=YOLOv8 Streamlit App
After=network.target

[Service]
User=your-user
WorkingDirectory=/home/your-user/tensorflow
ExecStart=/home/your-user/tensorflow/venv/bin/streamlit run yolo_tanima.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true
Restart=always
Environment="PATH=/home/your-user/tensorflow/venv/bin"

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable yolo-app
sudo systemctl start yolo-app
```

---

### 6. AWS Lambda + API Gateway

For AWS Lambda, you need to use a different approach (e.g., FastAPI wrapper), as Streamlit requires persistent connections.

---

## 📊 Performance Tips

1. **Use Nano Model** - Fastest for production
2. **Enable caching** - Already configured in app
3. **Adjust confidence** - Higher values = fewer detections = faster
4. **Use GPU** - For local/cloud with GPU support

```bash
# On GPU-enabled machine
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## 🔒 Security Considerations

1. **HTTPS/SSL** - Use Streamlit Cloud or reverse proxy (nginx)
2. **Rate limiting** - Add middleware for public deployments
3. **Model files** - Keep them private, don't commit to git
4. **Secrets** - Use `.streamlit/secrets.toml` for sensitive data

---

## 📈 Monitoring

For production deployments:
- Set up error tracking (Sentry)
- Add performance monitoring (Datadog)
- View logs regularly

---

## ❌ Troubleshooting

**Issue:** Models not downloading
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

**Issue:** WebRTC not working on HTTPS
- Use `streamlit-webrtc` latest version
- Ensure CORS is properly configured

**Issue:** Out of memory
- Switch to nano model
- Reduce video resolution
- Use smaller images

---

## 🎯 Estimated Costs

| Platform | Cost | Resources |
|----------|------|-----------|
| Streamlit Cloud | FREE | Limited |
| Google Cloud Run | ~$0.15-1/day | 2GB RAM, CPU |
| Heroku Free | FREE | 0.5GB RAM |
| AWS t3.micro | ~$5/month | 1GB RAM |
| VPS (Linode) | ~$5/month | 1GB RAM |

---

**Questions?** See [Streamlit Docs](https://docs.streamlit.io) or [YOLOv8 Docs](https://docs.ultralytics.com)
