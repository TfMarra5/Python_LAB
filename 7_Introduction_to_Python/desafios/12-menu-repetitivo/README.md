# Calculadora com menu

**Nível:** Consolidação · **Referência:** slides 16–26 da aula desta pasta.

## Desafio

Repita um menu: 1 somar, 2 dividir, 0 sair. Leia a opção como texto. Nas opções 1 e 2, leia dois números com float. Na divisão por zero, mostre "Divisão inválida" e retorne ao menu. Para opção desconhecida, mostre "Opção inválida" sem pedir números. Não use funções próprias. Assuma que entradas numéricas são válidas.

## Casos para conferir

1, 2, 3, 0 → resultado 5.0 e encerra. 2, 7, 2, 0 → 3.5. 2, 7, 0, 0 → Divisão inválida e encerra. 9, 0 → Opção inválida sem pedir operandos.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

O while representa a sessão; cada ramo trata uma opção.

</details>
