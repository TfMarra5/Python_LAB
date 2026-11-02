# Detetive de tipos

**Nível:** Fundamentos · **Referência:** slides 9–11 da aula desta pasta.

## Desafio

Crie variáveis com os valores 42, 3.5, True, "42" e None. Imprima o valor e seu tipo. Use isinstance para investigar se 42 é int e se "42" é int. Reatribua uma variável inicialmente inteira para uma string. Use id antes e depois e registre o que observou, sem tentar prever os números. Use dir("Python") e identifique dois nomes de métodos.

## Casos para conferir

42: int; 3.5: float; True: bool; "42": str; None: NoneType. isinstance(42, int): True; isinstance("42", int): False. Os valores numéricos de id não têm saída fixa.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

type, isinstance, id e dir respondem a perguntas diferentes. A reatribuição muda a associação de um nome.

</details>
