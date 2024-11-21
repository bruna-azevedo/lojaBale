import unittest

from abc import ABC, abstractmethod

class DescontoStrategy(ABC):
    @abstractmethod
    def calcular(self, total):
        pass

class DescontoPorValor(DescontoStrategy):
    def calcular(self, total):
        if total > 200:
            return 0.10 
        return 0.0

class DescontoFixo(DescontoStrategy):
    def calcular(self, total):
        return 0.15 

class SemDesconto(DescontoStrategy):
    def calcular(self, total):
        return 0.0

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class LojaBale:
    def __init__(self, desconto_strategy: DescontoStrategy):
        self.produtos = [
            Produto("Sapatilha de balé", 120.00),
            Produto("Collant de balé", 80.00),
            Produto("Meia de balé", 20.00),
            Produto("Saia de balé", 45.00),
            Produto("Pano para aquecimento", 30.00)
        ]
        self.carrinho = []
        self.desconto_strategy = desconto_strategy

    def exibir_produtos(self):
        print("Produtos disponíveis na Loja de Balé:")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto.nome} - R${produto.preco:.2f}")

    def adicionar_ao_carrinho(self, indice_produto):
        produto_selecionado = self.produtos[indice_produto]
        self.carrinho.append(produto_selecionado)
        print(f"{produto_selecionado.nome} foi adicionado ao seu carrinho.")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.carrinho)
        # Usando a estratégia de desconto
        desconto = self.desconto_strategy.calcular(total)
        total_com_desconto = total * (1 - desconto)
        return total_com_desconto

    def mostrar_carrinho(self):
        if not self.carrinho:
            print("Seu carrinho está vazio.")
        else:
            print("\nItens no seu carrinho:")
            for item in self.carrinho:
                print(f"{item.nome} - R${item.preco:.2f}")
            total = self.calcular_total()
            print(f"Total com desconto: R${total:.2f}")

# Execução do código com a nova estratégia de desconto
loja = LojaBale(DescontoPorValor())  
loja.exibir_produtos()
loja.adicionar_ao_carrinho(0)
loja.adicionar_ao_carrinho(1)
loja.mostrar_carrinho()

print("\nMudando para o desconto fixo...")
loja.desconto_strategy = DescontoFixo()
loja.mostrar_carrinho()
