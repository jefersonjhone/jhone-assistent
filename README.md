# Jhone-assistent
## Um assistente CLI para otimizar tempo 
### Requisitos 
* #### Ter um sistema Linux em sua maquina
* #### Ter o interpretador Python instalado (por padrão a maioria das distro linux já vem com python instalado, se não for o seu caso, Baixe em <https://www.python.org/downloads/>)
* #### Ter o Git instalado

### Passo a Passo
* #### . Clonar esse repositório em uma pasta de seu computador ´git clone https://github.com/jefersonjhone/jhone-assistent.git´
* #### . Criar um *alias*, isto é, um apelido para nosso arquivo. Para saber mais sobre *alias* execute o comando ´help alias´ no seu terminal. 
    ##### Para criar um apelido para nosso assistente vamos abrir a pasta do usuário com o comando ´cd ~´. 
    ##### Abra o arquivo __.bash_aliases__ com o comando ´nano .bash_alises´ ou com algum outro editor de sua preferência.
    ##### Em seguida adicione o apelido para o arquivo, aqui vc pode dar qulquer nome ao seu assistente, : qualquer_nome ='python3 caminho_da_pasta salva'
    ##### Exemplo : ´jhone='python3 ~/Documents/main.py'´
    ##### Salve o arquivo com *´ctrl+x'*, pressione *´s´* e tecle *´enter´*

### Funções já implementadas
* #### Consultas ao Google 
##### ´jhone -a gg x´ x é o termo a ser consultado, em caso de um termo com mais de uma palavra deve-se usar aspas ´jhone -a gg "termo a ser pesquisado"´ 
* #### Abrir redes sociais com um comando 
* #####  ´jhone -a tt´ -- Para abrir o Twitter
* ##### ´jhone -a yt´  -- Para abrir o Youtube
* ##### ´jhone -a inst´-- Para abrir o instagram
### Funções a serem implementadas futuramente
* #### Abrir em navegação anônima
* #### Implemetação de rotinas 
* #### Adição de reconhecimento de voz
* #### Implementação no sistema Windows