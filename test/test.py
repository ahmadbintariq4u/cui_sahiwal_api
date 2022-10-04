import pandas as pd

header=['section','subject','slot','day','teacher','room']
dataset=pd.read_csv("assets/timetable.csv")
dataset.columns=header


print(dataset['section'])