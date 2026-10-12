from pydantic import BaseModel, Field

class KullanilanArac(BaseModel):
    arac_adi : str = Field(min_length=2)
    basarili_mi : bool = True     
    calisma_suresi_ms : float = Field(gt=0.0)

class AjanEylemLog(BaseModel):
    ajan_id: str
    gorev_tanimi: str = Field(min_length=5)
    kullanilan_arac : KullanilanArac
    onaylandi_mi: bool = False

veri = {
    "ajan_id" : "agent-101",
    "gorev_tanimi" : "İnternette en güncel Python haberlerini arama",
    "kullanilan_arac" : {
        "arac_adi" : "sql_query_tool",
        "basarili_mi" : True,
        "calisma_suresi_ms" : 145.50
    },
    "onaylandi_mi" : True

}

# Modeli test verisiyle oluşturuyoruz
log_nesnesi = AjanEylemLog(**veri)

# JSON string olarak ekrana yazdırma 
print("--- JSON String Çıktısı ---")
print(log_nesnesi.model_dump_json(indent=2))

# 'ajan_loglari.json' dosyasına kaydediyoruz
import json

with open("ajan_loglari.json", "w", encoding="utf-8") as f:
    json.dump(log_nesnesi.model_dump(), f, ensure_ascii=False, indent=4)

print("\nLog basariyla ajan_loglari.json dosyasina yazildi")