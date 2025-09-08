import pandas as pd


data=pd.read_csv("D:\\github\\panda\\nyc_taxis.csv")

data.dropna() #removes all rows with Nan values