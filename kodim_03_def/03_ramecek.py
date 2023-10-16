
slovo= input("Zadej slovo: ")

pocet = len(slovo)

def ramecek(pocet): 
    return pocet * "*" + 4 * "*"


print(f"""
{ramecek(pocet)}
* {slovo} *
{ramecek(pocet)}
 """)


def srdickovy_ramecek(pocet):
    return pocet * "♥" + 4 * "♥"

print(f"""
{srdickovy_ramecek(pocet)}
♥ {slovo} ♥
{srdickovy_ramecek (pocet)}
 """)

znak = input("Zadej znak: ")

def selektivni_ramecek(pocet):
    return pocet * znak + 4 * znak

print(f"""
{selektivni_ramecek(pocet)}
{znak} {slovo} {znak}
{selektivni_ramecek (pocet)}
 """)