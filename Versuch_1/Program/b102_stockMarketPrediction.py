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


#plotte 5 Kurse
def print_five_charts(df):
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


def train_model(training_data, training_data_length, svr_c=500.0, svr_epsilon=0.6):
    training_data_in = training_data[:training_data_length, :-1]
    training_data_out = training_data[:training_data_length, -1]

    #generating SVR for learning, C and epsilon need to be optimized!
    svr = SVR(kernel="rbf", C=svr_c, epsilon=svr_epsilon)

    #train model using training_data_[in/out]
    model = svr.fit(training_data_in, training_data_out)

    return model


def predict_stockmarket(test_data, model, time_delay):
    #features
    test_data_in = test_data[:, :-1]
    #target
    test_data_out = test_data[:, -1]

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

    return predicted_data_out


def plot_predicted_stockmarket(actual_data, prediction_training, prediction_forecast):
    #real data
    plt.figure(figsize=(12, 5))
    ax = actual_data.plot(style='k', label='real')
    ax.set_ylabel('price in $')
    ax.set_xlabel('time in days')

    #predicted values on training data
    ts = pd.Series(prediction_training, index=range(len(prediction_training)))
    ts.plot(style='-b.', label='prediction')

    #forecast
    start = len(actual_data)-len(prediction_forecast)
    end = start + len(prediction_forecast)
    ts = pd.Series(prediction_forecast, index=range(start, end))
    ts.plot(style='-r.', label='forecast')

    plt.title('Stock market values and prediction')
    plt.legend()

    plt.savefig('../doc/stockpredict.png')
    plt.show()


#main program

df = pd.read_csv(resourceFolder + 'effectiveRates.csv')

#Teilaufgabe 2:
print_five_charts(df) #TODO remove comment

yahoo_df = df.ix[:, 'YHOO']

training_data_length = 650
test_data_length = 30


#initial values from script
time_delay = 30
c = 500.0
epsilon = 0.6

#optimized values from b102_stockMarketPrediction_Optimization.py
time_delay = 1
c = 400.0
epsilon = 0.85



#Teilaufgabe 3-6:
yahoo_cyclic_array = create_cyclic_data(yahoo_df, time_delay)
#print(yahoo_cyclic_array)

model = train_model(training_data=yahoo_cyclic_array, training_data_length=650, svr_c=c, svr_epsilon=epsilon)

print "*"*10, "predict stock market(svr_c=%s, svr_epsilon=%s)" % (c, epsilon), "*"*10

#test model with last 30 entries in stockmarket data
test_data = yahoo_cyclic_array[-test_data_length:, :]

#calculate mae
predicted_data_out = predict_stockmarket(test_data, model, time_delay)
test_data_out = test_data[:, -1]

mae = metrics.mean_absolute_error(test_data_out, predicted_data_out)
# getting mean absolute deviation (MAD) according to method from script
#mad = 1.0/len(predicted_data_out)*np.sum(np.abs(predicted_data_out-test_data_out))
print "  mae =", mae



#---------------
#generate output
#---------------
#print prediction
print "*"*15, "compare prediction and target", "*"*15
print "prediction: (%d elements)\n" % (len(predicted_data_out)), predicted_data_out
print "target: (%d elements)\n" % (len(predicted_data_out)), test_data_out
print "Mean Absolute Error: ", mae

#plot prediction
prediction_on_training_data = model.predict(yahoo_cyclic_array[:(len(df)-test_data_length), :-1])

plot_predicted_stockmarket(yahoo_df, prediction_on_training_data, predicted_data_out)
