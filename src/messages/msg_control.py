#import GreenMindLib

msg_menu = '''

    Use: sudo ./green -u http://businesscorp.com.br -o teste.txt \n\n
Green Recon
=============

    Command                 Description
    -------                 -----------
    greenrecon              Start recon OSINT
    recon                   Suite recon OSINT
        google_search       Recon google search
        shodan_search       Recon shodan search
        hostname            Recon IP using URL
        whois               Search whois
        traceroute          Recon traceroute
        check_robots        Check Robots.txt
        archive_search      Search archive history
        check_cms           Check CMS
        sharingmyip         Check using http://sharingmyip.com
    Use:
        greenrecon http://businesscorp.com.br teste.txt
        recon google_search https://greenmindlabs.com
        recon shodan_search 37.59.174.225
        recon hostname http://businesscorp.com.br
        recon whois 37.59.174.225
        recon traceroute http://businesscorp.com.br
        recon check_robots http://businesscorp.com.br
        recon archive_search http://businesscorp.com.br
        recon check_cms https://greenmindlabs.com
        recon sharingmyip https://greenmindlabs.com

Core Commands
=============

    Command                 Description
    -------                 -----------
    ?                       Help menu
    exit                    Exit the console
    help                    Help menu
    version                 Show the version numbers

Green Cripto
=============

    Command                 Description
    -------                 -----------
    cripto
        reverse             Reverse string
        encrypt_base64      Encrypt Base64
        decrypt_base64      Decrypt Base64
        encrypt_md5         Encrypt MD5
        encrypt_sha1        Encrypt SHA1
        encrypt_sha256      Encrypt SHA256
        encrypt_sha512      Encrypt SHA512
    Use:
        cripto reverse "54321"
        cripto encrypt_base64 teste
        cripto decrypt_base64 dGVzdGU=
        cripto encrypt_md5 teste
        cripto encrypt_sha1 teste
        cripto encrypt_sha256 teste
        cripto encrypt_sha512 teste

System Backend Commands
============================

    Command                 Description
    -------                 -----------
    help                    Menu help
    exit                    Green exit program
'''

msg_menu2 = '''

Green Basic Commands
=============

    Command                 Description
    -------                 -----------
    greenrecon              Start recon

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

Green Cripto
=============

    Command                 Description
    -------                 -----------
    cripto
        reverse             Reverse string
        encrypt_base64      Encrypt Base64
        decrypt_base64      Decrypt Base64
        encrypt_md5         Encrypt MD5
        encrypt_sha1        Encrypt SHA1
        encrypt_sha256      Encrypt SHA256
        encrypt_sha512      Encrypt SHA512
    Use:
        cripto reverse "54321"

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

msg_cripto='''
Green Cripto
=============

    Command                 Description
    -------                 -----------
    cripto
        reverse             Reverse string
        encrypt_base64      Encrypt Base64
        decrypt_base64      Decrypt Base64
        encrypt_md5         Encrypt MD5
        encrypt_sha1        Encrypt SHA1
        encrypt_sha256      Encrypt SHA256
        encrypt_sha512      Encrypt SHA512
    Use:
        cripto reverse "54321"

'''

msg_set='''
Green Set
=============

    Command                 Description
    -------                 -----------
    set
        payload             Insert payload

    Use: set payload "web"
'''
