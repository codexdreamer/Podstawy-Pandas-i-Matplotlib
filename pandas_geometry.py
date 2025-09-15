import pandas as pd  #import biblioteki pandas jako pd
import math  #import biblioteki math

dane = {
    'color':['red','pink','yellow','black'],
    'radius': [1,3,6,34]
}   #dane do arkusza



arkusz = pd.DataFrame(dane)  #tworzenie arkusza dataframe

arkusz['diameter'] = arkusz['radius'] * 2  #tworzenie nowej kolumny poprzez mnożenie *2 wartości w kolumnie 'radius'

arkusz['area'] = (arkusz['radius'])**2   * math.pi  #tworzenie nowej kolumny poprzez mnożenie wartości radius**2  razy liczba pi

print(arkusz)  #pokazuje nasz arkusz

print('Maksymalna średnica to:',arkusz['diameter'].max()) #wyswietla maksymalna srednice
print('Najmniejszy promień wynosi:',arkusz['radius'].min()) #wyswietla najmnijeszy promien
print("Średnia wartość area wynosi:",arkusz['area'].mean()) #liczy srednia z wartosci z kolumny 'area'



