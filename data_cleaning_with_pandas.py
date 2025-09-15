import pandas as pd #import biblioteki pandas jako pd

wczytany_arkusz = pd.read_csv('/home/moj_komp/Pulpit/arkusz.csv') #odczytywanie pliku 'csv' i przypisywanie wczytany_arkusz

arkusz = pd.DataFrame(wczytany_arkusz)  #tworzenie wykresu dataframe

print(arkusz)  #wyswietla wykres

print(arkusz.info())  #pokazuje informacje o arkuszu (podstawowe)

print(arkusz.isna().sum())  #liczy ile jest braków 


arkusz.dropna(inplace='brak danych')  #usuwa 

print(arkusz.tail(1))

print(arkusz)
