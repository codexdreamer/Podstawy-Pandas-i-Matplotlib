import pandas as pd


dane = {
    'description': ['event1', 'event2', 'event3'],
    'value': [100, 200, 300],
    'category': ['A1', 'B2', 'C3']
}

arkusz = pd.DataFrame(dane)

#dodaje nowy wiersz
nowy_wiersz = pd.DataFrame([['submarine implosion', 730, 'C1']], columns=arkusz.columns, index=['ref_0'])

arkusz = pd.concat([arkusz, nowy_wiersz])

#zmiana nazwy kolumny
arkusz = arkusz.rename(columns={'value': 'wartość'})

print(arkusz)


