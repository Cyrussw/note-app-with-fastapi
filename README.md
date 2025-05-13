# FastAPI Not Uygulaması

# Açıklama:
# Bu uygulama, FastAPI ve SQLite kullanılarak geliştirilmiş sade bir not yönetim sistemidir.

# Gerekli Paketler:
pip install fastapi uvicorn sqlalchemy

# Uygulamayı Başlat:
uvicorn main:app --reload

# Endpointler:

# Yeni Not Ekle
curl -X POST "http://127.0.0.1:8000/notlar/?baslik=Test&icerik=İçerik"

# Tüm Notları Listele
curl -X GET "http://127.0.0.1:8000/notlar/"

# Not Güncelle
curl -X PUT "http://127.0.0.1:8000/notlar/1?baslik=Yeni&icerik=Yeniİçerik"

# Not Sil
curl -X DELETE "http://127.0.0.1:8000/notlar/1"

# Dosya Yapısı:
# .
# ├── main.py
# ├── models.py
# ├── database.py
# └── .gitignore

# Not:
# 'notlar.db' dosyası ve '__pycache__' klasörü .gitignore tarafından yoksayılır.
