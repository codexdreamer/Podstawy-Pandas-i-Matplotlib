import pandas as pd


dane = {
    'region': ['North', 'South', 'North', 'East', 'West', 'South', 'East', 'North', 'West'],
    'type': ['A', 'B', 'A', 'C', 'B', 'B', 'C', 'A', 'B'],
    'weight': [70, 80, 75, 60, 85, 90, 65, 78, 88]
}


arkusz = pd.DataFrame(dane)




srednia_waga = arkusz.groupby('region')['weight'].mean()
print(srednia_waga)

ile_wystepuje = arkusz['type'].value_counts() 

print(ile_wystepuje)

srednia_waga_reset = srednia_waga.reset_index()
print(srednia_waga_reset)





