#1ª FUNÇÃO (Apresentar um relatório com o número de linhas do documento original, e os nomes das colunas, que descrevem os dados)

def apresentar_relatorio(nome_arquivo): #mostra as colunas e números de linhas do arquivo.
    arq = open(nome_arquivo, 'r')
    cabecalho = arq.readline() #readline lê linha por linha
    print(f"\nNome das colunas do arquivo:\n\n {cabecalho}")
    quantidade_linhas = 0
    for linha in arq:
       quantidade_linhas = quantidade_linhas + 1 #ele conta a partir da 2 linha. 
    print(f"O número de linhas do arquivo é: {quantidade_linhas}")
    return f'Nome das colunas do arquivo: {cabecalho}\n\n O número de linhas do arquivo original é: {quantidade_linhas}'
   
#2ª FUNÇÃO (Criar um arquivo parcial, com nome informado pelo usuário, que armazenará os dados correspondentes a uma filtragem de dados. Para este arquivo, também deverá ser possível chamar a função de relatório anterior.)

def criar_arquivo_parcial(arquivo_origem): #mostra o total de casos por estado
    arquivo_regiao = open(arquivo_origem, 'r')
    nome_arquivo_usuario = input("Qual o nome do arquivo: ")
    arquivo = open(f'{nome_arquivo_usuario}.txt', 'w') #abrindo um arquivo com o nome que o usuario escolheu
    escolha_estado = int(input("Escolha uma das opções para gerar informações:\n1.PR\n2.SC\n3.RS\n"))
    relatorio = apresentar_relatorio(nome_arquivo_usuario)
    for linha in arquivo_regiao:            
        if (escolha_estado == 1):
            if linha[0:2] == '41': #se o primeiro e o segundo carctere for 41
                arquivo.write(linha) #escreva no arquivo que o usuário nomeou, as informações contidas no arquivo origem
        elif (escolha_estado == 2):
            if linha[0:2] == '42':
                arquivo.write(linha)
        else:
            if linha[0:2] == '43':
                arquivo.write(linha)
    arquivo.write(relatorio) #return da função 1
    arquivo.close()
    print(f"Criando arquivo parcial: {nome_arquivo_usuario}")   

#3ª FUNÇÃO
def criar_arquivo_resumo(arquivo_origem): #mostra o total de casos pelo ano e estado escolhido
    resumo = open(arquivo_origem, 'r')
    estado_usuario = int(input("Qual estado você quer informações:\n41.PR\n42.SC\n43.RS\n"))
    ano_usuario = int(input("Qual ano você quer informações entre:\n2010\n2011\n2012\n"))
    resultado = ""
    total_casos = 0
    for linha in resumo:
        coluna = linha.split(';')
        if (linha[0:2] == estado_usuario.__str__()): # para fazer o comparativo, transformei em string devido ao arquivo original
          if(ano_usuario == 2010):
              total_casos = total_casos + int(coluna[4])
              resultado += coluna[0] + " - " + coluna[1] + " - " + coluna[4] + "\n" #coluna 0 codigo / 1 nome municipio / 4 total de casos
              print(coluna[0] + " - " + coluna[1] + " - " + coluna[4])
          elif (ano_usuario == 2011):
              total_casos = total_casos + int(coluna[5])
              resultado += coluna[0] + " - " + coluna[1] + " - " + coluna[5] + "\n"
              print(coluna[0] + " - " + coluna[1] + " - " + coluna[5])  
          elif (ano_usuario == 2012):
              total_casos = total_casos + int(coluna[6])
              resultado += coluna[0] + " - " + coluna[1] + " - " + coluna[6] + "\n"
              print(coluna[0] + " - " + coluna[1] + " - " + coluna[6])
    
    arquivo_resultado = open('resultado.txt', 'w')       
    arquivo_resultado.write(resultado)
    arquivo_resultado.write(f'O total de casos do estado do {estado_usuario} no ano de {ano_usuario} é de {total_casos}')
    arquivo_resultado.close()
    
#4ª FUNÇÃO
def dados_estatisticos(arquivo_origem): # mostra a média de casos pelo estado escolhido (casos / municipios)
    resumo = open(arquivo_origem, 'r')
    total_casos_pr = 0
    quantidade_casos_pr = 0 #por municipio
    total_casos_sc = 0
    quantidade_casos_sc = 0
    total_casos_rs = 0
    quantidade_casos_rs = 0
    for linha in resumo:
        coluna = linha.split(';')
        if (linha[0:2] == '41'):
            total_casos_pr = total_casos_pr + int(coluna[14])
            quantidade_casos_pr = quantidade_casos_pr + 1
        if (linha[0:2] == '42'):
            total_casos_sc = total_casos_sc + int(coluna[14])
            quantidade_casos_sc = quantidade_casos_sc + 1 
        if (linha[0:2] == '43'):
            total_casos_rs = total_casos_rs + int(coluna[14])
            quantidade_casos_rs = quantidade_casos_rs + 1
    print("A média de casos do Paraná é: ", total_casos_pr / quantidade_casos_pr)
    print("A média de casos de Santa Catarina é: ", total_casos_sc / quantidade_casos_sc)
    print("A média de casos do Rio Grande do Sul é: ", total_casos_rs / quantidade_casos_rs)
    
#5ª FUNÇÃO
def busca_de_dados(arquivo_origem): #mostra o total de casos pela cidade escolhida
    resumo = open(arquivo_origem, 'r')
    cidade_usuario = input("Qual cidade você quer informações: ")
    for linha in resumo:
        if cidade_usuario.lower() in linha.lower(): #o método lower transforma todo texto em minusculo, para comparar 
            print(linha)
    
#6ª FUNÇÃO EXTRA 
def casos_mortes(arquivo_origem): #mostra o número de mortes em 2020 nos estados da região sul
    resumo = open(arquivo_origem, 'r')
    total_casos_pr = 0
    total_casos_sc = 0
    total_casos_rs = 0
    for linha in resumo:
        coluna = linha.split(';')
        if (linha[0:2] == '41'):
            total_casos_pr = total_casos_pr + int(coluna[43])
        if (linha[0:2] == '42'):
            total_casos_sc = total_casos_sc + int(coluna[43]) 
        if (linha[0:2] == '43'):
            total_casos_rs = total_casos_rs + int(coluna[43])
    print("\nO total de mortes por AIDS em 2020 no estado do Paraná é: ", total_casos_pr)
    print("O total de mortes por AIDS em 2020 no estado de Santa Catarina é: ", total_casos_sc)
    print("O total de mortes por AIDS em 2020 no estado do Rio Grande do Sul é: ", total_casos_rs)
    print("\n")
    


print("\nInstituto Federal Catarinense - Campus Camboriú\nSistemas de Informação - 2023\n")
print("Matéria: Algoritmos II\nProfessor: Rafael Speroni\n")
print("\033[1m" + "TRABALHO FINAL""\033[0m")
print("\033[1m" + "\nAluna:""\033[0m"" Júlia Isadora Amorim\n")

while True:
    print("Menu Principal:")
    print("\n1. Apresentar relatório")
    print("2. Criar arquivo parcial")
    print("3. Criar arquivo de resumo")
    print("4. Apresentar dados estatísticos")
    print("5. Realizar busca de dados")
    print("6. Casos de mortes por AIDS em 2020")
    print("0. Sair\n")

    escolha_usuario = int(input("Escolha uma das opções acima: "))
    nome_do_arquivo = 'aids2.csv'



    if (escolha_usuario == 1):
        apresentar_relatorio(nome_do_arquivo)
    
    elif (escolha_usuario == 2):
        criar_arquivo_parcial(nome_do_arquivo)
    
    elif (escolha_usuario == 3):
        criar_arquivo_resumo(nome_do_arquivo)
    
    elif (escolha_usuario == 4):
        dados_estatisticos(nome_do_arquivo)

    elif (escolha_usuario == 5):
        busca_de_dados(nome_do_arquivo)
    
    elif (escolha_usuario == 6):
        casos_mortes(nome_do_arquivo)
    
    elif (escolha_usuario == 0):
        print("Obrigada por usar nosso banco de dados! Se proteja!\n")
        exit()
    
    else:
        print("\nEscolha umas das opções válidas: 1, 2, 3, 4, 5, 6 ou 0. Obrigada.\n")
