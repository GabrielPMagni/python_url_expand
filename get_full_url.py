import requests as req
import urllib
# site = input('Digite o site: ')
site = 'https://youtu.be/sypUNwrnenY'
site = urllib.parse.urlencode({'u': site})

request = req.post('https://checkshorturl.com/expand.php', data=site)

cont = request.content
table_index = cont.index('<table')
# a_index = cont.
print(cont)