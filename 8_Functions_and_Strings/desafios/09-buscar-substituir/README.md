# Editor de palavras

**Nível:** Consolidação · **Referência:** slides 20 da aula desta pasta.

## Desafio

Implemente primeira_posicao(texto, trecho) com find e substituir(texto, antigo, novo) com replace. A busca deve distinguir maiúsculas de minúsculas; trecho e antigo serão não vazios. A substituição troca todas as ocorrências não sobrepostas e devolve uma nova string.

## Casos para conferir

primeira_posicao("banana", "na") → 2; primeira_posicao("Python", "py") → -1. substituir("Java e Java", "Java", "Python") → "Python e Python". substituir("abc", "x", "y") → "abc".

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Uma busca que retorna zero encontrou algo na primeira posição; -1 significa ausência.

</details>
