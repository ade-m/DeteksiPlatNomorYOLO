import cv2
import torch
import numpy as np
import easyocr
import requests
import tempfile

# Inisialisasi EasyOCR Reader
reader = easyocr.Reader(['en'])

# Unduh model dari Hugging Face
model_url = "https://huggingface.co/ademaulana/DeteksiPlatNomorYOLO/resolve/main/best.pt"
response = requests.get(model_url)
if response.status_code == 200:
    # Simpan model ke file sementara
    temp_model_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pt").name
    with open(temp_model_path, "wb") as f:
        f.write(response.content)
else:
    print("Gagal mengunduh model dari Hugging Face.")
    exit()

# Muat model YOLO dari file sementara
model = torch.hub.load('ultralytics/yolov5', 'custom', path=temp_model_path)

# Path ke file video
video_path = "/Users/ademaulana/Documents/OCRImg/plate/mobil.mov"

def detect_plate(frame):
    """Deteksi plat nomor menggunakan YOLO dan EasyOCR."""
    # Deteksi objek menggunakan YOLO
    results = model(frame)
    detections = results.xyxy[0]  # Hasil prediksi (x1, y1, x2, y2, confidence, class)

    for *box, confidence, cls in detections.tolist():
        # Koordinat bounding box
        x1, y1, x2, y2 = map(int, box)
        label = model.names[int(cls)]

        if label == 'platnomor':  # Pastikan hanya mendeteksi kelas 'plat_nomor'
            # Ekstrak area plat nomor
            plate_region = frame[y1:y2, x1:x2]

            # Gunakan EasyOCR untuk membaca teks
            result = reader.readtext(plate_region)
            plate_text = ""
            if result:
                plate_text = " ".join([detection[1] for detection in result])

            # Gambar kotak di sekitar plat nomor
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Tambahkan teks plat nomor pada frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.9
            font_thickness = 2
            text_size = cv2.getTextSize(plate_text, font, font_scale, font_thickness)[0]
            text_x = x1
            text_y = y1 - 10
            text_width = text_size[0]
            text_height = text_size[1]
            cv2.rectangle(frame, (text_x, text_y - text_height), (text_x + text_width, text_y + 5), (0, 255, 0), -1)
            cv2.putText(frame, plate_text, (text_x, text_y), font, font_scale, (255, 255, 255), font_thickness)
            print(f"Detected Plate: {plate_text}")
    return frame

# Muat video
cap = cv2.VideoCapture(video_path)

# Periksa apakah video berhasil dimuat
if not cap.isOpened():
    print("Gagal membuka video.")
    exit()

# Ambil frame rate video
fps = cap.get(cv2.CAP_PROP_FPS)
interval = 1  # Interval dalam detik

# Ambil resolusi video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Atur resolusi baru (opsional)
new_width = frame_width // 2
new_height = frame_height // 2

# Mulai deteksi dari waktu 0
current_time = 0

while True:
    # Atur posisi waktu dalam video
    cap.set(cv2.CAP_PROP_POS_MSEC, current_time * 1000)

    # Baca frame dari video
    ret, frame = cap.read()
    if not ret:
        print("Video selesai atau tidak dapat dibaca.")
        break

    # Ubah ukuran frame (opsional)
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Deteksi plat nomor pada frame
    processed_frame = detect_plate(resized_frame)

    # Tampilkan frame hasil deteksi
    cv2.imshow("Detected License Plate", processed_frame)

    # Tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Pindah ke detik berikutnya
    current_time += interval

# Tutup semua jendela
cap.release()
cv2.destroyAllWindows()
