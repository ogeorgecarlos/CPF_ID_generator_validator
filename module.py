from time import sleep
from random import randint

def input_validator(cpf):
    while True:
        '''Checks if the input receveid the correct data: Only numbers, min 9 digits and max 11 digits.'''

        if cpf.isnumeric()==True and len(cpf)>=9 and len(cpf)<=11: #checks if the input is correct
            print('Verifying CPF...')
            sleep(1)
            break
        elif cpf.isnumeric()==False: #checks if the input has only numbers
            print('Just type nubers.')
        elif cpf.isnumeric()==True and len(cpf)<9: #checks if the input has minimum of 9 digits
            print('Enter at least 9 digits.')
        elif cpf.isnumeric()==True and len(cpf)>11: #checks if the input has maximun of 11 digits
            print('enter a maximum of 11 digits and a minimum of 9 digits. ')
    return cpf

def get_nine_digits(cpf):
    '''Isolates the first nine digits of the informad cpf'''

    nine_digits = '' #variable will get the first nine digits entered by the user.
    counter = 0 #counter to make sure that only the first nine digits will be taken.
    for num in list(cpf):
        counter += 1
        if counter > 9: #when the counter reach '9', this is function will be interrupted
            break
        else:
            nine_digits += num 
    return nine_digits

def cpf_generator(nine_digits):
    '''From the first nine digits entered by the user, this function uses the logical algorithm to generate the last two checker digits'''

    digit_to_verify = 0 #counter to check witch check digit is being calculated    
    while True:
        digit_to_verify  += 1
        sum_nine_digits = 0 #sum of digits as part of the logical algorithm

        if digit_to_verify == 1:
            counter = 11 #counter user as multiplier of the digits obtained, when these are 9 in total.
        else:
            counter = 12 #counter user as multiplier of the digits obtained, when these are 10 in total.
        
        for number  in nine_digits:
            counter -= 1
            sum_nine_digits += (int(number)*counter)

        if digit_to_verify  == 1:
            if sum_nine_digits%11 < 2:
                digit_1= '0'
                nine_digits += digit_1
            else:
                digit_1 = str((11-(sum_nine_digits%11)))
                nine_digits += digit_1

        if digit_to_verify  == 2:
            if sum_nine_digits%11 < 2:
                digit_2='0'
                break
            else:
                digit_2 = str((11-(sum_nine_digits%11)))
                break
              
    nine_digits += digit_2
    return nine_digits #in this return, the cariable 'nine_digits' will be 11 digits in total (the initial nine digits plus the last 2 digits obtained through the logical algorithm executed.)

def cpf_validator(cpf):
    '''checks if the typed cpf is equal to the Cpf generetad by the algorithm from the first nine digits '''

    first_nine_digits = get_nine_digits(cpf)
    cpf_checked = cpf_generator(first_nine_digits)
    if cpf == cpf_checked:
        cpf_situation = 'Cpf is valid.'
    else:
        cpf_situation = 'Cpf is invalid.'
    return cpf_situation


functions_avaliable = ['Validar CPf', 'Gerar CPF', 'Sair']

def menu():
    for index, value in enumerate(functions_avaliable):
        print(index,') ',value)

def header(texto):
    print(35*'-')
    print(f'{texto:^35}')
    print(35*'-')
    print()

def validator_cpf():
    cpf=input('Digite cpf: ')
    validator_input =input_validator(cpf)
    return cpf_validator(validator_input)

def cpf_creator():
        number_of_cpf = input("Quantos cpf's deseja gerar?\n")
        cpf_list = []
        counter = 1
        while counter <= int(number_of_cpf):
            cpf = str(randint(111111111, 999999999))
            complete = cpf_generator(cpf)
            if cpf not in cpf_list:
                counter += 1
                cpf_list.append(complete)
        return cpf_list





