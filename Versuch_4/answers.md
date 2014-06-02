#Fragen zu Versuch 4: Dokument Klassifikation / Spam Filter

## HINWEIS (ft020):
Bin mir bei den Antworten echt nicht sicher. Wenn ihr es besser Formuliert bekommt währs gut.
Eventuell habe ich auch einige Fehler in der Denkweise!

## 1.4.1 Wie wird ein Naiver Bayes Classifier trainiert?

Für jeden Trainingsdatensatz mit einer Menge von Variablen x muss jeder Wert einer Klasse C_i zugeordnet werden können.

    # Wahrscheinlichkeit für jede Klasse C_i das x teil von C_i ist
    # und wähle jeweils die Klasse mit größten Wahrscheinlichkeit aus
    P(C_i | x)

Die Berechnung erfolgt über die Bayes Formel wobei:

    P(C_i | x) # a-postprioi-Wahrscheinlichkeit
    p(x | C_i) # Ermittelt mit Likelihood Funktion
    P(C_i)  #a-priori-Wahrscheinlichkeit
    p(x) # Evidenz (größe irrelevant)

Hat man für die Variable x eine Klassifikation zur Klasse C_i geschaffen,
kann man neue Elemente nach diesen Kriterien testen.
Der Naive Bayes Classifier trainiert überwacht, aus der Aufgabenstellung
arbeitet der Parametrische-Ansatz mit bestehenden Wahrscheinlichkeits Werten.


## 1.4.2 Wie teilt ein Naiver Bayes Classifier ein neues Dokument ein?

Es wird für jede Klasse ein anteil an der Gesamtmenge ermittelt.
(Formel 7 und 8, sind nicht gekennzeichnet im pdf)
Hier wird die Formel für P(C) angegebenen,
dabei muss diese Wahrscheinlichkeit für jede Kategorie C ermittelt werden.

Es wird für die Likelihood Methode nun aus den Trainingsdaten die werte P(x|C) für jeden Wert x Ermittelt.
(Formel 3 und 4)
(anzahl der dokumente in denen die categorie C das wort x enthält) / (anzahl der dokumente die zur categorie C gehören)

Nun kann wieder die a-postpriori-Wahrscheinlichkeit in bezug zur gelernten Likelihood gelernt werden.
(Formel 5 und 6)
p(D) bleibt dabei immer gleich.

## 1.4.3 Welche naive Annahme liegt dem Bayes Classifier zugrunde?

Der Naive Bayes Classifier geht davon aus, dass alle Variablen unabhängig voneinander sind.
Währen sie abhängig, würde sich die Likelihood Methode weitaus schwerer berechnen lassen.

Mit der vereinfachten Annahme lässt sich alles auf die Formel (2) reduzieren.

## 1.4.4 Ist diese Annahme im Fall der Dokumentklasifikation tatsächlich gegeben?

Der Naive Bayes Classificator richtet sich sehr stark an der Anzahl von Worten in Dokumenten aus.
Für eine Klassifikation wie in der Vorbereitung in Spam oder Nicht-Spam ist diese Annahme anwendbar.

Generell gesehen, kann der Bayes Classificator jedoch nicht
unterscheiden zwischen Schreibstilen oder dem Kontext des Dokuments.

## 1.4.5 Betrachten Sie die Formeln 5 und 5. Welches Problem stellt sich ein, wenn in der Menge W(D) ein Wort vorkommt, das nicht in den Trainingsdaten der Kategorie G vorkommt und ein anderes Wort aus W(D) nicht in den Trainingsdaten der Kategorie B enthalten ist= Wie könnte dieses Problem gelöst werden?

Das Problem erzeugt einen Fehler in der Formel, da das Produkt eine der Likelihood damit eine Null enthält.
Man könnte für diesen Fall den Wert 0.5 für beide Kategorien wählen, damit währe eine Gleichverteilung gegeben.
Man könnte alternativ auch das Wort ausklammern und anschließend in eine neue Trainingsbildung einfließen lassen,
wobei die Wahrscheinlichkeit auf der Klassifikation der anderen Elemente des Dokuments beruht.





