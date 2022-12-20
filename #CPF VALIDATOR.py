#CPF VALIDATOR
from module import *

# organizar layout
# criar funcao para cada ação
# criar laço de repetição até o usuario desejar sair
# salvar arquivo de cpf gerado
# disponibilizar arquivo para download ou envio por e-mail
# pense possibilidade de tornar CPF um objeto e quais as vatagens de fazer assim
# ver nome melhor para funcoes cpf generator e cpf creator
# criar opcao de gerar cpf por regiao
# criar opção de identificar a regiao do cpf verificado

while True:
    header('MENU')

    menu()

    action = input('\nQual função deseja executar?\n').strip().lower()

    if action == '0' or action == 'validar CPf' :
        header('Validar CPF')
        print(validator_cpf(), '\n')
    elif action == '1' or action == 'gerar cpf':
        header('Gerar CPF')
        print(cpf_creator(), '\n')
    elif action == '2' or action == 'SAIR':
        header('SAINDO...')
        break
    else:
        print('Digite uma opção válida')




    
    
