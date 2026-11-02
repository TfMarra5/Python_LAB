# Ordenar sem perder o original

**Nível:** Fundamentos · **Referência:** slides 11–12 da aula desta pasta.

## Desafio

Implemente ranking(notas), retornando uma nova lista em ordem decrescente, incluindo notas repetidas. Preserve a lista recebida. Use slicing, sort e reverse. Mostre também quantas vezes a maior nota ocorre, ou "Sem notas" se vazia.

## Casos para conferir

[7,10,7,5] → [10,7,7,5], maior ocorre 1 vez; [8,8] → [8,8], 2 vezes; [] → [], Sem notas. A entrada deve continuar igual após a chamada.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

sort modifica a lista e retorna None; escolha a lista certa para ordenar.

</details>
