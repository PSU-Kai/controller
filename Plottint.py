
#!/usr/bin/env python
# coding: utf-8

# # Plotting WH Data
# 
# #### Pseudocode
# - Import modules
# - Read in the csv file
# - Convert to NumPy array
# - Create two variables
# - Create a line plot

#  ### Import Module and Convert to NumPy array

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')

# importing csv file
df = pd.read_csv('log.csv', header=None)
df = df.dropna(thresh=2) # drops lines with '0'
error_bad_lines=False


# In[2]:


#delete unnecessary data columns. adjust these column values depending on the delivered log.csv data
df.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12,14], axis=1, inplace=True)

# extract time data and converts to datetime
df.insert(1, 'Time', pd.to_datetime(df[0]))
df['Time'] = df['Time'].dt.strftime('%H:%M:%S')

# delete original timestamp data
df.drop([0], axis=1, inplace=True)


# ### Create Variables
# - 'EnergyTake' will be the XXXXXX column of the csv file
# - 'Time' will be the XXXXX column of the csv file
# - Is current included in the log.csv data? We can add that as a variable as well.

# In[3]:


# convert to numpy array

wd = np.array(df)

# create axis variables
Time = wd[:,0]
EnergyTake = wd[:,1]
Current = wd[:,2]/240 # current = power_column/voltage


# ### Create Line Plot
# #### Create a line plot of stress vs strain. (As stated, stress vs. strain, ensure you plot stress on the y-axis and strain on the x-axis)
# - <b>Include axis labels</b> 
# - <b>Include a title</b> 
# - <b>legend on your plot.</b>

# In[4]:


# create fig and ax objects
fig, ax1 = plt.subplots(1,1,figsize=(10,8))
ax2 = ax1.twinx()


# plot the values
ax1.plot(Time, EnergyTake)
ax2.plot (Time, Current, 'r--')


# set the labels
ax1.set_title('EnergyTake and Current vs Time')
ax1.set_xlabel('Timestamp (H:M:S)')
ax1.set_ylabel('EnergyTake (Wh)')
ax2.set_ylabel('Current (A)')


# set axis ticks
ax1.xaxis.set_major_locator(plt.MaxNLocator(25)) # set number of ticks on x-axis
ax1.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y1-axis
ax2.yaxis.set_major_locator(plt.MaxNLocator(15)) # set number of ticks on y2-axis
ax2.set_ylim(ymin=0) # forces current axis to start from 0 
fig.legend(['EnergyTake','Current'])

ax1.tick_params(axis='x', labelrotation=45)

#fig.autofmt_xdate(rotation=90) # rotate x-axis data
ax1.grid()


# display and save the plot
plt.tight_layout()
plt.savefig('wh_data.jpg', dpi=95, bbox_inches='tight') # change save file name and size of graph
plt.show()

