import os
import time
CONTATOS = {}



def add_cont(dict={}):
    
    
    while True:
        print ("Digite o nome do contato: \n")
        nome = input ("")
        
        if not nome.isidentifier():
            print ("Digite um nome válido. \n\n")
            time.sleep(3)
            os.system('cls')
            continue
        
        print ("Nome registrado!\n\n")
        time.sleep(3)
        os.system('cls')
        break
    
    
    
    while True:
        print ("Digite o número para contato: \n")
        num = input("")
        if num.isnumeric() is not True and len(num) == 11:
            print ("Digite um contato válido")
            time.sleep(3)
            os.system('cls')
            continue
        
        
        print ("Número registrado !\n\n")
        dict.update({nome:num})
        time.sleep(3)
        os.system('cls')
        
        break
    return dict
    
    
def remover_contato(dict=CONTATOS):
    
    while True:
        for nome, numero in (CONTATOS.items()):
            print (f"{nome} -- ({(numero[0:2])}) - {numero[2:7]}.{numero[7:11]} \n")
            
            
        cont_exc = input("Que contato deseja excluir? \n\n")
        print ("\n\n")
        
        
        
        
        if not cont_exc.isidentifier():
            print ("Digite um contato válido")
            time.sleep(3)
            os.system('cls')
            continue
        elif CONTATOS.get(cont_exc.capitalize()) is None:
            print ("O Contato informado não consta no banco de dados. \n\n")
            time.sleep(3)
            os.system('cls')
            continue
        else:
            del(CONTATOS[cont_exc.capitalize()])
            print (f"O contato {cont_exc} foi deletado com sucesso. \n")
            time.sleep(3)
            os.system('cls')

        
        
        while True:
            ESCOLHAS = ['1', '2']
            print ("Deseja excluir outro contato? \n\n [1] - Sim \n\n [2] - não")
            outr_contato = input ("")
            if (not outr_contato.isdigit()) | (outr_contato not in ESCOLHAS):
                print ("Entrada inválida")
            elif outr_contato == '1':
                break
            elif outr_contato == '2':
                print ('retornando ao menu!\n\n')
                return None
            
            
def listar_contatos(dict=CONTATOS):
    
    for nome, numero in (CONTATOS.items()):
        print (f"{nome} -- ({(numero[0:2])}) - {numero[2:7]}.{numero[7:11]} \n")
        
    while True:
        ESCOLHAS = ['1', '2']
        print ("Deseja retornar ao menu principal? \n\n [1] - Sim \n\n [2] - não")
        escolha = input ("")
        if (not escolha.isdigit()) | (escolha not in ESCOLHAS):
            print ("Entrada inválida")
            time.sleep(3)
            os.system("cls")
            continue
        elif escolha == '1':
            print ('retornando ao menu!\n\n')
            time.sleep(3)
            os.system("cls")
            return None
        elif escolha == '2':
            os.system("cls")
            continue
        
        
        
