import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
dane = pd.read_csv(r"D:\Uczelnia\Studia\Praca_Inzynierska\Dataset\ZnormalizowaneDane.csv")
print(dane.head())

kolumny_do_modelu = ['Header_Length', 'Protocol Type', 'Time_To_Live', 'Rate', 'fin_flag_number'
                         , 'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 'ack_flag_number', 'ece_flag_number'
                         , 'cwr_flag_number', 'ack_count', 'syn_count', 'fin_count', 'rst_count', 'HTTP', 'HTTPS', 'DNS'
                         , 'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IGMP', 'IPv', 'LLC', 'Tot sum'
                         , 'Min', 'Max', 'AVG', 'Std', 'Tot size', 'IAT', 'Number', 'Variance']

x = dane[kolumny_do_modelu]
model = IsolationForest(n_estimators = 120, n_jobs=-1)
model.fit(x)
y_pred = model.predict(x)
dane['Anomalie'] = y_pred
anomalie = len(dane[dane['Anomalie'] == -1])
print(f"Liczba wykrytych anomalii: {anomalie}")
plt.figure(figsize=(10, 6))
plt.scatter(dane.index, dane['Rate'], c=dane['Anomalie'], cmap='coolwarm', label='Anomalies')
plt.title("Wizualizacja wykrytych anomalii")
plt.xlabel("Indeks")
plt.ylabel("Rate")
plt.legend()
plt.show()