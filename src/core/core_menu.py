import subprocess,sys,random

import GreenLib

#Mensagens
sys.path.insert(0, 'messages')
import msg_control
import msg_logo

sys.path.insert(0, 'core')
import core_cripto
import core_recon
import core_menu

#--
# Função Menu principal
#--
def main_menu():
    subprocess.run(["clear"])
    logos = [msg_logo.msg_logo1,msg_logo.msg_logo2,msg_logo.msg_logo3]
    print(random.choice(logos))
    print(msg_control.msg_menu)
    choice = input(" >> ")
    exec_menu(choice)
    return

def cripto_main_menu():
    subprocess.run(["clear"])
    logos = [msg_logo.msg_logo1,msg_logo.msg_logo2,msg_logo.msg_logo3]
    print(random.choice(logos))
    print(msg_control.msg_cripto)
    choice = input(" >> ")
    exec_menu(choice)
    return

def recon_main_menu():
    subprocess.run(["clear"])
    logos = [msg_logo.msg_logo1,msg_logo.msg_logo2,msg_logo.msg_logo3]
    print(random.choice(logos))
    print(msg_control.msg_cripto)
    choice = input(" >> ")
    exec_menu(choice)
    return

#--
# Função executa menu
#--
def exec_menu(choice):
    subprocess.run(["clear"])
    # TODO
    # Deixa a escolha em letra minuscula
    # Foi comentado devida as strings com as hashs criptografadas com maiusculas
    #ch = choice.lower()
    ch = choice

    # Filtra por (Espaço , numeros e vazio)
    retorno_filtro = filtra_entrada(ch)
    # Caso tenha algum erro vai ser direcionado para a pagina principal
    if (retorno_filtro != True):
        exec_menu('main_menu')
    else:
        try:
            # Cria uma lista com o que foi digitado
            entrada_de_dados = [str(x) for x in ch.split()]
            # Caso o tamanho seja de 1 a escolha vai para a função menu_actions
            # para redirecionar para uma função
            if(len(entrada_de_dados) == 1):
                GreenLib.menu_actions[ch]()
            #Caso a entrada for menor que 1 ou maior que 3 por ter algo errado
            #Ja que por enquanto o maximo é de 3 (cripto reverse "54321")
            #Se for maior que 3 vamos alterar
            elif(len(entrada_de_dados) <= 1) or (len(entrada_de_dados) > 3):
                exec_menu('main_menu')

            #Se for igual a 3 argumentos vamos enviar para a função navega_green
            elif(len(entrada_de_dados) == 3):
                navega_green(entrada_de_dados[0],entrada_de_dados[1],entrada_de_dados[2])
            else:
                #
                # AQUI CHAMA MENU COM MULTIPLAS ESCOLHAS USANDO A LISTA CRIADA
                #
                navega_green(entrada_de_dados[0],entrada_de_dados[1],entrada_de_dados[2])
        # Caso de algum erro vai ser retornado a mensagem avisando.
        except KeyError:
            print ("Invalid selection, please try again.\n")
            exec_menu('main_menu')
        return

# Exit program
def exit():
    subprocess.run(["clear"])
    print("O "+sys.argv[0]+" foi finalizado com segurança!")
    sys.exit()

# Back Menu
# TODO Implementar ele
def back():
    GreenLib.exec_menu('main_menu')

def espera():
    print("Aperte um botao para continua...")
    go = input(">")
    exec_menu('main_menu')


def filtra_entrada(ch):
    #Checa se tem apenas numeros
    if(ch.isdigit() == True):
        return False
    #Checa se tem espaços
    elif(ch.isspace() == True):
        return False
    #Checa se esta vazio
    elif(ch == ''):
        return False
    else:
        return True

# Navegar
def navega_green(escolha,sub_escolha,key):
    if (escolha == "search") or (escolha.upper() == "SEARCH"):
        print("Função search")
        time.sleep(4)
    elif (escolha == "set") or (escolha.upper() == "SET"):
        print("Função set")
        time.sleep(4)
    elif (escolha == "cripto") or (escolha.upper() == "CRIPTO"):
        teste_cripto = core_cripto.Cripto(sub_escolha,key)
        teste_cripto.greenCripto(sub_escolha,key)
        espera()
    elif (escolha == "greenrecon") or (escolha.upper() == "GREENRECON"):
        teste_cripto = core_recon.Recon(sub_escolha,key)
        teste_cripto.greenScan()
        espera()

    elif (escolha == "reverseshell") or (escolha.upper() == "REVERSESHELL"):
        print("Sub Escolha:"+sub_escolha)
        print("Key:"+key)
        server = core_reverseshell.MultiServer()
        server.print_help()
        server.start_turtle()

    else:
        GreenLib.menu_actions['main_menu']()
