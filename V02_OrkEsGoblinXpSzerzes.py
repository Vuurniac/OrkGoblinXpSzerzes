voltSzintlepes = False # elavult változó
kezdoXp = int(input("kezdő xp: "))
goblinXp = 30 # elavult változó
orkXp = 75 # elavult változó
goblinDb = 5
orkDb = 1
szintKorlat = 700
jatekosSzint = 1

class OrkSzorny:
  xpErtek = 75
  szornyNev = "ork"

class GoblinSzorny:
  xpErtek = 30
  szornyNev = "goblin"

class TrollSzorny:
  xpErtek = 100
  szornyNev = "troll"

lehetsegesSzornyek = (OrkSzorny,GoblinSzorny,TrollSzorny)

def xp_ellenorzes_kiiras():
  # ezeknek globális változóknak kell lenniük, hogy függvényből lehessen módosítani
  global voltSzintlepes
  global osszesXp
  global jatekosSzint
  global szintKorlat

  # XP kiírása, ezt mindig kell
  print("XP-d jelenleg:",osszesXp)

  # XP vizsgálata elágazással
  if osszesXp >= szintKorlat:
    print("Szintet léptél!")  # igaz ág
    jatekosSzint += 1
    print("Jelenlegi szinted:",jatekosSzint)
    szintKorlat = szintKorlat+szintKorlat/2 # a szintkorlát egyre emelkedjen
  else:
    print("Még nem léptél szintet.")  # hamis ág

  print("A következő szinthez érj el ", szintKorlat, " XP-t!") # mindig írjuk ki mi a következő korlát
  print("Hiányzik: ",(szintKorlat-osszesXp)," XP")
  voltSzintlepes = True
  return

def szorny_kiiras(): # kiírja a valid szörnyeket
  global lehetsegesSzornyek
  print("A lehetséges szörnyek:")
  for x in lehetsegesSzornyek:
    print(x.szornyNev)
  return

def szorny_bekeres(): # kiírja a valid szörnyeket és kéri a usert, hogy adja meg milyen szörnyet ölünk, és mennyit
  # globális változók
  global lehetsegesSzornyek
  # helyi változók
  helyesinput = False

  print("CSATA!\n")
  while not helyesinput:
    szorny_kiiras() # írja ki milyen szörnyeket lehet megadni
    beirtszorny = input("\nKérlek add meg, milyen szörnnyel csatázol: ")
    beirtdarab = int(input("Kérlek add meg, hány darab szörnnyel csatázol: "))
    if type(beirtdarab) == int and type(beirtszorny) == str:
      for x in lehetsegesSzornyek:  # megkeressük melyik szörnyet írta be a user
        if x.szornyNev == beirtszorny:
          beirtszorny = x
          helyesinput = True
          break
      if not helyesinput:
        print("Hibásan adtad meg az adatokat! Kérlek add meg újra!")
    else:
      print("Hibásan adtad meg az adatokat! Kérlek add meg újra!") # Ez helyett kivételkezelés kellene?

  return beirtszorny, beirtdarab # visszaadjuk a szörny osztályát és hogy mennyi van belőle

def csata_inditas():
  global osszesXp
  szornytipus, darab = szorny_bekeres()
  osszesXp += szornytipus.xpErtek * darab
  xp_ellenorzes_kiiras()
  return

# XP kezdés
print("KEZDÉS")
print("A játék 3 fázisból áll, sok sikert!")
osszesXp = kezdoXp
xp_ellenorzes_kiiras() # kezdeti xp kiírása

for x in ("\n1. fázis","\n2. fázis","\n3. fázis"):
  print(x)
  csata_inditas() # szintlépés ellenőrzése és kiírni amit kell

print("\nStatisztika az utolsó fázis után:") # ezt mindenképpen végrehajtja
xp_ellenorzes_kiiras()

szorny_kiiras() # mondjuk meg miket írhat be a user
ellenfelTipusa = input("Add meg az egyik ellenfél típusát: ");
if ellenfelTipusa == "ork" or ellenfelTipusa == "goblin" or ellenfelTipusa == "troll":
    print("Ismert ellenfél")
else:
    print("Nem ismert ellenfél")