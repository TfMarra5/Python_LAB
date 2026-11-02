# Busca de nomes

**Nível:** Fundamentos · **Referência:** slides 11–12 da aula desta pasta.

## Desafio

Crie texto="global" no módulo, uma função externa com texto="externo" e uma função interna com texto="local" que o imprime. Chame a interna pela externa. Preveja e execute; depois remova somente a atribuição local, execute; por fim remova também a atribuição na externa, execute. Em observacoes.md explique L, E, G e B e por que chamar uma variável de len atrapalharia len("abc").

## Casos para conferir

Versão original → local. Sem atribuição na interna → externo. Sem as duas atribuições internas → global. Não remova a atribuição do módulo.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

O Python procura o nome no escopo mais próximo antes de subir.

</details>
