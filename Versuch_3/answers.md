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

**Euklische Ähnlichkeit:**

    d_E(a,b) = sqrt( sum(a-b)² )
    = sqrt( (1-3)² + (2-3)² + (3-5)² + (4-6)² + (5-7)² + (6-8)² )
    = sqrt( 21 )
    = 4.58

    s_e(a,b) = 1 / (1 + 4.58) = 0,18

**Pearson Ähnlichkeit:**

    aMean = 3.5
    aVar = 2.92
    bMean = 5.33
    bVar = 3.56
    p_(a,b) = 1/N * sum( ((a_i - aMean)*(b_i - bMean)) / (aVar * bVar) )
    = 1/6 * (
            ( ((1 - 3.5)*(3 - 5.33)) / (2.92 * 3.56) )
            + ( ((2 - 3.5)*(3 - 5.33)) / (2.92 * 3.56) )
            + ( ((3 - 3.5)*(5 - 5.33)) / (2.92 * 3.56) )
            + ( ((4 - 3.5)*(6 - 5.33)) / (2.92 * 3.56) )
            + ( ((5 - 3.5)*(7 - 5.33)) / (2.92 * 3.56) )
            + ( ((6 - 3.5)*(8 - 5.33)) / (2.92 * 3.56) )
        )
    = 0.31

**Cosinus Ähnlichkeit:**

    cos(a,b) = (a*b) / (|a| * |b|)
    = ({1,2,3,4,5,6} * {3,3,5,6,7,8}) / (6 * 6)
    = 131 / 36
    = 3.64
	
Mit: `|a| = sqrt(a*a)`

	|a| = 9.599
	|b| = 13.856
	(a * b) = {1,2,3,4,5,6} * {3,3,5,6,7,8} = 131
	cos(a,b) = (a*b) / (|a| * |b|)
	= 131 / (9.599 * 13.856)
	= 0.991
	
	

## 1.4.7 In welchen Fällen sind Cosinus und Pearsonähnlichkeit der euklidschen Ähnlichkeit vorzuziehen?

Cosinus und Peasonähnlichkeit eignet sich besonders für Skalierende werte,
da es nicht die Distanz zu 2 Werten berechnet sondern den Abstand von
einem Idealwert und darüberhinaus Informationen über die Richtung angibt.
Cosinus und Pearsonähnlichkeit eignet sich daher für Collaborative Fitting.

## 1.4.8 Wie wird in Python ein doppelt verschachteltes Dictionary angelegt und wie greift man auf dessen Elemente zu?

    >>> dict = {}
    >>> dict['dictA'] = {}
    >>> dict['dictB'] = {}
    >>> dict['dictA']['dictAA'] = {}
    >>> dict['dictA']['dictAB'] = {}
    >>> dict['dictA']['dictAA']['key1'] = 'value1'
    >>> dict['dictA']['dictAB']['key2'] = 'value2'
    >>> dict['dictB']['dictBA'] = {}
    >>> dict['dictB']['dictBB'] = {}
    >>> dict['dictB']['dictBA']['key3'] = 'value3'
    >>> dict['dictB']['dictBB']['key4'] = 'value4'
    >>> print dict
    >>> print dict['dictA']['dictAB']['key2']

    {
        'dictA':
        {
            'dictAA':
            {
                'key1': 'value1'
            },
            'dictAB':
            {
                'key2': 'value2'
            }
        },
        'dictB':
        {
            'dictBA':
            {
                'key3': 'value3'
            },
            'dictBB':
            {
                'key4': 'value4'
            }
        }
    }
    value2

## 1.4.9 Wie können mit Hilfe der last.fm-Api pylast.py alle Alben einer Band bestimmt werden?

Theoretisch ermittelbar über folgenden Code:

    import pylast as fm
    network=fm.get_lastfm_network()
    madonna = network.get_artist("Madonna")
    albums = madonna.get_top_albums()
    print madonna
    print albums

Ergebnis hier ist eine Liste wie hier (gekürzt):

    [TopItem(item=Madonna - Celebration, weight=u'481971'),
    TopItem(item=Madonna - Ray of Light, weight=u'330368'),
    TopItem(item=Madonna - Confessions on a Dance Floor, weight=u'352418'),
    ... ]

Problem: Wir erhalten jede CD die jemals erschienen ist, somit auch Singles, Compilations und Specials.


## helpful
[https://pylast.googlecode.com/hg-history/9b5130860d785e9936911ceb094fb9567c4978a3/documentation.html](https://pylast.googlecode.com/hg-history/9b5130860d785e9936911ceb094fb9567c4978a3/documentation.html)
