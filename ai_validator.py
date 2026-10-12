from pydantic import BaseModel, Field, ValidationError
import json

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


# 1.TEST Doğru veri senaryosu     Validation: Veriyi aldık, Pydantic kurallarıyla (Field) denetledik.
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


model = AIYanitModeli(
    kullanici_id = 103,
    yanit_metni = "Yapay zeka yaniti basariyla uretidi ve dogrulandi.",
    guven_skoru = 0.93,
    harcanan_token = 35,
    durum = "basarili"              # Durum zaten varsayılan olarak "basarili" olduğu için bunu yazamasak da olur.
)

# Nesneyi dict yapıp yanitlar.json dosyasına kaydediyoruz.(Serialization)
# Serialization: Doğrulanmış objeyi model_dump() ile alıp json.dump() kullanarak dosyaya yazdık.

with open("yanitlar.json", "w", encoding="utf-8") as f:
    json.dump(model.model_dump(), f, ensure_ascii=False, indent=4)

print("Dogrukanmis veri yanitlar.json dosyasina yazildi.")


# Şimdi tam tersini yapıyoruz JSON'dan verileri çekip okuyoruz.(Deserialization)
# Deserialization: json.load() ile dosyadan okuyup AIYanitModeli(**veri) ile tekrar Pydantic nesnesi yaptık.

with open("yanitlar.json", "r", encoding="utf-8") as f:
    okunan_veri = json.load(f)

yuklenen_model = AIYanitModeli(**okunan_veri)
print(f"JSON'dan Okundu ve Doğrulandı: {yuklenen_model.yanit_metni} (Kullanici ID: {yuklenen_model.kullanici_id})")


        