# Limpeza de uma frase

**Nível:** Prática · **Referência:** slides 18–19 da aula desta pasta.

## Desafio

Implemente normalizar_espacos(texto), removendo espaços no início e fim e reduzindo qualquer sequência de espaços, tabs ou quebras de linha a um único espaço. Use split sem separador e join. Não altere maiúsculas ou pontuação.

## Casos para conferir

"  Eu   estudo Python  " → "Eu estudo Python"; "A	B
C" → "A B C"; "   " → "".

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

split() sem argumento tem comportamento diferente de split(" ").

</details>
