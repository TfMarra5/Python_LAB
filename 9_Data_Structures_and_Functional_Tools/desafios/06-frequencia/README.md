# Contador de palavras

**Nível:** Prática · **Referência:** slides 14–15, 25 da aula desta pasta.

## Desafio

Implemente frequencias(texto). Separe por espaços em branco com split(), mantendo maiúsculas e pontuação; retorne um dicionário palavra → quantidade. Use get para acumular. Texto vazio resulta em dicionário vazio.

## Casos para conferir

"python e python" → {"python":2,"e":1}; "Oi oi Oi" → {"Oi":2,"oi":1}; "  " → {}; "oi oi!" → {"oi":1,"oi!":1}.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Uma palavra ainda ausente pode começar com contagem zero.

</details>
