# Cópia ou apelido?

**Nível:** Fundamentos · **Referência:** slides 7–13 da aula desta pasta.

## Desafio

Crie original=[10,20,30,40], apelido=original e copia=original[:]. Faça apelido[0]=99 e copia[1:3]=[7,8,9]. Mostre as três listas e explique quais compartilham identidade. Depois, em uma nova lista [1,2,3,4,5], remova os índices 1 a 3 com atribuição de slice.

## Casos para conferir

original e apelido: [99,20,30,40]; copia: [10,7,8,9,40]. original is apelido: True; original is copia: False. Lista após remoção: [1,5].

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Slicing copia a lista externa; este exercício usa apenas números para não envolver cópia profunda.

</details>
