##!/usr/bin/python
#Analitics of one day of data light, tempure and humedity

#Import Library
import pandas as pd
import os
import numpy as np
import datetime

def main():

    #get path
    dirname=os.path.dirname(__file__)
    filename=os.path.join(dirname, '../data/temperatura.csv')

    #get data
    df=pd.read_csv(filename, sep=',',header=0, na_values="NaN")

    #put into a data frame
    temperaturadf=pd.DataFrame(df)

    print("\n Base Information \n")

    #print csv structure
    print(temperaturadf.info())

    #print analytics
    print("\n Analized Data: \n")
    print(temperaturadf.describe())

    #copy data frame df
    df2 = df.copy()


if __name__=='__main__':
            main()

