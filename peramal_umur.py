import random

a = input("Apakah kamu siap untuk diramal?(Ya?Tidak) ")
if a == "Tidak":
    print("Baik, senang bertemu dangan kamu, DATANG KEMBALI!!!")
b = input("Siapa nama kamu? ")
c = int(input("Berapa umur kamu? "))
d = random.randint(c,110)
if d > 100:   
    Umur = ["ABADI", "TIDAK DAPAT DIRAMAL"]
    d = random.choice(Umur)
Kematian = ["Ketabrak Truk", "Sakit Jantung", "Tenggelam", "Kanker", "Diabetes"]
e = random.choice(Kematian)
print("----------------------------------------------------------------\n", "Nama: ", b, "\n", "Mati Pada Umur: ", d, "\n", "Latar Belakang: ", e, "\n","----------------------------------------------------------------")