import random

punti = 0

attivita = [
    "Doccia in 10 minuti",
    "Chiudere il rubinetto mentre ti lavi i denti",
    "Controllare se i rubinetti di casa perdono"
]

while True:
    sfida = random.choice(attivita)
    
    print("\n💧 Nuova sfida:")
    print(sfida)
    
    risposta = input("Completata? (s/n) oppure scrivi 'esci': ")
    
    if risposta.lower() == "s":
        punti += 10
        print("🎉 +10 punti!")
    elif risposta.lower() == "esci":
        break
    
    print("🏆 Punti totali:", punti)

print("Grazie per aver usato HydroHero 💧")
