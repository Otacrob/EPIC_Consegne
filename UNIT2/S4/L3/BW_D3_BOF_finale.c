// file: BW_D3_BOF_finale.c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <ctype.h>
#include <limits.h>

#define CAP 10  // capienza reale dell'array

/* Lettura robusta di un intero da stdin:
   - prompt opzionale
   - accetta solo numeri (con segno)
   - nessun carattere extra dopo il numero
   - range [min..max]
   Ritorna 1 se ok, 0 su EOF/errore stream.
*/
static int leggi_int_sicuro(const char *prompt, long min, long max, int *out) {
    char buf[128];
    for (;;) {
        if (prompt) printf("%s", prompt);
        if (!fgets(buf, sizeof buf, stdin)) return 0;  // EOF/errore

        char *p = buf;
        while (isspace((unsigned char)*p)) p++;

        errno = 0;
        char *end = NULL;
        long v = strtol(p, &end, 10);

        if (end == p || errno == ERANGE || v < LONG_MIN || v > LONG_MAX) {
            puts("Input non valido. Inserire un intero.");
            continue;
        }
        while (isspace((unsigned char)*end)) end++;
        if (*end != '\0' && *end != '\n') {
            puts("Caratteri extra dopo il numero. Riprova.");
            continue;
        }
        if (v < min || v > max) {
            printf("Valore fuori range (%ld..%ld). Riprova.\n", min, max);
            continue;
        }
        *out = (int)v;
        return 1;
    }
}

int main(void) {
    int scelta;
    if (!leggi_int_sicuro(
            "Scegli modalità:\n"
            "1) Vulnerabile (BOF: consente >10 inserimenti)\n"
            "2) Originale (base: sempre 10 inserimenti)\n"
            "Scelta: ",
            1, 2, &scelta)) return 1;

    if (scelta == 1) {
        /* ------------------ MODALITÀ VULNERABILE ------------------
           - Array fisso da 10
           - n scelto dall'utente, minimo 1 (nessun limite superiore)
           - LETTURE robuste, ma se n > CAP si scrive/legge OOB => BOF
        */
        int vector[CAP], i, j, k, swap_var;
        int n;

        if (!leggi_int_sicuro("Quanti interi vuoi inserire? ", 1, INT_MAX, &n)) return 1;

        printf("Inserire %d interi:\n", n);
        for (i = 0; i < n; i++) {                   // OOB se i >= CAP
            char prompt[32];
            snprintf(prompt, sizeof prompt, "[%d]:", i + 1);
            /* Leggiamo in modo robusto, ma NON limitiamo 'n' alla capienza:
               la vulnerabilità resta (si scrive oltre vector[CAP]). */
            if (!leggi_int_sicuro(prompt, INT_MIN, INT_MAX, &vector[i])) return 1;
        }

        printf("Il vettore inserito e':\n");
        for (i = 0; i < n; i++) {                   // OOB se i >= CAP
            printf("[%d]: %d\n", i + 1, vector[i]);
        }

        for (j = 0; j < n - 1; j++) {               // OOB se n > CAP
            for (k = 0; k < n - j - 1; k++) {
                if (vector[k] > vector[k + 1]) {
                    swap_var = vector[k];
                    vector[k] = vector[k + 1];
                    vector[k + 1] = swap_var;
                }
            }
        }

        printf("Il vettore ordinato e':\n");
        for (j = 0; j < n; j++) {                   // OOB se j >= CAP
            printf("[%d]: %d\n", j + 1, vector[j]);
        }

    } else {
        /* ------------------ MODALITÀ ORIGINALE (base SICURA) ------------------
           - Sempre 10 inserimenti
           - Input numerici validati (niente caratteri extra, niente EOF silenziosi)
        */
        int vector[10], i, j, k, swap_var;

        printf("\n[Modalità ORIGINALE] Inserire 10 interi:\n");
        for (i = 0; i < 10; i++) {
            char prompt[32];
            snprintf(prompt, sizeof prompt, "[%d]:", i + 1);
            if (!leggi_int_sicuro(prompt, INT_MIN, INT_MAX, &vector[i])) return 1;
        }

        printf("Il vettore inserito e':\n");
        for (i = 0; i < 10; i++) {
            printf("[%d]: %d\n", i + 1, vector[i]);
        }

        for (j = 0; j < 10 - 1; j++) {
            for (k = 0; k < 10 - j - 1; k++) {
                if (vector[k] > vector[k + 1]) {
                    swap_var = vector[k];
                    vector[k] = vector[k + 1];
                    vector[k + 1] = swap_var;
                }
            }
        }

        printf("Il vettore ordinato e':\n");
        for (j = 0; j < 10; j++) {
            printf("[%d]: %d\n", j + 1, vector[j]);
        }
    }

    return 0;
}
