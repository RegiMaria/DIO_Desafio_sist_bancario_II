**DESAFIO "Otimizando sistema bancário com funções Python" do curso"Potência Tech power by iFood| Ciência de Dados **

Objetivo:

1.Criar um programa 'sistema bancário' com:

2.saque, deposito,extrato e sair.

3.Separar em funções: saque, deposito, extrato. 
Crias duas funções novas: cadastrar usuário e cadastrar conta bancária.

4.Saque: A função saque deve conter argumentos nomeados.

5.Depósito: deve receber argumentos por posição: saldo, valor, extrato.

6.Função extrato: argumento por posição e nomeado. 

7.A função Criar usuário: com nome, data de nascimento, cpf e endereço. 

8.A função conta corrente O programa deve armazenar contas uma lista composta por: agencia, numero da conta e usuário.
O numero da conta é sequencial, iniciando em 1. O numero da agencia é fixo: "0001". 

- `cadastrar_usuario`: Sem argumentos.
- `cadastrar_conta_corrente`: Argumentos por posição (`usuarios` e `contas`).
- `saque`: Argumentos nomeados (`saldo`, `valor`, `extrato`, `numero_saques`, `limite_saques`).
- `deposito`: Argumentos por posição (`saldo`, `valor`, `extrato`).
- `exibir_extrato`: Argumento por posição (`saldo`) e argumento nomeado (`extrato`).

Obs:
O objetivo 8 ainda não foi atendido, também ainda não foi atendido a criação do vínculo do usuário (pelo cpf) a uma conta corrente, a filtragem da lista de usuário, e formatação de textos (string literais) em multilinhas.