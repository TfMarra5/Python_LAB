# Consultar dados aninhados

**Nível:** Prática · **Referência:** slides 16–17 da aula desta pasta.

## Desafio

Use alunos={"Ana":{"notas":[8,6]}, "Rui":{"notas":[]}}. Implemente media_aluno(alunos, nome), retornando a média ou None quando o aluno não existe ou não tem notas. Implemente adicionar_nota(alunos, nome, nota): acrescente nota à lista de um aluno existente e retorne True; se não existe, retorne False sem criar cadastro. Notas serão de 0 a 10.

## Casos para conferir

Média inicial de Ana → 7.0; Rui → None; Eva → None. Adicionar 10 para Ana → True e notas [8,6,10]; nova média 8.0. Adicionar para Eva → False; Eva continua ausente.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Verifique a presença do aluno e se a lista de notas está vazia antes de dividir.

</details>
