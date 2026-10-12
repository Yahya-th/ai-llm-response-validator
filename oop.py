class Araba():
    def __init__(self,marka,model,fiyat,renk):
        self.gelenMarka = marka
        self.gelenModel = model
        self.gelenFiyat = fiyat
        self.gelenRenk = renk

    def bilgileriYazdir(self):
        print(self.gelenMarka,self.gelenModel,self.gelenFiyat,self.gelenRenk)

    def renkDegistir(self,yeniRenk):
        self.gelenRenk = yeniRenk


araba1 = Araba("BMW","X5",1000000,"Siyah")

araba1.bilgileriYazdir()                         # BMW X5 1000000 Siyah
araba1.renkDegistir("Beyaz")
araba1.bilgileriYazdir()                         # BMW X5 1000000 Beyaz   



# Inheritance (Kalıtım) Örneği
# Ata(Parent) Sınıfı

class AIAjan():
    def __init__(self,ajan_adi,model):
        self.ajan_adi = ajan_adi
        self.model = model

    def durumBilgisi(self):
        print(f"{self.ajan_adi} göreve hazır.")

class KodlamaAjani(AIAjan):
    def __init__(self,ajan_adi,model,uzman_dil):
        super().__init__(ajan_adi,model)
        self.uzman_dil = uzman_dil

    def kod_uret(self):
        print(f"{self.ajan_adi}, {self.uzman_dil} dilinde kod yaziyor.")


KodlamaAjani1 = KodlamaAjani("DevBot", "claude-3-5", "Python")

KodlamaAjani1.durumBilgisi()
KodlamaAjani1.kod_uret()



