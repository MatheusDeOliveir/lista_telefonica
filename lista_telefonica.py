from funcoes_lista_telefonica import *


while True:
    print ("Lista Telefônica   \n\n\n")
    ESCOLHAS_1 = ['1', '2', '3']
    
    escolha = input("Menu\n\n [1] - Adicionar Contato\n\n [2] - Remover contato\n\n [3] - Listar Contatos\n\n")
    
    if (not escolha.isdigit()) | (escolha not in ESCOLHAS_1):
        print ("Entrada inválida")
        time.sleep(3)
        os.system("cls")
        continue
    elif escolha == '1':
        os.system('cls')
        contatos.update(add_cont())
        time.sleep(3)
        os.system("cls")   
        continue    
    elif escolha == '2':
        os.system('cls')
        remover_contato(contatos)
        time.sleep(3)
        os.system("cls") 
        continue
    elif escolha == '3':
        os.system('cls')
        listar_contatos(contatos)
        time.sleep(3)
        os.system("cls") 
        continue