import random as ran

sonlar = []

for i in range(50):
    son = ran.randint(1, 1000)
    sonlar.append(son)
sonlar.sort()
print(sonlar)
bosh = 0
oxir = len(sonlar) - 1
search = int(input(f"Qidirmoqchi bo'lgan sonni kiriting>>>"))
while True:
    orta = int((oxir + bosh) / 2)
    if search == sonlar[orta]:
        print(f"Qidirilayotgan son {orta}-indeksda joylashgan")
        break
    elif search > sonlar[orta]:
        bosh = orta
    else:
        oxir = orta
    if oxir - bosh == 1:
        print(f"Qidirilayotgan son massivda yo'q")
        break
