import jelszo
import oszthato
import autom
#kutya

"""jelszo.egy()"""
print("\n")
szamok = oszthato.Ottel_oszthato()

ottel_oszthato = oszthato.ottelOszthato(szamok)
print(f"\nA listában {ottel_oszthato} darab öttel osztható szám van.")

print("\n")
lista = autom.fajl()
print("\n")
autom.tabla(lista, 2)
print("\n")
autom.flotta(lista)
print("\n")
blabla = autom.ertekes(lista)
print(f"A legfiatalabb autó: {lista[blabla].nev} ({lista[blabla].gyart_datum})")