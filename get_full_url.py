import argparse
from urllib import request, parse

parser = argparse.ArgumentParser(description='Retorna URL completa')
parser.add_argument('url', type=str)
arg = parser.parse_args()
site = arg.url
if site == '':
    exit('Site inválido')
data = parse.urlencode({'u': site}).encode()

req = request.Request('https://checkshorturl.com/expand.php', data=data)

cont = request.urlopen(req)
cont = str(cont.read())
table_index = cont.find('<table')
if table_index < 0:
    exit('Não encontrado')
a_index = cont.find('<a', table_index)
if a_index < 0:
    exit('Não encontrado')
href_index = cont.find('href=', a_index)
if href_index < 0:
    exit('Não encontrado')
space_index = cont.find(' ', href_index)
if space_index < 0:
    exit('Não encontrado')
link = cont[href_index + 6:space_index - 1]
print(link)
