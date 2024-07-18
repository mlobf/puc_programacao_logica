"""
( )Tenho que criar uma funcao que peça ao usuario para informar o mes desejado;
jan a dez e
    que me retorne o mes escolhido.
    -Tenho que validar o input do usuario.
( )Criar um funcao que valide o mes informado - dentro de um range do mes 1 ao
mes 12, esse valor tem que ser convertido em um integer.
"""


def valida_mes(mes: int) -> bool:
    """Valida se o mes informado é um mes que esta de jan a dez"""
    if mes in range(1, 13):
        return True
    else:
        return False


def valida_int(elemento: int) -> bool:
    """Valida se o parametro é do tipo int"""
    if isinstance(elemento, int) and not isinstance(elemento, bool):
        return True
    else:
        return False
