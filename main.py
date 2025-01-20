from crud_operations import crea_prodotto, leggi_prodotti, aggiorna_prodotto, cancella_prodotto

def menu():
    print("\n--- MENU ---")
    print("1. Crea un prodotto")
    print("2. Visualizza prodotti")
    print("3. Aggiorna un prodotto")
    print("4. Cancella un prodotto")
    print("0. Esci")

def main():
    while True:
        menu()
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            nome = input("Nome del prodotto: ")
            prezzo = float(input("Prezzo del prodotto: "))
            categoria = input("Categoria del prodotto: ")
            quantità = int(input("Quantità disponibile: "))
            id_fornitore = int(input("ID del fornitore: "))
            crea_prodotto(nome, prezzo, categoria, quantità, id_fornitore)
        elif scelta == "2":
            leggi_prodotti()
        elif scelta == "3":
            id = int(input("ID del prodotto da aggiornare: "))
            nuovo_prezzo = float(input("Nuovo prezzo: "))
            aggiorna_prodotto(id, nuovo_prezzo)
        elif scelta == "4":
            id = int(input("ID del prodotto da cancellare: "))
            cancella_prodotto(id)
        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova!")

if __name__ == "__main__":
    main()
