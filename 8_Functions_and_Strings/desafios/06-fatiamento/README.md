# Recortes de uma palavra

**Nível:** Prática · **Referência:** slides 15–16 da aula desta pasta.

## Desafio

Com texto definido no código, imprima os primeiros três caracteres, os últimos três, os caracteres nos índices pares e a string invertida. Use somente slicing para os recortes. Acrescente uma explicação sobre o limite final exclusivo.

## Casos para conferir

"Python" → "Pyt", "hon", "Pto", "nohtyP". "ab" → "ab", "ab", "a", "ba". "" → quatro strings vazias. "Programming" nos índices pares → "Pormig".

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Slices toleram limites além do tamanho da string e aceitam passo negativo.

</details>
