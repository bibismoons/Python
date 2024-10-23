class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho_de_Compras:
    def __init__(self):
        self.itens = []

    def adicionar_item (self, produto, quantidade):
        item = Item_de_Compra (produto, quantidade)
        self.itens.append(item)

class Item_de_Compra:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

if __name__ == "__main__":
    #Criando produtos
    produto1 = Produto ("Camiseta", 20.0)
    produto2 = Produto ("Calça", 40.0)

    #Criando carrinho de compras e adicionando itens
    carrinho = Carrinho_de_Compras();
    carrinho.adicionar_item(produto1, 2)
    carrinho.adicionar_item(produto2, 1)

    #Exibindo os itens do carrinho
    for item in carrinho.itens:
        print(f"Produto: {item.produto.nome}, Quantidade: {item.quantidade}, Preço Unitário: R${item.produto.preco}")
