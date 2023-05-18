import random as ran

sonlar = []

for i in range(17):
    son = ran.randint(1, 100)
    sonlar.append(son)
sonlar.sort()
bosh = 0
oxir = len(sonlar) - 1
print(sonlar)
input(f"Biror son oylang\n oylagan bolsangiz enterni bosing")
orta = int((bosh + oxir) / 2)
print(f"siz oylagan son  {sonlar[orta]} \nagar siz "
      f"oylagan son bundan katta bolsa +\nkichik bolsa - qoying togri bolsa T qoying")
javob = input(">>")


def orta_son():
    global javob
    global oxir
    global bosh
    while True:
        orta = int((bosh + oxir) / 2)
        print(
            f"siz oylagan son  {sonlar[orta]} \nagar siz "
            f"oylagan son bundan katta bolsa +\nkichik bolsa - qoying togri bolsa T qoying")
        javob = input(">>")
        if javob == "+":
            bosh = orta
        elif javob == "-":
            oxir = orta
        else:
            print("Togri topibman !!")
            break


if javob == "T":
    print("Togri topibman !!")
else:
    if javob == "-":
        oxir = orta
    elif javob == "+":
        bosh = orta
    orta_son()