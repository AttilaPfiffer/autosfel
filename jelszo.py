def felhasznalonev_jelszo():
    print("Első feladat:")
    felhasznalo:str = str(input("\tAdja meg a felhasználónevét! "))
    jelszo = input("\tAdja meg a jelszavát! ")
    while not(felhasznalo == "bori99" and jelszo == "Szivecske<3"):
        print("\tBelépés megtagadva!")
        felhasznalo:str = str(input("\tAdja meg a felhasználónevét! "))
        jelszo = input("\tAdja meg a jelszavát! ")
    print("\tBelépés engedélyezve!")
    



def egy():
    felhasznalonev_jelszo()