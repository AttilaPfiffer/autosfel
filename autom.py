from Auto import Auto
def fajl():
    slista = []
    fajlom = open("auto.txt", "r", encoding = "UTF-8")
    fajlom.readline()
    lista = fajlom.readlines()
    fajlom.close()
    for i in range(0, len(lista), 1):
        sor_lista = lista[i].strip()
        sor_lista = lista[i].split("$")
        nev = sor_lista[0]
        gyart = sor_lista[1]
        autok = Auto(nev, int(gyart))
        slista.append(autok)
    
    for i in range(0, len(slista), 1):
        print(f"{slista[i].nev}, {slista[i].gyart_datum}")
    return slista

def tabla(lista, i):
    print("III/Tabla")
    print(f"{lista[i - 1].nev}: {len(lista[i - 1].nev)} hosszú")

def flotta(lista):
    print("III/Flotta")
    print(f"Az autók száma: {len(lista)} ")

def ertekes(lista):
    print("III/Értékes")
    legfiatalabb: int = 0
    for i in range(1, len(lista), 1):
        if lista[i].gyart_datum > lista[legfiatalabb].gyart_datum:
            legfiatalabb = i
    return legfiatalabb
            
