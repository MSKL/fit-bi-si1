# Model nasazení
Kapitola popisuje nasazení aplikace na server. 
Celá aplikace je koncipována vytvořena jako webová aplikace, takže je možné ji spouštět na zařízení, 
které bude sloužit jako webový server. 
Celý postup nasazení aplikace se skládá z těchto kroků:
1. Instalace všech balíků, na kterých chod aplikace závisí.
2. Inicializace databáze.
3. Konfigurace webového serveru.
4. Spuštění webového serveru umožňujícího ověření implementované funkčnosti.

## 1. Inicializace všech potřebných balíků
Aplikace je napsána v jazyce Python3 s použitím několika modulů.
- flask
- flask_login
- flask_bootstrap
- flask_sqlalchemy
Všechny moduly potřebné pro spuštění aplikace jsou vydefinované v souboru requirements.txt. Tyto moduly je nejsnažší nainstalovat pomocí apliakace pip3 pomocí příkazu:
```bash
pip3 install -r requirements.txt
```

## 2. Inicializace databáze
Aplikace je navázána na databázi sqlite3 a počítá s umístěním souboru database.db v rootu aplikace. Toto umístění je ovšem možné změnit v konfiguračním soboru. Databáze obsahuje data potřebná pro otestování základní funkčnosti a není potřeba nic dalšího instalovat či spouštět. 

## 3. Konfigurace webového serveru
Konfigurace webového serveru se provádí v souboru config_host.py. Je potřeba nastavit správnou IP adresu a port, 
na kterém bude služba běžet. Pokud není tento soubor změněn, běží aplikace na 127.0.0.1:3333.

## 4. Spuštění aplikace
Posledním krokem při nasazování této aplikace je její spuštění. Spuštění lze docílit zadáním:
```bash
python3 main.py 
```

Implementovaný protoyp aplikace obsahuje prozatím systém, do kterého se uživatel může přihlásit, a následně se podívat, 
jaké jsou nadcházející závody na které se může přihlásit. Je taktéž implementován základní login systém. Pokud má 
uživatel dostatečná oprávnění, je možné i závody editovat a případně mazat.
