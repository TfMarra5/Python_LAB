# Mesmo problema, três estilos

**Nível:** Consolidação · **Referência:** slides 33–36 da aula desta pasta.

## Desafio

Implemente quadrados_loop, quadrados_comprehension e quadrados_funcional. Todas recebem uma lista de inteiros e retornam os quadrados dos pares na ordem original, sem alterar a entrada. Use for/if/append na primeira, list comprehension na segunda e map/filter/lambda na terceira. Compare os resultados com == e explique qual versão você acha mais legível.

## Casos para conferir

[1,2,3,4] → [4,16] nas três; [-2,0,2,2] → [4,0,4,4]; [1,3] → []; [] → []. Todas as comparações entre versões devem ser True.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

A condição seleciona o número original; a transformação calcula o quadrado.

</details>
