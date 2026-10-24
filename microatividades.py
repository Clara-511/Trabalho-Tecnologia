import pandas as pd

pd.options.display.max_rows = 9999

dados = pd.read_csv(
    "dados.csv",
    sep=";",
    engine="python",
    encoding="utf-8"
)

print("Dados originais: ", dados.to_string())

subconjunto = dados[["ID","Duration","Date","Pulse","Maxpulse","Calories"]]

print("\nSubconjunto de dados:", subconjunto)

print("\nPrimeiras 10 linhas do conjunto de dados:", dados.head(10))

print("\nÚltimas linhas do conjunto de dados:", dados.tail(10))

print("\nInformações gerais sobre o conjunto de dados:", dados.info)

print("\nTotal de linhas:", dados.shape[0])

print("\nTotal de colunas:", dados.shape[1])

print("\nQuantidade de dados nulos por coluna:", dados.isnull().sum())

print("\nTotal de dados nulos:", dados.isnull().sum().sum())

print("\nTipo de dado de cada coluna:", dados.dtypes)

memoria = dados.memory_usage(deep=True).sum()

print("\nMemória utilizada:", memoria, "bytes")

print("Memória utilizada em KB:", round(memoria / 1024, 2), "KB")