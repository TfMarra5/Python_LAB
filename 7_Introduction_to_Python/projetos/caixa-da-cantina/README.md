# Caixa da cantina

**Nível:** Projeto integrador · **Referência:** slides 16–26 da aula desta pasta.

## Desafio

Crie um menu repetido: 1 café (2 euros), 2 sanduíche (5 euros), 3 água (1 euro), 0 finalizar. Para produto válido, leia quantidade inteira positiva; quantidade zero ou negativa mostra "Quantidade inválida" e não altera o total. Opção desconhecida mostra "Opção inválida" e não pede quantidade. Ao finalizar, mostre quantidade total de unidades e valor da compra. Use somente variáveis, condições e laços; sem funções próprias, listas ou dicionários. Entradas numéricas serão inteiros válidos.

## Casos para conferir

Opções/quantidades: 1,2,2,1,0 → 3 unidades, 9 euros. 0 → 0 unidades, 0 euros. 3,0,3,2,0 → Quantidade inválida; 2 unidades, 2 euros. 9,0 → Opção inválida e compra vazia.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Separe a seleção do preço, a validação da quantidade e a atualização dos totais.

</details>
