import os
texto = 'Uma longa saga para aprender a gostar de Python...'
arquivo = open(os.path.join('escrever_TXT/texto.txt'),'w')

for palavra in texto.split():
    arquivo.write(palavra + ' ')

arquivo.close()

arquivo = open('escrever_TXT/texto.txt','r')
conteudo = arquivo.read()
print(conteudo)