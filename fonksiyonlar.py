def topla(sayi, yazi):
    for i in range(sayi):
        print(yazi)

topla(3, "CR7")           

# Bu fonksiyon 3 kere CR7 yazdırır.


def ebob(sayi1, sayi2):
    enKucukSayi = min(sayi1, sayi2)
    enBuyukOrtakBolen = 1

    for i in range(1, enKucukSayi + 1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            enBuyukOrtakBolen = i

    print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {enBuyukOrtakBolen}'dir.")

ebob(12, 18)  # Yani 6.

# Bu fonksiyon 12 ve 18 sayılarının EBOB'unu hesaplar ve ekrana yazdırır.

