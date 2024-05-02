"""
Maps Graph of Sichuan Province, China
This program was made by kelompok 1 Struktur Data UNESA to fulfill project from our teacher Mr. I Gde Agung Sri Sidhimantra S.Kom M.Kom

Our member
1. Sekar Hanum (148)
2. Adip Setyaputra (158)
3. Regha Rahmadian Bintang (156)

See more on our github
https://github.com/SekarHanum/

"""
class Peta:
    def __init__(self):
        self.listkota = {}
    
    def tambahkota(self,kota):
        if kota not in self.listkota:
            self.listkota[kota] = {}
            print(f'Kota {kota} ditambahkan kedalam Peta')
    
    def tambahJalan(self,kota1,kota2,jarak):
        if kota1 and kota2 in self.listkota:
            self.listkota[kota1][kota2] = jarak
            self.listkota[kota2][kota1] = jarak
            print(f'Jalan antara kota {kota1} dan kota {kota2} sejauh {jarak}Km telah ditambahkan ke dalam Peta')

    def hapusKota(self,kotadihapus):
        if kotadihapus in self.listkota:
            for kota in self.listkota:
                if kotadihapus in self.listkota[kota]:
                    del self.listkota[kota][kotadihapus]
            del self.listkota[kotadihapus]
            print(f'Kota {kotadihapus} telah dihapus dari Peta')

    def hapusjalan(self,kota1,kota2):
        if kota1 and kota2 in self.listkota:
            del self.listkota[kota1][kota1]
            del self.listkota[kota2][kota1]
            print(f'Jalan antara kota {kota1} dan kota {kota2} telah dihapus dari Peta')
    
    def hitungkota(self):
        hitungan = 0
        for kota in self.listkota:
            if kota in self.listkota:
                hitungan += 1
        print(f'Jumlah kota yang ada pada peta ada {hitungan} kota')
        return hitungan
    
    def printpeta(self):
        for kota in self.listkota:
            print(f'{kota} -> {self.listkota[kota]}')

#Testzone
PetaTiongkok = Peta()
#Tambah Kota
PetaTiongkok.tambahkota("Garze Tibetan")
PetaTiongkok.tambahkota("Liangshan Yi")
PetaTiongkok.tambahkota("Panzhihua")
PetaTiongkok.tambahkota("Yaan")
PetaTiongkok.tambahkota("Meishan")
PetaTiongkok.tambahkota("Leshan")
PetaTiongkok.tambahkota("Chengdu")
PetaTiongkok.tambahkota("Deyang")
PetaTiongkok.tambahkota("Dazhou")
PetaTiongkok.tambahkota("Nanchong")
PetaTiongkok.tambahkota("Guang'an")
PetaTiongkok.tambahkota("Suining")
PetaTiongkok.tambahkota("Ziyang")
PetaTiongkok.tambahkota("Neijiang")
PetaTiongkok.tambahkota("Zigong")
PetaTiongkok.tambahkota("Yibin")
PetaTiongkok.tambahkota("Luzhou")
#Tambah Jalan
PetaTiongkok.tambahJalan("Garze Tibetan","Yaan",132)
PetaTiongkok.tambahJalan("Liangshan Yi","Panzhihua",215)
PetaTiongkok.tambahJalan("Liangshan Yi","Yaan",310)
PetaTiongkok.tambahJalan("Yaan","Chengdu",132)
PetaTiongkok.tambahJalan("Yaan","Meishan",103)
PetaTiongkok.tambahJalan("Meishan","Ziyan",114)
PetaTiongkok.tambahJalan("Meishan","Yaan",103)
PetaTiongkok.tambahJalan("Meishan","Leshan",76)
PetaTiongkok.tambahJalan("Leshan","Ziyang",141)
PetaTiongkok.tambahJalan("Leshan","Zigong",126)
PetaTiongkok.tambahJalan("Leshan","Yibin",162)
PetaTiongkok.tambahJalan("Chengdu","Deyang",84)
PetaTiongkok.tambahJalan("Chengdu","Suining",169)
PetaTiongkok.tambahJalan("Chengdu","Ziyang",101)
PetaTiongkok.tambahJalan("Deyang","Dazhou",421)
PetaTiongkok.tambahJalan("Deyang","Nanchong",220)
PetaTiongkok.tambahJalan("Dazhou","Guang'an",199)
PetaTiongkok.tambahJalan("Dazhou","Suining",168)
PetaTiongkok.tambahJalan("Nanchong","Guang'an",199)
PetaTiongkok.tambahJalan("Nanchong","Suining",76)
PetaTiongkok.tambahJalan("Guang'an","Suining",121)
PetaTiongkok.tambahJalan("Suining","Neijiang",145)
PetaTiongkok.tambahJalan("Suining","Ziyang",139)
PetaTiongkok.tambahJalan("Ziyang","Neijiang",93)
PetaTiongkok.tambahJalan("Neijiang","Zigong",45)
PetaTiongkok.tambahJalan("Neijiang","Luzhou",102)
PetaTiongkok.tambahJalan("Zigong","Luzhou",95)
PetaTiongkok.tambahJalan("Zigong","yibin",81)
PetaTiongkok.tambahJalan("Yibin","Luzhou",121)
#Hitung Kota
PetaTiongkok.hitungkota()
#Print Peta
PetaTiongkok.printpeta()
