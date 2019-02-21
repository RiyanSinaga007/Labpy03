print("===== LATIHAN 1 =====")
import random

jumlah = int(input("Masukkan jumlah n : "))
a = 0

for i in range(jumlah):
    a +=1
    b = random.uniform(.0,.5)
    print('Data ke :',a,'==>',b)
print("===== SELESAI =====")
