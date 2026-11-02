# Três coleções, três compreensões

**Nível:** Consolidação · **Referência:** slides 23–27 da aula desta pasta.

## Desafio

Dada uma lista de inteiros, crie: uma lista dos quadrados dos pares na ordem original; um dicionário número → cubo para valores positivos; um conjunto dos restos da divisão por 3. Use respectivamente list, dict e set comprehension.

## Casos para conferir

[-2,0,2,2,3] → lista [4,0,4,4]; dicionário {2:8,3:27}; conjunto {0,1,2}. [] → [], {}, set(). Chaves repetidas do dicionário aparecem uma só vez.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

A coleção escolhida determina se repetição e posição são preservadas.

</details>
