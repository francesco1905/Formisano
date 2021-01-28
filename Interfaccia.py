# includiamo questo modulo per creare numeri casuali
from random import randint

# per accedere ad un file devo assegnare
# ad un oggetto il file da aprire, in lettura o scrittura

# associo ad f il file, indico con "w" il tipo di operazione
# così lo aprirà in scrittura (write)

f = open("dati4.txt", 'w')

# definiamo una variabile stringa da riempire con i dati che poi scriverò
imput=str
# inizializzo la stringa
dati = ""

# il primo ciclo serve a creare le singole righe
for riga in range(100):

    # il secondo ciclo serve a compulare la singola riga
    for elemento in range(1):

        # aggiungo il numero casuale e inserisco uno spazio in coda
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
    
    # aggiungo un terminatore di riga, così il secondo rigo va a capo
    dati = dati + "\n"

# avremmo potuto creare una lista di righe:
# lines = [
#...     'prima riga del file\n',
#...     'seconda riga del file\n',
#...     'terza riga del file\n',
#... ]

print()

# scrivo la stringa nel file
f.write(dati)

# chdiuamo sempre il file
f.close()

60,92
57,63
1,34
59,50
40,18
92,79
4,66
8,32
54,36
26,56
50,23
34,8
92,31
5,42
81,66
61,73
81,36
49,49
17,81
51,14
16,49
32,16
66,54
72,5
82,14
51,88
21,7
76,53
87,59
65,93
44,73
70,65
82,33
22,61
69,49
91,89
25,1
5,80
82,54
40,64
37,60
75,6
92,62
88,48
97,11
86,20
61,70
22,25
20,49
98,62
48,16
20,50
83,44
71,31
19,61
22,98
9,63
3,89
81,58
6,92
74,70
2,88
20,66
58,72
45,59
73,23
66,13
18,2
37,75
33,53
90,33
74,62
29,48
82,46
89,21
85,66
36,51
13,83
66,19
10,31
8,6
59,60
87,48
74,74
82,88
32,17
99,54
91,30
31,57
62,74
39,41
45,44
58,26
55,74
46,29
1,24
77,28
90,80
53,67
37,37