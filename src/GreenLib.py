#!/usr/bin/python3
# -*- coding: utf-8 -*-

#title           :GreenLib.py
#description     :Este arquivo tem como meta ser a LIB principal de conexão do projeto Green
#author          :GreenMind (GreenMindLabs)
#date            :04 Agosto 2018
#version         :0.3DEV

#=======================================================================
#Modulos
import sys, os ,time, subprocess,random

#Mensagens
sys.path.insert(0, 'messages')
import msg_control
import msg_logo
import msg_alert


#
sys.path.insert(0, 'core')
import core_menu
import core_cripto
import core_recon

menu_actions  = {}
# =======================
# FUNÇÕES MENUS
# =======================

def set_armor():
    print(msg_control.msg_set)
    core_menu.espera()

def version():
    VERSION = "v0.3.1DEV"
    print(VERSION)
    core_menu.espera()

# DEFINIÇÃO DE MENUS
menu_actions = {
    'main_menu': core_menu.main_menu,
    'cripto_main_menu': core_menu.cripto_main_menu,
    # Chamar um menu HELP causa um erro!
    # Para resolver não vamos setar para sempre chamar main_menu
    #'main_menu': help,

    'cripto': core_cripto.cripto,
    'set': set_armor,
    'voltar': core_menu.back,
    'exit': core_menu.exit,
    'version': version,
}

if __name__ == "__main__":

    #Menu principaç
    main_menu()
