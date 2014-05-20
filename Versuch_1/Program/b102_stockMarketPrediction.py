# -*- coding:utf8 -*-

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
    #returns the first five rows
    printable_df = df.ix[:, 0:6]
    print(printable_df)
    #plt.figure()

    #printable_df.plot(yticks=df) #TODO: nice to have: yticks
    ax = printable_df.plot()

    plt.title('Stock values overview')
    ax.set_ylabel('price in $')
    ax.set_xlabel('time in days')

    plt.savefig(docFolder + 'stock_overview.png' )

    plt.show()


def train_model(df, time_delay=24):
    pass


def create_cyclic_data(df, time_delay=24):
    df_length = len(df)
    #initialize result array with zeros
    # appending data to an array always results in copying all data in the array
    result = np.zeros((df_length, time_delay+1))

    #set time_delay to default if stupid value was passed
    if time_delay < 1 or time_delay >= df_length:
        time_delay = 24

    #iterate over rows
    for x in df.index:
        #iterate over values in row
        for y in range(0, time_delay+1):
            #reverse index (df[x] = result[x,time_delay])
            index = x - (time_delay - y)
            if index < 0:
                index += df_length

            result[x,y] = df[index]

    return result



#Teilaufgabe 2:
#print_five_charts()

time_delay = 30
yahoo_df = df.ix[:, 'YHOO']
#Teilaufgabe 3-6:
#predict_stockvalues(df=yahoo_df, time_delay=30)
yahoo_cyclic_array = create_cyclic_data(yahoo_df, time_delay)
#print(yahoo_cyclic_array)

training_data_in = yahoo_cyclic_array[:650, :-1]
training_data_out = yahoo_cyclic_array[:650, -1]
print(training_data_out)

svr_c = 500.0
svr_epsilon = 0.6
#generating SVR for learning, C and epsilon need to be optimized!
svr = SVR(kernel="rbf", C=svr_c, epsilon=svr_epsilon)

model = svr.fit(training_data_in, training_data_out)

print "*"*15, "predict stock market", "*"*15

#test model with last 30 entries in stockmarket data
test_data_in = yahoo_cyclic_array[-30:, :-1]
test_data_out = yahoo_cyclic_array[-30:, -1]

#prediction must be done for each row separately
# (predicted values must be used in subsequent predictions)

#create array to hold all prediction values
predicted_data_out = np.zeros((len(test_data_out)))

#iterate over all rows
for index in range(0, len(test_data_out)):
    #retrieve/calculate data_in
    if index < time_delay:
        #use test_data_in
        data_in = test_data_in[index]

        if index > 0:
            #use test_data_in and predicted_data_out
            for i in range(0,index):
                #write already predicted values to data_in
                data_in[-1*i] = predicted_data_out[i]

    else:
        #use last time_delay values from prediction values
        data_in = predicted_data_out[index-time_delay:index]


    #predict value
    predicted_value = model.predict(data_in)[0]

    #print "predicted_value: %s" % (predicted_value)

    predicted_data_out[index] = predicted_value


#compare predicted_values und test_data_out
print "*"*15, "compare prediction and target", "*"*15
print "prediction: (%d elements)\n" % (len(predicted_data_out)), predicted_data_out
print "target: (%d elements)\n" % (len(predicted_data_out)), test_data_out

mae = metrics.mean_absolute_error(test_data_out, predicted_data_out)

print "Mean Absolute Error: ", mae

#TODO: plot predicted and actual stock market
#Darstellung des tatsächlichen Kursverlaufs und der vorhergesagten Daten
