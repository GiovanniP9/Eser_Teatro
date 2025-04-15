
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
    def prenota(self):#metodo per prenotare il posto VIP
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
        self.__costo_online = 1.20 if self.__prenotazione else 0.0 #costo per prenotazione online se prenotato online 
    
    def prenota(self, prenotazione=False):#metodo per prenotare il posto standard
        if not self._occupato:
            super().prenota()
            costo_totale = self.__costo_base + self.__costo_online
            print(f" Prenotato online: {"sì" if prenotazione else "no"}") 
            print(f"costo prenotazione: {self.__costo_online:.2f}€")
            print(f"Costo totale: {costo_totale:.2f}€")
        else:
            print(f"Posto Standard {self._numero} nella fila {self._fila} già occupato.")

        

        