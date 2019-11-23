### Domácí úkol 01: ZOBRAZENÍ



#### Průběh programu:

Program se uživatele zeptá na vstupní informace: zobrazení, měřítko a poloměr Země. Program je zaměřen na válcová tečná zobrazení. Pokud uživatel zadá nekorektní vstup má možnost zadat informaci opakovaně pomocí while cyklu. Dle zadaných informací program vypíše seznamy hodnot vypočtených vzdáleností na osách pro rovnoběžky a poledníky. Dále má uživatel možnost zadat zeměpisnou délku a zeměpisnou šířku konkrétního bodu a program vypíše přepočtené hodnoty podle zadaného zobrazení. Při zadání hodnot `(0,0)` program skončí. 

##### Vstupy:

- uživatel zadá zobrazení - `L` jako Lambertovo, `A` jako Marinovo, `B` jako Braunovo nebo `M` jako Mercatorovo, pokud uživatel zadá například jiné písmeno, je upozorněn a má možnost zadat vstup znovu

- dále se program ptá na měřítko, uživatel zadává `x`, kde výsledné měřítko je 1 : x, měřítko musí být větší než 0, pokud uživatel zadá nekorektní vstup,  je upozorněn a má možnost zadat vstup znovu

- následně se zeptá na poloměr Země v km, pokud uživatel zadá `0`, program použije výchozí poloměr 6371,11 km, pokud uživatel zadá číslo menší než 0, je upozorněn a má možnost zadat vstup znovu

- pro zjištění hodnot pro konkrétní bod uživatel zadá zeměpisnou délku a šířku, zeměpisná šířka musí být v rozmezí od -90 do 90 stupňů a zeměpisná délka od -180 do 180 stupňů, pokud uživatel zadá hodnoty `(0,0)` program skončí, pokud zadá nekorektní vstup je upozorněn a program skončí

##### Použité funkce:
- *kontrola_delky (a)*
  funkce zaokrouhlí hodnotu a na jedno desetinné místo a následně zkontroluje délku, pokud je větší nez 100cm vrátí místo hodnoty `-`, pokud je menší vrací zaokrouhlenou hodnotu a 

- *polednik (zem_delka,meritko,R)* 

  funkce na základě zeměpisné délky, měřítka a poloměru Země vypočítá poledníky pro dané zobrazení a vrátí hodnotu v cm zaokrouhlenou na desetiny, pokud je hodnota větší než 100 cm vrátí "-"

- *lambertovo_rovnobezka (zem_sirka,meritko,R), marinovo_rovnobezka (zem_sirka,meritko,R), braunovo_rovnobezka (zem_sirka,meritko,R), mercatorova_rovnobezka (zem_sirka,meritko,R)* 

  všechny tyto funkce vypočítají na základě zeměpisné šířky, měřítka a poloměru Země rovnoběžky podle zadaného zobrazení a vrátí hodnotu v cm zaokrouhlenou na desetiny, pokud je hodnota vyšší než 100 cm vrátí "-"

- *lambertovo(poledniky,rovnobezky), marinovo(poledniky,rovnobezky), braunovo(poledniky,rovnobezky), mercatorovo(poledniky,rovnobezky)* 

  všechny tyto funkce vypočítají rovnoběžky a poledníky po 10 stupních pomocí předchozích funkcí a vloží je do seznamů, které jsou vkládány do funkce jako parametr

##### Výstupy:

- seznam vzdáleností na ose x pro rovnoběžky od -90 do 90 stupňů s intervalem 10 stupňů v cm, pokud je hodnota vyšší než 1m v seznamu se vypíše `-`
- seznam vzdáleností na ose y pro poledníky od -180 do 180 stupňů s intervalem 10 stupňů v cm, pokud je hodnota vyšší než 1m v seznamu se vypíše `-`
- pokud uživatel zadá zeměpisnou šířku a délku pro konkrétní bod, program vypíše přepočtenou hodnotu v cm, pokud je hodnota vyšší než 1m, vypíše `-` a zeptá se na další dokud nejsou zadané souřadnice `(0,0)`, v případě Mercatora se rovnoběžky -90 a 90 stupňů zobrazují v nekonečnu a program vždy vypíše `-`

##### Příklad možného výstupu:

```
zadejte zobrazení:L
zadejte měřítko mapy:50000000
zadejte poloměr Země:0
rovnoběžky:[-12.7, -12.5, -12.0, -11.0, -9.8, -8.2, -6.4, -4.4, -2.2, 0.0, 2.2, 4.4, 6.4, 8.2, 9.8, 11.0, 12.0, 12.5, 12.7]
 poledniky:[-40.0, -37.8, -35.6, -33.4, -31.1, -28.9, -26.7, -24.5, -22.2, -20.0, -17.8, -15.6, -13.3, -11.1, -8.9, -6.7, -4.4, -2.2, 0.0, 2.2, 4.4, 6.7, 8.9, 11.1, 13.3, 15.6, 17.8, 20.0, 22.2, 24.5, 26.7, 28.9, 31.1, 33.4, 35.6, 37.8, 40.0]
 poledniky:[-40.0, -37.8, -35.6, -33.4, -31.1, -28.9, -26.7, -24.5, -22.2, -20.0, -17.8, -15.6, -13.3, -11.1, -8.9, -6.7, -4.4, -2.2, 0.0, 2.2, 4.4, 6.7, 8.9, 11.1, 13.3, 15.6, 17.8, 20.0, 22.2, 24.5, 26.7, 28.9, 31.1, 33.4, 35.6, 37.8, 40.0]
zadejte zeměpisnou délku:89
zadejte zeměpisnou šířku:54
přepočtená zeměpisná délka bodu: 19.8
přepočtená zeměpisná šířka bodu: 10.3
zadejte zeměpisnou délku:0
zadejte zeměpisnou šířku:0
Děkujeme za použití programu!
```



