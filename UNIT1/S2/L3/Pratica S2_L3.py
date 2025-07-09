

while True:

    domanda = input("Ciao, oggi proveremo a scegliere un nome per la tua band musicale! Sei pronto? ")

    if domanda.lower() == "si":

        città = input("Scrivimi il nome della tua città natale!: ")
        animale = input("Ora dimmi il nome di uno dei tuoi animali domestici!: ")
        risultato = f"Il nome per la tua band sarà: {città} {animale}"
        print(risultato)
        break

    else:
        print("Non accetto un no come risposta! :) Dovrai dirmi per forza Si")



