import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sci
import scipy.stats as ss
from jdcal import gcal2jd
df = pd.read_csv('Amtrak.csv')


class ridership:
    def __init__(self,df):
        self.df = pd.DataFrame(df)
        
    def julian_dates(self):
        self.df['Month'] = pd.to_datetime(self.df['Month'])

        year =  self.df['Month'].dt.year
        month = self.df['Month'].dt.month
        day =   self.df['Month'].dt.day
        julians = []
        for a,b,c in zip(year,month,day):
            jd = gcal2jd(a,b,c)
            julians.append(jd[0]+jd[1])

        self.df['Julians'] = julians
        return self.df

    def plotting(self):
        x = self.df['Julians']
        y = self.df['Ridership']
        #linear fit
        ln = sci.polyfit(x,y,1)
        qd = sci.polyfit(x,y,3)
        plt.figure(figsize=(10,5))
        plt.title('Time Series with Linear vs. Quadratic Fit')
        plt.plot(x,y,'-k')
        plt.plot(x,sci.polyval(ln,x),'-r')
        plt.plot(x,sci.polyval(qd,x),'b')
        plt.xlabel('Year')
        plt.ylabel('Ridership')
        plt.show()
    
    def predicted_vs_normal(self):
        self.df['Year'] = self.df['Month'].dt.year
        linear = sci.polyfit(self.df['Year'],
                             self.df['Ridership'],1)
        yfit = linear[0] * self.df['Year'] + linear[1]
        self.df['Predicted'] = yfit
        self.df['Residuals'] = self.df['Ridership'] - self.df['Predicted']
        sum_sq_res = sum(pow(self.df['Residuals'],2))
        ss_TOT = len(self.df['Ridership']) * sci.var(self.df['Ridership'])


        self.rsquare = 1 - (sum_sq_res/ss_TOT)
        print(self.rsquare)

    def stats_cals(self):
        x = self.df['Month'].dt.year
        y = self.df['Ridership']
        slope,intercept,r_val, p_val, st_err = ss.linregress(x,y)
        print('slope:',slope, 'intercept:',intercept,
              'pval:',p_val)
        print('RSQR:',pow(r_val,2))

    def run_program(self):
        self.julian_dates()
        self.plotting()
        self.predicted_vs_normal()
        self.stats_cals()

frame = ridership(df)
frame.run_program()

