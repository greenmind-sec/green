#!/usr/bin/python3
# -*- coding: utf-8 -*-

#title           :green
#description     :Este é o arquivo principal do Green
#author          :GreenMind (GreenMindLabs)
#date            :04 Agosto 2018
#usage		     :sudo green
#usage		     :sudo green -u https://greenmindlabs.com -o saida.txt
#version         :0.3DEV

VERSION = "0.3.DEV"
import os,sys

# Arquivo de configuração
import json

if os.geteuid() != 0:
    print("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
    sys.exit()
else:
    import GreenLib
    import argparse,random

    sys.path.insert(0, 'core')
    import core_menu
    import core_recon

    # Check Keys
    #TODO melhorar VERSION
    VERSION = "v0.3.1DEV"
    NAME_KEYS='keys.json'
    def key_open(NAME_KEYS,key):
        with open(NAME_KEYS) as f:
            data = json.load(f)
            if key == "shodan":
                return data['shodan']
            elif key == "whatcms":
                return data['whatcms']
            elif key == "hunter-io":
                return data['hunter-io']
            else:
                retorno = "Erro"
                return retorno

    list_options=["google-hacking","shodan-search","hostname","whois-ip","whois-url","traceroute","check_robots","archive","check_cms","sharingmyip"]
    parser = argparse.ArgumentParser(description = 'GreenMind Security Scan.')

    parser.add_argument('-t', action = 'store', dest = 'tipo', required = False,help = 'insert type.')
    parser.add_argument('-u', action = 'store', dest = 'url', required = False,help = 'insert target.')
    parser.add_argument('-o', action = 'store', dest = 'save', required = False,help = 'save output file.')
    parser.add_argument('-e', action = 'store', dest = 'email', required = False,help = 'search the email.')

    arguments = parser.parse_args()

    if arguments.tipo == "all" or arguments.tipo == "ALL":
        print("ALL")
    elif arguments.tipo == list_options[9]:
        print("SharingmyIP")
        print(core_recon.green_sharingmyip(arguments.url,arguments.save))
        exit()
    elif arguments.tipo == list_options[8]:
        print("Check CMS")
        key="whatcms"
        whatcms_key=key_open(NAME_KEYS,key)
        print(core_recon.green_whatcms(arguments.url,whatcms_key))
        exit()
    elif arguments.tipo == list_options[6]:
        print("Check Robots")
        print(core_recon.green_checkrobots(arguments.url))
    elif arguments.tipo == list_options[3]:
        print("Whois IP")
        print(core_recon.green_whois(arguments.url))
        exit()
    elif arguments.tipo == list_options[4]:
        print("Whois URL")
        print(core_recon.green_whois(arguments.url))
        exit()
    elif arguments.tipo == list_options[7]:
        print("Archive")
        print(core_recon.green_archive(arguments.url))
        exit()
    elif arguments.tipo == list_options[1]:
        print("Shodan search")
        # FIX - criar no topo algo que trate url e ips
        ip = core_recon.green_gethostname(arguments.url)
        key="shodan"
        key_shodan=key_open(NAME_KEYS,key)
        print(core_recon.green_shodansearch(ip,key_shodan))
        exit()
    elif arguments.tipo == list_options[5]:
        print("Traceroute")
        # FIX - criar no topo algo que trate url e ips
        ip = core_recon.green_gethostname(arguments.url)
        print(core_recon.green_traceroute(ip))
        exit()

    # PEOPLE
    #OK
    elif arguments.tipo == "hunter-io":
        print("Hunter.io")
        key="hunter-io"
        hunterio_key=key_open(NAME_KEYS,key)
        print(core_recon.hunterio_search(arguments.url,hunterio_key))
        exit()
    elif arguments.tipo == "pwnedornot":
        print("pwnedornot")
        print(core_recon.green_pwnedornot(arguments.email))
        exit()
    elif (arguments.url == None) or (arguments.email == None):
        core_menu.main_menu()
        exit()
    else:
        print("ERRO")
