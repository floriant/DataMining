#Fragen zu Versuch 6: 
##Gesichtserkennung

###Was sind Eigenvektoren und Eigenwerte?
Eigenvektor:
Der Eigenvektor ist ein um einen Betrag x skalierter Vektor des Ursprungsvektors.
Eigenwerte:
Der Betrag um den der ursprungsvektor skaliert wird, ist der Eigenwert.

###Was versteht man unter Eigenfaces?
Eigenfaces sind die Eigenvektoren (ui) die für die weitere Berechnung verwendet werden.

###Wie kann mit der PCA eine Dimensionalitätsreduktion durchgeführt werden?
Die Dimensionalität wird im Grund dadurch reduziert, indem man die Dimensionen bei der Konvarenzmatrix umkehrt.
So sind die Anzahl der Bildvektoren die vorgebende Dimension.
Grund dafür ist die annahme, das nur bestimmte Vektoren relevant sind, alle anderen liegen nahe null.

###Wie werden mit dem Python Modul Image Bilder in ein Python Programm geladen?
So:

    import Image

    im = Image.open("../res/FaceRecogBilder/training/1-2.png")
    print im.format, im.size, im.mode
    im.show()

NOTE: Es wird ein Python Modul für die Image Library benötigt.
im.show() öffnete beim testen photoshop o.0