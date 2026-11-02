# Nomes e notas em pares

**Nível:** Consolidação · **Referência:** slides 31 da aula desta pasta.

## Desafio

Implemente parear(nomes, notas), retornando list(zip(nomes, notas)). Implemente cadastro(nomes, notas), retornando um dicionário construído desses pares; os nomes serão únicos. Teste tamanhos diferentes e explique quais dados deixam de aparecer. Não preencha valores ausentes.

## Casos para conferir

["Ana","Rui"], [8,6] → [("Ana",8),("Rui",6)] e {"Ana":8,"Rui":6}. ["Ana","Rui"], [8] → [("Ana",8)] e {"Ana":8}. [], [8] → [] e {}.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Por padrão, zip encerra quando a menor entrada termina.

</details>
