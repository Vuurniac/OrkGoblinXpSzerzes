voltSzintlepes = False
kezdoXp = 700 # bekérés, előző beolvasása, stb.
goblinXp = 30
orkXp = 75
goblinDb = 5
orkDb = 1
szint_2 = 700
# XP kezdés
print("KEZDÉS")
osszesXp = kezdoXp
# XP kiírása
print(osszesXp)
# XP vizsgálata elágazással
if voltSzintlepes == False:
    if osszesXp >= szint_2: # feltételtől függően elágazik a program
      print("szintet léptél") # igaz ág
      voltSzintlepes = True
    else:
      print("nem léptél szintet") # hamis ág
else:
    print("nem léptél szintet")  # hamis ág

# XP goblinokért
print("CSATA goblinokkal")
osszesXp = kezdoXp + goblinXp * goblinDb # + orkXp * orkDb
# XP kiírása
print(osszesXp)
# XP vizsgálata elágazással
if voltSzintlepes == False:
    if osszesXp >= szint_2: # feltételtől függően elágazik a program
      print("szintet léptél") # igaz ág
      voltSzintlepes = True
    else:
      print("nem léptél szintet") # hamis ág
else:
    print("nem léptél szintet")  # hamis ág

# XP orkokért
print("CSATA orkokkal")
# osszesXp = osszesXp + orkXp * orkDb
osszesXp += orkXp * orkDb
# XP kiírása
print(osszesXp)
# XP vizsgálata elágazással
if voltSzintlepes == False:
    if osszesXp >= szint_2: # feltételtől függően elágazik a program
      print("szintet léptél") # igaz ág
      voltSzintlepes = True
    else:
      print("nem léptél szintet") # hamis ág
else:
    print("nem léptél szintet")  # hamis ág

print("program vége") # ezt mindenképpen végrehajtja