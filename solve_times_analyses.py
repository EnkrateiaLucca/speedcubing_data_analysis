import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import pathlib
import glob
from natsort import natsorted
from scipy.ndimage.filters import gaussian_filter1d



# Loading the csv files
file_paths = glob.glob(r"C:\Users\lucas\Desktop\projects\automation\rubiks\solve_times\*.csv")
# Setting the color palette for the plots
colors = sns.color_palette("hls", len(file_paths))
# Concatenating all the csvs into noe
df = pd.concat([pd.read_csv(file_path) for file_path in file_paths])
# Getting todays sessions (leveragint the fact that the csv files are sorted)
todays_session = pd.read_csv(file_paths[-1])


# Getting the following means:
df["Order"] = list(range(0,len(df)))
# Last 500 solves
mean_500 = df["Time"][-500:].mean()
# All time mean
all_time_mean = df["Time"].mean()
# Today's session mean
session_mean = todays_session["Time"].mean()
# Getting the index for the best and worst time for today (which would be removed in competition) 
index_min = todays_session["Time"][todays_session["Time"]==todays_session["Time"].min()].index[0]
index_max = todays_session["Time"][todays_session["Time"]==todays_session["Time"].max()].index[0]
# Smoothing the data from today's session to see how the average oscilated
today_time_smooth = gaussian_filter1d(todays_session["Time"], sigma=2)
# Getting my best time ever
best_ever = np.min(df["Time"].values)
# Smoothing all my times to see it on the raw data plot
time_smooth = gaussian_filter1d(df["Time"], sigma=2)

# Plotting the evolution of times
plt.subplot(1,3,1)
plt.plot(df["Order"],df["Time"], color="green", label="Times")    
plt.plot(df["Order"],time_smooth, color="red", label="Smoothed")
plt.title("Times evolution, current best time: {}".format(best_ever))
plt.legend()
# Plotting a histogram of times
plt.subplot(1,3,2)
plt.hist(df["Time"], color="green")
plt.title("Histogram of times, current mean (last 500): {}".format(round(mean_500,3)))
# Plotting today's session
plt.subplot(1,3,3)
plt.plot(todays_session["Time"], c="green")
plt.scatter(index_min,todays_session["Time"].min(), c="orange", label="Best Time today")
plt.scatter(index_max,todays_session["Time"].max(), c="black", label="Worst Time today")
plt.plot(today_time_smooth, label="Smothed time", c="red")
plt.legend()
plt.title("Todays Session, mean: {}".format(round(session_mean,3)))
plt.show()
