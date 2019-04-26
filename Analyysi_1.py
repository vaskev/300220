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

data_raw_read = pd.read_csv('/home/vaske/to_backup/300220/Datoja/data.txt', delimiter=';')
data_raw =data_raw_read.iloc[0:557,0:2]
max_value_index= data_raw.idxmax(0)


# debug tiedosto
dataRaw_arr = data_raw.values
dataRaw_pandas=pd.DataFrame(dataRaw_arr)
dataRaw_pandas.to_csv('/home/vaske/to_backup/300220/Datoja/data_from_calc.txt', sep=';')

freq =dataRaw_arr[:,0]
values=dataRaw_arr[:,1]

pointer_f = freq[max_value_index[1]]
pointer_v = values[max_value_index[1]]

freq_r  = round ( freq  [max_value_index[1]] , 2)
value_r = round ( values[max_value_index[1]] , 2)

print('f =     '+str(freq_r))
print('Value = '+str(value_r))

raami = plt.figure()
kuvaaja = raami.add_subplot(1,1,1)
kuvaaja.plot(freq,values)
teksti = str(freq_r)+"MHz,"+str(value_r)
kuvaaja.annotate(teksti,
                 xy=(pointer_f,pointer_v  ),
                 xytext = (pointer_f +5 ,pointer_v +5),
                 arrowprops=dict(arrowstyle="->",connectionstyle="arc,angleA=45,armA=10,rad=10")
                 )

plt.show()

print('DONE')