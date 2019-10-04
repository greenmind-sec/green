#!/usr/bin/python3

import GreenLib

#green_gethostname
import socket,sys
#green_checkrobots
import requests
#green_urlparse
from urllib.parse import urlparse

#Traceroute
# HIDE (https://stackoverflow.com/questions/24812604/hide-scapy-warning-message-ipv6)
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#archive
import json

#Whatcms
#pip install pywhatcms
from pywhatcms import whatcms

#Shodan
from shodan import Shodan

#Google Hacking
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from random import randint

# Sharingmyip
#import requests
#from bs4 import BeautifulSoup

# ---------------------
# Funções usadas Recon
# -------
# OK
def green_sharingmyip(url,save):
    #TODO - usar variavel save para gerar saida/output
    rec_site = requests.get('http://sharingmyip.com/?site='+url)

    soup = BeautifulSoup(rec_site.text,'html.parser')

    qt_textarea = len(soup('textarea'))
    msg_list = ['Site (s) neste endereço','DNS para ','Entradas de DNS relacionadas para']
    #for msg in range(msg_list):
    for i in range(qt_textarea):
        if (i == 0):
            print(msg_list[0]+" ")
            print(soup('textarea')[i].string)
        elif i == 1:
            print(msg_list[1]+" "+url)
            print(soup('textarea')[i].string)
        elif i == 2:
            print(msg_list[2]+" "+url)
            print(soup('textarea')[i].string)
        else:
            print("Aconteceu algo errado :D")

# OK
def green_whatcms(site,chave):
    whatcms(chave, site)
    print("Nome:",whatcms.name)
    print("CMS CODE:",whatcms.code)
    #print(whatcms.confidence)
    print("CMS URL:",whatcms.cms_url)
    print("Versão:",whatcms.version)
    #print(whatcms.msg)
    #print(whatcms.id)
    #print(whatcms.request)
    #print(whatcms.request_web)

#OK
def green_checkrobots(url):
    try:
        resposta = requests.get(url + '/robots.txt')
        if (resposta.status_code == 200):
            return resposta.text
        else:
            var = "[ Robots.txt ] - Não encontrado"
            return var
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))

#OK
#TODO
# Parar de usar a API do hackertarget
def green_whois(name_host):
    url_api = "http://api.hackertarget.com/whois/?q="
    requisicao = requests.get(url_api + name_host)
    return requisicao.text

#OK
#TODO - Filtrar saida
def green_archive(url):
    resposta_archive = json.loads(archive_search(url))
    return resposta_archive['results']
def archive_search(url):
    archive = "http://archive.org/wayback/available"
    try:
        r = requests.post(archive, data={'url': url})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text


#-----------------
# Shodan
# ------
# Precisamos de uma URL para resolver o nome
def green_gethostname(url):
    name_host = socket.gethostbyname(url)
    return name_host
def green_shodansearch(name_host,shodan_key):
    # ADD Key config
    api = Shodan(shodan_key)
    host = api.host(name_host)
    # print(ipinfo)
    # Print general info
    print("""
IP: {}
Organization: {}
Operating System: {}
                    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
    # Print all banners
    for item in host['data']:
        print("""
Port: {}
        """.format(item['port']))

# OK
def green_traceroute(host_ip):
    # TODO traceroute abaixo não usa uma base publica
    #retorno_traceroute = traceroute(host_ip,maxttl=50)
    url_api = "http://api.hackertarget.com/mtr/?q="
    requisicao = requests.get(url_api + host_ip)
    return requisicao.text

# ----------------
# HUNTER.io
# --------
#OK
def hunterio_search(url,key):
    hunterio = "https://api.hunter.io/v2/domain-search"
    try:
        r = requests.get(hunterio, data={'domain': url,'api_key': key})
    except Exception as e:
        print("Ocorreu um erro: %s" % (e))
    return r.text

def green_hunterio(url):
    resposta_hunterio = json.loads(hunterio_search(url))
    return resposta_hunterio['results']
