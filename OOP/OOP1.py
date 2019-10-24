class HERO:
    def __init__(self, nama):
        self.Nama = nama

    def getNama(self):
        return self.Nama

    def setName(self, NamaPemain):
        self.Nama = NamaPemain

alwi = HERO("alwi yahya")

print(alwi.getNama())
