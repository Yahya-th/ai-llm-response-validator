from pydantic import BaseModel, Field, ValidationError

class AIYanitModeli(BaseModel):
    kullanici_id: int = Field(gt=0)
    yanit_metni: str = Field(min_length=5, max_length=1000)
    guven_skoru: float = Field(ge=0.0, le=1.0)
    harcanan_token: int = Field(ge=1)
    durum: str = Field(default="basarili")

def yaniti_dogrula(veri: dict):
    try:
        model = AIYanitModeli(**veri)
        return f"Başariyla dogrulandı: {model.yanit_metni} (Skor: {model.guven_skoru})"
    except ValidationError as e:
        return f"Veri doğrulama hatası: {e.errors()}"


# 1.TEST Doğru veri senaryosu
gecerli_veri = {
    "kullanici_id": 101,
    "yanit_metni": "Yapay zeka yaniti basariyla dogrulandi.",
    "guven_skoru": 0.95,
    "harcanan_token": 42
}

print("-- Gecerli Veri Testi --")
print(yaniti_dogrula(gecerli_veri))


# 2.TEST Hatalı veri senaryosu
hatali_veri = {
    "kullanici_id": 102,
    "yanit_metni": "Hatalı veri testi.",
    "guven_skoru": 1.5,
    "harcanan_token": 10
}

print("\n-- Hatali Veri Testi --")
print(yaniti_dogrula(hatali_veri))