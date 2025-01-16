# Deteksi dan Pengenalan Plat Nomor Berbasis YOLO  

Repositori ini menunjukkan proses transisi dari metode tradisional deteksi tepi Sobel ke model YOLO untuk deteksi plat nomor kendaraan. Dengan menggunakan YOLO, deteksi plat nomor menjadi jauh lebih akurat, menghilangkan deteksi palsu yang sering terjadi pada metode berbasis tepi.  

## 🎯 Fitur Utama  
- **Persiapan Dataset:**  
  Penandaan data menggunakan LabelImg, konversi label, dan pengorganisasian folder terstruktur (set `train` dan `val` untuk gambar dan label).  
- **Pelatihan Model YOLO:**  
  Pelatihan dilakukan pada **200 gambar kendaraan** yang telah diberi anotasi selama **50 epoch**, dengan hasil performa yang mengesankan:  
  - Presisi: **88,3%**  
  - Recall: **80%**  
  - mAP@0.5: **88,7%**  
- **Integrasi dengan EasyOCR:**  
  Plat nomor yang terdeteksi dibaca menggunakan EasyOCR dengan mengabaikan karakter khusus untuk output yang lebih bersih.  
- **Penggantian yang Mulus:**  
  Model berbasis YOLO menggantikan metode deteksi tepi Sobel sebelumnya dalam pipeline.  

## 🗂️ Struktur File Dataset  
```plaintext  
dataset/  
├── images/  
│   ├── train/  
│   └── val/  
├── labels/  
│   ├── train/  
│   └── val/


## 📊 Highlight Performa
```plaintext  
Presisi: 88,3%
Recall: 80%
mAP@0.5: 88,7%
mAP@0.5:0.95: 49,2%
🌐 Media Sosial

## Ikuti perjalanan saya di media sosial untuk proyek-proyek seru lainnya:
```plaintext  
TikTok: @ademaulana_4
Instagram: @ademaulana_
Terima kasih telah berkunjung! Jangan ragu untuk memberi saran atau berkontribusi. 🚀


### Cara Menggunakan:
```plaintext  
1. Salin isi di atas.
2. Simpan ke file `README.md` di repositori Anda.
3. Tautan media sosial akan otomatis dapat diklik jika diunggah ke GitHub.

Jika Anda memerlukan tambahan lainnya, beri tahu saya! 😊
