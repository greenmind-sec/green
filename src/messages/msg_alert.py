import GreenLib

msg_menu = '''

Green Basic Commands
=============

    Command                 Description
    -------                 -----------
    greenrecon              Start recon


Green Encryption Module
=============

    Command                 Description
    -------                 -----------
    encrypt_base64          Encrypt Base64
    decrypt_base64          Decrypt Base64
    encrypt_md5             Encrypt MD5
    encrypt_sha1            Encrypt Sha1
    encrypt_sha256          Encrypt Sha256
    encrypt_sha512          Encrypt Sha512


Core Commands
=============

    Command                 Description
    -------                 -----------
    ?                       Help menu
    exit                    Exit the console
    help                    Help menu
    version                 Show the version numbers


Brute Force Commands
========================

    Command                 Description
    -------                 -----------
    bruteforce_linux        Brute force attack on a Linux password
    bruteforce_windows_nt   Brute force attack on Windows NT
    bruteforce_windows_lm   Brute force attack on Windows LM


System Backend Commands
============================

    Command                 Description
    -------                 -----------
    reverse_shell           Reverse shell using netcat
    pwd                     Current directory
    ls                      List dir
    help                    Menu help
    exit                    Green exit program


'''


msg_server = '''
    [ ON ] - Server
'''


# MENSAGENS para o usuario
msg_insira_porta = "Insira a porta: "
msg_rodando_porta = "Rodando na porta :"
## MSG Brute Force Linux
msg_brute_force_salt = "Insira o SALT :"
msg_brute_force_hash = "Insira o HASH :"
msg_brute_force_completa = "Insira a lista completa :"
msg_brute_force_senha_encontrada = "Senha encontrada :"
# MENSAGENS erro
msg_ocorreu_erro = "Ocorreu um erro: "
# MENSAGENS alertas
msg_alerta_aguarde3segundos = "Aguarde 3 segundos"

msg_erro_key_whatcms="Erro Key WhatCMS"
msg_erro_key_shodan="Erro Key Shodan"
