import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# importar os dados necessários 
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visulizar os dados importados
pd.set_option('display.max_columns', None)
print(tabela_vendas) 

# calcular faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# calcular quantidade de produtos vendidas por loja 
qtd_produtos_vendidos = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print(qtd_produtos_vendidos)

# calcular valor de tickt médio por loja
tikt_medio = (faturamento['Valor Final']/ qtd_produtos_vendidos['Quantidade']).to_frame()
print(tikt_medio)

# enviar cada reltório para uma planilha 
pd.DataFrame(faturamento)
faturamento.to_excel('Faturamento de cada loja.xlsx')


pd.DataFrame(qtd_produtos_vendidos)
qtd_produtos_vendidos.to_excel('quantidade de produtos vendidos por loja.xlsx')


pd.DataFrame(tikt_medio)
tikt_medio.to_excel('ticket médio de cada loja')

