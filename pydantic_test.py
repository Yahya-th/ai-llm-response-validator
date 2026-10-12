# Pydantic, Python'a gelen dış verileri içeri almadan önce denetleyen ve dönüştüren bir güvenlik kapısıdır.

# Kısaca yaptığı işler şunlardır:

# Veri Tipini Zorunlu Kılar: Normal Python : int veya : str yazdığında veri tipini denetlemez; Pydantic ise kurala uymayan veriyi içeri sokmaz ve doğrudan ValidationError fırlatır.

# Akıllı Dönüştürme Yapar (Coercion): Sayı olması gereken yere string olarak "25" gelirse, bunu otomatik ve hatasız bir şekilde sayısal 25 (int) değerine çevirir.

# Format ve Sınır Kontrolü Sağlar: Yaşın eksi olamayacağını, bir model sıcaklık (temperature) değerinin 0.0 ile 2.0 arasında kalması gerektiğini tek satırla denetler.

# Yapay Zekanın Çıktısını Sabitler (Structured Output): LLM'ler (OpenAI, Claude, Gemini vb.) bazen beklenmedik metinler üretir; modele bir Pydantic modeli verdiğinde cevabı tam istediğin JSON şablonunda döner.



"""
# Örnek hata veren pydantic kullanımı
from pydantic import BaseModel

class Kullanici(BaseModel):
    ad: str
    yas: int

# Durum 1: String sayı gelirse otomatik düzeltir (Type Coercion)
k1 = Kullanici(ad="Ahmet", yas="25") 
print(k1.yas)  # Çıktı: 25 (Otomatik int yaptı!)

# Durum 2: Saçma veri gelirse sistemi çökertmeden yakalar
k2 = Kullanici(ad="Ahmet", yas="yirmi")
# ValidationError fırlatır: "yas alanı geçerli bir tamsayı olmalıdır!"
"""


# Hata vermeyen şekilde pydantic kullanımı

from pydantic import BaseModel, ValidationError

class Kullanici(BaseModel):
    ad: str
    yas: int

gelen_veri = {"ad": "Ahmet", "yas": "yirmi"}    # Hatalı veri: yas alanı int olmalı ama string geldi.

try:
    k = Kullanici(**gelen_veri)
    print("Veri geçerli:", k)
except ValidationError as e:
    print("Yapay zekadan / kullanıcıdan hatalı veri geldi:")
    print(e.errors()[0]["msg"])



# Field ve Doğrulama (Validation) 
"""
Normalde BaseModel sadece veri tiplerine bakar (int, str vb.). Ancak yapay zeka projelerinde verinin sınırları da kritiktir:

Modelin sıcaklık parametresi (temperature) 0.0 ile 2.0 arasında olmalıdır.

max_tokens değeri 1'den küçük olamaz.

Bir kullanıcının girdiği prompt en az 3 karakter olmalıdır.

Bunu sağlamak için Pydantic'ten Field kullanılır:
"""

# Örnek Kod

from pydantic import BaseModel, Field

class LLMIstekYapilandirmasi(BaseModel):
    model_adi: str = Field(default="gpt-4o", description="Kullanılacak model adı")
    prompt: str = Field(min_length=3, max_length=500, description="Kullanıcı girdisi")
    temperature: float =Field(default=0.7, ge=0.0, le=2.0)   # ge: >= (büyük eşit), le: <= (küçük eşit)
    max_tokens: int = Field(default=500, gt=0, le=4096)      # gt: > (büyük)
    