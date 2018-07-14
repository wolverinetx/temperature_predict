#Libraries to use
import pandas as pd
import numpy as np
from scipy import stats

def main():

    ruta = '../data/'
    dfp1 = pd.read_csv(ruta+'Datos1.csv',sep=';')
    dfp2 = pd.read_csv(ruta+'Datos2.csv',sep=';')
    dfp3 = pd.read_csv(ruta+'Datos3.csv',sep=';')

    # copy dataframe in another
    dfp1iv = getInterestingVar(dfp1)
    dfp2iv = getInterestingVar(dfp2)
    dfp3iv = getInterestingVar(dfp3)

    # create variables of time to facility work
    dfp1ivhm = createHourMinute(dfp1iv)
    dfp2ivhm = createHourMinute(dfp2iv)
    dfp3ivhm = createHourMinute(dfp3iv)

    # calculating the mean and error of mean, grouped by 1 hour
    # division by every part of total dataset
    dfp1ivhmGroupedByHour = dfp1ivhm.groupby(['lth_date', 'hour']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp2ivhmGroupedByHour = dfp2ivhm.groupby(['lth_date', 'hour']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp3ivhmGroupedByHour = dfp3ivhm.groupby(['lth_date', 'hour']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()

    dfp1ivhmGroupedByHalfHour = dfp1ivhm.groupby(['lth_date', 'hour','minute30']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp2ivhmGroupedByHalfHour = dfp2ivhm.groupby(['lth_date', 'hour','minute30']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp3ivhmGroupedByHalfHour = dfp3ivhm.groupby(['lth_date', 'hour','minute30']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()

    dfp1ivhmGroupedByFifMin = dfp1ivhm.groupby(['lth_date', 'hour','minute15']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp2ivhmGroupedByFifMin = dfp2ivhm.groupby(['lth_date', 'hour','minute15']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()
    dfp3ivhmGroupedByFifMin = dfp3ivhm.groupby(['lth_date', 'hour','minute15']).agg([np.mean, lambda x: stats.sem(x)]).reset_index()


    #split by time: hour, 30 min, 15 min
    listByHourp1 = dfp1ivhmGroupedByHour.iloc[:,[0,1,2,3,4,5,6,7]]
    listByHourp2 = dfp2ivhmGroupedByHour.iloc[:,[0,1,2,3,4,5,6,7]]
    listByHourp3 = dfp3ivhmGroupedByHour.iloc[:,[0,1,2,3,4,5,6,7]]

    listByHalfHourp1 = dfp1ivhmGroupedByHalfHour.iloc[:,[0,1,2,3,4,5,6,7,8]]
    listByHalfHourp2 = dfp2ivhmGroupedByHalfHour.iloc[:,[0,1,2,3,4,5,6,7,8]]
    listByHalfHourp3 = dfp3ivhmGroupedByHalfHour.iloc[:,[0,1,2,3,4,5,6,7,8]]

    listByFifMinp1 = dfp1ivhmGroupedByFifMin.iloc[:,[0,1,2,3,4,5,6,7,8]]
    listByFifMinp2 = dfp2ivhmGroupedByFifMin.iloc[:,[0,1,2,3,4,5,6,7,8]]
    listByFifMinp3 = dfp3ivhmGroupedByFifMin.iloc[:,[0,1,2,3,4,5,6,7,8]]

    # hours
    # fill partial file - hours for 4,5 and 6 times back
    listahp4n1 = getVariableStudy(4,listByHourp1,0)
    listahp4n2 = getVariableStudy(4,listByHourp2,0)
    listahp4n3 = getVariableStudy(4,listByHourp3,0)

    listahp5n1 = getVariableStudy(5,listByHourp1,0)
    listahp5n2 = getVariableStudy(5,listByHourp2,0)
    listahp5n3 = getVariableStudy(5,listByHourp3,0)

    listahp6n1 = getVariableStudy(6,listByHourp1,0)
    listahp6n2 = getVariableStudy(6,listByHourp2,0)
    listahp6n3 = getVariableStudy(6,listByHourp3,0)

    # half hour - 30min
    # fill partial file - hours for 4,5 and 6 times back
    listafp4n1 = getVariableStudy(4,listByHalfHourp1,1)
    listafp4n2 = getVariableStudy(4,listByHalfHourp2,1)
    listafp4n3 = getVariableStudy(4,listByHalfHourp3,1)

    listafp5n1 = getVariableStudy(5,listByHalfHourp1,1)
    listafp5n2 = getVariableStudy(5,listByHalfHourp2,1)
    listafp5n3 = getVariableStudy(5,listByHalfHourp3,1)

    listafp6n1 = getVariableStudy(6,listByHalfHourp1,1)
    listafp6n2 = getVariableStudy(6,listByHalfHourp2,1)
    listafp6n3 = getVariableStudy(6,listByHalfHourp3,1)


    # 15 minutes
    # fill partial file - hours for 4,5 and 6 times back
    listamp4n1 = getVariableStudy(4,listByFifMinp1,1)
    listamp4n2 = getVariableStudy(4,listByFifMinp2,1)
    listamp4n3 = getVariableStudy(4,listByFifMinp3,1)

    listamp5n1 = getVariableStudy(5,listByFifMinp1,1)
    listamp5n2 = getVariableStudy(5,listByFifMinp2,1)
    listamp5n3 = getVariableStudy(5,listByFifMinp3,1)

    listamp6n1 = getVariableStudy(6,listByFifMinp1,1)
    listamp6n2 = getVariableStudy(6,listByFifMinp2,1)
    listamp6n3 = getVariableStudy(6,listByFifMinp3,1)


    # union files
    # hour
    listahp4n = [listahp4n1,listahp4n2,listahp4n3]
    listah4n = pd.concat(listahp4n)

    listahp5n = [listahp5n1,listahp5n2,listahp5n3]
    listah5n = pd.concat(listahp5n)

    listahp6n = [listahp6n1,listahp6n2,listahp6n3]
    listah6n = pd.concat(listahp6n)

    # 30 minutes
    listafp4n = [listafp4n1,listafp4n2,listafp4n3]
    listaf4n = pd.concat(listafp4n)

    listafp5n = [listafp5n1,listafp5n2,listafp5n3]
    listaf5n = pd.concat(listafp5n)

    listafp6n = [listafp6n1,listafp6n2,listafp6n3]
    listaf6n = pd.concat(listafp6n)

    # 15 minutes
    listamp4n = [listamp4n1,listamp4n2,listamp4n3]
    listam4n = pd.concat(listamp4n)

    listamp5n = [listamp5n1,listamp5n2,listamp5n3]
    listam5n = pd.concat(listamp5n)

    listamp6n = [listamp6n1,listamp6n2,listamp6n3]
    listam6n = pd.concat(listamp6n)


    # hour - calculating the error for  T-4, T-5 and T-6
    listah4n = sumdiff(listah4n, 4)
    listah5n = sumdiff(listah5n, 5)
    listah6n = sumdiff(listah6n, 6)

    # 30 minutes - calculating the error for  T-4, T-5 and T-6
    listaf4n = sumdiff(listaf4n, 4)
    listaf5n = sumdiff(listaf5n, 5)
    listaf6n = sumdiff(listaf6n, 6)

    # 15 minutes - calculating the error for  T-4, T-5 and T-6
    listam4n = sumdiff(listam4n, 4)
    listam5n = sumdiff(listam5n, 5)
    listam6n = sumdiff(listam6n, 6)


    # current columns for scene varibles
    light4 = pd.Series([0,1,2,3,4], index=[[0,1,2,4 ,6 ,8 ,10,12],[0,1,2,3,4,5,6,7,8,9,10,11,12],[0,1,2,33,34,35,36,37],[0,1,2,38,39,40,41,42],0])
    tempe4 = pd.Series([0,1,2,3,4], index=[[0,1,2,14,16,18,20,22],[0,1,2,13,14,15,16,17,18,19,20,21,22],[0,1,2,43,44,45,46,47],[0,1,2,48,49,50,51,52],0])
    humyd4 = pd.Series([0,1,2,3,4], index=[[0,1,2,24,26,28,30,32],[0,1,2,23,24,25,26,27,28,29,30,31,32],[0,1,2,53,54,55,56,57],[0,1,2,58,59,60,61,62],0])

    light5 = pd.Series([0,1,2,3,4], index=[[0,1,2,4,6,8,10,12,14],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],[0,1,2,39,40,41,42,43,44],[0,1,2,45,46,47,48,49,50],0])
    tempe5 = pd.Series([0,1,2,3,4], index=[[0,1,2,16,18,20,22,24,26],[0,1,2,15,16,17,18,19,20,21,22,23,24,25,26],[0,1,2,51,52,53,54,55,56],[0,1,2,57,58,59,60,61,62],0])
    humyd5 = pd.Series([0,1,2,3,4], index=[[0,1,2,28,30,32,34,36,38],[0,1,2,27,28,29,30,31,32,33,34,35,36,37,38],[0,1,2,63,64,65,66,67,68],[0,1,2,69,70,71,72,73,74],0])

    light6 = pd.Series([0,1,2,3,4], index=[[0,1,2,4,6,8,10,12,14,16],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[0,1,2,45,46,47,48,49,50,51],[0,1,2,52,53,54,55,56,57,58],0])
    tempe6 = pd.Series([0,1,2,3,4], index=[[0,1,2,18,20,22,24,26,28,30],[0,1,2,17,18,19,20,21,22,23,24,25,26,27,28,29,30],[0,1,2,59,60,61,62,63,64,65],[0,1,2,66,67,68,69,70,71,72],0])
    humyd6 = pd.Series([0,1,2,3,4], index=[[0,1,2,32,34,36,38,40,42,44],[0,1,2,31,32,33,34,35,36,37,38,39,40,41,42,43,44],[0,1,2,73,74,75,76,77,78,79],[0,1,2,80,81,82,83,84,85,86],0])


    # Generating stage by hour
    generateScene(listah4n, light4, tempe4, humyd4, 'hour', 'T-4',ruta)
    generateScene(listah5n, light5, tempe5, humyd5, 'hour', 'T-5',ruta)
    generateScene(listah6n, light6, tempe6, humyd6, 'hour', 'T-6',ruta)

    # Generating stage by 30 minutes
    generateScene(listaf4n, light4, tempe4, humyd4, '30min', 'T-4', ruta)
    generateScene(listaf5n, light5, tempe5, humyd5, '30min', 'T-5', ruta)
    generateScene(listaf6n, light6, tempe6, humyd6, '30min', 'T-6', ruta)

    # Generating stage by 15 minutes
    generateScene(listam4n, light4, tempe4, humyd4, '15min', 'T-4', ruta)
    generateScene(listam5n, light5, tempe5, humyd5, '15min', 'T-5', ruta)
    generateScene(listam6n, light6, tempe6, humyd6, '15min', 'T-6', ruta)


# functin that selects interesting variables
def getInterestingVar(df):
    return df[['lth_datetime', 'lth_date', 'lth_value_light', 'lth_value_temperature', 'lth_value_humidity']].copy()


# function that identify rowa every 30 minutes
def minut30_group(minute):
    if minute <= 30:
        return 30
    else:
        return 0


# function that identify rowa every 15 minutes
def minut15_group(minute):
    if int(minute) <= 15:
        return 15
    elif int(minute) > 15 and int(minute) <= 30:
        return 30
    elif int(minute) > 30 and int(minute) <= 45:
        return 45
    elif int(minute) > 45:
        return 0
    else:
        return 0


# create 2 variables for hour and minute
def createHourMinute(df):
    df['hour'] = pd.DatetimeIndex(df['lth_datetime']).hour
    df['minute'] = pd.DatetimeIndex(df['lth_datetime']).minute
    #group each 30 min
    df['minute30'] = df['minute'].map(minut30_group)
    #group each 15 min
    df['minute15'] = df['minute'].map(minut15_group)
    return df


#sum error to variable
# types 1: sum, 2: dif.
def calculo_error(value, error, types):
    if int(types) == 1:
        return value + error
    else:
        return value - error


# function that help to create a scenario T-2, 3,4,5 and 6
# sol: if time is in hours or minutes. 0,1
def getVariableStudy(nro, df, sol):
    # number of rows on dataset
    n = len(df.index)
    # number of times back
    m = int(nro)
    g = pd.Series([])

    if int(sol) == 0:
        columna = [2,3,4,5,6,7]
        for x in range(m,(n+1)):
            g.set_value(x,0)
    else:
        columna = [3,4,5,6,7,8]
        g = df.iloc[m : (n),2]

    if m == 6:
        desde = [0,1,2,3,4,5,6]
        hasta = [6,5,4,3,2,1,0]
    elif m == 5:
        desde = [0,0,1,2,3,4,5]
        hasta = [0,5,4,3,2,1,0]
    elif m == 4:
        desde = [0,0,0,1,2,3,4]
        hasta = [0,0,4,3,2,1,0]
    elif m == 3:
        desde = [0,0,0,0,1,2,3]
        hasta = [0,0,0,3,2,1,0]
    elif m == 2:
        desde = [0,0,0,0,0,1,2]
        hasta = [0,0,0,0,2,1,0]
    else:
        desde = [0,0,0,0,0,1,2]
        hasta = [0,0,0,0,2,1,0]

    #light
    l6 = df.iloc[desde[0] : (n-hasta[0]),columna[0]].copy()
    l5 = df.iloc[desde[1] : (n-hasta[1]),columna[0]]
    l4 = df.iloc[desde[2] : (n-hasta[2]),columna[0]]
    l3 = df.iloc[desde[3] : (n-hasta[3]),columna[0]]
    l2 = df.iloc[desde[4] : (n-hasta[4]),columna[0]]
    l1 = df.iloc[desde[5] : (n-hasta[5]),columna[0]]
    l = df.iloc[desde[6] : (n-hasta[6]),columna[0]]
    #error light
    el6 = df.iloc[desde[0] : (n-hasta[0]),columna[1]]
    el5 = df.iloc[desde[1] : (n-hasta[1]),columna[1]]
    el4 = df.iloc[desde[2] : (n-hasta[2]),columna[1]]
    el3 = df.iloc[desde[3] : (n-hasta[3]),columna[1]]
    el2 = df.iloc[desde[4] : (n-hasta[4]),columna[1]]
    el1 = df.iloc[desde[5] : (n-hasta[5]),columna[1]]
    el = df.iloc[desde[6] : (n-hasta[6]),columna[1]]
    #temperature
    t6 = df.iloc[desde[0] : (n-hasta[0]),columna[2]]
    t5 = df.iloc[desde[1] : (n-hasta[1]),columna[2]]
    t4 = df.iloc[desde[2] : (n-hasta[2]),columna[2]]
    t3 = df.iloc[desde[3] : (n-hasta[3]),columna[2]]
    t2 = df.iloc[desde[4] : (n-hasta[4]),columna[2]]
    t1 = df.iloc[desde[5] : (n-hasta[5]),columna[2]]
    t = df.iloc[desde[6] : (n-hasta[6]),columna[2]]
    #error temperature
    et6 = df.iloc[desde[0] : (n-hasta[0]),columna[3]]
    et5 = df.iloc[desde[1] : (n-hasta[1]),columna[3]]
    et4 = df.iloc[desde[2] : (n-hasta[2]),columna[3]]
    et3 = df.iloc[desde[3] : (n-hasta[3]),columna[3]]
    et2 = df.iloc[desde[4] : (n-hasta[4]),columna[3]]
    et1 = df.iloc[desde[5] : (n-hasta[5]),columna[3]]
    et = df.iloc[desde[6] : (n-hasta[6]),columna[3]]
    #humidity
    h6 = df.iloc[desde[0] : (n-hasta[0]),columna[4]]
    h5 = df.iloc[desde[1] : (n-hasta[1]),columna[4]]
    h4 = df.iloc[desde[2] : (n-hasta[2]),columna[4]]
    h3 = df.iloc[desde[3] : (n-hasta[3]),columna[4]]
    h2 = df.iloc[desde[4] : (n-hasta[4]),columna[4]]
    h1 = df.iloc[desde[5] : (n-hasta[5]),columna[4]]
    h = df.iloc[desde[6] : (n-hasta[6]),columna[4]]
    #error humidity
    eh6 = df.iloc[desde[0] : (n-hasta[0]),columna[5]]
    eh5 = df.iloc[desde[1] : (n-hasta[1]),columna[5]]
    eh4 = df.iloc[desde[2] : (n-hasta[2]),columna[5]]
    eh3 = df.iloc[desde[3] : (n-hasta[3]),columna[5]]
    eh2 = df.iloc[desde[4] : (n-hasta[4]),columna[5]]
    eh1 = df.iloc[desde[5] : (n-hasta[5]),columna[5]]
    eh = df.iloc[desde[6] : (n-hasta[6]),columna[5]]
    #date
    f = df.iloc[m : (n),0]
    ho = df.iloc[m : (n),1]


    #create data frame
    if m == 6:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-6','L-6','EL-5','L-5','EL-4','L-4','EL-3','L-3','EL-2','L-2','EL-1','L-1','EL','L','ET-6','T-6','ET-5','T-5','ET-4','T-4','ET-3','T-3','ET-2','T-2','ET-1','T-1','ET','T','EH-6','H-6','EH-5','H-5','EH-4','H-4','EH-3','H-3','EH-2','H-2','EH-1','H-1','EH','H'])
        #loop
        for x in range(0, (n-m)):
            idf.loc[x] = [f.iloc[x],ho.iloc[x],g.iloc[x] ,el6.iloc[x],l6.iloc[x],el5.iloc[x],l5.iloc[x],el4.iloc[x],l4.iloc[x],el3.iloc[x],l3.iloc[x],el2.iloc[x],l2.iloc[x],el1.iloc[x],l1.iloc[x],el.iloc[x],l.iloc[x] ,et6.iloc[x],t6.iloc[x],et5.iloc[x],t5.iloc[x],et4.iloc[x],t4.iloc[x],et3.iloc[x],t3.iloc[x],et2.iloc[x],t2.iloc[x],et1.iloc[x],t1.iloc[x],et.iloc[x],t.iloc[x]  ,eh6.iloc[x],h6.iloc[x],eh5.iloc[x],h5.iloc[x],eh4.iloc[x],h4.iloc[x],eh3.iloc[x],h3.iloc[x],eh2.iloc[x],h2.iloc[x],eh1.iloc[x],h1.iloc[x],eh.iloc[x],h.iloc[x]]
        #return
        return idf
    elif m == 5:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-5','L-5','EL-4','L-4','EL-3','L-3','EL-2','L-2','EL-1','L-1','EL','L','ET-5','T-5','ET-4','T-4','ET-3','T-3','ET-2','T-2','ET-1','T-1','ET','T','EH-5','H-5','EH-4','H-4','EH-3','H-3','EH-2','H-2','EH-1','H-1','EH','H'])
        #loop
        for x in range(0, (n-m)):
            idf.loc[x] = [f.iloc[x],ho.iloc[x],g.iloc[x],el5.iloc[x],l5.iloc[x],el4.iloc[x],l4.iloc[x],el3.iloc[x],l3.iloc[x],el2.iloc[x],l2.iloc[x],el1.iloc[x],l1.iloc[x],el.iloc[x],l.iloc[x] ,et5.iloc[x],t5.iloc[x],et4.iloc[x],t4.iloc[x],et3.iloc[x],t3.iloc[x],et2.iloc[x],t2.iloc[x],et1.iloc[x],t1.iloc[x],et.iloc[x],t.iloc[x]  ,eh5.iloc[x],h5.iloc[x],eh4.iloc[x],h4.iloc[x],eh3.iloc[x],h3.iloc[x],eh2.iloc[x],h2.iloc[x],eh1.iloc[x],h1.iloc[x],eh.iloc[x],h.iloc[x]]
        #return
        return idf
    elif m == 4:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-4','L-4','EL-3','L-3','EL-2','L-2','EL-1','L-1','EL','L','ET-4','T-4','ET-3','T-3','ET-2','T-2','ET-1','T-1','ET','T','EH-4','H-4','EH-3','H-3','EH-2','H-2','EH-1','H-1','EH','H'])
        #loop
        for x in range(0, (n-m)):
            idf.loc[x] = [f.iloc[x],ho.iloc[x],g.iloc[x],el4.iloc[x],l4.iloc[x],el3.iloc[x],l3.iloc[x],el2.iloc[x],l2.iloc[x],el1.iloc[x],l1.iloc[x],el.iloc[x],l.iloc[x] ,et4.iloc[x],t4.iloc[x],et3.iloc[x],t3.iloc[x],et2.iloc[x],t2.iloc[x],et1.iloc[x],t1.iloc[x],et.iloc[x],t.iloc[x]  ,eh4.iloc[x],h4.iloc[x],eh3.iloc[x],h3.iloc[x],eh2.iloc[x],h2.iloc[x],eh1.iloc[x],h1.iloc[x],eh.iloc[x],h.iloc[x]]
        #return
        return idf
    elif m == 3:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-3','L-3','EL-2','L-2','EL-1','L-1','EL','L','ET-3','T-3','ET-2','T-2','ET-1','T-1','ET','T','EH-3','H-3','EH-2','H-2','EH-1','H-1','EH','H'])
        #loop
        for x in range(0, (n-m)):
            idf.loc[x] = [f.iloc[x],ho.iloc[x],g.iloc[x],el3.iloc[x],l3.iloc[x],el2.iloc[x],l2.iloc[x],el1.iloc[x],l1.iloc[x],el.iloc[x],l.iloc[x] ,et3.iloc[x],t3.iloc[x],et2.iloc[x],t2.iloc[x],et1.iloc[x],t1.iloc[x],et.iloc[x],t.iloc[x]  ,eh3.iloc[x],h3.iloc[x],eh2.iloc[x],h2.iloc[x],eh1.iloc[x],h1.iloc[x],eh.iloc[x],h.iloc[x]]
        #return
        return idf
    elif m == 2:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-2','L-2','EL-1','L-1','EL','L','ET-2','T-2','ET-1','T-1','ET','T','EH-2','H-2','EH-1','H-1','EH','H'])
        #loop
        for x in range(0, (n-m)):
            idf.loc[x] = [f.iloc[x],ho.iloc[x],g.iloc[x],el2.iloc[x],l2.iloc[x],el1.iloc[x],l1.iloc[x],el.iloc[x],l.iloc[x], et2.iloc[x],t2.iloc[x],et1.iloc[x],t1.iloc[x],et.iloc[x],t.iloc[x], eh2.iloc[x],h2.iloc[x],eh1.iloc[x],h1.iloc[x],eh.iloc[x],h.iloc[x]]
        #return
        return idf
    else:
        idf = pd.DataFrame(columns=['Date','Hour','Min','EL-2','L-2','EL-1','L-1','EL','L','ET-2','T-2','ET-1','T-1','ET','T','EH-2','H-2','EH-1','H-1','EH','H'])
        return idf



# new variables for sum and diff of mean-error
def sumdiff(df, tipo):
    # tipo: diferents types of Times back
    if int(tipo) == 6:
        df['L-6Esum'] = df.apply(lambda x: calculo_error(x['L-6'], x['EL-6'], 1), axis=1)
        df['L-5Esum'] = df.apply(lambda x: calculo_error(x['L-5'], x['EL-5'], 1), axis=1)
    if int(tipo) == 5:
        df['L-5Esum'] = df.apply(lambda x: calculo_error(x['L-5'], x['EL-5'], 1), axis=1)

    df['L-4Esum'] = df.apply(lambda x: calculo_error(x['L-4'], x['EL-4'], 1), axis=1)
    df['L-3Esum'] = df.apply(lambda x: calculo_error(x['L-3'], x['EL-3'], 1), axis=1)
    df['L-2Esum'] = df.apply(lambda x: calculo_error(x['L-2'], x['EL-2'], 1), axis=1)
    df['L-1Esum'] = df.apply(lambda x: calculo_error(x['L-1'], x['EL-1'], 1), axis=1)
    df['L-Esum'] = df.apply(lambda x: calculo_error(x['L'], x['EL'], 1), axis=1)

    if int(tipo) == 6:
        df['L-6Edif'] = df.apply(lambda x: calculo_error(x['L-6'], x['EL-6'], 0), axis=1)
        df['L-5Edif'] = df.apply(lambda x: calculo_error(x['L-5'], x['EL-5'], 0), axis=1)
    if int(tipo) == 5:
        df['L-5Edif'] = df.apply(lambda x: calculo_error(x['L-5'], x['EL-5'], 0), axis=1)

    df['L-4Edif'] = df.apply(lambda x: calculo_error(x['L-4'], x['EL-4'], 0), axis=1)
    df['L-3Edif'] = df.apply(lambda x: calculo_error(x['L-3'], x['EL-3'], 0), axis=1)
    df['L-2Edif'] = df.apply(lambda x: calculo_error(x['L-2'], x['EL-2'], 0), axis=1)
    df['L-1Edif'] = df.apply(lambda x: calculo_error(x['L-1'], x['EL-1'], 0), axis=1)
    df['L-Edif'] = df.apply(lambda x: calculo_error(x['L'], x['EL'], 0), axis=1)

    if int(tipo) == 6:
        df['T-6Esum'] = df.apply(lambda x: calculo_error(x['T-6'], x['ET-6'], 1), axis=1)
        df['T-5Esum'] = df.apply(lambda x: calculo_error(x['T-5'], x['ET-5'], 1), axis=1)
    if int(tipo) == 5:
        df['T-5Esum'] = df.apply(lambda x: calculo_error(x['T-5'], x['ET-5'], 1), axis=1)

    df['T-4Esum'] = df.apply(lambda x: calculo_error(x['T-4'], x['ET-4'], 1), axis=1)
    df['T-3Esum'] = df.apply(lambda x: calculo_error(x['T-3'], x['ET-3'], 1), axis=1)
    df['T-2Esum'] = df.apply(lambda x: calculo_error(x['T-2'], x['ET-2'], 1), axis=1)
    df['T-1Esum'] = df.apply(lambda x: calculo_error(x['T-1'], x['ET-1'], 1), axis=1)
    df['T-Esum'] = df.apply(lambda x: calculo_error(x['T'], x['ET'], 1), axis=1)

    if int(tipo) == 6:
        df['T-6Edif'] = df.apply(lambda x: calculo_error(x['T-6'], x['ET-6'], 0), axis=1)
        df['T-5Edif'] = df.apply(lambda x: calculo_error(x['T-5'], x['ET-5'], 0), axis=1)
    if int(tipo) == 5:
        df['T-5Edif'] = df.apply(lambda x: calculo_error(x['T-5'], x['ET-5'], 0), axis=1)

    df['T-4Edif'] = df.apply(lambda x: calculo_error(x['T-4'], x['ET-4'], 0), axis=1)
    df['T-3Edif'] = df.apply(lambda x: calculo_error(x['T-3'], x['ET-3'], 0), axis=1)
    df['T-2Edif'] = df.apply(lambda x: calculo_error(x['T-2'], x['ET-2'], 0), axis=1)
    df['T-1Edif'] = df.apply(lambda x: calculo_error(x['T-1'], x['ET-1'], 0), axis=1)
    df['T-Edif'] = df.apply(lambda x: calculo_error(x['T'], x['ET'], 0), axis=1)

    if int(tipo) == 6:
        df['H-6Esum'] = df.apply(lambda x: calculo_error(x['H-6'], x['EH-6'], 1), axis=1)
        df['H-5Esum'] = df.apply(lambda x: calculo_error(x['H-5'], x['EH-5'], 1), axis=1)
    if int(tipo) == 5:
        df['H-5Esum'] = df.apply(lambda x: calculo_error(x['H-5'], x['EH-5'], 1), axis=1)

    df['H-4Esum'] = df.apply(lambda x: calculo_error(x['H-4'], x['EH-4'], 1), axis=1)
    df['H-3Esum'] = df.apply(lambda x: calculo_error(x['H-3'], x['EH-3'], 1), axis=1)
    df['H-2Esum'] = df.apply(lambda x: calculo_error(x['H-2'], x['EH-2'], 1), axis=1)
    df['H-1Esum'] = df.apply(lambda x: calculo_error(x['H-1'], x['EH-1'], 1), axis=1)
    df['H-Esum'] = df.apply(lambda x: calculo_error(x['H'], x['EH'], 1), axis=1)

    if int(tipo) == 6:
        df['H-6Edif'] = df.apply(lambda x: calculo_error(x['H-6'], x['EH-6'], 0), axis=1)
        df['H-5Edif'] = df.apply(lambda x: calculo_error(x['H-5'], x['EH-5'], 0), axis=1)
    if int(tipo) == 5:
        df['H-5Edif'] = df.apply(lambda x: calculo_error(x['H-5'], x['EH-5'], 0), axis=1)

    df['H-4Edif'] = df.apply(lambda x: calculo_error(x['H-4'], x['EH-4'], 0), axis=1)
    df['H-3Edif'] = df.apply(lambda x: calculo_error(x['H-3'], x['EH-3'], 0), axis=1)
    df['H-2Edif'] = df.apply(lambda x: calculo_error(x['H-2'], x['EH-2'], 0), axis=1)
    df['H-1Edif'] = df.apply(lambda x: calculo_error(x['H-1'], x['EH-1'], 0), axis=1)
    df['H-Edif'] = df.apply(lambda x: calculo_error(x['H'], x['EH'], 0), axis=1)

    return df



# print all the scenes about light, temprerature, humidity

def generateScene(df, light, temperature, humidity, groupingBy,timesBack,ipath):
    #names to generate
    iname = pd.Series(['By', 'ErrorBy', 'ErrorSumBy', 'ErrorDifBy', '0'])

    #light
    for i, v in light.items():
        if v < 4:
            df.iloc[:, i].to_csv(ipath+'sceneLight'+iname.iloc[v]+groupingBy+timesBack+'.csv', encoding='latin-1', header=True, index=False,sep=',')

            #temperature
    for i, v in temperature.items():
        if v < 4:
            df.iloc[:, i].to_csv(ipath+'sceneTemperature'+iname.iloc[v]+groupingBy+timesBack+'.csv', encoding='latin-1',header=True, index=False,sep=',')

            #humidity
    for i, v in humidity.items():
        if v < 4:
            df.iloc[:, i].to_csv(ipath+'sceneHumidity'+iname.iloc[v]+groupingBy+timesBack+'.csv', encoding='latin-1',header=True, index=False,sep=',')



if __name__=='__main__':
    main()

