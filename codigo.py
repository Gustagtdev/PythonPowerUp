#Passo a passo do projeto
#Passo 1-Entrar no sistema da empresa
#comandos pyautogui
#Clicar-> pyautogui.click
#Escrever-> pyautogui.write
#Apertar uma tecla-> pyautogui.press
import pyautogui
#tempo de espera entre os comandos do pyautogui
pyautogui.PAUSE= 1
#apertar a tecla windows   
pyautogui.press("win")
#escrever o nome do navegadohttpsr
pyautogui.write("opera")
#apertar a tecla enter
pyautogui.press("enter")
#criar uma variável para armazenar o link do sistema,caso o mesmo mude
link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#posição do mouse para clicar na barra de pesquisa
pyautogui.click(x=366, y=67)
#colocando o nome da variável armazenada
pyautogui.write(link)
#aperte a tecla enter para confirmar e ir até a página de login
pyautogui.press("enter")
#pausar uma automação por determinado tempo em segundos
import time
time.sleep(1.5)


#Passo 2-Fazer login
#posição do mouse para clicar no campo de login
pyautogui.click(x=534, y=369)
#colocando o email
pyautogui.write("python3estudante@gmail.com")
#passaando para o próximo campo
pyautogui.press("tab")
#inserindo a senha
pyautogui.write("12346789")
#passaando para o próximo campo
pyautogui.press("tab")
#apertar a tecla enter
pyautogui.press("enter")
#tempo de espera de 3 segundos até o próximo passo do programa.
time.sleep(2)
#Passo 3-Importar a base de dados
#disponibilizando as ferramentas da biblioteca pandas
import pandas
#lendo a base de dados e atribuindo ela a variável 'tabela'
tabela=pandas.read_csv("produtos.csv")
#imprimindo a variável
print(tabela)
#Passo 4-Cadastrar um produto
#estrutura de reptição que significa 'para cada linha/número no índice da tabela faça isso'
for linha in tabela.index:
    #posição do mouse para clicar no campo 'Código do Produto'
    pyautogui.click(x=606, y=259)
    codigo=tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))#pega o codigo da tabela e escreve no campo
    pyautogui.press("tab")#Pula para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs=tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #verifica se existe informação para preencher, caso o contrário não preenche
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)#rola até o topo da página
#Passo 5-Repetir isso até python3estudante@gmail. acabar a base de dados


