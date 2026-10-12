from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class AjanDurumu(str, Enum):
    CALISIYOR = "calisiyor"
    TAMAMLANDI = "tamamlandi"
    HATA = "hata"

class GorevLog(BaseModel):
    gorev_id : str
    durum : AjanDurumu
    etiketler : List[str] = Field(min_length=1)
    hata_detayi : Optional[str] = None


basarili_gorev = GorevLog(
    gorev_id = "task-001",
    durum = AjanDurumu.TAMAMLANDI, 
    etiketler = ["pyhton", "pydantic"],
    hata_detayi = None
)

hatali_gorev = GorevLog(
    gorev_id = "task-002",
    durum = AjanDurumu.HATA,
    etiketler = ["C++", "Inharitance"],
    hata_detayi = "API Zaman Asimi: Sunucu 500 hatasi döndü."
)

gorev_listesi = [basarili_gorev, hatali_gorev]

# Listeyi ekrana JSON olarak yazdırmak için
for gorev in gorev_listesi:
    print(gorev.model_dump_json(indent=2))