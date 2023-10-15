list= [
    [2001, 7.8], 
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
    ]

# Získejte teplotu na třetím řádku tabulky.
teploty = [teplota[1] for teplota in list]
print(teploty[2])
# Získejte rok na pátém řádku tabulky.
roky = [rok[0] for rok in list]
print(roky[4])
# Získejte poslední řádek tabulky jako seznam.
# Vytvořte tabulku bez prvních dvou řádků.
# Vytvořte tabulku pouze z prvních dvou řádků.
# Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
# Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.
