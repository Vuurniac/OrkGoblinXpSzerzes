voltSzintlepes = False
kezdoXp = 500 # bekérés, előző beolvasása, stb.
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
if osszesXp >= szint_2 and not(voltSzintlepes):
  print("szintet léptél") # igaz ág
  voltSzintlepes = True
else:
  print("nem léptél szintet") # hamis ág

# XP goblinokért
print("CSATA goblinokkal")
osszesXp = kezdoXp + goblinXp * goblinDb # + orkXp * orkDb
# XP kiírása
print(osszesXp)
# XP vizsgálata elágazással
if osszesXp >= szint_2 and not(voltSzintlepes):
  print("szintet léptél") # igaz ág
  voltSzintlepes = True
else:
  print("nem léptél szintet") # hamis ág

# XP orkokért
print("CSATA orkokkal")
# osszesXp = osszesXp + orkXp * orkDb
osszesXp += orkXp * orkDb
# XP kiírása
print(osszesXp)
# XP vizsgálata elágazással
if osszesXp >= szint_2 and not(voltSzintlepes):
  print("szintet léptél") # igaz ág
  voltSzintlepes = True
else:
  print("nem léptél szintet") # hamis ág

print("Statisztika") # ezt mindenképpen végrehajtja
ellenfelTipusa = input("add meg az egyik ellenfél típusát: ");
if ellenfelTipusa == "ork" or ellenfelTipusa == "goblin":
    print("ismert ellenfél")
else:
    print("nem ismert ellenfél")