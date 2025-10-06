/*
In questo esercizio proverò a creare un programma che includa la gran parte degli argomenti trattati nella lezione.
Cercherò dunque di redigere un algoritmo che:

1 calcoli la media di un tot numero di valutazioni(voti universitari), espresse in 30esimi, inseriti dall'utente.

3 Restituisca il voto massimo ed eventualmente il numero di 30 e lode ricevuti.
*/

//Richiamo la libreria stdio.h
#include <stdio.h>
//richiamo la funzione main
int main(){
printf("Ciao! Benvenuto! Con questo programma calcoleremo la media dei tuoi voti espressa in trentesimi! (Il numero massimo di valori inseriti non può superare 100)");
printf("\nIn caso di 30 e lode ti preghiamo di inserire il valore '31'");
printf("\nProcediamo dunque senza indugi!");
//Dichiarazione di un array dove contenere i voti inseriti dall'utente
int voti [100] = {0};
//Dichiarazioni variabili per ciclo while
int n;
n = 0;
int voto;
//Costruisco il ciclo while con un numero massimo di 100 voti
while (n<100) {
    //Chiedo all'utente di inserire il voto
    printf("\nInserisci di seguito il tuo voto oppure il valore '-1' per terminare: ");
    scanf("%d", &voto);
    //se il valore -1 è inserito si procede a terminare il ciclo.
    if (voto == -1) {
        break;
    }
    //se il voto non è compreso tra 18 e 30, ritorno l'errore e ignoro questo valore saltando il ciclo con "continue;"
    if (voto < 18 || voto >31) {
        printf("\nVoto non valido. Inserire un valore compreso tra 18 e 31");
        continue;
    }
    //ultima fase del while per inserire all'interno dell'array "voti" il voto inserito dall'utente nella posizione dell'array con valore dell'attuale n
    voti[n] = voto;
    //incremento poi il contatore n di 1 per proseguire il ciclo
    n = n + 1;
    if (n == 100) {
        printf("\nNumero massimo di voti raggiunto. Si procederà automaticamente al calcolo della media dei voti già inseriti");
    }
}
//dichiariamo ora le variabili, impostando il loro valore a 0, per l'esecuzione della media, il calcolo dei 30 e lode ed il voto massimo
int somma = 0;
int lode = 0;
int max = 0;

//iniziamo un ciclo for dove "i", il contatore, viene impostato a 0, il processo verrà eseguito finchè i sarà minore degli elementi contenuti nell'array e ad ogni ciclo i incrementerà di 1
for (int i=0; i<n; i=i+1) {

    //creo la variabile voto corrente a cui verrà attribuito il valore inserito dall'utente in corrispondenza dell'indice di valore i
    int voto_corrente = voti [i];

    //creo l'eccezione per il 30 e lode attribuendogli il valore 30 e aggiungendo il conteggio alla variabile lode
    if (voto_corrente == 31){
        somma = somma +30;
        lode = lode + 1;
    }
    //Se il valore è diverso da 31 allora la somma diventa somma + voto_corrente
    else {
        somma = somma + voto_corrente;
    }
    //Se il voto_corrente è superiore a max allora max assume il valore di voto_corrente
    if (voto_corrente > max) { 
        max = voto_corrente;
     }
}
//calcolo la media aritmetica dei voti nell'array
float media;
media = (float) somma / n;

//Restituisco i risultati all'utente
printf("\nLa media dei tuoi voti è: %f", media);
printf("\nIl voto massimo che hai ricevuto è stato: %d", max);

if (lode > 0) {
printf("\nCongratulazioni! Il numero di 30 e lode ricevuti è di: %d", lode);

}

return 0;
}
