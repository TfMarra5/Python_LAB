# Percorrer caracteres

**Nível:** Consolidação · **Referência:** slides 22–23 da aula desta pasta.

## Desafio

Implemente contar_vogais(texto), retornando a quantidade de caracteres em "aeiouAEIOU". Use for e um contador; não use count. Considere somente essas dez letras: letras acentuadas não contam neste exercício.

## Casos para conferir

"Python" → 1; "AEiou" → 5; "xyz" → 0; "" → 0; "ação" → 2.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Teste cada caractere com in e incremente apenas quando houver correspondência.

</details>
