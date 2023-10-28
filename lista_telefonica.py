from funcoes_lista_telefonica import *


try:
        parent_dir = os.getcwd()  
        
        pasta = 'Agenda' 
        caminho = os.path.join(parent_dir, pasta)
        
        os.mkdir(caminho)
except FileExistsError:
    try:
        with open (caminho+'\Listagem.txt', encoding='UTF-8') as bd:
            ctt = bd.readlines()
        for line in ctt:
            ctt_separado = line.split('--')
            
            chars = '()-. \n'
            num = ctt_separado[1].translate(str.maketrans('','',chars)).strip()
            nom = ctt_separado[0].strip()
            contatos.update({nom:num})
            
    except FileNotFoundError:
        pass





while True:

    print ("Lista Telefônica   \n\n\n")
    ESCOLHAS_1 = ['1', '2', '3', '4']
    
    escolha = input("Menu\n\n [1] - Adicionar Contato\n\n [2] - Remover contato\n\n [3] - Listar Contatos\n\n [4] - Encerrar e salvar contatos\n\n")
    
    if (not escolha.isdigit()) | (escolha not in ESCOLHAS_1):
        print ("Entrada inválida")
        time.sleep(3)
        os.system("cls")
        continue
    elif escolha == '1':
        os.system('cls')
        contatos.update(add())
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
    elif escolha == '4':
        os.system('cls')
        gerar_listagem(contatos)
        time.sleep(3)
        os.system("cls") 
        break