import matplotlib.pyplot as plt

def grafico_linhas():
    dias = [1, 2, 3, 4, 5, 6, 7]
    estoque = [100, 95, 110, 105, 120, 115, 130]

    plt.plot(dias, estoque, label="Entradas", color="green")
    plt.title("Tendencia de Estoque Diário")
    plt.xlabel("Dias")
    plt.ylabel("Quantidade")
    plt.grid()
    plt.show()

def grafico_pizza():
    categorias = ["Eletrônicos", "Vestuário", "Alimentos"]
    valores = [15000, 8000, 5000]
    plt.pie(valores, labels=categorias, autopct='%1.1f%%')
    plt.title("Proporção de categorias")
    plt.show()

def grafico_barras():
    produtos = ["Teclado", "Mouse", "Monitor", "Webcam"]
    quantidades = [50, 75, 30, 60]
    plt.bar(produtos, quantidades)
    plt.title("Comparação de Produtos")
    plt.ylabel("Quantidade")
    plt.show()

def grafico_dispersao():
    precos = [50, 120, 300, 80, 20]
    estoque = [80, 25, 10, 70, 150]

    plt.scatter(precos, estoque)
    plt.title("Preço vs Quantidade")
    plt.xlabel("Preços")
    plt.ylabel("Quantidade")
    plt.show()

grafico_linhas()
grafico_pizza()
grafico_barras()
grafico_dispersao()