# Contador e escopo

**Nível:** Fundamentos · **Referência:** slides 7–10 da aula desta pasta.

## Desafio

Parte A: defina contador=10 no módulo e uma função demonstrar() com uma variável local contador=3; imprima o contador dentro e fora da função. Parte B: crie incrementar_global() que use global e incremente o contador do módulo. Parte C: implemente incrementar(valor), retornando valor+1 sem global. Registre a diferença.

## Casos para conferir

A: dentro 3, fora 10. B: duas chamadas levam o contador global de 10 a 12. C: incrementar(12) retorna 13, mas não altera sozinho o contador global, que continua 12.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Ter o mesmo nome não significa estar no mesmo escopo.

</details>
