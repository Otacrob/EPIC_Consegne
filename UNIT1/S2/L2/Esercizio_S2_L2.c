//inserisco la libreria stdio.h
#include <stdio.h>

//avvio la funzione main
int main(){
//definisco le due variabili
int n1;
int n2;
//chiedo all'utente di inserire i due valori
printf("Ciao! Questo programma ti aiuterà a calcolare il prodotto tra due numeri interi e la loro media!");
printf("\nInserisci il primo valore!: ");
scanf("%d", &n1);
printf("\nInserisci ora il secondo numero!: ");
scanf("%d", &n2);
//definisco la variabile prodotto e la variabile media
int prodotto;
int media;
//assegno il valore corretto alle nuova variabile
prodotto = n1 * n2;
media = (n1 + n2) / 2;
//stampo l'output dell'operazione
printf("\nOttimo! Ecco il tuo risultato: %d", prodotto);
printf("\nEcco invece la media dei due numeri!: %d", media);
return 0;
}
