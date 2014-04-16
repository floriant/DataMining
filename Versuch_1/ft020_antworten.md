Kapitel Theorie:
1. Eine Transformation soll die vorverarbeiteten Daten auf die f�r das Model wichtigen Elemente herunterbrechen. Das Model ist dabei von der Aufgabe und dem Ziel abh�ngig. 
2. Beim �berwachten Lernen sind die Zieldaten bereits bekannt und die Lern Algorithmen pr�fen anhand der Zieldaten. 
Beim un�berwachten Lernen sind keine Zieldaten bekannt, sondern mit hilfe von Clustering versucht sich �hnelnde Elemente zu gruppieren. 
3. Bei der Regression werden Eingaben und Zielwerte in ein Koordinatensystem eingetragen, und Anschlie�end eine Funktion gelernt, welche diese Ergebnisse wiederspiegelt.
Bei einer Klassifikation wird zus�tzlich ein Wert (bsp r) an jeden Punkt zugeordnet welcher die Klasse definiert. Eine Klasse kann dann mit einer gelernten Funktion verallgemeinert werden. Beispiel: Bereiche f�r Typische Klassen.
Beim Clustering sind keine Zieldaten bekannt, hier werden Cluster aus sich �hnelnden Daten gebildet. Ziel ist dabei eine Menge an Clustern die sich untereinander m�glichst stark unterscheiden.

Python Allgemein:
1. Eine List Comprehension ist eine Schnellschreibform f�r Listen (und andere objekttypen). Dabei kann man eine Funktion verwenden um Listen schnell mit Werten zu f�llen.
Bsp.: myList = [x**2 for x in range(10)]
Das Beispiel baut Quadratzahlen f�r jede Zahl 1-10, mit hilfe einer kleinen schleife.
2. Man Importiert Dateien unter verwendung der open funktion. 
Bsp.: 
file = 'README.md'
fileContent = open(file, 'r') 
das 'r' ist dabei das attribut f�r read access. w w�hre schreiben und a ist attachen. 
3. F�r das schreiben ist die Methode close verwendbar.
Bsp.:
file = 'README.md'
fileContent = open(file, 'w')
fileContent.write('Hallo Welt')
fileContent.close()
4. F�r das integrieren der 2. Liste kann man den + Operator verwenden, ansonsten geht auch ein x.append([4,5]) welches das Listenelement selbst anh�ngt (schachteln).
x = [1, 2, 3]
y = [4,5]
x = x+y

Numpy: 


Pandas:
1. Man baut sich ein Numpy Array und kann dieses an ein DataFrame als Inhalt �bergeben. Alternativ kann man auch mit direkten zugriffen wie myArray(0:) die Columns mit �bergeben.
numpyArray = np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(numpyArray, index=range(3), columns=list(['Vektor A','Vektor B']))
2. Einzelne spalten myDataFrame['Column'], einzelne Zeilen �ber den index Selektor myDataFrame[0:3] (w�rde col 0 - 2 ausgeben. 0:1 w�hre auch m�glich um nur 0 zu erhalten.)
es gibt noch loc f�r label und position (iloc). Position arbeitet mit Slices.
3. Sort by Columns: myDataFrame.sort(columns='Column') und myDataFrame.sort_index(axis=0, ascending=False), f�r columns ist axis=1 oder index= n�tig.
4. Einf�gepunkt muss selektiert werden -> by label: myDataframe.at[myIndex[0], 'A'] // by position: myDataframe.iat[0,1]
F�r mehrere Datens�tze gibt es noch die concat Funktion und die Append funktion. (append nur rows, concat gleichf�rmige listen)
5. Pandas hat eine import funktion: myDataFrame.read_csv('source.csv')
6. Pandas kann auch Exportieren: myDataFrame.to_hdf('foo.csv')

Matplotlib:
1. 
import numpy as np 
import matplotlib.pyplot as plt
range2 = np.arange(0.0,7.0,0.1) #get range 0-7 with 0.1 steps
plt.plot(range2, np.sin(1*range2), 'ro') #build sinplot with ro for dotted display
plt.grid(True) #force grids
plt.title('Sinusfunktion') #set title
plt.xlabel('x') #set x label
plt.ylabel('sin(x)') #set y label
plt.show() #show plot

2. Einfach mehrere funktionen in die plot funktion eintragen. Die regel lautet immer: x achse, y achse, draw pattern.

3.  Hierf�r ist es besser die Attribute der subplot funktion mit kommas zu separieren. numrows -> 4, numcols -> 3, fignum -> 1-12
plt.subplot(4,3,1)
plt.subplot(4,3,2)
plt.subplot(4,3,3)
plt.subplot(4,3,4)
...
plt.subplot(4,3,11)
plt.subplot(4,3,12)

4. mit der hist funktion: plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
x -> ein array aus werten, 50 -> anzahl der balken, normed=1 -> normalisiert das histogram zur darstellung
facecolor -> farbe der balken, alpha -> alpha channel der balken (transparenz)

5. ...
