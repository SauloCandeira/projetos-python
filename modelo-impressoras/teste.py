from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from requests import NullHandler


# IMP--------------------------------------------------------------            
Listaurl = [#'http://172.16.11.40/status.htm',  #IMP-01
            'http://172.16.12.32/status.htm',  #IMP-02
            'http://172.16.11.36/status.htm',  #IMP-03
            #'http://172.16.10.35/status.htm',  #IMP-04
            'http://172.16.12.31/status.htm',  #IMP-05
            #'http://172.16.11.35/status.htm',  #IMP-06
            'http://172.16.10.33/status.htm',  #IMP-08
            'http://172.16.12.30/status.htm',  #IMP-09
            'http://172.16.10.38/status.htm',  #IMP-10
            'http://172.16.13.34/status.htm',  #IMP-11
            'http://172.16.12.37/status.htm',  #IMP-12
            'http://172.16.12.34/status.htm',  #IMP-13
            'http://172.16.12.39/status.htm',  #IMP-14
            'http://172.16.11.33/status.htm',  #IMP-15
            'http://172.16.12.33/status.htm',  #IMP-16
            'http://172.16.13.35/status.htm',  #IMP-17
            'http://172.16.10.31/status.htm',  #IMP-18
            'http://172.16.14.36/status.htm',  #IMP-19
            'http://172.16.12.42/status.htm',  #IMP-20
            'http://172.16.14.32/status.htm',  #IMP-21
            'http://172.16.14.33/status.htm',  #IMP-22
            'http://172.16.14.41/status.htm',  #IMP-23
            'http://172.16.12.35/status.htm',  #IMP-24
            'http://172.16.11.37/status.htm',  #IMP-25
            #'http://172.16.14.37/status.htm',  #IMP-26
            'http://172.16.14.30/status.htm',  #IMP-27
            'http://172.16.13.36/status.htm',  #IMP-28
            'http://172.16.14.40/status.htm',  #IMP-29
            'http://172.16.10.30/status.htm',  #IMP-30
            'http://172.16.12.36/status.htm',  #IMP-31
            'http://172.16.11.30/status.htm',  #IMP-32
            #'http://172.16.14.31/status.htm',  #IMP-33
            'http://172.16.13.40/status.htm',  #IMP-34
            'http://172.16.13.39/status.htm',  #IMP-35
            'http://172.16.10.37/status.htm',  #IMP-36
            'http://172.16.13.38/status.htm',  #IMP-37
            'http://172.16.12.38/status.htm',  #IMP-38
            'http://172.16.12.40/status.htm',  #IMP-39
            'http://172.16.10.34/status.htm',  #IMP-40
            ]

#Listaurl = ['http://172.16.12.31/status.htm']  #VERMELHO
#Listaurl = ['http://172.16.12.34/status.htm']  #AZUL


for i in Listaurl:
    html = urlopen(i)
    #html = urlopen(Request(i, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}))
    bs = BeautifulSoup(html, 'html.parser')
    ver_layout=bs.find_all('font')
    
    #URL COUNTER
    url_counter=i.split('/s')[0]+'/countsum.htm'
    html2=urlopen(url_counter)
    bs2 = BeautifulSoup(html2, 'html.parser')
    #print(url_counter)


    #URL SUPPLYSUM
    url_supplies=i.split('/s')[0]+'/printer/suppliessum.htm'
    html3=urlopen(url_supplies)
    bs3 = BeautifulSoup(html3, 'html.parser')
    print(url_supplies)

    # AZUL
    if '<font color="white" size="4">READY TO PRINT</font>' in str(ver_layout): #verifica o layout do gerenciador da impressora

        #imp-info
        tabela1 = bs.find_all('input', attrs={'name': 'AVAILABELBLACKTONER'})
        tbody = bs.find_all('tbody')
        tr = tbody[3].find_all('tr')
        nome=tr[2].get_text().split('\n')[2]
        ip=tr[3].get_text().split('\n')[2]
        sala_comp=tr[5].get_text().replace(':','').split('\n')[2]
        sala=sala_comp.split('-')[0].replace('SALA','').strip()        
        setor=sala_comp.split('-')[1].strip()
        andar=sala[0:2]

        #Countsum
        tbody2 = bs2.find_all('table')
        total_impressao = tbody2[1].find_all('tr')[1].find_all('td')[1].get_text()
        total_scan = ''


        #Supplies
        table_supplies = bs3.find_all('table')
        total_cilindro = table_supplies[2].find_all('tr')[1].find_all('td')[0].get_text()


        #print(total_impressao)
        #o = 1
        #for i in table_supplies:
        #    print(i)
        #    print(o)
        #    o = o + 1
        #    print('----------------')

        #for i in total_cilindro:
        #    print(i)
        #    print(o)
        #    o = o + 1
        #    print('----------------')




        for coluna in tabela1:
            print(' Tonner (%) :', coluna['value'], 'Device Name:', nome, 'ANDAR', andar, 'Sala : ' , sala, 'IP:', ip, 'SETOR', setor, 'Total de Impressão :', total_impressao, 'Total Scan:', total_scan, 'Total Cilindro :', total_cilindro)


    # VERMELHA
    if '<font color="white" size="4">READY TO PRINT</font>' not in str(ver_layout): #verifica o layout do gerenciador da impressora

        #imp-info
        tabela1 = bs.find_all('input', attrs={'name': 'AVAILABELBLACKTONER'})
        table = bs.find_all('table')
        t=1
        nome=table[2].find_all('tr')[0].find_all('td')[1].get_text()
        ip=table[2].find_all('tr')[1].find_all('td')[1].get_text()
        sala_comp=table[2].find_all('tr')[3].find_all('td')[1].get_text().replace(':','')
        sala=sala_comp.split('-')[0].replace('SALA','').strip()        
        setor=sala_comp.split('-')[1].strip()
        andar=sala[0:2]
        

        #Countsum
        table2 = bs2.find_all('table')
        total_impressao = table2[1].find_all('tr')[1].find_all('td')[1].get_text()
        total_scan = table2[3].find_all('tr')[0].find_all('td')[1].get_text()


        #Supplies
        table_supplies = bs3.find_all('table')
        total_cilindro = table_supplies[2].find_all('tr')[1].find_all('td')[1].get_text()
        #total_scan = table2[3].find_all('tr')[0].find_all('td')[1].get_text()
        


        
        #o = 1
        #for i in table_supplies:
        #    print(i)
        #    print(o)
        #    o = o + 1
        #    print('----------------')

        #for i in drumkit:
        #    print(i)
        #    print(o)
        #    o = o + 1
        #    print('----------------')



        for coluna in tabela1:
            print('Tonner (%) :', coluna['value'], 'Device Name:', nome, 'ANDAR', andar, 'Sala : ' , sala, 'IP:', ip, 'SETOR', setor, 'Total de Impressão :', total_impressao, 'Total Scan:', total_scan, 'Total Cilindro', total_cilindro)
        
        

    
  


