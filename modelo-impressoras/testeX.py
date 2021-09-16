from bs4 import BeautifulSoup
from urllib.request import urlopen

# MODELO II
url = 'http://172.16.12.31/status.htm'
html=urlopen(url)
bs=BeautifulSoup(html,'html.parser')
tbody = bs.find_all('tbody')



print(tbody)
#i=1
#tr=tbody[1].find_all('tr')
#print(tr)
#----------------------------------#
#tr=tbody[3].find_all('tr')
#nome=tr[2].get_text().split('\n')[2]
#ip=tr[3].get_text().split('\n')[2]
#sala=tr[5].get_text().split('\n')[2]
#print('nome: '+nome)
#print('ip: '+ip)
#print('sala: '+sala)

#for n in tbody:
#    i=i+1
#    print(n)
#    print(i)
#    print('***********************')
