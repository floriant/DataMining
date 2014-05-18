import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
from sklearn.svm import SVR


resourceFolder = '../res/'
docFolder = '../doc/'
df = pd.read_csv(resourceFolder + 'effectiveRates.csv')

#print(df)


#plotte 5 Kurse
def print_five_charts():
    printable_df = df.ix[:, 0:6]
    print(printable_df)
    #plt.figure()

    #printable_df.plot(yticks=df) #?? yticks setzen
    ax = printable_df.plot()

    plt.title('Stock values overview')
    ax.set_ylabel('price in $')
    ax.set_xlabel('time in days')


    plt.savefig(docFolder + 'stock_overview.png' )

    plt.show()





def predict_stockvalues(df, time_delay=24):
    print(df)
    print "prediction-df:"
    full_prediction_df = df[:650]
    #erster Vorhersagewert ist für Datensatz time_delay + 1
    prediction_df = full_prediction_df[:30]
    print(prediction_df)

    #für den nächsten Tag muss das erste Element aus der Liste entfernt werden, und der gerade berechnete Wert angehängt werden
    predicted_value = 0
    #prediction_df.pop
    #prediction_df.append(predicted_value)


#Teilaufgabe 2:
#print_five_charts()

yahoo_df = df.ix[:, 'YHOO']
#Teilaufgabe 3-6:
predict_stockvalues(df=yahoo_df, time_delay=30)

#Darstellung des tatsächlichen Kursverlaufs und der vorhergesagten Daten
