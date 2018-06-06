
import pandas as pd
import os
import numpy as np
import datetime

def main():
    print('hola')
    dirname=os.path.dirname(__file__)
    filename=os.path.join(dirname, '../data/temperatura.csv')
    df=pd.read_csv(filename, sep=',',header=0, na_values="NaN")

    temperaturadf=pd.DataFrame(df)
    print(temperaturadf.info())
    print(temperaturadf.describe())

    df2 = df.copy()


if __name__=='__main__':
            main()

