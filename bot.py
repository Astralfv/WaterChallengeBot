import random

punti = 0
litri_risparmiati = 0

attivita = {
    "Doccia di massimo 5 minuti": 50,
    "Chiudere il rubinetto mentre ti lavi i denti": 6,
    "Controllare se i rubinetti di casa perdono": 20,
    "Usare la lavatrice solo a pieno carico": 40,
    "Usare la lavastoviglie solo a pieno carico": 25,
    "Riutilizzare l’acqua per innaffiare le piante": 10,
    "Lavare l’auto con secchio invece che con tubo": 100,
    "Non scongelare cibo sotto acqua corrente": 15,
    "Installare un riduttore di flusso nei rubinetti": 30,
    "Raccogliere acqua piovana per le piante": 35
}

sfide_fatte = []

while True:

    sfide_disponibili = [a for a in attivita if a not in sfide_fatte]

    if not sfide_disponibili:
        print("\nHai completato tutte le sfide disponibili.")
        break

    sfida = random.choice(sfide_disponibili)
    sfide_fatte.append(sfida)

    print("\nNuova sfida:")
    print(sfida)

    risposta = input("Completata? (s/n) oppure scrivi 'esci': ")

    if risposta.lower() == "s":
        punti += 10
        litri_risparmiati += attivita[sfida]
        print("Hai guadagnato 10 punti.")
        print("Hai risparmiato circa", attivita[sfida], "litri di acqua.")
    elif risposta.lower() == "esci":
        break
    else:
        print("Sfida non completata.")

    print("Punti totali:", punti)
    print("Litri totali risparmiati:", litri_risparmiati)

print("\nRiepilogo finale")
print("Punti totali:", punti)
print("Litri totali risparmiati:", litri_risparmiati)
print("Grazie per aver usato HydroHero")
