# 🏦 Sistema Bancário em Python

Este projeto foi desenvolvido como parte de um desafio de Bootcamp que estou realizando pela DIO em parceria com a LuizaLabs utilizando linguagem Python.  
O objetivo foi criar um **sistema bancário simples**, utilizando funções, boas práticas de código e manipulação de listas para armazenar **clientes** e **contas bancárias**.

---

## 💻 Funcionalidades Implementadas

- **Depósito**
- **Saque**
- **Extrato**
- **Cadastro de Usuário (Cliente)**
- **Cadastro de Conta Bancária**

Além disso, foram aplicadas boas práticas como:
- Uso de **parâmetros position-only e keyword-only**
- Controle de limite de saques diários
- Armazenamento de dados em listas
- Validação para evitar CPFs duplicados

---

## 🔧 Regras Exigidas no Desafio

| Função | Regras | Retorno |
|-------|--------|---------|
| Depósito| Deve receber argumentos **apenas por posição** | Novo saldo e extrato |
| Saque| Deve receber argumentos **apenas por nome (keyword-only)** | Novo saldo, extrato e número de saques |
| Extrato| Deve receber **saldo por posição** e **extrato por nome** | Apenas exibição |
| Cadastrar Usuário | Armazena nome, data de nascimento, endereço e CPF | Usuário é inserido na lista |
| Cadastrar Conta Bancária | Número da conta é sequencial, agência fixa `0001`, vinculada a um usuário | Conta adicionada na lista |

---

