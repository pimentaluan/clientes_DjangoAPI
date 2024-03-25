import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    """Verifica se o CPF é valido (123.456.789-01)"""
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_valido(nome):
    return nome.isalpha()
    
def rg_valido(rg):
    return len(rg) >= 7

def celular_valido(celular):
    """Verifica se o celular é válido (83 91234-5678)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta