# cycler	0.10.0	0.10.0
# kiwisolver	1.1.0	1.1.0
# matplotlib	3.0.3	3.0.3
# numpy	1.16.3	1.16.3
# pandas	0.24.2	0.24.2
# pip	10.0.1	19.1
# pyparsing	2.4.0	2.4.0
# python-dateutil	2.8.0	2.8.0
# pytz	2019.1	2019.1
# setuptools	39.1.0	41.0.1
# six	1.12.0	1.12.0


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataRaw = pd.read_csv('/home/vaske/to_backup/300220/Datoja/data.txt', delimiter=';')
dataRaw_arr = dataRaw.iloc[0:557,0:2].values

dataRaw_pandas=pd.DataFrame(dataRaw_arr)
dataRaw_pandas.to_csv('/home/vaske/to_backup/300220/Datoja/data_from_calc.txt', sep=';')

freq =dataRaw_arr[:,0]
values=dataRaw_arr[:,1]

plt.plot(freq,values)
plt.show()

print('DONE')