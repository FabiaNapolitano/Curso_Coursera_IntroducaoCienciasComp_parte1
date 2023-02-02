# último exercício do curso de Ciências da Computação em Python
# utilizaremos um código escrito por terceiros. Partindo de um programa já iniciado vamos completá-lo
# Introdução: Manuel Estandart é monitor na disciplina Introdução à Produção Textual na Universidade de Pasárgada (UPA).
# Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. 
# Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muitos 
# semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH
# Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita de ajuda
# para identificar os alunos contaminados.
# DETECÇÃO DE AUTORIA: Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas,
# outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma 
# "assinatura" do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa "assinatura"
# pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.
# TRAÇOS LÍNGUÍSTICOS: Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:
# Tamanho médio de palavra: Média simples do número de caracteres por palavra;
# Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
# Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
# Tamanho médio de sentença: Média simples do número de caracteres por sentença.
# Complexidade de sentença: Média simples do número de frases por sentença.
# Tamanho médio de frase: Média simples do número de caracteres por frase.
# A partir da assinatura conhecida de um portador de COH-PIAH, o programa deverá receber diversos textos e calcular os valores dos diferentes 
# traços linguísticos desses textos para compará-los com a assinatura dada. 
# Basicamente, a tarefa é implementar corretamente as seguintes funções:
# compara_assinatura(as_a, as_b)  ;  calcula_assinatura(texto)  ;  avalia_textos(textos, ass_cp)


import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca) # o split tem limitação de caracteres!!'''

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split() # este métudo é usado para separar os espaços em uma frase e devolve uma lista com todas as palavras

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict() # cria um dicionário para incluir as palavras analisadas
    unicas = 0 # palavras únicas que começam com zero na contagem
    for palavra in lista_palavras:
        p = palavra.lower() # aqui a primeira palavra é convertida em minúscula na variável p        
        if p in freq: # aqui é feita a condição de p (a 'palavra' da laço 'for') já existe no meu dicionário
            if freq[p] == 1: # aqui questiona-se a chave(p) existente no dicionário (freq) tem valor igual a 1.
                unicas -= 1 # nesse caso já existe esta palavra no dicionário então únicas é diminuido um valor por ser repetido
            freq[p] += 1# aqui se a condição acima já tenha sido true ao valor da chave é somado 1 para indicar a frequência de repetições 
        else:
            freq[p] = 1 # nesta linha é incluído no dicionário freq[o valor de p QUE É A CHAVE] e seu valor que é 1
            unicas += 1 # neste caso a palavra sendo única é somado um para se ter o valor total de palavras únicas
        
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

## Texto tratado devolve uma lista de palavras

def texto_tratado_palavras(texto):
    
    #>> 1º Passo: utilizar a função separa_sentencas(texto) dentro de uma variável que criará uma lista de sentenças
    lista_sentenca = separa_sentencas(texto)  
    num_palavras_texto = 0
    diferentes = 0    
    lista_palavras = []
    
    #>> 2º Passo: criar um loop para cada sentença e seguir os passos a seguir:
    for i in lista_sentenca:      
        
    #>> 3º Passo: usar a função 'separa_frases(sentenca)' dentro do loop, é necessário outro loop para considerar todas as frases;        
        separador_frases = separa_frases(i)        
        for i in separador_frases:
            
            #>> 4º Passo: utilizar a função separa_palavras para devolver a lista de palavras em cada frase;
            separador_palavras = separa_palavras(i) 
            for i in separador_palavras:
                lista_palavras.append(i)           
    
            
    return lista_palavras

# Tamanho médio de palavra: Média simples do número de caracteres por palavra.

def tamanho_md_palavras(texto):
    
    separador_palavras = texto_tratado_palavras(texto) # retorna uma lista de todas as palavras do texto  
    num_caracter_frase = 0    
    total_palavras = len(texto_tratado_palavras(texto))
    
    while total_palavras > 0:
        tamanho_cada_palavra = len(separador_palavras[total_palavras-1])                
        num_caracter_frase += tamanho_cada_palavra                
        total_palavras -= 1
   
    tamanho_medio_palavras = num_caracter_frase / len(separador_palavras)
    
    return tamanho_medio_palavras


## Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
## Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes
## (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale 4/5 = 0.8

def type_token(texto):
    
    lista_palavras = texto_tratado_palavras(texto)
    soma_palavras = len(lista_palavras)
    diferentes = n_palavras_diferentes(lista_palavras)
    razao_type_token = diferentes/soma_palavras
    
    return razao_type_token


# Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
# Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem 
# só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale 3/5 = 0.6

def razao_hapax(texto):
    lista_palavras = texto_tratado_palavras(texto)
    soma_palavras = len(lista_palavras)
    unicas = n_palavras_unicas(lista_palavras)
    rz_Hapax = unicas/soma_palavras
    
    return rz_Hapax

# Tamanho médio de sentença: Média simples do número de caracteres por sentença.

def tamanho_md_sentenca(texto):

    sent_texto =  len(separa_sentencas(texto))
    sent_caracter = 0
    for i in (separa_sentencas(texto)):        
        sent_caracter += len(i)
        
    md =  sent_caracter / sent_texto
    
    return md

# Complexidade de sentença é o número total de frases divido pelo número de sentenças.

def complex_sentenca(texto):
    
    sentenca = separa_sentencas(texto)    
    number_frases = 0
    
    for i in sentenca:        
        frases = separa_frases(i)        
        number_frases += len(frases)
        
    complexidade_sent = number_frases / len(sentenca)
    
    return complexidade_sent

# Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
# (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).

def tamanho_md_frase(texto):
    
    sentenca = separa_sentencas(texto)    #devolve uma lista de sentenças
    number_frases = 0
    number_caracter_frases = 0
    
    for i in sentenca:        
        frases = separa_frases(i) # devolve uma lista de frases de uma sentença
        number_frases += len(frases) 
        
        for i in frases:
            number_caracter_frases += len(i)
            
    md_frase = number_caracter_frases / number_frases
    
    return md_frase

'''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
def calcula_assinatura(texto):
    
    md_palavras = tamanho_md_palavras(texto) # resultado correto 4.507142857142857
    token = type_token(texto) # resultado correto 0.6928571428571428
    Hapax = razao_hapax(texto) # resultado correto 0.55
    md_sentenca = tamanho_md_sentenca(texto) # resultado correto 70.81818181818181
    complex_sent = complex_sentenca(texto) # resultado correto 1.8181818181818181
    md_frase = tamanho_md_frase(texto) # resultado correto 38.5
    
    return [md_palavras, token, Hapax, md_sentenca, complex_sent, md_frase]



'''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
def compara_assinatura(as_a, as_b): # parâmetros são as listas com as assinaturas de textos individuais
    diferenca_ab = []
    cont = 0
    
    for i in as_a:
        
        diferenca_iab = abs(float(i) - float(as_b[cont]))
        diferenca_ab.append(diferenca_iab)
        cont += 1
    soma_i = 0
    for i in diferenca_ab:
        soma_i += float(i)
    S_ab = soma_i / 6
    
    return S_ab # devolve o cálculo de Similaridade



'''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior 
                                                                            probabilidade de ter sido infectado por COH-PIAH.'''
def avalia_textos(textos, ass_cp):
    lista_S_ab = []
    ind_text = 1
    
    for i in textos:
        as_a = calcula_assinatura(i) # devolve uma lista com os valores da assinatura calculada         
        comparacao_ab = compara_assinatura(as_a, ass_cp) # devolve a similaridade de cada texto individualmente
        lista_S_ab.append(comparacao_ab)          
    
    menor_ind = lista_S_ab.index(min(lista_S_ab))
    menor_ind += 1
    
    return menor_ind

# main

ass_cp = le_assinatura() # devolve uma lista com os valores do aluno infectado
lista_textos = le_textos() # devolve uma lista dos textos a serem analisados

analisa = avalia_textos(lista_textos, ass_cp) # devolve os números do texto com maior probabilidade de COH-PIAH
print('\nO autor do texto', analisa, 'está infectado com COH-PIAH')
