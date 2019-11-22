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

# pokud uživatel zadá nulu, program použije původní poloměr
while polomer < 0:
    print("neplatný vstup, zadejte prosím kladné číslo nebo 0")
    polomer = float(input("zadejte poloměr Země:"))
if polomer == (0):
    R = 6371.11
else:
    R = polomer

def polednik (zem_delka,meritko):
    # funkce fce_poledniky vypočte poledníky pro každé zobrazení, protože vzorec pro výpočet poledníků daných zobrazení je stejný a vloží je do seznamu poledniky
    # pokud vyjde vzdálenost větší než 1 m program vypíše "-"
   x = (R*radians(zem_delka)*cos(radians(0)))/meritko * 100000
   x_z = round(x,1)
   if (x_z > -100) and (x_z < 100):
       return x_z
   else:
       return "-"
def lambertovo_rovnobezka (zem_sirka,meritko):
   # vypočte rovnoběžky pro Lambertovo zobrazení dle zadané zeměpisné šířky a měřítka
   # vrátí hodnotu v cm nebo -
   y = (R * sin(radians(zem_sirka))) / meritko * 100000
   y_z = round(y, 1)
   if (y_z > -100) and (y_z < 100):
       return y_z
   else:
       return "-"
def marinovo_rovnobezka (zem_sirka,meritko):
   # vypočte rovnoběžky pro Marinovo zobrazení dle zadané zeměpisné šířky a měřítka
   # vrátí hodnotu v cm nebo -
   y = (R * radians(zem_sirka)) / meritko * 1000000
   y_z = round(y, 1)
   if (y_z > -100) and (y_z < 100):
       return y_z
   else:
       return "-"
def braunovo_rovnobezka (zem_sirka,meritko):
   # vypočte rovnoběžky pro Braunovo zobrazení dle zadané zeměpisné šířky a měřítka
   # vrátí hodnotu v cm nebo -
   y = (2 * R * tan(radians(zem_sirka / 2))) / meritko * 1000000
   y_z = round(y, 1)
   if (y_z > -100) and (y_z < 100):
       return y_z
   else:
       return "-"
def mercatorovo_rovnobezka (zem_sirka,meritko):
   # vypočte rovnoběžky pro Mercatorovo zobrazení dle zadané zeměpisné šířky a měřítka
   # vrátí hodnotu v cm nebo -
   y = (R * log(1 / tan(radians((90 - zem_sirka) / 2)))) / meritko * 1000000
   y_z = round(y, 1)
   if (y_z > -100) and (y_z < 100):
       return y_z
   else:
       return "-"

def lambertovo(poledniky,rovnobezky):
   # funkce lambert vypočítá poledníky a rovnoběžky pro lambertovo zobrazení a vloží je do seznamů
   for zem_delka in range(-180, 190, 10):
       x = polednik(zem_delka,meritko)
       poledniky.append(x)
   for zem_sirka in range(-90, 100, 10):
       y = lambertovo_rovnobezka(zem_sirka,meritko)
       rovnobezky.append(y)

def marinovo(poledniky,rovnobezky):
   # funkce marinovo vypočítá poledníky a rovnoběžky pro marinovo zobrazení a vloží je do seznamů
   for zem_delka in range(-180, 190, 10):
       x = polednik(zem_delka,meritko)
       poledniky.append(x)
   for zem_sirka in range(-90, 100, 10):
       y = marinovo_rovnobezka(zem_sirka,meritko)
       rovnobezky.append(y)

def braunovo(poledniky,rovnobezky):
   # funkce braunovo vypočítá poledníky a rovnoběžky pro braunovo zobrazení a vložíí je do seznamu
   for zem_delka in range(-180, 190, 10):
       x = polednik(zem_delka, meritko)
       poledniky.append(x)
   for zem_sirka in range(-90, 100, 10):
       y = braunovo_rovnobezka(zem_sirka, meritko)
       rovnobezky.append(y)

def mercatorovo(poledniky,rovnobezky):
   # funkce mercator vypočítá poledníky a rovnoběžky pro mercatorovo zobrazení a vloží je do seznamu
   for zem_delka in range(-180, 190, 10):
       x = polednik(zem_delka,meritko)
       poledniky.append(x)
   for zem_sirka in range(-90, 100, 10):
       if zem_sirka == (90):
           rovnobezky.append("-")
       else:
           y = mercatorovo_rovnobezka(zem_sirka,meritko)
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

# uživatel zadá zeměpisnou délku a šířku a program dvojici uloží do seznamu bod
zem_delka = float(input("zadejte zeměpisnou délku:"))
if (zem_delka < -180) or (zem_delka > 180):
   print ("Neplatný vstup.")
   quit()
else:
   zem_sirka = float(input("zadejte zeměpisnou šířku:"))
   if (zem_sirka <-90.0) or (zem_sirka > 90.0):
       print("Neplatný vstup.")
       quit()
   else:
       bod = [zem_delka,zem_sirka]

# dokud bod nebude mít nulovou zeměpisnou délku a šířku, bude program podle zadaného zobrazení, měřítka a poloměru počítat bod
# hodnoty zaokrouhlí na desetiny centimetrů, vypíše a zeptá se znovu, dokud uživatel nezadá 0,0
while bod != [0,0]:
   if zobrazeni == "L":
       x = polednik(zem_delka, meritko)
       y = lambertovo_rovnobezka(zem_sirka, meritko)

   elif zobrazeni == "A":
       x = polednik(zem_delka, meritko)
       y = marinovo_rovnobezka(zem_sirka, meritko)

   elif zobrazeni == "B":
       x = polednik(zem_delka, meritko)
       y = braunovo_rovnobezka(zem_sirka, meritko)

   elif zobrazeni == "M":
       if (zem_sirka == -90) or (zem_sirka == 90):
           x = polednik(zem_delka, meritko)
           print("přepočtená zeměpisná délka bodu:",x)
           print("přepočtená zeměpisná šířka bodu:-")
       else:
           x = polednik(zem_delka, meritko)
           y = mercatorovo_rovnobezka(zem_sirka, meritko)

   print("přepočtená zeměpisná délka bodu:", x)
   print("přepočtená zeměpisná šířka bodu:", y)
   zem_delka = float(input("zadejte zeměpisnou délku:"))
   if (zem_delka < -180) or (zem_delka > 180):
       print("Neplatný vstup.")
       quit()
   else:
       zem_sirka = float(input("zadejte zeměpisnou šířku:"))
       if (zem_sirka < -90.0) or (zem_sirka > 90.0):
           print("Neplatný vstup.")
           quit()
       else:
           bod = [zem_delka, zem_sirka]
