import time
import json


lista_dict = []

with open('lista.txt', 'r') as lista:
    conteudo = lista.readlines()


for i in range(len(conteudo)):
    mes_atual = time.localtime().tm_mon
    dia_atual = time.localtime().tm_mday
    hora_atual = time.localtime().tm_hour
    minuto_atual = time.localtime().tm_min
    segundo_atual = time.localtime().tm_sec
    
    aux = conteudo[i].replace(',' , ' ')
    aux = aux.split()
    template_dicio = {"nome": aux[0], 
                  "RM": aux[2], 
                  "turma": aux[1]}

    with open(f'{dia_atual}-{mes_atual}-{hora_atual}-{minuto_atual}-{segundo_atual}.json', 'w') as arquivo:
        json.dump(template_dicio, arquivo)
    time.sleep(0.5)
#Esta criando o dict tudo no mesmo json, a cada 2 segundos, não consegui resolver para criar em um json cada dict
#Caso tenha alguma dica, ficaria muito grato, professor!
lista_dict.append(template_dicio)
print(lista_dict)






