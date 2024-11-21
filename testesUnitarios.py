import unittest

class TestLojaBale(unittest.TestCase):

    def setUp(self):
        self.loja_com_desconto_por_valor = LojaBale(DescontoPorValor())
        self.loja_com_desconto_fixo = LojaBale(DescontoFixo())
        self.loja_sem_desconto = LojaBale(SemDesconto())

        # Adicionando produtos ao carrinho para os testes
        self.loja_com_desconto_por_valor.adicionar_ao_carrinho(0)
        self.loja_com_desconto_por_valor.adicionar_ao_carrinho(1)

        self.loja_com_desconto_fixo.adicionar_ao_carrinho(0)
        self.loja_com_desconto_fixo.adicionar_ao_carrinho(1)

        self.loja_sem_desconto.adicionar_ao_carrinho(0)
        self.loja_sem_desconto.adicionar_ao_carrinho(1)

    def test_calcular_total_com_desconto_por_valor(self):
        total = self.loja_com_desconto_por_valor.calcular_total()
        self.assertEqual(total, 180.00)

    def test_calcular_total_com_desconto_fixo(self):
        total = self.loja_com_desconto_fixo.calcular_total()
        self.assertEqual(total, 170.00)

    def test_calcular_total_sem_desconto(self):
        total = self.loja_sem_desconto.calcular_total()
        self.assertEqual(total, 200.00)

    def test_mudar_estrategia_de_desconto(self):
        self.loja_com_desconto_por_valor.desconto_strategy = DescontoFixo()
        total = self.loja_com_desconto_por_valor.calcular_total()
        self.assertEqual(total, 170.00)

    def test_adicionar_produto_ao_carrinho(self):
        self.assertEqual(len(self.loja_com_desconto_por_valor.carrinho), 2)
        
        self.loja_com_desconto_por_valor.adicionar_ao_carrinho(2)
        self.assertEqual(len(self.loja_com_desconto_por_valor.carrinho), 3)

    def test_exibir_produtos(self):
        try:
            self.loja_com_desconto_por_valor.exibir_produtos()
            sucesso = True
        except:
            sucesso = False
        self.assertTrue(sucesso)

if __name__ == "__main__":
    unittest.main()
