import os
import sys


def abrir(arq:str,query:str=None) -> None:
    """open the url"""
    urls = {
        'tw' : "https://twitter.com/home/",
        'yt' : "https://www.youtube.com/",
        'inst': "https://www.instagram.com/",
        'gg': "https://www.google.com/"
        }
    if arq in urls:
        if query:
            try:
                url = urls[arq]+'search?q={}'.format(query)
                os.system('google-chrome "{}"'.format(url))
            except:
                print('error')
        else:
            os.system('google-chrome "{}"'.format(urls[arq]))
    else:
        
        print('{} not in urls paths defined')


comands = {'-c': 'linha de comando','-a':abrir}


if len(sys.argv) == 3:
    if (sys.argv[1] in comands):
        comands[sys.argv[1]](sys.argv[2])
    else:
        print('command not found!!')
elif len(sys.argv) == 4:
    if (sys.argv[1] in comands):
        comands[sys.argv[1]](sys.argv[2],sys.argv[3])
elif len(sys.argv) > 3:
    print(sys.argv) 
else:
    print(" ola mister, nenhum argumento foi passado, entao estou no modo de leitura")

