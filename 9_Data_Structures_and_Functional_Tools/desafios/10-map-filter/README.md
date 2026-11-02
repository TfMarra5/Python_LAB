# Transformar e selecionar

**Nível:** Consolidação · **Referência:** slides 28–30 da aula desta pasta.

## Desafio

Dada uma lista de temperaturas Celsius, obtenha com map e lambda uma lista Fahrenheit pela fórmula C*9/5+32. Separadamente, use filter e lambda sobre a lista original para obter apenas temperaturas abaixo de zero. Materialize os dois resultados em listas. Não use laços ou comprehensions nesta atividade.

## Casos para conferir

[-10,0,20] → Fahrenheit [14.0,32.0,68.0], negativas [-10]. [0] → [32.0], []. [] → [], [].

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

lambda recebe um valor. map transforma; filter decide quais valores conservar.

</details>
