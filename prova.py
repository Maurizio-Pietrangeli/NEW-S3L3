print("Scegli la figura geometrica di cui vuoi calcolare il perimetro:")
print("1. Quadrato")
print("2. Rettangolo")
print("3. Cerchio")

scelta = int(input("Inserisci il numero corretto per alla tua scelta: "))

if scelta == 1:
    lato = float(input("Inserisci il lato del quadrato: "))
    perimetro = lato * 4
    print("Il perimetro del quadrato è:", perimetro)
elif scelta == 2:
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo:"))
    perimetro = base * 2 + altezza *2
    print("Il perimetro del rettangolo è:", perimetro)
elif scelta == 3:
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circonferenza = 2 * 3.14 * raggio
    print("La circonferenza del cerchio è:", circonferenza)
else:
    print("Scelta errata. Riprova.")
