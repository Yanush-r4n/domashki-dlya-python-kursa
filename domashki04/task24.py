import os
os.system("cls")

gryadka = [1, 3, 4, 6, 5, 2, 1]

urozhai_treh_kustov = {}

for kust in range(len(gryadka)):
    if kust - 3 < 0:
        tri_kusta = gryadka[kust-3::] + gryadka[:kust:]
    else:
        tri_kusta = gryadka[kust-3:kust:]

    if not sum(tri_kusta) in urozhai_treh_kustov:
        urozhai_treh_kustov[sum(tri_kusta)] = [tri_kusta]
    else:
        urozhai_treh_kustov[sum(tri_kusta)].append(tri_kusta)

max_urozhai = max(urozhai_treh_kustov.keys())
tri_kusta = urozhai_treh_kustov[max_urozhai]

print(f"{tri_kusta} => {max_urozhai}")