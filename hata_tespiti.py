try:
    tokenSayisi = int(input("Token miktarını giriniz: "))
    sonuc = 1000 / tokenSayisi

except ValueError:
    print("Hata: Lütfen geçerli bir tamsayı gir!")

except ZeroDivisionError:
    print("Hata: Token miktarı sıfır olamaz!")

else:
    print(f"İşlem başarılı! Sonuç: {sonuc}")