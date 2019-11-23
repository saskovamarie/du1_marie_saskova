from math import radians, sin, cos, tan, log

# program se zeptá uživatele na vstupní informace: zobrazení, měřítko, poloměr Země
zobrazeni = input("zadejte zobrazení:")
while zobrazeni not in ("L, A, B, M"):
    print("neplatný vstup, napište prosím L, A, B, nebo M")
    zobrazeni = input("zadejte zobrazení:")

meritko = int(input("zadejte měřítko mapy:"))
while meritko <= 0:
    print("neplatný vstup, zadejte prosím měřítko větší než 0.")
    meritko = int(input("zadejte měřítko mapy:"))

polomer = float(input("zadejte poloměr Země:"))
# pokud je poloměr roven 0 program použije původní hodnotu
while polomer < 0:
    print("neplatný vstup, zadejte prosím kladné číslo nebo 0")
    polomer = float(input("zadejte poloměr Země:"))
if polomer == 0:
    R = 6371.11
else:
    R = polomer

def kontrola_delky(a):
    # funkce zaokrouhlí číslo a na 1 desetinné místo
    # zkontroluje zda není hodnota vyšší nebo rovna 100 cm, pokud ano vrátí "-", pokud ne vrátí zaokrouhlenou hodnotu a
    a_z = round(a, 1)
    if (a_z <= -100) or (a_z >= 100):
        a_z = "-"
    return a_z

def polednik (zem_delka,meritko,R):
    # funkce polednik vypočte poledníky pro každé zobrazení, protože vzorec pro výpočet poledníků daných zobrazení je stejný
    # vrací hodnotu x zaokrouhlenou na 1 desetinné místo nebo "-", dle funkce kontrola_délky
    x = (R*radians(zem_delka)*cos(radians(0)))/meritko * 100000
    x_z = kontrola_delky(x)
    return x_z

def lambertovo_rovnobezka (zem_sirka,meritko,R):
    # vypočte rovnoběžky pro Lambertovo zobrazení dle zadané zeměpisné šířky, měřítka a poloměru
    # vrací hodnotu x zaokrouhlenou na 1 desetinné místo nebo "-", dle funkce kontrola_délky
    y = (R * sin(radians(zem_sirka))) / meritko * 100000
    y_z = kontrola_delky(y)
    return y_z

def marinovo_rovnobezka (zem_sirka,meritko,R):
    # vypočte rovnoběžky pro Marinovo zobrazení dle zadané zeměpisné šířky, měřítka a poloměru
    # vrací hodnotu x zaokrouhlenou na 1 desetinné místo nebo "-", dle funkce kontrola_délky
    y = (R * radians(zem_sirka)) / meritko * 1000000
    y_z = kontrola_delky(y)
    return y_z

def braunovo_rovnobezka (zem_sirka,meritko,R):
    # vypočte rovnoběžky pro Braunovo zobrazení dle zadané zeměpisné šířky, měřítka a poloměru
    # vrací hodnotu x zaokrouhlenou na 1 desetinné místo nebo "-", dle funkce kontrola_délky
    y = (2 * R * tan(radians(zem_sirka / 2))) / meritko * 1000000
    y_z = kontrola_delky(y)
    return y_z

def mercatorovo_rovnobezka (zem_sirka,meritko,R):
    # vypočte rovnoběžky pro Mercatorovo zobrazení dle zadané zeměpisné šířky, měřítka a poloměru
    # vrací hodnotu x zaokrouhlenou na 1 desetinné místo nebo "-", dle funkce kontrola_délky
    y = (R * log(1 / tan(radians((90 - zem_sirka) / 2)))) / meritko * 1000000
    y_z = kontrola_delky(y)
    return y_z

def lambertovo(poledniky,rovnobezky):
    # funkce lambertovo vypočítá poledníky a rovnoběžky pro lambertovo zobrazení a vloží je do seznamů
    for zem_delka in range(-180, 190, 10):
        x = polednik(zem_delka,meritko,R)
        poledniky.append(x)
    for zem_sirka in range(-90, 100, 10):
        y = lambertovo_rovnobezka(zem_sirka,meritko,R)
        rovnobezky.append(y)

def marinovo(poledniky,rovnobezky):
    # funkce marinovo vypočítá poledníky a rovnoběžky pro marinovo zobrazení a vloží je do seznamů
    for zem_delka in range(-180, 190, 10):
        x = polednik(zem_delka,meritko,R)
        poledniky.append(x)
    for zem_sirka in range(-90, 100, 10):
        y = marinovo_rovnobezka(zem_sirka,meritko,R)
        rovnobezky.append(y)

def braunovo(poledniky,rovnobezky):
    # funkce braunovo vypočítá poledníky a rovnoběžky pro braunovo zobrazení a vloží je do seznamu
    for zem_delka in range(-180, 190, 10):
        x = polednik(zem_delka, meritko,R)
        poledniky.append(x)
    for zem_sirka in range(-90, 100, 10):
        y = braunovo_rovnobezka(zem_sirka,meritko,R)
        rovnobezky.append(y)

def mercatorovo(poledniky,rovnobezky):
    # funkce mercator vypočítá poledníky a rovnoběžky pro mercatorovo zobrazení a vloží je do seznamu
    for zem_delka in range(-180, 190, 10):
        x = polednik(zem_delka,meritko,R)
        poledniky.append(x)
    for zem_sirka in range(-90, 100, 10):
        if (zem_sirka == -90) or (zem_sirka == 90):
            rovnobezky.append("-")
        else:
            y = mercatorovo_rovnobezka(zem_sirka,meritko,R)
            rovnobezky.append(y)

poledniky = []
rovnobezky = []
# podle zadaného zobrazení se provede daná funkce
if zobrazeni == "L":
    lambertovo(poledniky,rovnobezky)

elif zobrazeni =="A":
    marinovo(poledniky,rovnobezky)

elif zobrazeni == "B":
    braunovo(poledniky,rovnobezky)

elif zobrazeni == "M":
    mercatorovo(poledniky,rovnobezky)

print(f"rovnoběžky:{rovnobezky}\n poledniky:{poledniky}")

# dokud bod nebude mít nulovou zeměpisnou délku a šířku, bude program podle zadaného zobrazení, měřítka a poloměru počítat bod
# hodnoty zaokrouhlí na desetiny centimetrů, vypíše a zeptá se znovu, dokud uživatel nezadá 0,0
while True:
    zem_delka = float(input("zadejte zeměpisnou délku:"))
    if (zem_delka < -180) or (zem_delka > 180):
        print("Neplatný vstup.")
        quit()
    else:
        zem_sirka = float(input("zadejte zeměpisnou šířku:"))
        if (zem_sirka < -90.0) or (zem_sirka > 90.0):
            print("Neplatný vstup.")
            quit()
        elif (zem_sirka == 0) and (zem_delka == 0):
            print("Děkujeme za použití programu!")
            quit()
        else:
            True
    if zobrazeni == "L":
        x = polednik(zem_delka,meritko,R)
        y = lambertovo_rovnobezka(zem_sirka,meritko,R)
    elif zobrazeni == "A":
        x = polednik(zem_delka,meritko,R)
        y = marinovo_rovnobezka(zem_sirka,meritko,R)
    elif zobrazeni == "B":
        x = polednik(zem_delka,meritko,R)
        y = braunovo_rovnobezka(zem_sirka,meritko,R)
    elif zobrazeni == "M":
        if (zem_sirka == -90) or (zem_sirka == 90):
            x = polednik(zem_delka,meritko,R)
            y = "-"
        else:
            x = polednik(zem_delka, meritko,R)
            y = mercatorovo_rovnobezka(zem_sirka, meritko,R)
    print("přepočtená zeměpisná délka bodu:",x)
    print("přepočtená zeměpisná šířka bodu:",y)
