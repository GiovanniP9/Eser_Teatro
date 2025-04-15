# Eser_Teatro
# Gestione Posti Teatro - Progetto Python con Polimorfismo

## Descrizione

Questo progetto implementa un sistema di **gestione dei posti in un teatro** tramite un'interfaccia testuale. L'obiettivo è simulare l'aggiunta, la prenotazione e la liberazione dei posti, sfruttando il **polimorfismo** per gestire diverse tipologie di posto (Standard e VIP) in modo flessibile e scalabile.

## Funzionalità principali

- Aggiunta di posti standard e VIP
- Prenotazione con calcolo dei costi (inclusi servizi extra o prenotazione online)
- Liberazione dei posti prenotati
- Visualizzazione dello stato attuale dei posti (occupati/liberi)
- Interfaccia testuale semplice tramite menu

## Architettura del codice

Il progetto si basa su una **gerarchia di classi**:

### `Posto` (classe base)
Rappresenta un posto generico con:
- numero
- fila
- stato (occupato/libero)

Metodi principali:
- `prenota()`
- `libera()`
- `is_occupato()`

### `PostoStandard` (classe derivata)
Estende `Posto` e rappresenta un posto prenotabile anche online, aggiungendo un piccolo sovrapprezzo.

Polimorfismo: ridefinisce il metodo `prenota(prenotazione=False)` per includere la logica del costo online.

### `PostoVIP` (classe derivata)
Estende `Posto` e rappresenta un posto con **servizi extra** e costi aggiuntivi.

Polimorfismo: ridefinisce `prenota()` per calcolare il costo in base ai servizi selezionati.

### `Teatro`
Gestisce una lista di oggetti `Posto`, che possono essere di qualsiasi sottoclasse (`PostoStandard`, `PostoVIP`, ecc.).

Metodi:
- `aggiungi_posto()`
- `prenota_posto()`
- `libera_posto()`
- `mostra_posti()`

Usa **`isinstance`** per applicare il comportamento corretto in base alla sottoclasse del posto.

## Documentazione
- Giovanni si è occupato della scrittura della classe `Posto` (base) e delle classi `PostoVIP` e `PostoStandard` (derivate) e della risoluzione degli errori che erano sorti durante la fase di debug del codice.
- Nunzio si è occupato della scrittura della classe `Teatro` che fa da gestore delle altre classi posto attraverso una lista, e del menù.
  
## Esempio d'uso

Una volta avviato il programma (`menu_teatro()`), l'utente può:

1. **Aggiungere posti** specificando il tipo (standard o VIP)
2. **Prenotare posti**, anche online nel caso di standard
3. **Liberare posti** occupati
4. **Visualizzare lo stato** di tutti i posti
5. **Uscire** dal programma

---

## Come eseguire

Assicurati di avere Python 3 installato. Per avviare il programma:

```bash
python nome_del_file.py

