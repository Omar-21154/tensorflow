# ============================================================
#   Şəkil Tanıma Proqramı - TensorFlow / Keras
#   Nə edir: Əl ilə yazılmış rəqəmləri (0-9) tanıyır
#   Dataset: MNIST (60,000 şəkil - avtomatik yüklənir)
# ============================================================

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# ── 1. DATASETİ YÜKLƏ ──────────────────────────────────────
# MNIST: 28x28 piksel ağ-qara şəkillər (rəqəmlər 0-9)
print("📦 Dataset yüklənir...")
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Piksel dəyərlərini 0-255 aralığından 0-1 aralığına gətir
# (Model bu şəkildə daha yaxşı öyrənir)
x_train = x_train / 255.0
x_test  = x_test  / 255.0

print(f"✅ Train şəkilləri: {x_train.shape}")   # (60000, 28, 28)
print(f"✅ Test şəkilləri:  {x_test.shape}\n")  # (10000, 28, 28)


# ── 2. MODELİ QUR ──────────────────────────────────────────
# Sequential: qatları ardıcıl əlavə etmək üçün istifadə olunur
model = keras.Sequential([

    # Flatten: 28x28 şəkli → 784 ədəd sıra halına gətirir
    keras.layers.Flatten(input_shape=(28, 28)),

    # Dense(128): 128 neyronlu gizli qat, relu aktivasiyası ilə
    keras.layers.Dense(128, activation='relu'),

    # Dropout: öyrənmə zamanı 20% neyronu söndürür (overfitting-in qarşısını alır)
    keras.layers.Dropout(0.2),

    # Dense(10): 10 çıxış (0-9 rəqəmlər üçün)
    keras.layers.Dense(10, activation='softmax')
])

model.summary()  # Modelin quruluşunu göstər


# ── 3. MODELİ HAZIRLA ──────────────────────────────────────
model.compile(
    optimizer='adam',           # Öyrənmə alqoritmi
    loss='sparse_categorical_crossentropy',  # Zərər funksiyası
    metrics=['accuracy']        # Dəqiqliyi ölç
)


# ── 4. MODELİ ÖYRƏT ────────────────────────────────────────
print("\n🧠 Model öyrənir... (bu 1-2 dəqiqə çəkə bilər)\n")
tarixce = model.fit(
    x_train, y_train,
    epochs=5,           # 5 dəfə bütün datanı oxu
    validation_split=0.1,  # 10%-ni doğrulama üçün saxla
    verbose=1
)


# ── 5. MODELİ TEST ET ──────────────────────────────────────
print("\n📊 Test nəticəsi:")
itki, deqiqlik = model.evaluate(x_test, y_test, verbose=0)
print(f"   Dəqiqlik: {deqiqlik * 100:.2f}%")


# ── 6. NƏTİCƏLƏRİ VİZUAL GÖSTƏR ───────────────────────────
# Test setindən 10 şəkil götürüb proqnoz ver
tahminler = model.predict(x_test[:10])

plt.figure(figsize=(14, 4))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i], cmap='gray')

    dogru   = y_test[i]
    tahmin  = np.argmax(tahminler[i])
    renk    = 'green' if dogru == tahmin else 'red'

    plt.title(f"Düzgün: {dogru}\nTahmin: {tahmin}", color=renk, fontsize=9)
    plt.axis('off')

plt.suptitle("Model Proqnozları (Yaşıl=Düzgün, Qırmızı=Yanlış)", fontsize=12)
plt.tight_layout()
plt.savefig("netice.png", dpi=150)
plt.show()
print("\n🖼️  Nəticə 'netice.png' faylına saxlanıldı.")


# ── 7. MODELİ SAXLA ────────────────────────────────────────
model.save("reqem_tanima_modeli.h5")
print("💾 Model 'reqem_tanima_modeli.h5' faylına yazıldı.")
print("\n✅ Hər şey tamamdı!")
# 