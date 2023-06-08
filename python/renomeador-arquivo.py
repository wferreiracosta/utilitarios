import os

caminho_pasta = str(input('Digite o caminho: '))
additional_new_name = str(input('Digite oque sera acrescentado no nome do arquivo: '))
partition_new_name = str(input('Digite qual sera a divisoria no nome do arquivo: '))

os.chdir(caminho_pasta)
# os.chdir troca o diretório no qual o python vai trabalhar

for f in os.listdir():
    old_name, ext_name = os.path.splitext(f)
    print('Old Name: '+old_name)
    print('Ext Name: '+ext_name)
    
    new_name = additional_new_name+partition_new_name+old_name+ext_name
    print('New Name: '+new_name)

    os.rename(f, new_name)