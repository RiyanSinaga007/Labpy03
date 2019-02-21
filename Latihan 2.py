print("===== LATIHAN 2 =====")
print("Menampilkan bilangan, Berhenti ketika bilangan 0, dan Menampilkan Bilangan Terbesar")
max=0
while True:
    a=int(input("Masukkan Bilangan = "))
    if max < a :
        max = a
    if a==0:
        break
print("Bilangan Terbesarnya adalah = ",max)
