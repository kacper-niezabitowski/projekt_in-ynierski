#Import potrzebnych bibliotek
import pandas as pd
import numpy as np
#from sklearn.ensemble import IsolationForest

#Wczytanie danych z pliku
dane = pd.read_csv(r"D:\Uczelnia\Studia\Praca_Inzynierska\Dataset\BenignTraffic.pcap.csv")

#Usunięcie wierszy, w których występują puste dane
dane.dropna(inplace=True) 

#Sprawdzenie pustych wierszów
print(dane.isnull().sum())
#print(dane['Telnet'].head())
#print(dane['SMTP'].head())

#Funkcja odpowiedzialna za normalizacje danych, metoda min-max
def min_max_normalizacja(kolumna):
    min_wart = kolumna.min()
    max_wart = kolumna.max()
    return (kolumna - min_wart)/(max_wart - min_wart)

#wybrane kolumny do normalizacji
kolumny_do_normalizacji = ['Header_Length', 'Protocol Type', 'Time_To_Live', 'Rate', 'fin_flag_number'
                         , 'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 'ack_flag_number', 'ece_flag_number'
                         , 'cwr_flag_number', 'ack_count', 'syn_count', 'fin_count', 'rst_count', 'HTTP', 'HTTPS', 'DNS'
                         , 'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IGMP', 'IPv', 'LLC', 'Tot sum'
                         , 'Min', 'Max', 'AVG', 'Std', 'Tot size', 'IAT', 'Number', 'Variance']

#iteracja przez każdą kolumne
for kolumna in kolumny_do_normalizacji:
    dane[kolumna] = min_max_normalizacja(dane[kolumna])

#dane['Telnet'].fillna(0, inplace=True)
#dane['SMTP'].fillna(0, inplace=True)
#Zapis danych do nowego pliku
dane.to_csv(r"D:\Uczelnia\Studia\Praca_Inzynierska\Dataset\ZnormalizowaneDane.csv", index=False)
print(dane.head())
print(dane.isnull().sum())
#print(dane['Telnet'].head())
#print(dane['SMTP'].head())
