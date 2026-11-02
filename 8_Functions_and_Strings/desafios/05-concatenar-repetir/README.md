# Etiqueta de texto

**Nível:** Prática · **Referência:** slides 13–14, 24–25 da aula desta pasta.

## Desafio

Implemente etiqueta(nome, repeticoes=1), retornando a repetição de "[NOME]" sem separadores. Use concatenação e repetição de strings. repeticoes será inteiro não negativo. Inclua uma docstring e consulte help(etiqueta).

## Casos para conferir

etiqueta("Ana") → "[Ana]"; etiqueta("Py", 3) → "[Py][Py][Py]"; etiqueta("", 2) → "[][]"; etiqueta("Ana", 0) → "".

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Monte uma unidade de texto antes de repeti-la.

</details>
