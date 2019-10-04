import GreenLib
import base64,hashlib,sys

#Mensagens
sys.path.insert(0, 'messages')
import msg_control
import msg_logo



# Verificar Cripto
class Cripto():
    def __init__(self, cripto_tipo, key):
        self.cripto_tipo = cripto_tipo
        self.key    = key

    def greenCripto(self, cripto_tipo,key):
        # Adicionar
        #Inserir API para descriptografar
        #- Sha512
        #- Sha256
        #- SHA1
        #- MD5

        tipo_chave = self.key
        if self.cripto_tipo == 'reverse':
            self.resultado = tipo_chave[::-1]
            print(self.resultado)
        #Base64
        elif self.cripto_tipo == 'decrypt_base64':
            decode = base64.b64decode(tipo_chave.encode('UTF-8')).decode('ascii')
            print(decode)
        elif self.cripto_tipo == 'encrypt_base64':
            encode = base64.b64encode(tipo_chave.encode('UTF-8')).decode('ascii')
            print(encode)
        #md5 (http://md5decrypt.net)
        elif self.cripto_tipo == 'encrypt_md5':
            encode = hashlib.md5(tipo_chave.encode('utf-8')).hexdigest()
            print(encode)
        #sha1 (http://md5decrypt.net/en/Sha1/)
        elif self.cripto_tipo == 'encrypt_sha1':
            encode = hashlib.sha1(tipo_chave.encode('utf-8')).hexdigest()
            print(encode)
        #sha256 (http://md5decrypt.net/en/Sha256/)
        elif self.cripto_tipo == 'encrypt_sha256':
            encode = hashlib.sha256(tipo_chave.encode('utf-8')).hexdigest()
            print(encode)
        #sha512 (http://md5decrypt.net/en/Sha512/)
        elif self.cripto_tipo == 'encrypt_sha512':
            encode = hashlib.sha512(tipo_chave.encode('utf-8')).hexdigest()
            print(encode)
        else:
            GreenLib.menu_actions['cripto_main_menu']()

def cripto():
    print(msg_control.msg_cripto)
    core_menu.espera()
