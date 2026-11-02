# Frete configurável

**Nível:** Fundamentos · **Referência:** slides 4–6 da aula desta pasta.

## Desafio

Implemente total_compra(valor, frete=5), retornando valor + frete. Considere ambos não negativos. Faça chamadas com frete omitido, explícito e argumentos nomeados em ordem invertida. A função não deve ler input nem imprimir.

## Casos para conferir

total_compra(20) → 25; total_compra(20, 0) → 20; total_compra(frete=3, valor=10) → 13.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

O valor padrão vale quando o argumento é omitido, não quando ele é zero.

</details>
