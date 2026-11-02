# Perfil em dicionário

**Nível:** Prática · **Referência:** slides 6, 14–15 da aula desta pasta.

## Desafio

Crie {"nome":"Ana", "idade":20}. Consulte cidade com get e padrão "Não informada". Atualize idade para 21 e inclua cidade="Riga" com update. Percorra items e imprima cada chave e valor. Remova cidade com pop, guardando o valor removido. Mostre keys e values convertidos em listas e, por fim, limpe o cadastro com clear.

## Casos para conferir

Consulta inicial → Não informada. Após update → nome Ana, idade 21, cidade Riga. pop → Riga. Antes de clear, chaves ["nome","idade"] e valores ["Ana",21]. Depois → {}.

Os exemplos descrevem resultados, não um código de solução. Quando não houver formato exato, rótulos de saída são livres. Em funções, confira o valor retornado e o tipo, além do que aparece no terminal.

## Sua entrega

1. Implemente em [main.py](main.py).
2. Antes de executar, anote suas previsões em [observacoes.md](observacoes.md).
3. Confira todos os casos acima e acrescente um caso seu.
4. Explique sua escolha de variáveis e operações.

Na pasta desta atividade, execute `python main.py` (ou `py main.py` no Windows).

<details>
<summary>Pista — abra depois de tentar</summary>

Dicionários atuais preservam a ordem de inserção; valores são acessados pela chave.

</details>
