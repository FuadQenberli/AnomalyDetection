# 🛡️ Anomaliya Tapma Sistemi – NSL_KDD ilə Şəbəkə Hücumlarının Aşkarlanması

Bu layihə, "machine learning" istifadə edərək şəbəkə hücumlarını avtomatik şəkildə aşkarlayan sadə bir sistemdir. **NSL_KDD** məlumat dəstindən istifadə olunmuşdur.

## 📌 Layihənin Məqsədi

- Normal və hücum trafiki arasında fərq qoymaq
- Anomaliya əsaslı aşkarlama ilə şəbəkə təhlükəsizliyini gücləndirmək
- Yeni başlayanlar üçün praktik maşın öyrənməsi layihəsi yaratmaq

## 🧰 İstifadə Olunan Texnologiyalar

- **Python**
- `pandas`, `scikit-learn`
- **Isolation Forest** modeli

## Dataset

Layihədə istifadə olunan dataset:
- [NSL_KDD Dataset](https://github.com/defcom17/NSL_KDD)

### Əsas fayllar:
- `KDDTrain+.txt`
- `KDDTest+.txt`
- `Field Names` – sütun adları üçün fayl

## ⚙️ İstifadə Qaydası

```bash
# Lazımi kitabxanaları quraşdırın
pip install pandas scikit-learn

# Python skriptini işə salın
python anomaly.py
