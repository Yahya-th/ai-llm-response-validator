# .model_dump() : Pydantic modelini saf bir Python sözlüğüne (dict) çevirir.
# .model_dump_json() : Pydantic modelini doğrudan bir JSON string formatına çevirir.



from pydantic import BaseModel, Field

class AjanModeli(BaseModel):
    id: int
    ad: str
    aktif: bool = True

ajan = AjanModeli(id=1, ad="Çeviri Botu")

# 1. Sözlüğe Çevirme
sozluk = ajan.model_dump()
print(type(sozluk))  # <class 'dict'>
print(sozluk)        # {'id': 1, 'ad': 'Çeviri Botu', 'aktif': True}

# 2. JSON String'e Çevirme
json_veri = ajan.model_dump_json()
print(type(json_veri)) # <class 'str'>
print(json_veri)       # {"id":1,"ad":"Çeviri Botu","aktif":true}




import json
from pydantic import BaseModel

# 1. Pydantic Modelini Tanımlıyoruz
class AjanModeli(BaseModel):
    id: int
    ad: str

# 2. Nesneyi Oluşturuyoruz
ajan = AjanModeli(id=1, ad="Çeviri Botu")

# 3. Pydantic nesnesini dict'e çevirip JSON dosyasına yazıyoruz
# (json.dump standart Python kütüphanesidir, from pydantic demeye gerek yoktur)
with open("ajanlar.json", "w", encoding="utf-8") as f:
    json.dump(ajan.model_dump(), f, ensure_ascii=False, indent=4)