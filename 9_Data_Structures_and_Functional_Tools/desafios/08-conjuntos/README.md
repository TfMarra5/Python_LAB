# Quem participa de quais cursos?

**Nível:** Prática · **Referência:** slides 5, 18–22 da aula desta pasta.

## Desafio

Use python={"Ana","Bia","Caio"} e c={"Bia","Davi"}. Calcule união, interseção, só Python, só C e diferença simétrica. Crie também um conjunto a partir de ["Ana","Ana","Bia"]. Não use índices em sets. Repita com um conjunto vazio criado por set().

## Casos para conferir

União: Ana,Bia,Caio,Davi; interseção: Bia; só Python: Ana,Caio; só C: Davi; simétrica: Ana,Caio,Davi. Duplicatas → Ana,Bia. Interseção com vazio → vazio; união com vazio mantém o conjunto. A ordem impressa não faz parte da resposta.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Os operadores são |, &, -, ^. {} cria um dicionário vazio.

</details>
