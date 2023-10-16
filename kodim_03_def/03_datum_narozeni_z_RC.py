rodne_cislo = input("Zadej rodné číslo bez lomítka: ")
cilo = int(rodne_cislo[2])
mesic = int(rodne_cislo[2:4])
print(mesic)
den = rodne_cislo[4:6]
rok = rodne_cislo[0:2]


def overeni_rodneho_cisla():
    if len(rodne_cislo)== 10:
        print("Rodné číslo je platné:")
    else:
        print("Zadali jste nesprávný tvar rodného čílsa.")

def muz_zena(mesic):
    if mesic > 50:
        return ("žena")
    elif mesic < 50:
        return ("muž")
               

def mesic_narozeni(mesic):
    if mesic > 50:
        return mesic - 50
    else:
        return mesic
    
print(f"""
Váš den narození je {den}.
Váš měsíc narození je {mesic_narozeni(mesic)}.
Vaše pohlaví je {muz_zena(mesic)}.
       """)




