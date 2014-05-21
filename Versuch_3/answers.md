#Fragen zu Versuch 3 (Recommender Systeme mit Collaborative Filtering)

## 1.4.1 Beschreiben Sie das Prinzip des userbasierten Collaborativen Filterin (UCF).

Beim UCF wird die Ähnlichkeit zwischen Benutzern (Usern) verwendet. Für einen User A wird dann ein User B,
oder auch Gruppe von Usern, gesucht die B am ähnlichsten sind.
Nun werden User A Produkte angeboten die B gekauft hat aber A noch nicht besitzt.

## 1.4.2 Welche Nachteile hat das UCF?

Beim UCF wird immer ein passender ähnlicher User gefunden und mit dem aktuellen User verglichen.
Dieses Vorgehen skaliert schlecht bei großen User- und Produkt-Beständen, da eine Analyse aller User
und aller Produkte der User durchgeführt werden muss.
Zusätzlich liefert dieses System für neue User mit wenigen Daten ein ungenaues Ergebniss.

## 1.4.3 Worin besteht der Unterschied zwischen UCF und itembasierten Collaborativen Filtering (ICF)?

Das UCF vegleicht den Datenbestand zweier User, wohingegen das ICF die Ähnlichkeit zwischen Produkten nutzt.
Beim ICF muss man nur einzelne Produktklassen betrachten,
daher skaliert das ICF weitaus besser mit großen Datenmengen.

**Beispiel:**
Eine Festplatte der Firma Hitachi ist ein ähnliches Produkt wie eine Festplatte der Firma Samsung.
A und viele andere User haben die Hitachi Festplatte gekauft. Ein Großteil der anderen Benutzer haben aber auch
die Samsung Festplatte gekauft.
A besitzt die Samsung Festplatte jedoch nicht, daher wird ihm diese Festplatte Empfohlen.

## 1.4.4 Gegeben seien die Vektoren a=[1,2,3,4,5,6] und b=[3,3,5,6,7,8] Zeigen Sie am Beispiel des Vektors a wie Mittelwert und Varianz eines Vektors berechnet werden.

**Mittelwert:**

    (1 + 2 + 3 + 4 + 5 + 6) / 6
    = 21 / 6
    = 3.5

**Varianz:**

    ( (1-3.5)²+(2-3.5)²+(3-3.5)²+(4-3.5)²+(5-3.5)²+(6-3.5)² ) / 6
    = 17.5 / 6
    = 2.92

## 1.4.5 Wie werden Mittelwert und Varianz mit numpy berechnet?

**Mittelwert:**

in python mit numpy:

    aMean = np.mean(a)

**Varianz:**

in python mit numpy:

    aVar = np.var(a)


## 1.4.6 Wie groß ist die:  Euklidsche Ähnlichkeit, Pearson Ähnlichkeit und Cosinus Ähnlichkeit zwischen den Vektoren a und b?



## 1.4.7 In welchen Fällen sind Cosinus und Pearsonähnlichkeit der euklidschen Ähnlichkeit vorzuziehen?



## 1.4.8 Wie wird in Python ein doppelt verschachteltes Dictionary angelegt und wie greift man auf dessen Elemente zu?



## 1.4.9 Wie können mit Hilfe der last.fm-Api pylast.py alle Alben einer Band bestimmt werden?


