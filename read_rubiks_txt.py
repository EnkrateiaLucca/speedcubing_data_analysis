import pandas as pd
from datetime import datetime

file = "times.txt"
df = pd.DataFrame()
times_list = []
scrambles = []
with open(file, "r") as times:
	for line in times.readlines():
		if "(" in line or ")" in line:
			line = line.replace("(","")
			line = line.replace(")","")
		index = line.index(":")+1
		time = line[index:index+6]
		times_list.append(time)
		scramble = line[index+6:]
		scrambles.append(scramble)
	df["Time"] = times_list
	df["Scramble"] = scrambles
	year = datetime.today().year
	month = datetime.today().month
	day = datetime.today().day
	df.to_csv("{}_{}_{}.csv".format(year,month,day))
print(df.head())
		
		
