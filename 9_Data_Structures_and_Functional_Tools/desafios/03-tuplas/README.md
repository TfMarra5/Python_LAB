# Coordenadas fixas

**Nível:** Fundamentos · **Referência:** slides 4, 9 da aula desta pasta.

## Desafio

Implemente distancia_quadrada(ponto_a, ponto_b), recebendo duas tuplas de duas coordenadas numéricas e retornando (diferença em x)² + (diferença em y)². Não modifique as tuplas. Explique por que ponto_a[0] = 0 não funciona, sem deixar essa linha ativa.

## Casos para conferir

(0,0) e (3,4) → 25; (2,2) e (2,2) → 0; (-1,-2) e (2,2) → 25.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Use índices ou desempacotamento; não precisa calcular raiz quadrada.

</details>
