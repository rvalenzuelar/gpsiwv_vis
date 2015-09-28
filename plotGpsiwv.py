
import Meteoframes as mf 
import matplotlib.pyplot as plt 
from matplotlib import dates
import datetime

import seaborn as sns 
import pandas as pd

f='/home/rvalenzuela/GPS_IWV/case03/bby_gpsiwv_010123-24.dat'

df = mf.parse_gps_iwv(f)

st = datetime.datetime(2001, 1, 23, 0, 0)
en = datetime.datetime(2001, 1, 25, 0, 0)
xticks = pd.date_range(start=st,end=en, freq='3H')

fig,ax=plt.subplots()
ax.plot(df.index, df['IPW'],'-o')
ax.set_xticks(xticks)
ax.invert_xaxis()
datefmt = dates.DateFormatter('%H\n%d')
ax.xaxis.set_major_formatter(datefmt)
ax.set_xlabel(r'$\Leftarrow$'+' Time [UTC]')
ax.set_ylabel('IWV [cm]')
t1='GPS-IWV at Bodega Bay'
t2='\nDate: ' + st.strftime('%b-%Y')
plt.title(t1+t2)

plt.show(block=False)