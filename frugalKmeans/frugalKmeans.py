import pandas as pd
from biKMeans import *

data=loadDataSet('coordinates_cleaned.txt')

clusterList,clusterAss=biKmeans(data,10)

data=hstack((array(data),array(clusterAss)))

df=pd.DataFrame(data)

def case(x):
    return {
        0: 'blue',
        1: 'orange',
        2: 'yellow',
        3: 'green',
        4: 'pink',
        5: 'brown',
        6: 'grey',
        7: 'black',
        8: 'red',
        9: 'white',
    }[x]

for i in range(df[2].shape[0]):
    df[2].ix[i]=case(df[2].ix[i])

df[4]=['circle1' for i in range(df.shape[0])]

