# Painel da turma

**Nível:** Projeto integrador · **Referência:** slides 3–36 da aula desta pasta.

## Desafio

Use alunos={"Ana":[8,10],"Rui":[5,6],"Bia":[],"Caio":[6,6]}. Implemente medias(alunos), retornando nome → média (None para notas vazias); aprovados(alunos), retornando um set de nomes com média >=6; e ranking(alunos), retornando uma lista de tuplas (nome,média) em ordem decrescente de média, excluindo alunos sem notas e ordenando nomes crescentemente em empates. Use sorted com key para o ranking: key recebe uma função que calcula a chave de ordenação. Crie também o set de alunos sem notas. Preserve a entrada. Use pelo menos uma comprehension e uma função lambda.

## Casos para conferir

Médias: Ana 9.0, Rui 5.5, Bia None, Caio 6.0. Aprovados: Ana e Caio. Sem notas: Bia. Ranking: [("Ana",9.0),("Caio",6.0),("Rui",5.5)]. Para {}: {}, set(), [], set(). Para {"Zoe":[7],"Eva":[7]}: ranking Eva antes de Zoe.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Uma chave em tupla permite combinar prioridade por nota e desempate por nome. sorted/key é a pequena extensão deste projeto.

</details>
