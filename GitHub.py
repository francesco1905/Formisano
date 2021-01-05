Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from os import system, path
>>> from sys import platform, executable
>>> #Importo le librerie
>>> assert platform  in ['darwin', 'win32', 'cygwin']
>>> directory = path.dirname(executable)
>>> #Controllo la cartella di installazione di Python
>>> print("Benvenuto!")
Benvenuto!
>>> while True:
...     while True:
...         #Chiedo se si deve installare o disinstallare una libreria
...         choice = input("\n-Premi 1 per installare una libreia\n-Premi 2 per disinstallare una libreria\n--> ")
...         if choice in [1,2,"1","2"]:
...             #Se la risposta dell'utente è valida rompo il ciclo
...             break
...         else:
...             #Altrimenti avverto l'utente e ricomincio il ciclo
...             print("Valore non valido\nI valori validi sono solo 1 e 2")
...     #Controllo se il sistema operativo è MacOS o Windows, diversamente da errore
...     libreria = input("Come si chiama la tua libreria?  --> ")
...     #Chiedo il nome della libreria da installare
...     if choice in [1,"1"]:
...         #A seconda della scelta dell'utente il comando sarà di installare o disinstallare la libreria
...         command = "install"
...     else:
...         command = "uninstall -y"
...         #-y indica che non verrà chiesta la conferma per disinstallare la libreria
...
...     if platform  in ['win32', 'cygwin']:
...         system(f"cd {directory}\\Scripts && pip {command} {libreria}")
...         #Se la piattaforma è Windows lo slash è \, si usa doppio da sintassi di python
...     else:
...         system(f"cd {directory}/Scripts && pip {command} {libreria}")
...         #Se la piattaforma è MacOS lo slash è /
...     #Grazie al terminale vado nella cartella Scripts di Python e installo\disinstallo la libreria
...     input("\n\n\n-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne  l'esecuzione  ")
...     #Se viene premuto invio il ciclo si ripete, se l'utente preme ctrl+c il programma verrà chiuso dall'errore KeyboardInterrupt
...

-Premi 1 per installare una libreia
-Premi 2 per disinstallare una libreria
--> 1
Come si chiama la tua libreria?  --> matplotlib
Requirement already satisfied: matplotlib in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (3.3.3)
Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (1.3.1)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (2.4.7)
Requirement already satisfied: python-dateutil>=2.1 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (2.8.1)
Requirement already satisfied: pillow>=6.2.0 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (8.1.0)
Requirement already satisfied: cycler>=0.10 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (0.10.0)
Requirement already satisfied: numpy>=1.15 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from matplotlib) (1.19.4)
Requirement already satisfied: six>=1.5 in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (from python-dateutil>=2.1->matplotlib) (1.15.0)
WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.
You should consider upgrading via the 'c:\users\formisano\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.
0



-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne  l'esecuzione
''

-Premi 1 per installare una libreia
-Premi 2 per disinstallare una libreria
--> 1
Come si chiama la tua libreria?  --> numpy
Requirement already satisfied: numpy in c:\users\formisano\appdata\local\programs\python\python39\lib\site-packages (1.19.4)
WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.
You should consider upgrading via the 'c:\users\formisano\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip' command.
0



-Premi invio per riutilizzare il programma o premi ctrl + c per terminarne  l'esecuzione