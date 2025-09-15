import pandas as pd  #import biblioteki pandas jako pd

dane = {
    'density': [4.5, 5.2, 6.3, 4.9, 7.1],
    'depth': [10, 5, 20, 5, 30],
    'base': [3, 4, 5, 6, 7],
    'height': [2, 3, 4, 5, 6]    #dane do arkusza
}


arkusz = pd.DataFrame(dane)  #tworzymy arkusz dataframe na podstawie danych wyzej

print(arkusz.query('density > 5'))  #filtruje i wyswietla tylko te wiersze w ktorych wartosc kolumny 'density' jest wieksza od 5

wartosc = arkusz['depth'].min() #przypisuje najmniejsza wartosc w kolumnie 'depth' do zmiennej 'wartosc'

print(arkusz.query('depth == @wartosc')) #wypisuje tylko wiersze gdzie wartosc 'depth' jest rowna zmiennej 'wartosc' czyli 5

arkusz['volume'] = arkusz['base'] * arkusz['height'] * 0.5 #tworzy nową kolumne i oblicza bazujac na wartosciach z kolumn 'height' i 'base'

print(arkusz)  #pokazuje arkusz po powyzszych poprawkach