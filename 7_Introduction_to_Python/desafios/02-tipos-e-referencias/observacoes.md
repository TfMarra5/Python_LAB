# Minhas observações

## Previsão antes de executar

- O laço vai imprimir cada valor seguido do seu tipo, uma linha por valor. Não será necessário digitar uma entrada.

## Casos conferidos e resultados

- Com `a = 41`, a saída é:
  - `41 <class 'int'>`
  - `3.5 <class 'float'>`
  - `True <class 'bool'>`
  - `42 <class 'str'>`
  - `None <class 'NoneType'>`

## Meu caso adicional

- Entrada: nenhuma. Alterar `a` de `41` para `42`.
- Resultado esperado: a primeira linha passa a ser `42 <class 'int'>`.
- Resultado obtido: conferir depois de fazer a alteração e executar novamente.

## O que aprendi e dúvidas

- `type()` mostra o tipo de um objeto. O inteiro `42` e o texto `"42"` têm tipos diferentes.
- Um laço `for` percorre cada valor da tupla.
- Ainda preciso praticar `isinstance()`, reatribuição, `id()` e `dir()`, que também aparecem no enunciado.
