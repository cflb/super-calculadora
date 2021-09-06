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

def velocidadeMedia (dist, t):
    """" A função de velocidade média recebe dois argumentos e retorna a velocidade
     média"""
    return dist/t 

def imc (imc, peso, altura):
    """" Função criada para calcular o índice de massa corporal de uma 
    pessoa. """

    imc = peso / (altura * altura)

    if (imc < 18.5) : 
	    print("O seu IMC é de " , imc , ",você está magro demais. ")
    elif (imc < 24.9) :
	    print("O seu IMC é de " , imc , ",você está no peso normal. ")
    elif (imc >= 24.9):
	    print("O seu IMC é de " , imc , ",você está acima do peso. ")
    elif (imc > 30):
	    print("O seu IMC é de " , imc , ",você está obeso. ")
    
    return imc
    
    