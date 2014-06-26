#Fragen zu Versuch 5: 
##Merkmalsextraktion mit der Nicht-Negativen Matrixfaktorisierung

###Was versteht man unter Artikel/Wort-Matrix? Wie sieht diese im aktuellen Versuch aus?
Eine Artikel/Wort-Matrix besteht aus einem Vektor i für die Dokumente und einem Vektor j für die Worte.
Dabei sind die Worte in mindestens einem Dokument enthalten.

In diesem Versuch verwenden wir die Nicht-Negative Matrix Faktorisierung.
Hierbei werden die Worte auf thematisch Relevante Worte reduziert.
Dabei fallen Füllworte weg, und eine Gewichtung für bestimmte Keywords kann gelegt werden.

###Wie multipliziert man die Matrix A mit dem Vektor v?
[Multiplikation Matrix A mit Vektor v](answers_partial/matrix_multiply.png)

           ( a00*v0 + a01*v1 + a02*v2 + a03*v3 )
    A * v= ( a10*v0 + a11*v1 + a12*v2 + a13*v3 )
           ( a20*v0 + a21*v1 + a22*v2 + a23*v3 )

[Ergebnis](answers_partial/multipliziert.gif)

Bei der NNMF wird die Rechnung aufgeteilt.
A ist hierbei:

    A = W * H


###Was versteht man im Kontext der NNMF unter
####Merkmalsmatrix
Aus dem Skript, die Matrix H

Beschreibt aus welchen Worten die Merkmale gebildet werden.

####Gewichtsmatrix

Aus dem Skript, die Matrix W

Beschreibt mit welchem Gewicht die Merkmale in den jeweiligen Artikeln auftreten.

###Wie definieren die Zeilen der Merkmalsmatrix die einzelnen Merkmale (Topics)?

Mit Stichworten zu einem Topic:
Bsp.:{Obama, visit, Germany}
Dieser Vektor enthält die Wörter aus welchen die Merkmale gebildet werden.
Es werden also Merkmale auf Wörter abgebildet.

###Was definieren die Zeilen der Gewichtungsmatrix?

Sie geben eine Gewichtung der Merkmale für jeden Artikel an.


###Wie werden in Numpy zwei Arrays (Typ numpy.array)
####im Sinne der Matrixmultiplikation miteinander multipliziert?
(x2t it trotzdem elementweise glaube ich)

    import numpy as np
    x1 = np.matrix("0,1,2; 3,4,5; 6,7,8")
    x2 = np.matrix("0,1,2")
    x2t = x2.T
    print x1*x2t


####elementweise multipliziert?**

    import numpy as np
    x = np.arange(9).reshape((3,3))
    y = np.arange(3)
    print np.dot(x,y)

###Wie wird die Transponierte eines Numpy-Arrays berechnet?

    import numpy as np
    xTest = np.arange(9).reshape((3,3))
    xTrans = np.transpose(xTest)
    print xTest
    print xTrans