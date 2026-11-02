# Bônus opcional — Pandas apply

Referência: aula 9, slide 32. Esta atividade usa uma biblioteca externa; os demais desafios não precisam dela.

## Preparação

Se Pandas ainda não estiver instalado, na pasta Python_LAB execute:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install pandas
.venv\Scripts\python.exe 9_Data_Structures_and_Functional_Tools/bonus/pandas-apply/main.py
```

## Desafio

Crie um DataFrame com Name=["Ana","Rui","Bia"] e Score=[90,80,98]. Usando apply e lambda na coluna Score, crie Bonus somando 10, limitado ao máximo de 100. Preserve Score. Imprima as três colunas. Depois repita com Score=[0,100]. Não use laços.

## Resultados esperados

- Primeiro conjunto: Bonus=[100,90,100]; Score continua [90,80,98].
- Segundo conjunto, com Name=["X","Y"]: Bonus=[10,100]; Score continua [0,100].

Pista: a função passada a apply recebe uma nota de cada vez; min pode limitar o resultado.
