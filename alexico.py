import re #Lib que permite a criação de Expressões Regulares#
import nltk #Lib que automatiza o processo de criação de tokens#

p = open("Código.txt", 'r') #Recebe o arquivo e realiza a leitura do mesmo com o 'r'#
cod = p.read() #Criação de uma nova variável que realizará a leitura do código#
lex = nltk.wordpunct_tokenize(cod) #Variável que receberá o corpo do código, dessa vez completamente tokenizado com o wordpunct#


print(lex, "\n") #Imprime o código inserido no arquivo, para verificar se a leitura e tokenização foram feitas da maneira correta#

#Criação das Expressões Regulares e armazenamento de valores#

#Palavras chaves utilizadas na linguagem criada#
PR = "mostrar|natural|decimal|inserir|retornar|vazio|loop|quando|execute|selecao|etapa|parar|condinicial|condinter|condfinal|funcao"
#Operadores utilizados na linguagem#
OP = "(\+)|(-)|(\*)|(/)|(^)"
#Operadores relacionais utilizados#
OP_R = "(<=)|(<)|(==)|(>)|(>=)|(!=)|(=)"
#Expressão regular para números#
NUM = "^(\d+)$"
#Caracteres especiais que podem a vir ser utilizados#
CS = "[\[@&~!$\\|\]:;<>?,\']|\(\)|\(|\)|{}|\[\]|\""
#Expressão regular para definição de identificadores#
ID = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
#Caracteres para criação de blocos#
BL = "({)|(})"

count = 0 #Contagem para possibilitar identificação de quantos tokens são utilizados#
for token in lex:
    count = count + 1
    #Uso da função re.findall para identificar todas as expressões regulares no corpo do arquivo e os tokens que elas representam#
    #Trazendo a contagem como a sua "posição", o token identificado e o que ele representa#
    if(re.findall(PR,token)):
        print(count,":", " ' " + token + " ' ",": Palavra Reservada" + "\n----------------------")
    elif(re.findall(OP,token)):
        print(count,":", " ' " + token + " ' ",": Operador" + "\n----------------------")
    elif(re.findall(OP_R, token)):
        print(count,":", " ' " + token + " ' ",": Operador relacional" + "\n----------------------")
    elif(re.findall(NUM,token)):
        print(count,":", " ' " + token + " ' ",": Número Natural" + "\n----------------------")
    elif(re.findall(CS,token)):
        print(count,":", " ' " + token + " ' ",": Símbolo" + "\n----------------------")
    elif(re.findall(ID,token)):
        print(count,":", " ' " + token + " ' ",": Identificador" + "\n----------------------")
    elif(re.findall(BL, token)):
        print(count, ":", " ' " + token + " ' ", ": Blocos" + "\n----------------------")
    else:
        print("ERRO: CARACTERE INVALIDO!\n----------------------")