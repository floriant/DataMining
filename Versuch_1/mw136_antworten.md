#Fragen zu Versuch 1 (Energy Data)
##Aus der in Kapitel 1.3 beschriebenen Theorie
###1. Erklären Sie den Sinn der Transformation innerhalb der Data Mining Prozesskette:
Ziel der Transformation ist es, vorverarbeitete Daten so zu transformieren, dass nicht nur die Datenmenge reduziert wird, sondern auch Mustererkennung oder Modellbestimmung vereinfacht wird.  
Neben der Reduktion der Attribute gehört auch das Normalisieren der Attribute dazu.

###2. Worin besteht der Unterschied zwischen überwachtem und unüberwachtem Lernen?
Bei _überwachtem Lernen_ wird nach jeder Iteration geprüft, ob die Eingangsdaten und die erwarteten Ausgangsdaten (Sollausgabe) übereinstimmen und das Lernen kann bewertet werden.  
Beim _unüberwachten Lernen_ gibt es nur Eingangsdaten, aber keine Sollausgabe.  

###3. Beschreiben Sie die Unterschiede zwischen Klassifikation, Regression und Clustering. Nennen Sie für diese 3 verschiedenen Verfahren je ein Anwendungsbeispiel.
**Klassifikation** wird beim überwachten Lernen eingesetzt und zwar wird ein diskretes Ausgabeattribut zurückgegeben. _Bsp: .  

**Regression** wird beim überwachten Lernen eingesetzt und liefert zu jedem möglichen Ausgabeattribut einen numerischen Funktionswert zurück. Die Trennung erfolgt durch eine mathematische Funktion.  
_Bsp: Bei der Gesichtserkennung kann von Wahrscheinlichkeiten ausgegangen werden, welche Person auf dem Bild ist._  

**Clustering** wird beim unüberwachten Lernen eingesetzt und liefert Gruppen von Eingabewerten zurück, die sich im Bezug auf ihre Attribute relativ ähnlich sind.  
_Bsp: Bildsegmentierung für Video-Codierungen_  

##Python Allgemein:
###1. Was ist eine Python List-Comprehension?
Mit List Comprehension kann man auf verkürzte Weise Lambda Funktionen einsetzen, um Listen zu erzeugen.

	squares = [ (x*x) for x in range(2,10,2) ]
	points = [ (x,y) for x in range(1,3) for y in range(2,4) ]
 
Ergebnis:

	squares = [4, 16, 36, 64]
	points = [(1, 2), (1, 3), (2, 2), (2, 3)]

_Achtung: points hält einen List mit N x N Verknüpfungen der Liste x und der Liste y in Tupeln_


###2. Wie importiert man Daten aus einem Textfile?

	f = open('rumspielen.py', 'r')
	daten = f.read()
	f.close()

###3. Wie speichert man Daten aus Python in ein Textfile?

	f2 = open('textspeichern.txt', 'w')
	f2.write("hallo")
	f2.close()

###4. Wie hängt man an eine Python-Liste die Elemente einer zweiten Liste an?
**fehlt noch**  

	arr1 = [1, 2, 3]
	arr2 = [4, 5, 6]
	arr1.extend(arr2)
	
Ergebnis:	
	
	arr1 =[1, 2, 3, 4, 5, 6]

_Achtung:_  
`arr1.append(arr2)` liefert `[1, 2, 3, [4, 5, 6]` zurück

##Numpy:
###1. Nennen Sie zwei verschiedene Möglichkeiten ein Numpy-Array zu erzeugen.

	import numpy as np
	arr1 = np.array( [1, 17, 23])
	**@todo**

###2. Wie legt man ein (3,4)-Array mit ausschlieÿlich 0-Einträgen an?

	import numpy as np
	arr3 = np.zeros( (3, 4) )

###3. Wie ruft man die Anzahl der Dimensionen, die Anzahl der Elemente pro Dimension und den Datentyp der Arrayelemente ab?
*	Anzahl Dimensionen: `arr1.ndim`
*	Anzahl Elemente pro Dimension: `arr1.shape`
*	Datentyp der Arrayelemente: `arr1.dtype`
	
###4. Wie wandelt man ein (3,4)-Array in ein (2,6)-Array um?

	import numpy as np
	arr1 = np.floor(10*np.random.random((3,4,)))
	arr1.shape = (2,6)
	
###5. Wie transponiert man ein zweidimensionales Array?

	arr1.transpose()

###6. Wie multipliziert man zwei Arrays elementweise?

	arr1 * arr2
	
###7. Wie führt man eine Matrixmultiplikation zweier zweidimensionaler Arrays A und B aus? Welche Bedingungen müssen A und B erfüllen, damit überhaupt eine Matrixmultiplikation durchgeführt werden kann?
_A muss gleich viele Zeilen wie B Spalten haben, und umgekehrt.

	arr1=np.floor(10*np.random.random( (2,3) ))
	arr2=np.floor(10*np.random.random( (3,2) ))
	arrayA.dot(arrayB)

###8. Wie greift man auf das Element (2,3) in einem (4,4)-Array A zu? Wie greift man auf die erste Spalte, wie auf die erste Zeile dieses Arrays zu?
*	Element(2,3): `arr[2,3]`
*	Erste Spalte: ``
*	erste Zeile: ``

###9. Wie berechnet man die Quadratwurzel aller Elemente eines Arrays?
Hierfür werden _Universal Functions_ verwendet.  
`np.sqrt( np.array( [1, 2, 4] ) )` liefert `array([ 1, 1.41421356, 2])`
	

###10. Wie legt man eine flache Kopie, wie eine tiefe Kopie eines Arrays an?

	a = np.array( [1, 2, 3] )
	shallowCopy = a.view()
	deepCopy = a.copy()

##Pandas:
--  

##Matplotlib:
--  

##Scipy: Geben Sie kurz die Schritte an, die für die Durchführung eines hierarchischen Clustering mit Scipy notwendig sind.
Frage versteh ich nicht richtig: Mögliche Antwort: Quantifizierung und Clustering? Danach muss die Anzahl der gewünschten Cluster angegeben werden, damit die passenden Ähnlichkeiten zusammenbleiben.  
Ein Lnk, der vielleicht weiterhilft [bei so](http://stackoverflow.com/questions/21638130/tutorial-for-scipy-cluster-hierarchy), _marc: ich kuck mir das morgen nochmal an._  
Genereller Ablauf: 


##Scikit Learn: 
Sklearn stellt u.a. eine umfassende Bibliothek von Klassen für das überwachte Lernen bereit. 
Mit welchem Methodenaufruf werden diese Kassen trainiert? 

Mit welchem Methodenaufruf können die trainierten Modelle auf neue Eingabedaten angewandt werden um den entsprechenden Ausgabewert zu berechnen? 

Mit welchem Leistungsmaß kann die Qualität eines Regressionsmodells bewertet werden? Wie wird dieses Leistungsmaÿ mit Sklearn berechnet?

Mit welchem Leistungsmaß kann die Qualität eines Klassifikationsmodells bewertet werden? 

Wie wird dieses Leistungsmaß mit Sklearn berechnet? 

Was versteht man unter x-facher Kreuzvalidierung und wie wird diese mit Sklearn durchgeführt?
