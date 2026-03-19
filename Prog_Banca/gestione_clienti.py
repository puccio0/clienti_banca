#stampa priorità su lista data:

import json

def funzione_ordine(file_json='clienti.json'):
    """
    Legge i clienti da un file JSON, li ordina per priorità (5→1)
    e poi per patrimonio (alto→basso), e ritorna la lista ordinata.
    """
    # Leggi il file JSON
    with open(file_json, 'r', encoding='utf-8') as file:
        clienti = json.load(file)  # lista di dizionari

    # Se il file contiene un singolo dizionario, mettilo in lista
    if isinstance(clienti, dict):
        clienti = [clienti]

    # Ordina per priorità decrescente, poi per patrimonio decrescente
    clienti_ordinati = sorted(
        clienti,
        key=lambda x: (-x["priorita"], -x["patrimonio"])
    )

    # Ritorna la lista ordinata
    return clienti_ordinati

clienti_ordinati = funzione_ordine()

# Ciclo per stampare in modo lineare
print("\nClienti ordinati:\n")
for cliente in clienti_ordinati:
    print(f"{cliente['nome']:<15} {cliente['cognome']:<15} Priorità: {cliente['priorita']:<2} Patrimonio: {cliente['patrimonio']:>10.2f}")