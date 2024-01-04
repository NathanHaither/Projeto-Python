#Pandas
import pandas as pd

lista_compras = [
    {
    "Código da Compra" : 1,
    "Nome do Produto" : "Sabão",
    "Categoria do Produto" : "Limpeza",
    "Quantidade Comprada" :3,
    "Valor Unitário" : 10,
    "Valor Total Comprado" : 10*3 
    },
    {
     "Código da Compra" : 2,
    "Nome do Produto" : "Bolacha",
    "Categoria do Produto" : "Alimentos",
    "Quantidade Comprada" :7,
    "Valor Unitário" : 25,
    "Valor Total Comprado" : 25*7 
    },
    {
     "Código da Compra" : 3,
    "Nome do Produto" : "Água",
    "Categoria do Produto" : "Bebida",
    "Quantidade Comprada" :5,
    "Valor Unitário" : 5,
    "Valor Total Comprado" : 5*5
    },
    {
    "Código da Compra" : 4,
    "Nome do Produto" : "Água",
    "Categoria do Produto" : "Bebida",
    "Quantidade Comprada" :4,
    "Valor Unitário" : 3,
    "Valor Total Comprado" : 4*3      
    },
    {
    "Código da Compra" : 5,
    "Nome do Produto" : "Detergente",
    "Categoria do Produto" : "Limpeza",
    "Quantidade Comprada" :2,
    "Valor Unitário" : 6,
    "Valor Total Comprado" : 2*6       
    },
    {
      "Código da Compra" : 6,
     "Nome do Produto" : "Carne",
     "Categoria do Produto" : "Alimentos",
     "Quantidade Comprada" :1,
     "Valor Unitário" : 50,
     "Valor Total Comprado" : 50*1
    }
        
    
    
]


print(lista_compras)

df = pd.DataFrame(lista_compras)

print(df)


#Obtendo o ticket médio
print(
   "O Valor do Tícket médio é :", df["Valor Total Comprado"].mean()
)


# Obtendo a Quantidade da  Média comprada
print(
    "O valor da média comprada é:", df["Quantidade Comprada"].mean()
)

#Total vendido por produto
print("Total vendido por produto é :",df.groupby(["Nome do Produto"]).sum()
  
)

# Quantidade vendida por produto

print(
  "A Quantidade vendida por produto é :" , df.groupby("Nome do Produto")["Quantidade Comprada"].sum()
)