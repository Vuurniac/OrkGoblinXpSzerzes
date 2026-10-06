voltSzintlepes = False
kezdoXp = int(input("kezdő xp: "))
goblinXp = 30 # elavult változó
orkXp = 75 # elavult változó
goblinDb = 5
orkDb = 1
szintKorlat = 700

class OrkSzorny:
  xpErtek = 75
  szornyNev = "ork"

class GoblinSzorny:
  xpErtek = 30
  szornyNev = "goblin"

class TrollSzorny:
  xpErtek = 100
  szornyNev = "troll"

lehetsegesSzornyek = (OrkSzorny.szornyNev,GoblinSzorny.szornyNev,TrollSzorny.szornyNev)

def xpEllenorzesKiiras():
  # ezeknek globális változóknak kell lenniük, hogy függvényből lehessen módosítani
  global voltSzintlepes
  global osszesXp

  # XP kiírása, ezt mindig kell
  print("XP-d jelenleg:",osszesXp)

  # XP vizsgálata elágazással
  if osszesXp >= szintKorlat and not (voltSzintlepes):
    szintvisszajelzes = "szintet léptél"  # igaz ág
    voltSzintlepes = True
  else:
    szintvisszajelzes = "nem léptél szintet"  # hamis ág
  return szintvisszajelzes

# XP kezdés
print("KEZDÉS")
osszesXp = kezdoXp
print(xpEllenorzesKiiras()) # szintlépés ellenőrzése és kiírni amit kell

# XP goblinokért
print("CSATA goblinokkal")
osszesXp += GoblinSzorny.xpErtek * goblinDb # + orkXp * orkDb
print(xpEllenorzesKiiras()) # szintlépés ellenőrzése és kiírni amit kell

# XP orkokért
print("CSATA orkokkal")
osszesXp += OrkSzorny.xpErtek * orkDb
print(xpEllenorzesKiiras()) # szintlépés ellenőrzése és kiírni amit kell

print("Statisztika") # ezt mindenképpen végrehajtja
ellenfelTipusa = input("add meg az egyik ellenfél típusát: ");
if ellenfelTipusa == "ork" or ellenfelTipusa == "goblin":
    print("ismert ellenfél")
else:
    print("nem ismert ellenfél")