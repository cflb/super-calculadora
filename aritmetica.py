""" Modulo de funcoes aritmeticas """

def soma(v1,v2):
    """ A funcao soma recebe dois argumentos e retorna
    a soma dos mesmos """
    return v1+v2


def divisao(v1,v2):
    """a função de divisão recebe dois argumentos e retorna a divisão dos mesmo"""
    if v2==0:
        print ("Isso é um erro matematico não posso dividir por 0")
    else:
        return v1/v2