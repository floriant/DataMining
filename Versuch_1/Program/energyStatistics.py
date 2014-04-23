import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def write_to_file(aString, filename):
    aFile = open(filename, 'w')
    aFile.write(aString)
    aFile.close()

def describe_statistics():
    #2.1.3.2 Zusammenfassung Statistik
    print df.describe()
    write_to_file(df.describe().to_string(), "../doc/energyStatistics")


def draw_combined_boxplots():
    #df.boxplot(by='Country') #hat wohl Komfort-Funktionen
    all_in_one_boxplot(with_fliers=True)

    plt.savefig('../doc/energyStatistics_with_fliers.png')
    #plt.show()
    plt.clf()

    all_in_one_boxplot(with_fliers=False)
    plt.savefig('../doc/energyStatistics.png')


def all_in_one_boxplot(with_fliers=True):
    fig, axes = plt.subplots()#figsize=(10,6))

    if with_fliers:
        sym_parameter = 'b+'
    else:
        sym_parameter = ''


    data = [df['Oil'], df['Gas'], df['Coal'], df['Nuclear'], df['Hydro']]
    plt.boxplot(data, sym=sym_parameter, vert=False) # plot x1 and set boxplot vertical

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    axes.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
    axes.set_axisbelow(True)
    axes.set_title('Comparison of the distribution of different energy resources')

    plt.yticks(range(0, 6), ['', 'Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro'])


def draw_separate_boxplots():
    resources = ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']
    fig, axes = plt.subplots()
#    fig, axes = plt.subplots(2, 3, sharex=True, sharey=True)

    for resource in resources:
        draw_single_boxplot(resource, with_fliers=True)
        draw_single_boxplot(resource, with_fliers=False)

    plt.clf()

def draw_single_boxplot(resource, with_fliers=True):
    if with_fliers:
        sym_parameter = 'b+'
        filename_suffix = '_with_fliers'
    else:
        sym_parameter = ''
        filename_suffix = ''

    print "Drawing boxplot for resource '%s'" % (resource)

    plt.clf()
    plt.boxplot([df[resource]], sym=sym_parameter, vert=False)
    plt.title('Boxplot for %s' % (resource) )

    #plt.show()
    plt.savefig('../doc/energyStatistic_%s%s.png' % (resource, filename_suffix) )


if __name__ == '__main__':
    df = pd.read_csv("../res/EnergyMix.csv")

    describe_statistics()

    draw_separate_boxplots()

    #draw_combined_boxplots()
    plt.show()

