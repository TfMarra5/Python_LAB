# Uma lista, dois nomes

**Nível:** Consolidação · **Referência:** slides 12–15 da aula desta pasta.

## Desafio

Crie a = [1, 2] e b = a. Antes de executar b.append(3), preveja o conteúdo de a e b. Imprima os dois e compare id(a) == id(b). Em seguida crie x = "Oi" e y = x; execute y += "!" e imprima x e y. Explique a diferença em observacoes.md.

## Casos para conferir

Depois do append: a e b contêm [1, 2, 3] e a comparação de ids é True. Depois de y += "!": x é "Oi" e y é "Oi!". Não exija um número específico para id.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

append modifica a lista existente; concatenação de strings produz um valor de string diferente.

</details>
