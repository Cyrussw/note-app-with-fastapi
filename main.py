from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import database, models

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()


# Veritabanı bağlantısı al
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Not Oluştur
@app.post("/notlar/")
def not_ekle(baslik: str, icerik: str, db: Session = Depends(get_db)):
    yeni_not = models.Not(baslik=baslik, icerik=icerik)
    db.add(yeni_not)
    db.commit()
    db.refresh(yeni_not)
    return yeni_not


# Notları Listele
@app.get("/notlar/")
def notlari_listele(db: Session = Depends(get_db)):
    return db.query(models.Not).all()


# Notu Sil
@app.delete("/notlar/{not_id}")
def not_sil(not_id: int, db: Session = Depends(get_db)):
    not_obj = db.query(models.Not).filter(models.Not.id == not_id).first()
    if not_obj is None:
        raise HTTPException(status_code=404, detail="Not Bulunamadı")
    db.delete(not_obj)
    db.commit()
    return {"mesaj": "Not silindi"}


# Not güncelle
@app.put("/notlar/{not_id}")
def not_guncelle(not_id: int, baslik: str, icerik: str, db: Session = Depends(get_db)):
    not_obj = db.query(models.Not).filter(models.Not.id == not_id).first()

    if not_obj is None:
        raise HTTPException(status_code=404, detail="Not yok")

    not_obj.baslik = baslik
    not_obj.icerik = icerik
    db.commit()
    return not_obj
