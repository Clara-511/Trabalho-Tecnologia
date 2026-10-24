import pandas as pd

dados = pd.read_csv(
    "dados.csv",
    sep=";",
    engine="python",
    encoding="utf-8")

print("Informações gerais do conjunto de dados: ", dados.info)

print("\nPrimeiras 10 linhas:", dados.head(10))

print("\nÚltimas 10 linhas:", dados.tail(10))

dados_tratados = dados.copy()

dados_tratados["Calories"] = dados_tratados["Calories"].fillna(0)

print("\nDados após substituir nulos de Calories por 0:", dados_tratados.to_string())

dados_tratados["Date"] = dados_tratados["Date"].fillna("1900/01/01")

print("\nDados após substituir nulos de date:", dados_tratados.to_string())

try:
    dados_tratados["Date"] = pd.to_datetime(
      dados_tratados["Date"],
      format = "%Y/%m/%d"
    )
except ValueError as erro:
    print("\nErro esperado na conversão de Date:")
    print(erro)

dados_tratados["Date"] = dados_tratados["Date"].replace(
    "1900/01/01", pd.NA
)

print("\nDados após substituir 1900/01/01 por NaN:", dados_tratados.to_string())

dados_tratados["Date"] = dados_tratados["Date"].replace(
    "20201226",
    pd.to_datetime("20201226", format="%Y%m%d").strftime("%Y/%m/%d")
)

dados_tratados["Date"] = pd.to_datetime(
    dados_tratados["Date"],
    format="%Y/%m/%d",
    errors="coerce"
)

print("\nDados após a conversão da coluna date:", dados_tratados.to_string())

dados_tratados = dados_tratados.dropna(subset=["Date"])

print("\nConjunto de dados final após remover datas nulas:", dados_tratados.to_string())

print("\nTipos de dados finais:", dados_tratados.dtypes)
