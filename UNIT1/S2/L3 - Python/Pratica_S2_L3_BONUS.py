# Descrizione: Scrivi una funzione che calcoli la media mobile di una lista di numeri.
# La media mobile di un elemento è definita come la media degli ultimi n elementi della lista, inclusi l'elemento corrente.
# Suggerimenti: ● Usa slicing per ottenere gli ultimi n elementi. ● Usa la funzione sum() per calcolare la somma degli elementi e poi dividi per n. 
# Esempio di input: numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] n = 3 Esempio di output: [1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]

#definisco il nome della variabile al cui interno conterrà un parametro "numeri" ed un parametro "n"
def media_mobile(numeri, n):
#creo una variabile lista in cui poi andrò a memorizzare le varie medie mobili
    risultato =[]
#creo un ciclo for che vada a scorrere gli elementi della lista e svolga le successive operazioni
    for i in range(len(numeri)):
#creo una variabile gruppo per prendere ad ogni iterazione il gruppo di numeri positivi con inizio= "i - n + 1" e fine = "i+1"
        gruppo = numeri[max(0,i - n + 1): i + 1]
#creo la variabile media che equivarrà alla somma degli elementi nel gruppo fratto il numero degli elementi del gruppo
        media = sum(gruppo) / len(gruppo)
#aggiungo alla variabile risultato, in ultima posizione, la media ottenuta
        risultato.append(media)
#al termine del ciclo ritorno il contenuto della variabile risultato
    return risultato

#numeri = [11, 37, 16, 4, 12, 15, 22]
#n = 2
#print(media_mobile(numeri, n))





# Scrivi una funzione che analizzi una stringa di testo e restituisca un dizionario con il conteggio delle occorrenze di ciascuna parola.
# Ignora la punteggiatura e considera le parole in modo case-insensitive. 
# Suggerimenti: ● Usa il metodo str.lower() per convertire il testo in minuscolo. 
# ● Usa il modulo re per rimuovere la punteggiatura. 
# ● Usa un dizionario per tenere traccia delle occorrenze delle parole. 
# Esempio di input: testo = "Ciao, ciao! Come stai? Stai bene?" Esempio di output: {'ciao': 2, 'come': 1, 'stai': 2, 'bene': 1}

#importo il modulo re
import re
#definisco il nome della funzione ed i parametri
def conteggio_parole(frase):

#converto tutto in lower case
    frase = frase.lower()

#rimuovo tutta la punteggiatura e la sostituisco con uno spazio
    frase = re.sub(r'[^\w\s]', "", frase)

# Divido la frase in parole (ogni parola è separata da uno spazio)
    elementi = frase.split()

# Creo un dizionario vuoto per salvare le occorrenze
    conteggio = {}

#credo un ciclo for che per ogni i all'interno della variabile elementi controlli se i è presente nel dizionario conteggio.
#in caso affermativo aumenta il conteggio di 1 altrimenti lo imposta ad 1
    for i in elementi:
        if i in conteggio:
            conteggio[i] += 1
        else:
            conteggio[i] = 1

#restituisce il dizionario conteggio
    return conteggio

#print(conteggio_parole("Ciao, sono Marco e sono felice"))