#Analisador de textos
#Fazer uma análise textual, para saber se há algum plágio.

import re
from math import fabs as modulo
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
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
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
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

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    while i <= 5:
        soma += (modulo(as_a[i] - as_b[i]))
        i += 1
    similaridade = soma/6
    return similaridade

def tamanho_medio(x):
    soma = 0
    palavras = x.replace('-', '').replace(':', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ').split().lower()
    for i in palavras:
        soma += len(i)
    total = soma / len(palavras)
    return total

def type_token(x):
    tudo = x.replace('-', '').replace(':', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ').split().lower
    diferente = n_palavras_diferentes(tudo)
    palavras = len(tudo)
    typetok = diferente / palavras
    return typetok

def hapax_legomana(x):
    tudo = x.replace('-', '').replace(':', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ').split().lower()
    palavraunica = n_palavras_unicas(tudo)
    palavras = len(tudo)
    hapax = palavraunica / palavras
    return hapax

def tamanho_mediosentença(x):
    sentence = separa_sentencas(x)
    soma = 0
    letrastotal = 0
    for i in sentence:
        frase = i.replace('-', '').replace('!', ' ').replace(':', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ').split().lower()
        for a in frase:
            letrastotal += len(a)
    mediosentence = letrastotal / len(sentence)
    return mediosentence

def complexidade(x):
    sentence = separa_sentencas(x)
    frase = 0
    for i in sentence:
        frases = separa_frases(i)
        for a in frases:
            frase += len(a)
    complex = frase / len(sentence)
    return complex

def tamanho_frase(x):
    sentence = separa_sentencas(x)
    letra = 0
    frases = 0
    for i in sentence:
        frase = separa_frases(i)
        frases += len(frase)
        for a in frase:
            letras = len(a.replace('-', '').replace('!', ' ').replace(':', ' ').replace('(', ' ').replace(')', ' ').replace('"', ' ').replace(',', ' ').replace(';', ' ').replace('.', ' ').lower())
            letra += letras
    average = letra / frases
    return average

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    assinatura.append(tamanho_medio(texto))
    assinatura.append(type_token(texto))
    assinatura.append(hapax_legomana(texto))
    assinatura.append(tamanho_mediosentença(texto))
    assinatura.append(complexidade(texto))
    assinatura.append(tamanho_frase(texto))

    return assinatura
    #pass

def avalia_textos():
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o
    numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura = le_assinatura()
    textos = le_textos()
    menor = []
    for i in textos:
        ass_cp = calcula_assinatura(i)
        similar = compara_assinatura(ass_cp, assinatura)
        menor.append(similar)
    num_infect = menor.index(min(menor)) + 1
    return num_infect
    #pass

def fim():
    infectado = avalia_textos()
    print(f'\nO autor do texto {infectado} está infectado com COH-PÌAH')


fim()
























'''
Tamanho médio de palavra: Média simples do número de caracteres por palavra.
Relação Type-Token: Número de palavras diferentes utilizadas em um texto 
divididas pelo total de palavras.
Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo 
número total de palavras.
Tamanho médio de sentença: Média simples do número de caracteres por sentença.
Complexidade de sentença: Média simples do número de frases por sentença.
Tamanho médio de frase: Média simples do número de caracteres por frase.
'''



