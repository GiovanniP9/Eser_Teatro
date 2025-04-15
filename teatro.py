
class Posto: #classe base
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    def prenota(self): #metodo per prenotare il posto
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._numero} nella fila {self._fila} prenotato.")
        else:
            print(f"Posto {self._numero} nella fila {self._fila} già occupato.")
    def libera(self):#metodo per liberare il posto
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._numero} nella fila {self._fila} liberato.")
        else:
            print(f"Posto {self._numero} nella fila {self._fila} non era prenotato.")
    
    def get_numero(self):#metodo per ottenere il numero del posto
        return self._numero
    def get_fila(self):#metodo per ottenere la fila del posto
        return self._fila
    def is_occupato(self):#metodo per verificare se il posto è occupato
        return self._occupato

#classe Posto VIP
class PostoVIP(Posto):
    def __init__(self, numero, fila, servizi_extra, costo_base, costo_extra):
        super().__init__(numero, fila)
        self.__servizi_extra = servizi_extra
        self.__costo_base = costo_base
        self.__costo_extra = costo_extra
    def prenota(self, *args):#metodo per prenotare il posto VIP
        if not self._occupato:
            super().prenota()
            costo_totale = self.__costo_base + (self.__costo_extra * len(self.__servizi_extra))
            print(f"Servizi extra:", "," .join(self.__servizi_extra))
            print(f"Costo totale: {costo_totale:.2f}€")
        else:
            print(f"Posto VIP {self._numero} nella fila {self._fila} già occupato.")

#CLASSE POSTO STANDARD
class PostoStandard(Posto):
    def __init__(self, numero, fila, costo_base,):
        super().__init__(numero, fila)
        self.__costo_base = costo_base
        self.__costo_online = 1.20 #costo per prenotazione online se prenotato online 
    
    def prenota(self, prenotazione=False):#metodo per prenotare il posto standard
        if not self._occupato:
            super().prenota()
            if prenotazione:
                costo_totale = self.__costo_base + self.__costo_online
                print(f" Prenotato online: {"sì" if prenotazione else "no"}") 
                print(f"costo prenotazione: {self.__costo_online:.2f}€")
                print(f"Costo totale: {costo_totale:.2f}€")
            else:
                print(f" Prenotato online: {"sì" if prenotazione else "no"}")
                print(f"Costo totale: {self.__costo_base:.2f}€")

        else:
            print(f"Posto Standard {self._numero} nella fila {self._fila} già occupato.")
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

    def prenota_posto(self, numero, fila, prenotato=False):
        """Cerca il posto specificato nella lista e prova a prenotarlo"""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                if isinstance(posto, PostoStandard):
                    posto.prenota(prenotato)
                else:
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
            tipo = input("Tipo di posto (standard/vip): ").lower()
            fila = input("Inserisci la fila (es. A): ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            if tipo == "vip":
                servizi = input("Servizi extra (es. champagne, snack): ").split(",")
                servizi = [s.strip() for s in servizi]
                costo_base = float(input("Inserisci il costo base: "))
                costo_extra = float(input("Inserisci il costo extra per servizio: "))
                posto_vip = PostoVIP(numero, fila, servizi, costo_base, costo_extra)
                teatro._posti.append(posto_vip)
            elif tipo == "standard":
                costo_base = float(input("Inserisci il costo base: "))
                posto_standard = PostoStandard(numero, fila, costo_base)
                teatro._posti.append(posto_standard)
            else:
                print("Tipo di posto non valido. Inserire 'standard' o 'vip'.")
                continue

        elif scelta == "2":
            fila = input("Inserisci la fila del posto da prenotare: ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            risposta = input("Prenotato online? (si/no): ").strip().lower()
            prenota_online = risposta == "si"
            print(f"[DEBUG] prenotato_online interpretato come: {prenota_online}")
            teatro.prenota_posto(numero, fila, prenota_online)

            
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
