class CPF():
    def validar_cpf(cpf: str): 
        '''limpando o cpf para deixar apenas os dígitos:'''
        cpf_tratado = cpf.replace(".","").replace("-","").replace(" ", "") 
        if(len(cpf_tratado) != 11):
            print("CPF inválido")

        primeiro_digito = 0
        segundo_digito = 0

        '''aplicando condições de validação do cpf:'''

        for i in range(0,9):
            primeiro_digito += int(cpf_tratado[i]) * (10 - i)
        primeiro_digito = (primeiro_digito * 10) % 11

        if(primeiro_digito > 9):
            primeiro_digito = 0

        for i in range(0,9):
            segundo_digito += int(cpf_tratado[i]) * (11 - i)
        segundo_digito += primeiro_digito * 2
        segundo_digito = (segundo_digito * 10) % 11

        if(segundo_digito > 9):
            segundo_digito = 0

        '''validação final: se os dígitos finais do cpf são iguais aos''' 
        '''dígitos calculados pelo verificador:'''

        if(int(cpf_tratado[-1]) != segundo_digito or int(cpf_tratado[-2]) != primeiro_digito):
            return False
        return True

if True:
    print('CPF válido')
elif False:
    print('CPF inválido')

    # teste: print(validar_cpf('112 605.824-69'))
    cpf = str(input('Digite seu CPF: '))
    print(validar_cpf(cpf))

