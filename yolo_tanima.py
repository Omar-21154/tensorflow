# ============================================================
#   Əşya Tanıma - YOLOv8 + Canlı Kamera (WebRTC)
#   İşlətmək: streamlit run yolo_tanima.py
# ============================================================

import streamlit as st
from ultralytics import YOLO
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration
from PIL import Image
import numpy as np
import cv2
import av
import logging

# ── Logging Configuration ──────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ── Səhifə ayarları ────────────────────────────────────────
st.set_page_config(
    page_title="YOLOv8 · Əşya Tanıma",
    page_icon="🎯",
    layout="centered"
)

# ── CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Mono:wght@400;500&display=swap');
.stApp { background:#080c14; color:#e8eaf0; font-family:'Syne',sans-serif; }
.hero  { text-align:center; padding:2rem 0 1rem 0; }
.hero h1 {
    font-size:2.8rem; font-weight:800;
    background:linear-gradient(135deg,#facc15 0%,#f97316 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero p { color:#6b7280; font-family:'DM Mono',monospace; font-size:0.85rem; }
.stat-big {
    text-align:center; background:#111827; border:1px solid #1f2937;
    border-radius:12px; padding:1rem;
}
.stat-num { font-size:2.2rem; font-weight:800; color:#facc15; }
.stat-lbl { font-family:'DM Mono',monospace; font-size:0.7rem; color:#6b7280; letter-spacing:1px; }
.result-card {
    background:#0d1117; border:1px solid #1f2937;
    border-radius:16px; padding:1rem 1.4rem; margin:0.4rem 0;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🎯 YOLOv8 Vision</h1>
    <p>real-time object detection · canlı video · 80 sinif</p>
</div>
""", unsafe_allow_html=True)

# ── Model seçimi ───────────────────────────────────────────
model_secim = st.select_slider(
    "Model gücu:",
    options=["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"],
    value="yolov8s.pt",
    format_func=lambda x: {
        "yolov8n.pt": "⚡ Nano — çox sürətli",
        "yolov8s.pt": "⚖️ Small — balanslaşdırılmış",
        "yolov8m.pt": "🎯 Medium — daha dəqiq"
    }[x]
)

@st.cache_resource
def model_yukle(ad):
    try:
        logger.info(f"Loading model: {ad}")
        model = YOLO(ad)
        logger.info(f"Model loaded successfully: {ad}")
        return model
    except Exception as e:
        logger.error(f"Error loading model {ad}: {str(e)}")
        st.error(f"❌ Model yükləmə xətası: {str(e)}")
        st.stop()

with st.spinner("⚡ Model yüklənir..."):
    try:
        model = model_yukle(model_secim)
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        st.error("Model yükləmə uğursuz oldu. Sayfanı yeniləyin.")
        st.stop()

# ── Dəqiqlik həddi ─────────────────────────────────────────
conf = st.slider(
    "Minimum əminlik həddi", 0.1, 0.9, 0.30, 0.05,
    help="Aşağı = daha çox nəticə | Yuxarı = az amma dəqiq"
)

# ── Rejim seçimi ───────────────────────────────────────────
rejim = st.radio(
    "Rejim:", ["🎥 Canlı video", "📷 Foto çək", "📁 Fayl yüklə"],
    horizontal=True, label_visibility="collapsed"
)


# ── Analiz funksiyası (foto + fayl üçün) ──────────────────
def analiz_et(sekil):
    try:
        img_np    = np.array(sekil)
        results   = model.predict(img_np, conf=conf, verbose=False)[0]
        annotated = cv2.cvtColor(results.plot(), cv2.COLOR_BGR2RGB)
        st.image(annotated, use_container_width=True)

        boxes = results.boxes
        sayi  = len(boxes)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f'<div class="stat-big"><div class="stat-num">{sayi}</div>'
                f'<div class="stat-lbl">TAPILAN ƏŞYA</div></div>',
                unsafe_allow_html=True)
        with col2:
            mx = float(boxes.conf.max()) * 100 if sayi > 0 else 0
            st.markdown(
                f'<div class="stat-big"><div class="stat-num">{mx:.0f}%</div>'
                f'<div class="stat-lbl">MAX ƏMİNLİK</div></div>',
                unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if sayi == 0:
            st.warning("⚠️ Heç nə tapılmadı — dəqiqlik həddini aşağı sal.")
        else:
            for box in boxes:
                ad  = model.names[int(box.cls[0])].replace("_", " ").title()
                pct = float(box.conf[0]) * 100
                st.markdown(f"""
                <div class="result-card">
                    <span style="font-weight:700;font-size:1.05rem">📦 {ad}</span>
                    <span style="float:right;font-family:'DM Mono',monospace;
                        color:#facc15;font-weight:700">{pct:.1f}%</span>
                    <div style="background:#1f2937;border-radius:999px;height:5px;margin-top:8px">
                        <div style="width:{pct:.0f}%;
                            background:linear-gradient(90deg,#facc15,#f97316);
                            height:5px;border-radius:999px"></div>
                    </div>
                </div>""", unsafe_allow_html=True)
        logger.info(f"Analysis complete. Objects detected: {sayi}")
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        st.error(f"❌ Analiz xətası: {str(e)}")



# ══════════════════════════════════════════════════════════
# 🎥 CANLİ VİDEO — WebRTC (brauzer kamerası)
# ══════════════════════════════════════════════════════════
if rejim == "🎥 Canlı video":
    st.info("📹 'START' düyməsinə bas → brauzer kamera icazəsi istəyəcək → İcazə ver!")

    # Hər frame üçün YOLO işləyən sinif
    class YoloProcessor(VideoProcessorBase):
        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            try:
                img = frame.to_ndarray(format="bgr24")

                # YOLO ilə analiz et
                results = model.predict(img, conf=conf, verbose=False)[0]
                annotated = results.plot()  # qutuları çək

                return av.VideoFrame.from_ndarray(annotated, format="bgr24")
            except Exception as e:
                logger.error(f"Error in video processing: {str(e)}")
                # Return original frame on error
                return frame

    try:
        # WebRTC streamer — brauzerdən kamera açır
        webrtc_streamer(
            key="yolo-stream",
            video_processor_factory=YoloProcessor,
            rtc_configuration=RTCConfiguration(
                {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
            ),
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )
        logger.info("WebRTC streamer started successfully")
    except Exception as e:
        logger.error(f"WebRTC error: {str(e)}")
        st.error("❌ WebRTC bağlantı xətası. Brauzer kamera icazəsini yoxlayın.")


# ══════════════════════════════════════════════════════════
# 📷 FOTO
# ══════════════════════════════════════════════════════════
elif rejim == "📷 Foto çək":
    kamera = st.camera_input("", label_visibility="collapsed")
    if kamera:
        try:
            with st.spinner("🔍 Analiz edilir..."):
                analiz_et(Image.open(kamera).convert("RGB"))
                logger.info("Photo analysis completed")
        except Exception as e:
            logger.error(f"Camera input error: {str(e)}")
            st.error("❌ Fotoya çevrilmə xətası.")

# ══════════════════════════════════════════════════════════
# 📁 FAYL
# ══════════════════════════════════════════════════════════
else:
    fayl = st.file_uploader("", type=["jpg","jpeg","png"],
                            label_visibility="collapsed")
    if fayl:
        try:
            with st.spinner("🔍 Analiz edilir..."):
                analiz_et(Image.open(fayl).convert("RGB"))
                logger.info(f"File analysis completed: {fayl.name}")
        except Exception as e:
            logger.error(f"File upload error: {str(e)}")
            st.error("❌ Fayl oxuma xətası. Başqa fayl yüklənməsi cəhd edin.")

# ══════════════════════════════════════════════════════════
# 📝 Footer
# ══════════════════════════════════════════════════════════
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="text-align:center;font-size:0.8rem;color:#6b7280">
    <strong>🎯 YOLOv8</strong><br>
    Real-time Detection
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="text-align:center;font-size:0.8rem;color:#6b7280">
    <strong>⚡ Streamlit</strong><br>
    Web Framework
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="text-align:center;font-size:0.8rem;color:#6b7280">
    <strong>🔥 Live</strong><br>
    GPU Accelerated
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;font-size:0.75rem;color:#4b5563;margin-top:1rem">
Made with ❤️ | 80 COCO Classes | v1.0
</div>
""", unsafe_allow_html=True)
