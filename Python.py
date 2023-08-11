# criação e análise do conteudo#
import pandas as pd

tabela = pd.read_excel("Vendas.xlxs")
display(tabela)

#Calcular faturamento final
Faturamento_total = tabela["Coluna Valor Final"].sum()
print(Faturamento_total)

#Faturamento por loja
Faturamento_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
display(Faturamento_loja)

#Informações de uma loja
Faturamento_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(Faturamento_produto)
