# -*- coding:utf8 -*-
import urllib2
#from numpy import *
#import h5py
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

symbol_dict = {
        'TOT'  : 'Total',
        'XOM'  : 'Exxon',
        'CVX'  : 'Chevron',
        'COP'  : 'ConocoPhillips',
        'VLO'  : 'Valero-Energy',
        'MSFT' : 'Microsoft',
        'IBM'  : 'IBM',
        'TWX'  : 'Time-Warner',
        'CMCSA': 'Comcast',
        'CVC'  : 'Cablevision',
        'YHOO' : 'Yahoo',
        'DELL' : 'Dell',
        'HPQ'  : 'Hewlett-Packard',
        'AMZN' : 'Amazon',
        'TM'   : 'Toyota',
        'CAJ'  : 'Canon',
        'MTU'  : 'Mitsubishi',
        'SNE'  : 'Sony',
        'F'    : 'Ford',
        'HMC'  : 'Honda',
        'NAV'  : 'Navistar',
        'NOC'  : 'Northrop-Grumman',
        'BA'   : 'Boeing',
        'KO'   : 'Coca-Cola',
        'MMM'  : '3M',
        'MCD'  : 'Mc-Donalds',
        'PEP'  : 'Pepsi',
        'KFT'  : 'Kraft-Foods',
        'K'    : 'Kellogg',
        'UN'   : 'Unilever',
        'MAR'  : 'Marriott',
        'PG'   : 'Procter-Gamble',
        'CL'   : 'Colgate-Palmolive',
        'GE'   : 'General-Electrics',
        'WFC'  : 'Wells Fargo',
        'JPM'  : 'JPMorgan-Chase',
        'AIG'  : 'AIG',
        'AXP'  : 'American-express',
        'BAC'  : 'Bank-of-America',
        'GS'   : 'Goldman-Sachs',
        'AAPL' : 'Apple',
        'SAP'  : 'SAP',
        'CSCO' : 'Cisco',
        'TXN'  : 'Texas-instruments',
        'XRX'  : 'Xerox',
        'LMT'  : 'Lookheed_Martin',
        'WMT'  : 'Wal-Mart',
        'WAG'  : 'Walgreen',
        'HD'   : 'Home-Depot',
        'GSK'  : 'GlaxoSmithKline',
        'PFE'  : 'Pfizer',
        'SNY'  : 'Sanofi-Aventis',
        'NVS'  : 'Novartis',
        'KMB'  : 'Kimberly-Clark',
        'R'    : 'Ryder',
        'GD'   : 'General-Dynamics',
        'RTN'  : 'Raytheon',
        'CVS'  : 'CVS',
        'CAT'  : 'Caterpillar',
        'DD'   : 'DuPont-de-Nemours',
        }
tickers=symbol_dict.keys()
prices={}
openVals={}
closeVals={}
dates={}

numTicks=len(tickers)

for t in tickers:
      print "Ticker:                 ",t
      rows=urllib2.urlopen('http://ichart.finance.yahoo.com/table.csv?'+\
                           's=%s&d=02&e=20&f=2012&g=d&a=3&b=12&c=2009'%t +\
                           '&ignore=.csv').readlines()    
      print "Anzahl der Datensätze:  ",len(rows)-1
      print "Struktur Datensatz:     ",rows[0]
      print "Erster Datensatz:       ",rows[-1]
      print "Letzter Datensatz:      ",rows[1]
      prices[t]=[float(r.split(',')[6]) for r in rows[1:] if r.strip()!='']
      prices[t].reverse()
      openVals[t]=[float(r.split(',')[1]) for r in rows[1:] if r.strip()!='']
      openVals[t].reverse()
      closeVals[t]=[float(r.split(',')[4]) for r in rows[1:] if r.strip()!='']
      closeVals[t].reverse()
      dates[t]=[str(r.split(',')[0]) for r in rows[1:] if r.strip()!='']
      dates[t].reverse()



