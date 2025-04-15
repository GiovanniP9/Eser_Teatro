class Teatro:
    def __init__(self):
        # Lista che conterrà tutti gli oggetti Posto (posti disponibili nel teatro)
        self._posti = []

    def aggiungi_posto(self, numero, fila):
        """Controlla se il posto esiste già nella lista"""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                print(f"Posto {numero} nella fila {fila} esiste già.")
                return
        # Se non esiste, crea un nuovo Posto e lo aggiunge alla lista
        nuovo_posto = Posto(numero, fila)
        self._posti.append(nuovo_posto)
        print(f"Posto {numero} nella fila {fila} aggiunto.")

    def prenota_posto(self, numero, fila):
        """Cerca il posto specificato nella lista e prova a prenotarlo"""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
        # Se il posto non esiste, stampa un messaggio di errore
        print(f"Posto {numero} nella fila {fila} non trovato.")

    def libera_posto(self, numero, fila):
        """Cerca il posto specificato nella lista e prova a liberarlo"""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.libera()
                return
        # Se il posto non esiste, stampa un messaggio di errore
        print(f"Posto {numero} nella fila {fila} non trovato.")

    def mostra_posti(self):
        """Se non ci sono posti nella lista, informa l'utente"""
        if not self._posti:
            print("Nessun posto presente.")
            return
        # Ordina i posti per fila e numero per una visualizzazione ordinata
        posti_ordinati = sorted(self._posti, key=lambda p: (p.get_fila(), p.get_numero()))
        print("\nElenco posti:")
        # Stampa lo stato di ciascun posto (occupato o libero)
        for posto in posti_ordinati:
            stato = "Occupato" if posto.is_occupato() else "Libero"
            print(f"Fila {posto.get_fila()} - Posto {posto.get_numero()}: {stato}")

# Creazione del menu a tendina
def menu_teatro():
    teatro = Teatro() # istanzia teatro

    while True:
        print("\n--- GESTIONE TEATRO ---")
        print("1. Aggiungi posto")
        print("2. Prenota posto")
        print("3. Libera posto")
        print("4. Mostra tutti i posti")
        print("5. Esci")

        scelta = input("Seleziona un'opzione (1-5): ")

        if scelta == "1":
            fila = input("Inserisci la fila (es. A): ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            teatro.aggiungi_posto(numero, fila)

        elif scelta == "2":
            fila = input("Inserisci la fila del posto da prenotare: ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            teatro.prenota_posto(numero, fila)

        elif scelta == "3":
            fila = input("Inserisci la fila del posto da liberare: ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            teatro.libera_posto(numero, fila)

        elif scelta == "4":
            teatro.mostra_posti()

        elif scelta == "5":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")

# Avvio del menu
menu_teatro()
