# Observações para não levar erros dos slides aos exercícios

## Aula 7

- Slides 3–4: na implementação usual CPython existe compilação para bytecode e execução pelo interpretador; não há a etapa manual de compilação e ligação típica de C. Arquivos .pyc podem ser criados ao importar módulos; executar um script não garante um .pyc ao lado dele.
- Slide 8: strings entre aspas triplas são literais de string, não comentários de bloco. Em posições específicas são docstrings. Para comentários comuns, use #.
- Slide 10: id identifica um objeto durante seu tempo de vida; não use seus números como resultados esperados nem como endereço portátil de memória.
- Slide 18: use aspas retas válidas no código, como sep="" e end="!". Aspas tipográficas copiadas dos slides podem causar erro.

## Aula 8

- Slide 16: para word="Programming", word[::2] resulta em "Pormig". O resultado "Progra" mostrado no slide não corresponde a esse slice.
- Slides 7–12: a busca por nomes segue os escopos. Atribuir a um nome dentro de uma função normalmente o torna local; global refere-se ao nome no módulo, não a todas as variáveis de todos os arquivos.
- Slide 25: a docstring de uma função é a string que aparece como primeira instrução no corpo da função. Aspas triplas, por si só, não tornam qualquer string uma docstring.

## Aula 9

- Slide 12: um slice de lista cria uma nova lista externa, mas a cópia é superficial. Objetos mutáveis dentro dela ainda podem ser compartilhados. Os desafios iniciais usam listas de valores simples para isolar o conceito.
- Slide 14: dicionários preservam a ordem de inserção no Python 3.7 e posteriores. Sets não têm ordem de posição garantida.
- Slide 14: chaves de dicionário precisam ser hashable. Uma tupla que contém uma lista, por exemplo, não serve como chave, apesar de a tupla ser imutável.
- Slides 23–36: compreensão e estilo funcional não são sempre mais rápidos ou legíveis. Escolha considerando o problema. map e filter produzem iteradores; use list para visualizar todos os resultados. zip encerra pela menor entrada por padrão.

Nos resultados com sets, compare membros, não a ordem do texto impresso. Não confunda {} (dict vazio) com set() (set vazio).
