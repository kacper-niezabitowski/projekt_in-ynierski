#Import potrzebnych bibliotek
import pandas as pd
import numpy as np

#Wczytanie danych z pliku
data = pd.read_csv(r"C:\Users\Kacper\Desktop\BenignTraffic.pcap.csv")
#data.dropna(inplace=True)
#print(data.isnull().sum())
print(data.describe())
#data_normalization = data.copy()


