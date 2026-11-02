# Python Lab — aulas 7, 8 e 9

Trilha de prática em português, no formato do [C_LAB](https://github.com/TfMarra5/C_LAB): uma pasta por aula, desafios com enunciados, arquivos para implementar, pistas e registro de progresso.

## Comece aqui

| Aula | Conteúdo | Atividades |
|---|---|---|
| [7 — Introdução](7_Introduction_to_Python/README.md) | Tipos, referências, operadores, entrada/saída, condições e laços | 12 desafios + caixa da cantina |
| [8 — Funções e strings](8_Functions_and_Strings/README.md) | Parâmetros, escopo, slicing, métodos e iteração | 12 desafios + oficina de textos |
| [9 — Estruturas e ferramentas funcionais](9_Data_Structures_and_Functional_Tools/README.md) | Listas, tuplas, dicionários, sets, comprehensions, map/filter/zip | 12 desafios + painel da turma + bônus Pandas |

**36 desafios, 3 projetos e 1 bônus opcional.** Os arquivos main.py são pontos de partida sem respostas. Cada desafio tem casos esperados para conferência manual; não há corretor automático.

## Como praticar

1. Leia as [observações sobre os slides](docs/observacoes-sobre-slides.md).
2. Faça as aulas na ordem 7 → 8 → 9 e os desafios na ordem numérica.
3. Abra README.md de um desafio e escreva sua resposta no main.py ao lado.
4. Execute um arquivo por vez. Confira todos os casos e registre dúvidas em observacoes.md.
5. Marque progresso.md da aula e, ao terminar os 12 desafios, faça o projeto.

Para quem já estudou C: tente os primeiros desafios como diagnóstico, mas dê atenção à divisão //, às referências, à mutabilidade e ao retorno de funções em Python.

## Executar

Requer Python 3. Abra esta pasta no editor e use o terminal:

```powershell
python --version
python 7_Introduction_to_Python/desafios/01-primeiro-programa/main.py
```

No Windows, se `python` não estiver disponível, tente `py`. Executar um ponto de partida sem implementação não produz saída. O bônus tem instruções próprias para instalar Pandas; nada foi instalado por este pacote.

Salve em UTF-8, use quatro espaços na indentação, nomes claros e comentários que expliquem decisões. Nos exercícios com entrada numérica, assuma o tipo informado no enunciado; tratamento de texto não numérico com exceções não faz parte destas aulas. Casos de domínio inválido explicitamente pedidos, como divisor zero, precisam ser tratados.

## Quando considerar concluído

- Todos os casos do enunciado foram conferidos.
- Você testou um caso adicional, incluindo um limite quando aplicável.
- Você consegue explicar a lógica e adaptar os dados sem copiar uma solução.
- Funções devolvem o tipo e valor pedidos; entradas que devem ser preservadas continuam iguais.

Para revisão, envie o enunciado, seu código, a entrada usada e a saída obtida. Sugestão de rotina: tentativa → pista → nova tentativa → revisão.

## Organização e fontes

Cada aula contém desafios/, projetos/ e progresso.md. As atividades são independentes: arquivos de solução de uma atividade não precisam importar arquivos de outra.

Consulte [fontes.md](docs/fontes.md) para identificar os materiais usados. Os slides originais não estão incluídos. Este pacote foi criado localmente, sem publicar ou alterar o C_LAB. Se quiser versionar depois, faça um commit por atividade concluída.

