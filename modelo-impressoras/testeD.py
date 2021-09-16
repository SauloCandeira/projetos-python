from bs4 import BeautifulSoup
from urllib.request import urlopen

# IMP-01 ------------------------------------------
Listaurl = ['http://172.16.11.40/printer/suppliessum.htm','http://172.16.12.32/printer/suppliessum.htm']


for i in Listaurl:
    html = urlopen(i)
    bs = BeautifulSoup(html, 'html.parser')
    tabela1 = bs.find_all('input', attrs={'name': 'AVAILABELBLACKTONER'})

    for coluna in tabela1:
        print(' Remaining Toner (%) :', coluna['value'])


