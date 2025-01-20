from models import Session, Prodotto, Fornitore

# Creazione di una nuova sessione
session = Session()

# Funzione per creare un prodotto
def crea_prodotto(nome, prezzo, categoria, quantità, id_fornitore):
    try:
        nuovo_prodotto = Prodotto(
            nome=nome,
            prezzo=prezzo,
            categoria=categoria,
            quantità=quantità,
            id_fornitore=id_fornitore
        )
        session.add(nuovo_prodotto)
        session.commit()
        print("Prodotto creato con successo!")
    except Exception as e:
        session.rollback()
        print(f"Errore durante la creazione del prodotto: {e}")
    finally:
        session.close()

# Funzione per leggere tutti i prodotti
def leggi_prodotti():
    try:
        prodotti = session.query(Prodotto).all()
        for prodotto in prodotti:
            print(f"ID: {prodotto.id}, Nome: {prodotto.nome}, Prezzo: {prodotto.prezzo}€, Categoria: {prodotto.categoria}")
    except Exception as e:
        print(f"Errore durante la lettura dei prodotti: {e}")
    finally:
        session.close()

# Funzione per aggiornare un prodotto
def aggiorna_prodotto(id, nuovo_prezzo):
    try:
        prodotto = session.query(Prodotto).get(id)
        if prodotto:
            prodotto.prezzo = nuovo_prezzo
            session.commit()
            print("Prezzo aggiornato con successo!")
        else:
            print("Prodotto non trovato!")
    except Exception as e:
        session.rollback()
        print(f"Errore durante l'aggiornamento del prodotto: {e}")
    finally:
        session.close()

# Funzione per cancellare un prodotto
def cancella_prodotto(id):
    try:
        prodotto = session.query(Prodotto).get(id)
        if prodotto:
            session.delete(prodotto)
            session.commit()
            print("Prodotto cancellato con successo!")
        else:
            print("Prodotto non trovato!")
    except Exception as e:
        session.rollback()
        print(f"Errore durante la cancellazione del prodotto: {e}")
    finally:
        session.close()
