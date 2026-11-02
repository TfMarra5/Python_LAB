# Trocar a inicial

**Nível:** Prática · **Referência:** slides 15–17 da aula desta pasta.

## Desafio

Implemente trocar_inicial(texto, nova), retornando uma nova string com a primeira posição substituída. nova sempre terá exatamente um caractere. Se texto for vazio, retorne nova. Preserve a variável original e mostre os dois valores depois da chamada.

## Casos para conferir

trocar_inicial("gato", "p") → "pato", original "gato". trocar_inicial("a", "b") → "b". trocar_inicial("", "X") → "X".

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Não atribua a texto[0]; combine a nova inicial com um recorte.

</details>
