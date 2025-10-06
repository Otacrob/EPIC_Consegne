# Si scriva un programma in Python che in base alla scelta dellʼutente permetta di 
# calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi).
# Per la risoluzione dellʼesercizio abbiamo scelto: 
# ● Quadrato (perimetro = lato*4). 
# ● Cerchio (circonferenza = 2*pi greco*r). 
# ● Rettangolo (perimetro= base*2 + altezza*2).

#importo la libreria per usare pigreco
import math

#stampo il messaggio iniziale
print("Ciao! Con questo programma ti aiuterò a calcolare il perimetro di alcune tra le figure geometriche più iconiche!")

#creo ciclo while per accettare solo risposte "si/no"
while True:

#determino la variabile volontà associata alla scelta dell'utente
    volontà = input("Ti va di proseguire? ")

#se "si" parte la scelta del tipo di figura ed il relativo calcolo del perimetro a seguito delle richieste dei dati
    if volontà.lower() == "si" :
        print("Ottimo! Al momento sono programmato per aiutarti nel calcolo perimetrale delle seguenti figure:")
        print("*Quadrato")
        print("*Cerchio")
        print("*Rettangolo")
        print("*Triangolo")
    
        figura = input("Di quale delle figure geometriche elencate vorresti calcolare l'area? ")

        if figura.lower() == "quadrato":
            lato = float(input("Grandioso! Ora inserisci il valore relativo alla lunghezza del lato del quadrato d'interesse: "))
            perimetro = lato * 4
            print(f"Facile! Il perimetro del quadrato in questione è {perimetro}")

        elif figura.lower() == "cerchio":
            raggio = float(input("Grandioso! Ora inserisci il valore relativo alla lunghezza del raggio del cerchio d'interesse: "))
            perimetro = 2 * math.pi * raggio
            print(f"Facile! Il perimetro del cerchio in questione è {perimetro}")

        elif figura.lower() == "rettangolo":
            base = float(input("Grandioso! Ora inserisci il valore relativo alla lunghezza della base del rettangolo d'interesse: "))
            altezza = float(input("Grazie! Ora inserisci il valore relativo alla lunghezza dell'altezza del rettangolo d'interesse: "))
            perimetro = base * 2 + altezza * 2
            print(f"Ecco a te! Il perimetro del rettangolo in questione è {perimetro}")
        
        elif figura.lower() == "triangolo":
            latoA = float(input("Super! Ora inserisci il valore relativo alla lunghezza del primo lato del triangolo d'interesse: "))
            latoB = float(input("Grandioso! Ora inserisci il valore relativo alla lunghezza del secondo lato del triangolo d'interesse: "))
            latoC = float(input("Grandioso! Ora inserisci il valore relativo alla lunghezza del terzo lato del triangolo d'interesse: "))
    
        else:
            print("Mi spiace ma l'input inserito non rientra tra le scelte proposte")
        break

#se "no" faccio terminare il programma
    elif volontà.lower() == "no" :
        print("D'accordo, sarà per la prossima volta! :) A presto!")
        exit()

#se la scelta non è nelle opzioni avviso e ripeto il ciclo
    else:
        print("Mi spiace ma l'input inserito non rientra nel mio vocabolario")
