# lojaBale
Problema: descontos não estão sendo aplicados corretamente. Os descontos são definidos de acordo com o total de compras, mas a lógica para aplicar esse desconto não está separada e acaba sendo misturada com outras lógicas.
Solução: O padrão Strategy, neste case, define diferentes formas de calcular o desconto e os encapsula de modo que eles possam ser trocados dinamicamente. Logo, torna o código mais flexível e desacoplado.

O Stratefy foi aplicado/definido na classe DescontoStrategy, que define o método calcular(total) que será implementado pelas classes de estratégia de desconto.
