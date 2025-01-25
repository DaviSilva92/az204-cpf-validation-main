import re

def validar_cpf(cpf):
    def calcular_dv(cpf, peso):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf[:9], peso))
        dv = (soma * 10) % 11
        return 0 if dv == 10 else dv

    # Primeiro dígito
    primeiro_dv = calcular_dv(cpf, [10, 9, 8, 7, 6, 5, 4, 3, 2])
    if int(cpf[9]) != primeiro_dv:
        return False

    # Segundo dígito
    segundo_dv = calcular_dv(cpf, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2])
    if int(cpf[10]) != segundo_dv:
        return False

    return True