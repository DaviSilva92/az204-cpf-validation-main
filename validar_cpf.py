import json
import logging
import azure.functions as func
from validar_cpf import validar_cpf

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Recebendo requisição para validação de CPF.')

    # CPF no corpo da requisição
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Por favor, envie o CPF no formato JSON.",
            status_code=400
        )
    
    cpf = req_body.get('cpf', '').strip()

    if not cpf:
        return func.HttpResponse(
            "CPF não informado.",
            status_code=400
        )

    # Validação
    if validar_cpf(cpf):
        return func.HttpResponse(
            json.dumps({"message": f'O CPF {cpf} é válido'}),
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"message": f'O CPF {cpf} é inválido'}),
            status_code=400
        )