ilk_liste = [1, 2, 3, 4, 5, 6]
ikinci_liste = [4, 5, 6, 7]
ucuncu_liste =(5, 6, 7, 8 )

ilk_ikilist_ortak_elemanlar = []

for eleman in ilk_liste:
    if eleman in ikinci_liste:
        ilk_ikilist_ortak_elemanlar.append(eleman)
print(ilk_ikilist_ortak_elemanlar) # [4, 5, 6]

ortak_eleman=[eleman for eleman in ilk_liste if eleman in ikinci_liste and eleman in ucuncu_liste]

print(ortak_eleman) #[5, 6]