# Palíndromo com regras explícitas

**Nível:** Consolidação · **Referência:** slides 2, 16, 19–25 da aula desta pasta.

## Desafio

Implemente eh_palindromo(texto): ignore apenas espaços comuns e diferença entre maiúsculas e minúsculas, usando replace e lower (lower converte letras para minúsculas). Pontuação e acentos permanecem. Retorne False se o texto normalizado ficar vazio; caso contrário, compare com o inverso. Inclua docstring e mantenha input/print fora da função.

## Casos para conferir

"Arara" → True; "A sacada da casa" → True; "Python" → False; "   " → False; "arara!" → False.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Defina a normalização antes de testar a simetria.

</details>
