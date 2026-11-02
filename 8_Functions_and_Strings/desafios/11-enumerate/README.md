# Posições de um caractere

**Nível:** Consolidação · **Referência:** slides 23 da aula desta pasta.

## Desafio

Implemente mostrar_posicoes(texto, alvo), que imprime os índices de todas as ocorrências do caractere alvo, um por linha. Use enumerate; a comparação distingue maiúsculas. Se não houver ocorrências, imprima "Não encontrado". alvo terá um caractere. Esta função imprime em vez de retornar um resultado útil.

## Casos para conferir

("banana", "a") → linhas 1, 3, 5. ("Ana", "a") → 2. ("", "x") → Não encontrado. ("abc", "z") → Não encontrado.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Uma variável booleana pode registrar se apareceu pelo menos uma ocorrência.

</details>
