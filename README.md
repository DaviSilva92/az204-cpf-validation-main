# az204-cpf-validation-main
az204-cpf-validation-main


# Microsserviço de Validação de CPF com Azure Functions

Este projeto cria um microsserviço serverless para validação de CPF usando **Azure Functions** com **Python**.

## Descrição

O microsserviço valida um CPF recebido via uma requisição HTTP POST. A validação verifica se o CPF é composto apenas por números, se não é um CPF conhecido como inválido, e se os dois dígitos verificadores estão corretos.

## Tecnologias Usadas

- **Azure Functions**: Plataforma serverless para rodar funções em resposta a eventos.
- **Python**: Linguagem de programação para implementar a lógica de validação de CPF.
- **HTTP Trigger**: A função é acionada por requisições HTTP.

## Como Usar

1. **Implantar no Azure**:
   - Crie uma **Function App** no portal Azure.
   - Crie uma função do tipo **HTTP Trigger** com o runtime **Python**.
   - Suba o código da função (arquivo `__init__.py` e `validar_cpf.py`).

2. **Testar a Função**:
   - Após a implantação, obtenha o URL da função.
   - Realize uma requisição HTTP POST para a URL da função com o CPF no corpo da requisição.

   Exemplo de requisição cURL:

   ```bash
   curl -X POST https://<seu-app>.azurewebsites.net/api/<sua-funcao> \
       -H "Content-Type: application/json" \
       -d '{"cpf": "12345678909"}'
