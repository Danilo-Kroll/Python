# 114 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except: # except urllib.error.URLError:
    print('ERRO!')
else:
    print('OK!')
    print(site.read())