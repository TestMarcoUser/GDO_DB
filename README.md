# GDO_DB
Configurazione per MySQL
1. Creazione del Database
Prima di eseguire il codice Python, crea il database in MySQL:

CREATE DATABASE GDO_DB;

2. Modifica del File models.py
Aggiornare la stringa di connessione DATABASE_URL con le tue credenziali MySQL:

DATABASE_URL = "mysql+pymysql://username:password@localhost/GDO_DB"
Vanno Sostituite:

Ho utilizzato valori generici sul DB locale.
username con il nome utente di MySQL.
password con la tua password di MySQL.
