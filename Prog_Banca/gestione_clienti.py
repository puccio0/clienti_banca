#stampa priorità su lista data:

import json

def funzione_ordine(file_json='clienti.json'):
    """
    Legge i clienti da un file JSON, li ordina per priorità (5→1)
    e poi per patrimonio (alto→basso), e ritorna la lista ordinata.
    """
    with open(file_json, 'r', encoding='utf-8') as file:
        clienti = json.load(file)  # lista di dizionari

    if isinstance(clienti, dict):
        clienti = [clienti]

    clienti_ordinati = sorted(clienti, key=lambda x: (-x["priorita"], -x["patrimonio"]))
    return clienti_ordinati

# Lista iniziale ordinata
clienti_ordinati = funzione_ordine()

print("\nClienti ordinati iniziali:\n")
for cliente in clienti_ordinati:
    print(f"{cliente['nome']:<15} {cliente['cognome']:<15} Priorità: {cliente['priorita']:<2} Patrimonio: {cliente['patrimonio']:>10.2f}")

# Nuovo cliente da inserire
nuovo_cliente = {
    "nome": "Marco",
    "cognome": "Conti",
    "eta": 19,
    "patrimonio": 517913.47,
    "priorita": 6
}

# Funzione per aggiungere il nuovo cliente
def aggiungi_cliente(clienti, nuovo_cliente):
    clienti.append(nuovo_cliente)
    return sorted(clienti, key=lambda x: (-x["priorita"], -x["patrimonio"]))

# Aggiorna lista con il nuovo cliente
clienti_ordinati = aggiungi_cliente(clienti_ordinati, nuovo_cliente)

print("\nLista aggiornata con nuovo cliente:\n")
for cliente in clienti_ordinati:
    print(f"{cliente['nome']:<15} {cliente['cognome']:<15} Priorità: {cliente['priorita']:<2} Patrimonio: {cliente['patrimonio']:>10.2f}")

# Funzione per trovare il cliente più ricco
def cliente_piu_ricco(clienti):
    return max(clienti, key=lambda x: x["patrimonio"])

piu_ricco = cliente_piu_ricco(clienti_ordinati)
print("\nCliente più ricco:\n")
print(f"{piu_ricco['nome']} {piu_ricco['cognome']} - Patrimonio: {piu_ricco['patrimonio']:.2f}")